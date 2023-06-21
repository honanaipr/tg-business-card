from dotenv import load_dotenv
import environ
from attr.validators import matches_re
from traceback import print_exception

load_dotenv(override=True)

TOKEN_RE = "[0-9]{8,10}:[a-zA-Z0-9_-]{35}"
REDIS_URL_RE = ".*"
@environ.config(prefix="")
class AppConfig():
    @environ.config(prefix="BOT")
    class BotConfig():
        token = environ.var(help="Telegram bot's token", validator=matches_re(TOKEN_RE))
    @environ.config(prefix="REDIS")
    class RedisConfig():
        url = environ.var(help="Redis url", validator=matches_re(REDIS_URL_RE))
    bot = environ.group(BotConfig)
    redis = environ.group(RedisConfig)

try:
    config = environ.to_config(AppConfig)
    print(config)
except Exception as e:
    print_exception(e)
    print("\n",environ.generate_help(AppConfig), "\n")
    quit()

