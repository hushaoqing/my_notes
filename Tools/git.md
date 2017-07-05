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
目前存在的问题:
新打开shell终端，git push 的时候，需要再次执行 eval "$(ssh-agent -s)"， ssh-add ~/.ssh/id_rsa 两条命令，
解决方案：1.将这两条命名加入.zhsrc文件里，每次打开shell，自动执行命令。 2. 手动执行
```