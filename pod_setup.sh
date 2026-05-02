echo "installing deps"
apt-get update
apt-get install zstd
apt-get install lshw
curl -fsSL https://ollama.com/install.sh | sh
git config --global user.email "akshayc_118@hotmail.com"
git config --global user.name "Akshay"
echo "ready"
echo "ollama serve & -- ollama pull llama3.2"