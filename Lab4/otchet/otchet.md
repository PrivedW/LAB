echo Sergei
pwd > 2.txt  whoami >> 2.txt
ls -la > otchet/files/3.txt 
chmod o-r 4.txt
chmod 755 4.md
mv 4.txt ~/otchet/files    mv 4.md ~/otchet/files
sudo chown -c root ~/otchet/files/4.md  //8
sudo useradd -mg wheel -s /bin/zsh  test_user  
sudo passwd test_user    (123321)
sudo usermod -aG wheel test_user   
cat /etc/passwd > ~/otchet/files/12.txt  //12
chmod a+w ~/otchet/files/12.txt   
sudo -P test_user
whoami > ~/otchet/files/12.txt   pwd > ~/otchet/files/12.txt   //15
sudo su
cd ..  cd test_user  pwd >> /home/sergei/otchet/files/12.txt   whoami >> /home/sergei/otchet/files/12.txt 
tail -n 2 ~/otchet/files/12.txt     
sudo userdel -r test_user 
//21  find .  -maxdepth 2 -type d -empty  >> ~/otchet/files/21.txt 
sudo find / -maxdepth 3 -user root -name "dev*" > ~/otchet/files/22.txt   //22
mkdir -p test_find/permissions test_find/time //23
touch -a -t 202401010000 ~/test_find/time/one.txt   touch -m -t 202410140000 ~/test_find/time/two.txt  //24
 touch ~/test_find/permissions/cant_write.txt ~/test_find/permissions/can_execute.txt 
 chmod a+x ~/test_find/permissions/can_execute.txt 
 chmod a-w ~/test_find/permissions/cant_write.txt //25
find ~/test_find -atime +183 -delete (-exec delete {} \; )  //26
find ~/test_find -empty -type f -perm 755 -exec chmod a-x {} \;  //27
man ls > man_ls.txt //28
grep -n '^$' man_ls.txt  //29
grep '[0-9]' ~/man_ls.txt  //30
grep "Richard M. Stallman" ~/man_ls.txt > ~/otchet/files/31.txt //31
wc -lc ~/man_ls.txt  //32
ps -u sergei > ~/otchet/files/33.txt
pgrep nano //34
pkill nano
