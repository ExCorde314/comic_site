if grep -Fxq "deb http://ftp.debian.org/debian jessie-backports main" /etc/apt/sources.list 
then
    echo "PPA already exists" 
else
    echo "Added PPA"
    echo 'deb http://ftp.debian.org/debian jessie-backports main' >> /etc/apt/sources.list
fi