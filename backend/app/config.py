from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    frontend_url: str = "http://localhost:5173"
    environment: str = "development"
    secret_key: str = "dev-secret-change-me-in-production"

    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 465
    smtp_user: str = ""
    smtp_app_password: str = ""
    email_from_name: str = "Global Digital Skills Assessment"

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
