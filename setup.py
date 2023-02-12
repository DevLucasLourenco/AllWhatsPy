from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='allwhatspy_awp',
    version='0.0.5',
    license='MIT License',
    author='Lucas Lourenço',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='dev.lucaslourenco@gmail.com',
    keywords='whatsapp api bot mensagem automática analise de mensagem',
    description=u'Whatsapp API - Envio de Mensagem Automática - PT-BR. ',
    packages=['AllWhatsPy'],
    install_requires=['webdriver-manager', 'selenium'],)