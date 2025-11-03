sudo apt update && sudo apt install -y python3-pip libatlas-base-dev
pip install -r requirements.txt
sudo modprobe v4l2loopback
echo "Boot complete. Run: python infer.py"
