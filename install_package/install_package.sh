#!/bin/bash

# 提问用户选择在线安装或本地软件包
read -p "在线安装/本地软件包（1/0）: " choice

if [ "$choice" == "1" ] || [ -z "$choice" ]; then
    # 用户选择在线安装或者输入为空（默认在线安装）
    read -p "在线安装地址: " url
    # 使用 wget 下载软件包
    wget "$url" -O /tmp/package.deb
    if [ $? -eq 0 ]; then
        # 安装下载的软件包
        sudo dpkg -i /tmp/package.deb
        # 自动解决依赖
        sudo apt-get install -f
        # 删除下载的软件包
        rm -f /tmp/package.deb
    else
        echo "下载失败，请检查URL是否正确。"
        exit 1
    fi
elif [ "$choice" == "0" ]; then
    # 用户选择本地软件包
    read -p "软件包安装路径: " package_path
    if [ -f "$package_path" ]; then
        # 安装本地的软件包
        sudo dpkg -i "$package_path"
        # 自动解决依赖
        sudo apt-get install -f
    else
        echo "文件不存在，请检查路径是否正确。"
        exit 1
    fi
else
    echo "无效的输入，请输入1或0。"
    exit 1
fi

echo "安装完成！"
