# Image Converter

Esse projeto nasceu de uma **necessidade bem prática do dia a dia**.

Meu pai está financiando a construção da nossa casa, e durante o processo precisamos enviar **fotos da obra dentro de uma planilha do Excel** para acompanhamento do financiamento. O problema é que o Excel **só aceita alguns formatos específicos de imagem**, e muitas fotos tiradas no celular vêm em formatos diferentes.

A primeira solução que pensamos foi usar **sites de conversão de imagem**, mas rapidamente apareceram alguns problemas:

* muitos desses sites têm **limite de conversões gratuitas por dia**
* é preciso **enviar as fotos para a internet**
* quando você precisa converter várias imagens, isso fica **bem pouco prático**

Ao mesmo tempo, meu irmão também estava passando por algo parecido ao postar **carros em sites de venda (como a OLX)**, que também aceitam apenas alguns tipos de imagem.

Então resolvi fazer algo simples: **um pequeno aplicativo para converter várias imagens direto no computador**, sem limite e sem depender de serviços online.

Assim nasceu o **Image Converter**.



## O que o aplicativo faz

* Permite selecionar **várias imagens de uma vez**
* Converte automaticamente para **formato JPG**
* Permite abrir rapidamente a pasta com as imagens convertidas


## Tecnologias utilizadas

* Python
* Tkinter (interface gráfica)
* Pillow (manipulação de imagens)
* PyInstaller (para gerar o executável)



## Como executar o projeto

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/image-converter.git
```

Entre na pasta do projeto:

```bash
cd image-converter
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o aplicativo:

```bash
python app.py
```

---

## 📦 Gerar o executável (.exe)

Caso queira gerar o executável da aplicação:

```bash
py -m PyInstaller --onefile --windowed --name ImageConverter app.py
```

O executável será gerado dentro da pasta:

```
dist/
```
