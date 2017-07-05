```
git clone https://github.com/hushaoqing/326.git
cd 326
#　以下部分替换hushaoqing　为自己的名字
git branch hushaoqing
git checkout hushaoqing
echo "hello" > git.txt
git add .
git commit -m "first commit"
git push origin hushaoqing
#　输入github账号密码
```

## Github SSH
```
Ubuntu:
在用户目录下操作
ssh-keygen -t rsa -b 4096 -C "hu253955106@163.com" 生成ssh钥匙
cd .ssh        
cc id_rsa.pub          进入.ssh文件夹, 复制id_ras.pub公钥，粘贴到github(cc 命令是xclip -selection c的alias)
eval "$(ssh-agent -s)" ssh-agent验证
ssh-add ~/.ssh/id_rsa  加入
ssh -T git@github.com  测试能否ssh上
git remote -v          查看git仓库远程
git remote set-url origin git@github.com:hushaoqing/my_notes.git  改为ssh方式
```