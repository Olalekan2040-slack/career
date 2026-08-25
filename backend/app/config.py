from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    frontend_url: str = "http://localhost:5173"
    environment: str = "development"
    secret_key: str = "dev-secret-change-me-in-production"

    email_from_name: str = "Global Digital Skills Assessment"

    # Brevo (formerly Sendinblue) transactional email HTTP API — used instead of
    # SMTP because Render's free web services block outbound SMTP ports
    # (25/465/587) as of Sep 2025, while HTTPS (443) is never blocked.
    brevo_api_key: str = ""
    email_from_address: str = "olalekanquadri58@gmail.com"

    # Payments are temporarily deactivated platform-wide — signup replaced the
    # $1 unlock tier. Flip to True to re-enable checkout without other changes.
    payments_enabled: bool = False

    stripe_secret_key: str = ""
    stripe_webhook_secret: str = ""
    stripe_price_usd_cents: int = 100

    paystack_secret_key: str = ""
    paystack_public_key: str = ""
    paystack_amount_kobo: int = 150000

    consultation_booking_url: str = "https://calendly.com/your-handle/consultation"
    portfolio_url: str = "https://quaddev.onrender.com/"

    database_url: str = "sqlite:///./assessment.db"

    # Comma-separated list of emails auto-granted admin access on signup/login.
    admin_emails: str = "olalekanquadri58@gmail.com"

    @property
    def admin_email_list(self) -> list[str]:
        return [e.strip().lower() for e in self.admin_emails.split(",") if e.strip()]


settings = Settings()
