# Conversor de Imagens

Cansado de precisar converter uma imagem e ter que aguentar anúncio em cima de anúncio, delay artificial, página travando — tudo isso pra algo que leva menos de um segundo?

Criei esse projeto por conta própria pra resolver exatamente isso. Roda local, sem anúncios, sem espera, sem nada armazenado. Só converte e entrega.

---

## Preview

![Interface do conversor](example.png)

## O que faz

- Converte entre **PNG, JPG, WEBP e BMP**
- Aceita **múltiplos arquivos** de uma vez (retorna `.zip`)
- Permite **renomear cada arquivo** de saída individualmente
- Valida nomes duplicados
- Processamento 100% local — nenhum arquivo é salvo no servidor

## Tecnologias

- Python + Flask
- Pillow
- HTML/CSS/JS puro (sem frameworks)

## Como rodar

**1. Clone o repositório**
```bash
git clone https://github.com/DanielFA1/converte-img.git
cd converte-img
```

**2. Instale as dependências**
```bash
pip install flask pillow
```

**3. Inicie o servidor**
```bash
python main.py
```

**4. Acesse no navegador**
```
http://localhost:5000
```
