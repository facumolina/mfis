---
title: "MFIS - Tools"
layout: textlay
excerpt: "Tools"
sitemap: false
permalink: /tools/
---

## **Tools**


<div style="padding-left: 20px;">

{% for tool in site.data.tools %}

<h4><a href="{{tool.web}}" target="_blank">{{tool.name}}</a></h4>

<div class="row">
<div class="col-sm-10 clearfix">
  <i>{{ tool.description }}<br></i>
  <ul style="overflow: hidden">
  </ul>
</div>
</div>

{% endfor %}

</div>