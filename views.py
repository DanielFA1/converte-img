from main import app
from flask import render_template, request, send_file
from PIL import Image
import io
import os
import zipfile

@app.route('/')
def hello_word():
    return render_template('index.html')

@app.route('/converter', methods=['GET', 'POST'])
def converter():
    if request.method == 'GET':
        return render_template('index.html')

    arquivos = request.files.getlist('imagens')
    formato  = request.form['formato'].upper()
    nomes    = request.form.getlist('nomes') 

    ext = 'jpg' if formato == 'JPEG' else formato.lower()

    def converter_imagem(arquivo, nome_base):
        imagem = Image.open(arquivo)

        if formato == 'JPEG' and imagem.mode in ('RGBA', 'P'):
            imagem = imagem.convert('RGB')

        buf = io.BytesIO()
        imagem.save(buf, format=formato)
        buf.seek(0)
        return buf, nome_base + '.' + ext

    if len(arquivos) == 1:
        arquivo = arquivos[0]
        nome = nomes[0].strip() if nomes and nomes[0].strip() else os.path.splitext(arquivo.filename)[0]
        buf, filename = converter_imagem(arquivo, nome)

        return send_file(
            buf,
            mimetype='image/' + ext,
            as_attachment=True,
            download_name=filename
        )

    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        for i, arquivo in enumerate(arquivos):
            nome = nomes[i].strip() if i < len(nomes) and nomes[i].strip() else os.path.splitext(arquivo.filename)[0]
            buf, filename = converter_imagem(arquivo, nome)
            zf.writestr(filename, buf.read())

    zip_buffer.seek(0)
    return send_file(
        zip_buffer,
        mimetype='application/zip',
        as_attachment=True,
        download_name='imagens_convertidas.zip'
    )
