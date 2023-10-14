from setuptools import setup

with open(r"README.md", "r") as arq:
    readme = arq.read()

setup(name='allwhatspy',
    version='0.2.00.5',
    license='MIT License',
    author='Lucas Lourenço',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='dev.lucaslourenco@gmail.com',
    keywords='whatsapp api bot mensagem automática analise whatsappAPI allwhatspy awp allwhatspy-awp wrapper message contact analysis github',
    description=u'Whatsapp Wrapper - Envio de Mensagem Automática - PT-BR. ',
    packages=['AllWhatsPy'],
    install_requires=['webdriver-manager', 'selenium', 'requests'],)