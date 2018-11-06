import os


def process_template():
	if not os.path.isfile(os.getcwd() + '/template.md'):
		raise Exception('No se encuentra el archivo de plantilla de post')
	
	fp = os.getcwd() + '/template.md'
	with open(fp, 'r', encoding='utf8') as f:
		content = f.read()
	
	# reemplazar fecha de post y corregir enlaces (usar etiqueta ancla y optimizar SEO)


if __name__ == '__main__':
	process_template()