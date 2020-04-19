import re
import string
# 解析内容并生成目录
with open('KBQA Industry.md', 'r', encoding='utf-8') as f:
	for line in f:
		if line.startswith("#"):
		
			line = line.strip().split(" ", 1)

			# 缩进
			indentation = "&emsp;" * 2 * (len(line[0]) - 1)

			# 标题
			title = line[1].replace(" ", "&nbsp;")

			# 去掉特殊字符，空格替换为-
			herf = re.compile(r'<[^>]+>',re.S).sub('', line[1])
			herf = herf.translate(str.maketrans('', '', string.punctuation))
			herf = herf.replace(" ", "-")

			out_line = "%s[%s](#%s)\n"%(indentation, title, herf)
		
			print(out_line)
