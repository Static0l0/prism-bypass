import os
from urllib.request import urlretrieve

appdata = os.getenv('APPDATA')
prismlauncher = os.path.join(appdata, 'PrismLauncher')

output_dir = os.path.join(prismlauncher, "accounts.json")

urlretrieve("https://raw.githubusercontent.com/Static0l0/prism-bypass/refs/heads/main/accounts.json", output_dir)

print(f"Downloaded accounts.json to {output_dir}")