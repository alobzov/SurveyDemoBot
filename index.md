---
layout: default
date: 2023-10-02
title: Бот для проведения опросов через Telegram
description: Это описание моего Pet-проекта по проведению опросов через Telegram
author: Алексей Лобзов
keywords: алексей лобзов, опрос, проведение опросов, telegram, telegram-бот
---

# {{ page.title }}

<div class="subline">
  <time datetime="{{ page.date | date-to_xmlschema }}">
    {% assign m = page.date | date: "%-m" %}
    {{ page.date | date: "%-d" }}
    {% case m %}
      {% when '1' %}января
      {% when '2' %}февраля
      {% when '3' %}марта
      {% when '4' %}апреля
      {% when '5' %}мая
      {% when '6' %}июня
      {% when '7' %}июля
      {% when '8' %}августа
      {% when '9' %}сентября
      {% when '10' %}октября
      {% when '11' %}ноября
      {% when '12' %}декабря
    {% endcase %}
    {{ page.date | date: "%Y" }}
  </time>
</div>

[Бот](https://github.com/alobzov/SurveyDemoBot) предназначен для иллюстрации проведения опросов через Telegram.

Бот загружает вопросы (с ответами по [шкале Лайкерта](https://ru.wikipedia.org/wiki/Шкала_Ликерта)) из файла ``Affirmations.txt`` и направляет их пользователю. Ответы пользователя записываются в файл ``XXXXXXXXX_Answers.txt``. Опрос запускается каждый раз, когда пользователь вводит команду ``/start`` либо получены ответы на все вопросы.

Результаты исследования бота и его модификаций приведены в статьях:

1. Лобзов А.В. Использование мессенджеров в маркетинговых исследованиях // Маркетинг и маркетинговые исследования. — 2017. — No2. — С.92–98. URL: [https://grebennikon.ru/article-zsq3.html](https://grebennikon.ru/article-zsq3.html)

2. Лобзов А.В. Использование мессенджеров для оптимизации затрат некоммерческой организации // Менеджмент сегодня. — 2018. — No1. — С.52–59. URL: [https://grebennikon.ru/article-5cq9.html](https://grebennikon.ru/article-5cq9.html)

3. Лобзов А.В. Факторы использования мессенджеров аудиторией московского клуба Toastmasters International // Реклама. Теория и практика. — 2018. — No2. — С.136–142. URL: [https://grebennikon.ru/article-yzqf.html](https://grebennikon.ru/article-yzqf.html)

4. Лобзов А.В. Использование мессенджеров для работы с аудиторией языкового клуба // Маркетинг и маркетинговые исследования. — 2018. — No2. — С.160–166. URL: [https://grebennikon.ru/article-q6b4.html](https://grebennikon.ru/article-q6b4.html)

5. Лобзов А.В. Мессенджер как канал коммуникации с аудиторией клуба Toastmasters International // Реклама. Теория и практика. — 2018. — No3. — С.198–206. URL: [https://grebennikon.ru/article-vozs.html](https://grebennikon.ru/article-vozs.html)