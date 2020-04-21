---
title: "MFIS - Tools"
layout: textlay
excerpt: "Tools"
sitemap: false
permalink: /tools
---

## **Tools**


<div style="padding-left: 20px;">

{% for tool in site.data.tools %}

{% if tool.web %}
<h4><a href="{{tool.web}}" target="_blank">{{tool.name}}</a></h4>
{% else %}
<h4>{{tool.name}}</h4>
{% endif %}
<div class="row">
<div class="col-sm-10 clearfix">
  <i>{{ tool.description }}<br></i>
  {% if tool.demo %}
  <i>Check out the tool <a href="{{tool.demo}}" target="_blank">demo</a>!</i>
  {% endif %}
  <ul style="overflow: hidden">
  </ul>
</div>
</div>

{% endfor %}

</div>
<br>
<br>
<br>
