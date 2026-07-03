"""Transactional email delivery via Gmail SMTP.

Sends the 2-recommendation (anonymous) and 4-recommendation (signed-in /
unlocked) result emails, styled to match the platform's milky, warm-neutral
visual theme. Every recommendation shown — in either tier — includes its
full curriculum, resources, and the plain-language reason it was recommended.
"""

import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .config import settings

BRAND_CREAM = "#FBF8F3"
BRAND_MILK = "#F3EEE4"
BRAND_ACCENT = "#B08968"
BRAND_INK = "#3A332C"
BRAND_MUTED = "#7A7266"


def _footer_html() -> str:
    return f"""
    <tr>
      <td style="padding:28px 32px;background:{BRAND_MILK};border-top:1px solid #E7E0D3;">
        <p style="margin:0 0 6px 0;font-size:13px;color:{BRAND_MUTED};font-family:Georgia,'Times New Roman',serif;">
          With care, from
        </p>
        <p style="margin:0 0 4px 0;font-size:15px;font-weight:600;color:{BRAND_INK};font-family:Georgia,'Times New Roman',serif;">
          Sharafdeen Quadri Olalekan
        </p>
        <p style="margin:0;font-size:13px;">
          <a href="{settings.portfolio_url}" style="color:{BRAND_ACCENT};text-decoration:none;">{settings.portfolio_url}</a>
        </p>
      </td>
    </tr>
    """


def _wrap_email(inner_html: str) -> str:
    return f"""
    <!DOCTYPE html>
    <html>
    <body style="margin:0;padding:0;background:{BRAND_MILK};font-family:'Segoe UI',Helvetica,Arial,sans-serif;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{BRAND_MILK};padding:32px 0;">
        <tr>
          <td align="center">
            <table role="presentation" width="560" cellpadding="0" cellspacing="0" style="background:{BRAND_CREAM};border-radius:14px;overflow:hidden;box-shadow:0 2px 18px rgba(58,51,44,0.08);">
              <tr>
                <td style="padding:32px 32px 8px 32px;">
                  <p style="margin:0;font-size:12px;letter-spacing:1.5px;text-transform:uppercase;color:{BRAND_ACCENT};font-weight:700;">
                    Global Digital Skills Career Assessment
                  </p>
                </td>
              </tr>
              <tr>
                <td style="padding:8px 32px 32px 32px;color:{BRAND_INK};">
                  {inner_html}
                </td>
              </tr>
              {_footer_html()}
            </table>
          </td>
        </tr>
      </table>
    </body>
    </html>
    """


def _recommendation_block(rank: int, recommendation: dict) -> str:
    career = recommendation["career"]
    curriculum_items = "".join(f"<li style='margin-bottom:6px;'>{step}</li>" for step in career["curriculum"])
    resource_items = "".join(f"<li style='margin-bottom:6px;'>{res}</li>" for res in career["resources"])
    entry_note = recommendation.get("entry_note")
    entry_note_html = (
        f"""<p style="margin:0 0 14px 0;padding:10px 14px;background:{BRAND_CREAM};border:1px dashed {BRAND_ACCENT};border-radius:8px;font-size:13px;color:{BRAND_INK};">{entry_note}</p>"""
        if entry_note
        else ""
    )

    return f"""
    <div style="margin:18px 0;padding:18px 20px;border-radius:10px;background:{BRAND_MILK};">
      <p style="margin:0;font-size:12px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:{BRAND_ACCENT};">
        Recommendation #{rank}
      </p>
      <p style="margin:8px 0 4px 0;font-size:17px;font-weight:700;color:{BRAND_INK};">{career['name']}</p>
      <p style="margin:0 0 10px 0;font-size:13px;color:{BRAND_MUTED};">{career['focus']} &middot; Typical duration: {career['duration']}</p>
      <p style="margin:0 0 14px 0;font-size:13px;color:{BRAND_ACCENT};font-style:italic;">Why this fits: {recommendation['reason']}</p>
      {entry_note_html}
      <p style="margin:0 0 6px 0;font-size:13px;font-weight:700;color:{BRAND_ACCENT};text-transform:uppercase;letter-spacing:0.5px;">Curriculum Path</p>
      <ul style="margin:0 0 14px 0;padding-left:18px;font-size:14px;color:{BRAND_INK};">{curriculum_items}</ul>
      <p style="margin:0 0 6px 0;font-size:13px;font-weight:700;color:{BRAND_ACCENT};text-transform:uppercase;letter-spacing:0.5px;">Recommended Resources</p>
      <ul style="margin:0;padding-left:18px;font-size:14px;color:{BRAND_INK};">{resource_items}</ul>
    </div>
    """


def render_recommendations_email(
    name: str,
    recommendations: list[dict],
    unlocked: bool,
    result_url: str,
    consultation_url: str,
) -> str:
    blocks = "".join(_recommendation_block(i + 1, rec) for i, rec in enumerate(recommendations))

    if unlocked:
        intro = f"""
        <h1 style="margin:0 0 6px 0;font-size:22px;color:{BRAND_INK};">Hi {name}, here are your top {len(recommendations)} matches 🚀</h1>
        <p style="margin:0 0 16px 0;font-size:15px;color:{BRAND_MUTED};line-height:1.6;">
          Based on your responses, here are your top {len(recommendations)} recommended career paths — each with the
          reason it was recommended, a full curriculum, and hand-picked resources.
        </p>
        """
    else:
        intro = f"""
        <h1 style="margin:0 0 6px 0;font-size:22px;color:{BRAND_INK};">Hi {name}, your top {len(recommendations)} matches are in 🎉</h1>
        <p style="margin:0 0 20px 0;font-size:15px;color:{BRAND_MUTED};line-height:1.6;">
          Based on your responses, here are your top {len(recommendations)} recommended career paths, each with a full
          curriculum and reasons why it fits. Create a free account to unlock your top 4 matches instead of 2 —
          no payment required.
        </p>
        <a href="{result_url}" style="display:inline-block;margin-bottom:16px;padding:14px 28px;background:{BRAND_INK};color:{BRAND_CREAM};border-radius:8px;text-decoration:none;font-weight:600;font-size:14px;">
          See My Full Result →
        </a>
        """

    inner = f"""
    {intro}
    {blocks}
    <p style="margin:26px 0 10px 0;font-size:15px;color:{BRAND_INK};line-height:1.6;">
      Want a second opinion, or help mapping this to a concrete study plan? Book a free consultation with Sharafdeen —
      it's included regardless of your plan.
    </p>
    <a href="{consultation_url}" style="display:inline-block;padding:14px 28px;background:{BRAND_INK};color:{BRAND_CREAM};border-radius:8px;text-decoration:none;font-weight:600;font-size:14px;">
      Book a Free Consultation →
    </a>
    """
    return _wrap_email(inner)


def send_email(to_email: str, subject: str, html_body: str) -> None:
    if not settings.smtp_user or not settings.smtp_app_password:
        print(f"[email_service] SMTP not configured — skipping send to {to_email} ({subject})")
        return

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = f"{settings.email_from_name} <{settings.smtp_user}>"
    message["To"] = to_email
    message.attach(MIMEText(html_body, "html"))

    app_password = settings.smtp_app_password.replace(" ", "")

    with smtplib.SMTP_SSL(settings.smtp_host, 465, context=ssl.create_default_context()) as server:
        server.login(settings.smtp_user, app_password)
        server.sendmail(settings.smtp_user, [to_email], message.as_string())
