import asyncio
from pypinyin import pinyin


async def get_initials(chinese_str):
    initials = [word[0][0].upper() for word in pinyin(chinese_str)]
    return "".join(initials)


async def main():
    try:
        with open("names.txt", "r", encoding="utf-8") as f:
            names = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("names.txt文件未找到")
        return

    # 创建首字母到名字的映射
    initials_dict = {}
    initials = await asyncio.gather(*[get_initials(name.strip()) for name in names])

    for idx, initial in enumerate(initials):
        if initial not in initials_dict:
            initials_dict[initial] = []
        initials_dict[initial].append(names[idx])

    print("对应字典:", initials_dict)

    name = input("输入缩写: ")
    name = name.upper()

    # 查找对应的名字
    if name in initials_dict:
        print("找到的名字:", initials_dict[name])
    else:
        print("未找到")


if __name__ == "__main__":
    asyncio.run(main())
