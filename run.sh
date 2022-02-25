#!usr/bin/bash
#Open Source Nih Ajg
#Kalo Mau Ubah Kasih Credit Ajg
clear
main() {
echo -e "
1.Cari Manga
2.Install Bahan Rempah (Disarankan)
3.Join EXECUTE TEAM
4.Report Tools
5.Exit Tools"
echo
read -p "Pilih Menu > " pil
if [[ $pil == 1 ]]; then
python login.py
fi
if [[ $pil == 2 ]]; then
echo -e "[•] Installing Data..."
pkg install python &> /dev//null
pkg install python2 &> /dev//null
pip install requests &> /dev//null
pip2 install requests &> /dev//null
pip install bs4 &> /dev//null
pip2 install bs4 &> /dev//null
pip install colorama &> /dev//null
pip2 install colorama &> /dev/null
echo -e "[•] Done Installing Data..."
main
fi
if [[ $pil == 3 ]]; then
python sishej.py
fi
if [[ $pil == 5 ]]; then
echo "THX FOR USING TOOLS"
fi
if [[ $pil == 4 ]]; then
python report.py
fi
if [[ $pil == '' ]]; then
echo "[!] Input Yang Bener:)"
sleep 3
bash run.sh
fi
}
main
