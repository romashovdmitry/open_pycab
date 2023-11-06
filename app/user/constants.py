class UserTelegramStatus:

    STARTED = "STARTED"  # send command /start
    WAITING_PASSWORD = "WAITING_PASSWORD"  # send email
    PASSWORD_IS_VALIDATED = "PASSWORD_IS_VALIDATED"  # password and email verified 

    USER_TELEGRAM_STATUS = [
        (STARTED, "STARTED"),
        (WAITING_PASSWORD, "WAITING_PASSWORD"),
        (PASSWORD_IS_VALIDATED, "PASSWORD_IS_VALIDATED")
    ]