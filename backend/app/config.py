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


settings = Settings()
