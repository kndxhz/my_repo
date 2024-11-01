#!/bin/bash

# 提问用户选择在线安装或本地软件包
read -p "在线安装/本地软件包（1/0）: " choice

if [ "$choice" == "1" ] || [ -z "$choice" ]; then
    # 用户选择在线安装或者输入为空（默认在线安装）
    read -p "在线安装地址: " url
    # 使用 wget 下载软件包
    wget "$url" -O /tmp/package
    if [ $? -eq 0 ]; then
        read -p "压缩包二进制？（1/0）: " is_binary
        if [ "$is_binary" == "1" ]; then
            # 检查文件类型并解压
            if [[ "$url" == *.zip ]]; then
                unzip /tmp/package -d /tmp/package_content
            elif [[ "$url" == *.tar.gz ]]; then
                tar -xzf /tmp/package -C /tmp/package_content
            else
                echo "不支持的压缩包格式。"
                exit 1
            fi
            # 让用户输入可执行文件路径
            read -p "请输入压缩包中可执行文件的路径（例如 /abc 或 /bin/abc）: " binary_path
            if [ -f "/tmp/package_content$binary_path" ]; then
                # 将可执行文件复制到 /usr/local/bin
                sudo cp "/tmp/package_content$binary_path" /usr/local/bin/
                sudo chmod +x /usr/local/bin/$(basename "$binary_path")
                echo "$(basename "$binary_path") 已成功安装到 /usr/local/bin/，可以通过命令 $(basename "$binary_path") 运行。"
            else
                echo "找不到可执行文件，请检查路径是否正确。"
                exit 1
            fi
        elif [[ "$url" == *.snap ]]; then
            # 安装snap文件，使用 --dangerous 选项
            sudo snap install /tmp/package --classic --dangerous || {
                echo "安装snap失败，请检查包是否有效。"
                exit 1
            }
        elif [[ "$url" == *.rpm ]]; then
            # 安装rpm文件
            sudo rpm -i /tmp/package || {
                echo "安装rpm失败，请检查包是否有效。"
                exit 1
            }
        else
            # 安装下载的deb文件
            sudo dpkg -i /tmp/package
            sudo apt-get install -f
        fi
        # 删除临时文件
        rm -f /tmp/package
        rm -rf /tmp/package_content
    else
        echo "下载失败，请检查URL是否正确。"
        exit 1
    fi
elif [ "$choice" == "0" ]; then
    # 用户选择本地软件包
    read -p "软件包安装路径: " package_path
    if [ -f "$package_path" ]; then
        read -p "压缩包二进制？（1/0）: " is_binary
        if [ "$is_binary" == "1" ]; then
            # 检查文件类型并解压
            if [[ "$package_path" == *.zip ]]; then
                unzip "$package_path" -d /tmp/package_content
            elif [[ "$package_path" == *.tar.gz ]]; then
                tar -xzf "$package_path" -C /tmp/package_content
            else
                echo "不支持的压缩包格式。"
                exit 1
            fi
            # 让用户输入可执行文件路径
            read -p "请输入压缩包中可执行文件的路径（例如 /abc 或 /bin/abc）: " binary_path
            if [ -f "/tmp/package_content$binary_path" ]; then
                # 将可执行文件复制到 /usr/local/bin
                sudo cp "/tmp/package_content$binary_path" /usr/local/bin/
                sudo chmod +x /usr/local/bin/$(basename "$binary_path")
                echo "$(basename "$binary_path") 已成功安装到 /usr/local/bin/，可以通过命令 $(basename "$binary_path") 运行。"
            else
                echo "找不到可执行文件，请检查路径是否正确。"
                exit 1
            fi
        elif [[ "$package_path" == *.snap ]]; then
            # 安装snap文件，使用 --dangerous 选项
            sudo snap install "$package_path" --classic --dangerous || {
                echo "安装snap失败，请检查包是否有效。"
                exit 1
            }
        elif [[ "$package_path" == *.rpm ]]; then
            # 安装rpm文件
            sudo rpm -i "$package_path" || {
                echo "安装rpm失败，请检查包是否有效。"
                exit 1
            }
        else
            # 安装本地deb文件
            sudo dpkg -i "$package_path"
            sudo apt-get install -f
        fi
    else
        echo "文件不存在，请检查路径是否正确。"
        exit 1
    fi
else
    echo "无效的输入，请输入1或0。"
    exit 1
fi

echo "安装完成！"
