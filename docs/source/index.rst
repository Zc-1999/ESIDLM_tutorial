.. ESIDLM documentation master file, created by
   sphinx-quickstart on Thu Apr 27 16:28:33 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: ../images/bnu-logo.png
   :alt: bnulogo
   :scale: 40%
   :align: center

.. raw:: html

   <div style="height: 30px;"></div>

===================================================================
ESIDLM: Enhanced Spatial-Temporal Interpretable Deep Learning Model
===================================================================

.. toctree::
   :maxdepth: 2
   :hidden:
   :titlesonly:

   introduction.rst
   installation.rst
   quickstart/index.rst
   api/index.rst
   publications.rst

.. raw:: html

   <div style="height: 30px;"></div>

.. panels::
   :card: + intro-card text-center
   :column: col-2 d-flex custom-col

   ---
   .. image:: ../images/introduction.png
      :class: panel-image

   .. rst-class:: intro-card-description

   Get an overview of ESDLM and its purpose.Start your journey here

   +++
   .. link-button:: introduction
      :type: ref
      :text: Introduction
      :classes: btn-block btn-secondary stretched-link

   ---
   .. image:: ../images/installation.png
      :class: panel-image

   .. rst-class:: intro-card-description

   Learn how to install and set up ESDLM on your system

   +++
   .. link-button:: installation
         :type: ref
         :text: Installation
         :classes: btn-block btn-secondary stretched-link

   ---
   .. image:: ../images/quickstart.png
      :class: panel-image

   .. rst-class:: intro-card-description

   Jump right in and get hands-on experience with ESDLM

   +++
   .. link-button:: quickstart/index
      :type: ref
      :text: Quickstart
      :classes: btn-block btn-secondary stretched-link

   ---
   .. image:: ../images/api.png
      :class: panel-image

   .. rst-class:: intro-card-description

   Explore the comprehensive API documentation

   +++
   .. link-button:: api/index
      :type: ref
      :text: API
      :classes: btn-block btn-secondary stretched-link

   ---
   .. image:: ../images/paper.png
      :class: panel-image

   .. rst-class:: intro-card-description

   Discover research papers and other resources related to ESDLM

   +++
   .. link-button:: publications
      :type: ref
      :text: Publications
      :classes: btn-block btn-secondary stretched-link

.. raw:: html

   <div class="container">
   <div class="toggle-wrapper blue">
      <input type="checkbox" class="toggle-checkbox" onclick="jumpToCNdocument()">
      <div class="toggle-container">
         <div class="toggle-ball"></div>
      </div>
      <span class="toggle-text">切换中文文档</span>
   </div>
   </div>

   <script>
   function jumpToCNdocument() {
      if (document.querySelector('.toggle-checkbox').checked) {
         setTimeout(function() {
         window.location.href = 'https://esidlm-tutorial.readthedocs.io/zh_CN/latest/';
         }, 500); 
         }
      }
   </script>


