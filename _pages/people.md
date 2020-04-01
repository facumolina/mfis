---
title: "MFIS - Team"
layout: gridlay
excerpt: "Team"
sitemap: false
permalink: /people
---

## Chair

{% assign number_printed = 0 %}
{% for member in site.data.chair %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  {% if member.email %}
  <i>{{ member.info }}<br>email: <{{ member.email }}></i>
  {% else %}
  <i>{{ member.info }}<br></i>
  {% endif %}
  {% if member.web %}
  <a href="{{member.web}}" target="_blank">Web</a>
  {% endif %}
  <ul style="overflow: hidden">

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

## Faculty

{% assign number_printed = 0 %}
{% for member in site.data.faculty %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  {% if member.email %}
  <i>{{ member.info }}<br>email: <{{ member.email }}></i>
  {% else %}
  <i>{{ member.info }}<br></i>
  {% endif %}
  {% if member.web %}
  <a href="{{member.web}}" target="_blank">Web</a>
  {% endif %}
  <ul style="overflow: hidden">

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

## Members

{% assign number_printed = 0 %}
{% for member in site.data.member %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}
<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  {% if member.email %}
  <i>{{ member.info }}<br>email: <{{ member.email }}></i>
  {% else %}
  <i>{{ member.info }}<br></i>
  {% endif %}
  {% if member.web %}
  <a href="{{member.web}}" target="_blank">Web</a>
  {% endif %}
  <ul style="overflow: hidden"></ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}
