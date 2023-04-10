from pathlib import Path

import dotenv
import yaml

config_dir = Path(__file__).parent.parent.resolve() / "config"

# load yaml config
with open(config_dir / "config.yml", 'r') as f:
    config_yaml = yaml.safe_load(f)

# load .env config
config_env = dotenv.dotenv_values(config_dir / "config.env")

# config parameters
telegram_token = config_yaml["telegram_token"]
openai_api_key = config_yaml["openai_api_key"]
use_chatgpt_api = config_yaml.get("use_chatgpt_api", True)
allowed_telegram_usernames = config_yaml["allowed_telegram_usernames"]
new_dialog_timeout = config_yaml["new_dialog_timeout"]
enable_message_streaming = config_yaml.get("enable_message_streaming", True)
mongodb_uri = f"mongodb://{config_env['MONGODB_HOST']}:{config_env['MONGODB_PORT']}"
mongodb_db = config_env["MONGODB_DB"]

enable_webhook = config_yaml.get("enable_webhook", False)
webhook_host = config_yaml.get("webhook_host", None)
webhook_listen = config_yaml.get("webhook_listen", "0.0.0.0")
webhook_port = config_yaml.get("webhook_port", 8443)
webhook_cert = config_yaml.get("webhook_cert", None)
webhook_key = config_yaml.get("webhook_key", None)

# chat_modes
with open(config_dir / "chat_modes.yml", 'r') as f:
    chat_modes = yaml.safe_load(f)

# models
with open(config_dir / "models.yml", 'r') as f:
    models = yaml.safe_load(f)
