I installed the following packages:

pip install deepsensor
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

I needed to downgrade numpy because there was an issue with the latest version.
python -m pip install numpy==1.26.0