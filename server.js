const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const port = 3000; // Ou qualquer porta que você preferir

app.use(bodyParser.urlencoded({ extended: true }));

// Servir arquivos estáticos (HTML, CSS, JS)
app.use(express.static(path.join(__dirname, 'public')));

// Rota para processar o formulário
app.post('/processar-formulario', (req, res) => {
    const { name, email, Senha } = req.body;

    // Armazenar os dados ou processar conforme necessário
    // Aqui estamos apenas enviando os dados como parte do corpo da resposta

    res.redirect(`/teste.html?name=${encodeURIComponent(name)}&email=${encodeURIComponent(email)}&Senha=${encodeURIComponent(Senha)}`);
});

app.listen(port, () => {
    console.log(`Servidor rodando na porta ${port}`);
});
