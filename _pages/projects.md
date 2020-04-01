---
title: "MFIS - Projects"
layout: textlay
excerpt: "Projects"
sitemap: false
permalink: /projects/
---

## **Research Projects**

<div style="padding-left: 20px;">

{% for project in site.data.projects %}

<div class="row">

<div class="col-sm-10 clearfix">
  <h4 style="color:#158CBA"> {{ project.title }} </h4>
  <b>Principal Investigator: </b><i>{{ project.investigator }}<br></i>
  <b>Funding: </b><i>{{ project.funding }}<br></i>
  <ul style="overflow: hidden">
  </ul>
</div>


</div>

{% endfor %}

</div>