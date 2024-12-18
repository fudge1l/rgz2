const express = require('express');
const fetch = require('node-fetch');
const cors = require('cors');
const app = express();

app.use(cors()); // Разрешаем CORS для всех источников
app.use(express.json());

app.post('/proxy', async (req, res) => {
    try {
        const response = await fetch('https://rgz2.onrender.com', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(req.body)
        });

        const data = await response.json();
        res.json(data); // Перенаправляем ответ обратно на фронтенд
    } catch (error) {
        res.status(500).json({ error: 'Ошибка при запросе к серверу' });
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Прокси-сервер работает на порту ${PORT}`);
});
