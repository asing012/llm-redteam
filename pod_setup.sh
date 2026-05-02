echo "installing deps"
apt-get update
apt-get install zstd
apt-get install lshw
curl -fsSL https://ollama.com/install.sh | sh
echo "ready"
echo "ollama serve & -- ollama pull llama3.2"