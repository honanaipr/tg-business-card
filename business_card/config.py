from traceback import print_exception

import environ
from attr.validators import matches_re, optional
from dotenv import load_dotenv

load_dotenv()

TOKEN_RE = "[0-9]{8,10}:[a-zA-Z0-9_-]{35}"
REDIS_URL_RE = "redis://.+:[0-9]+/.+"
HOSTNAME_RE = ".+"
PORT_RE = "[0-9]+"

vault = environ.secrets.VaultEnvSecrets(vault_prefix="BOT")
@environ.config(prefix="")
class AppConfig():
    debug = environ.bool_var(help="Redis url", default=False)
    @environ.config(prefix="BOT")
    class BotConfig():
        token = vault.secret(help="Telegram bot's token")
    @environ.config(prefix="REDIS")
    class RedisConfig():
        url = environ.var(help="Redis url", validator=optional(matches_re(REDIS_URL_RE)), default=None)
        host = environ.var(help="Redis host", validator=optional(matches_re(HOSTNAME_RE)), default=None)
        port = environ.var(help="Redis port", validator=optional(matches_re(PORT_RE)), default=None)
    bot = environ.group(BotConfig)
    redis = environ.group(RedisConfig)

try:
    config = environ.to_config(AppConfig)
except Exception as e:
    print_exception(e)
    print("\n",environ.generate_help(AppConfig), "\n")
    quit()

