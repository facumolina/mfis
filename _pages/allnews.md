---
title: "Noticias"
layout: default
excerpt: "DC at Universidad Nacional de Río Cuarto"
sitemap: false
permalink: /noticias
---

## Noticias

{% for article in site.data.news %}
<p>{{ article.date }} <br>
<em>{{ article.headline }}</em></p>
{% endfor %}
