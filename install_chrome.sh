# Crear el archivo install_chrome.sh con el script necesario
@"
#!/usr/bin/env bash
set -o errexit

STORAGE_DIR=/opt/render/project/.render

if [[ ! -d \$STORAGE_DIR/chrome ]]; then
  echo \"...Descargando Chrome\"
  mkdir -p \$STORAGE_DIR/chrome
  cd \$STORAGE_DIR/chrome
  wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  dpkg -x ./google-chrome-stable_current_amd64.deb \$STORAGE_DIR/chrome
  rm ./google-chrome-stable_current_amd64.deb
  cd \$HOME/project/src
else
  echo \"...Usando Chrome desde caché\"
fi

pip install -r requirements.txt
"@ | Out-File -FilePath install_chrome.sh -Encoding UTF8
