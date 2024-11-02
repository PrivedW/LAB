man tree (-dL [x])
tree -dL 2
cd /etc/
ls -a
ls -lX
cd .., cd home, cd sergei, mkdir structures
mkdir {2018..2023}/files, mkdir {2018..2023}/pictures, mkdir {2018..2023}/.passwords

 touch {2018..2023}/files/data.md   touch {2018..2023}/pictures/picture.png  sudo touch {2018..2023}/.passwords/.passwords.txt 

touch -mat 202401010000.00 {2018..2023}/files/data.md  
sudo touch -md 20181006 2018/.passwords/.passwords.txt  sudo touch -md 20191006 2019/.passwords/.passwords.txt   sudo touch -md 20201006 2020/.passwords/.passwords.txt sudo touch -md 20211006 2021/.passwords/.passwords.txt   sudo touch -md 20221006 2022/.passwords/.passwords.txt sudo touch -md 20231006 2023/.passwords/.passwords.txt 
cp -rf structures/2023 Downloads/2025 
touch -md 20251006 Downloads/2025/.passwords/.passwords.txt 
cp -rf Downloads/2025 structures/2025    
mv structures/2025 structures/2024       
cd structures  mv 2018/pictures/picture.png 2018/pictures/image.png  mv 2019/pictures/picture.png 2019/pictures/image.png  mv 2020/pictures/picture.png 2020/pictures/image.png  mv 2021/pictures/picture.png 2021/pictures/image.png    mv 2022/pictures/picture.png 2022/pictures/image.png     mv 2023/pictures/picture.png 2023/pictures/image.png     mv 2024/pictures/picture.png 2024/pictures/image.png 
mv 2018 ~/Documents/2018 & mv 2024 ~/Documents/2024 
rmdir -r ~/Documents/2024
rm -r ~/Documents/2024     __step20made__ 
cat >structures/2019/files/data.md
nano structures/2020/files/data.md   
cat structures/2020/files/data.md > structures/2022/files/data.md    
mkdir structures/soft_links structures/hard_links  
{
for Num in {2019..2023}; do                                               
  ln -s ~/structures/$Num $Num
done
} // 26

ln  ~/structures/2020/files/data.md data.md & sudo ln ~/structures/2021/.passwords/.passwords.txt passwords.txt //27
mkdir archives   //28
mv ~/Downloads/image.jpg ~/structures/archives  //30
tar -cf image.tar structures/archives/image.jpg     tar -czf image.tar.gz structures/archives/image.jpg   tar -cjf image.tar.bz2 structures/archives/image.jpg  
zip -er structures.zip structures/        