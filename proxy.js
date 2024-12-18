const express = require('express');
const fetch = require('node-fetch');
const cors = require('cors');
const app = express();

// Используем cors для разрешения запросов с вашего фронтенда
app.use(cors({
    origin: '*', // Разрешаем все источники для тестов
    methods: ['GET', 'POST'],
    allowedHeaders: ['Content-Type'],
}));

// Устанавливаем заголовок Content Security Policy (CSP) для разрешения изображений
app.use((req, res, next) => {
    res.setHeader('Content-Security-Policy', "default-src 'self'; img-src 'self' https://yastatic.net;");
    next();
});

// Разрешаем обработку JSON
app.use(express.json());

// Маршрут для обработки запросов от фронтенда
app.post('/proxy', async (req, res) => {
    try {
        // Делаем запрос к удаленному API (например, rgz2.onrender.com)
        const response = await fetch('https://rgz2.onrender.com', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(req.body), // Перенаправляем данные от клиента
        });

        // Если ответ успешен, отправляем данные обратно на клиент
        if (response.ok) {
            const data = await response.json();
            res.json(data);
        } else {
            // Если API возвращает ошибку, отправляем ошибку 500
            res.status(500).json({ error: 'Ошибка при запросе к серверу' });
        }
    } catch (error) {
        // Логируем ошибку и отправляем ответ с ошибкой
        console.error('Ошибка запроса:', error);
        res.status(500).json({ error: 'Ошибка при запросе к серверу' });
    }
});

// Запуск сервера на нужном порту
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Сервер работает на порту ${PORT}`);
});
