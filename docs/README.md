<style>
a.cta {
  background-color: #FFE55A;
  border-radius: 50px;
  font-family: Roboto, Helvetica, sans-serif;
  font-weight: normal;
  font-size: 1.6rem;
  padding: 12px 60px;
  margin: auto;
  margin-top: 0;
  text-align: center;
  color: #0b0080;
  text-decoration: None;
}
.splash-end img, .splash-end a {
  box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
}
.splash-start p {
  display: flex;
  align-items: center;
  gap: 6px;
}
.splash-start p img {
  height: 30px;
}

</style>

<div class="splash">
<div class="splash-start">

<div class="splash-logo" style="display:flex;align-items:center;">
    <img src="https://juncture-digital.github.io/juncture/static/images/favicon.svg" style="margin:-12px 0 0 -12px;height:90px">
    <div style="font-size:3rem;color:#455;margin-top:-10px;font-weight:bold;">Juncture</div>
</div>

<h3 style="line-height:1.3;margin-top:1rem;"><i>Create and share rich, interactive essays in minutes!</i></h3>

- Quickly create single essays or full web sites
- Minimal setup and no ongoing administration
- Easy-to-use drag-n-drop editor with preview
- Flexible content viewers for displaying images, video, audio, maps, diagrams, and more
- Use web-based resources and your own content
- Image and text annotation tools
- IIIF-enabled features for using high-quality, attributed digital objects
- WordPress compatible
- Open source and built on open tools and data formats

Juncture was developed and is maintained by [![JSTOR](https://raw.githubusercontent.com/juncture-digital/juncturemain/static/images/labs.jpg)](https://labs.jstor.org)

</div>
<div class="splash-end">
    <div style="display:flex; flex-direction:column; align-items:center; gap:2rem;">
        <img class="splash-image" src="https://iiif-image.juncture-digital.org/iiif/2/e058046a1379d7dfc9a4daee11a9a6ca1b7ac9bafd78fd30d40ff92fef99ce86/full/500,/0/default.jpg" alt="Juncture graphic">
        <div><a href="#/getting-started" class="cta">Get Started</a></div>
    </div>
</div>
</div>

# Welcome to Juncture

**Juncture** is a suite of tools and services that enable anyone to easily create engaging web pages with rich visualizations, including interactive images, videos, maps, and more.  

Juncture is developed and maintained by the friendly folks at [JSTOR Labs](https://labs.jstor.org) and [grew out of a project](https://www.doaks.org/research/mellon-initiatives/plant-humanities-initiative) that used visual essays for a form of digital storytelling.  Visual essays are text narratives augmented with interactive visualizations providing depth and context.  

This version of Juncture represents the second generation of the Juncture concept.  It's a complete rewrite of the Juncture code base and documentation.  The rendering engine in version 2 is backwards compatible with visual essays written for version 1, so if you're an existing Juncture user, no worries, your Juncture essays will continue to work.  

?> Documentation for Juncture version 1 can be found [here](https://github.com/jstor-labs/juncture/wiki).

In its current form Juncture is still well-suited for the type of digital story telling emphasized in version 1 but now can be more easily used for generating web pages that are less text-centric, such as an image exhibitions.

A few examples are provided to help explain what Juncture is.  Press any of the buttons below for a quick demo.

<ve-modal button-label="Hello, Juncture" src="juncture-digital/juncture/examples/hello-juncture"></ve-modal> <ve-modal button-label="Bedroom in Arles" src="juncture-digital/juncture/examples/bedroom-in-arles"></ve-modal>

# What problem does this solve?

Juncture's primary goal is to make the use of modern web technology (deep-zoom and panning for high-resolution images, interactive maps, etc) accessible to anyone with an interest in sharing something on the web, regardless of background or technical skills.  In the [Quick Start guide](/quick-start) you can give it try and see for yourself.  All that is required for this quick start (and to use Juncture generally) is an active Github account.  If you already have one the "hard" part is done.  If not, you'll need to take a take a couple minutes to signup with Github.  Signing up for a Github account is free and painless.

If you're looking for a set of easy-to-use tools for quickly creating web pages with engaging and interactive content with minimal setup and zero on-going administration, Juncture might be exactly what you need.

# Juncture design principles

In developing Juncture we were guided by a few key principles.

1. **Juncture will not store user data.** **  We just want to make it easier for you to use it to create and share great web content.
    - Many web hosting services store a copy of the source files used to render a web page or site.  Juncture does not.  It is principally an HTML rendering engine and set of authoring tools.  Content is stored in a Github repository that is user owned and managed.  Juncture only requires read access to the Github repository to access the files for rendering.
    - The Juncture tool suite includes an optional browser-based editor that may be used to create and modify user files in Github.  When using the Juncture editor a user will first need to authorize the editor to perform Github file updates on their behalf.  This authorization can be easily revoked by a user at any time.
    - ** The only caveat to the "Juncture does not retain user data" principle is that an optimized copy of user-hosted image files used in a rendered page are cached by the Juncture image server for a fixed period of time for performance reasons.
2. **Juncture will use open and non-proprietary tools and data where possible.**  This includes:
    - Markdown (with a few Juncture extensions) for visual essay definitions
    - The International Image Interoperability Framework (IIIF) for media (image, video, audio) rendering
    - GeoJSON for map features and overlays
    - Various data and services provided by the Wikimedia Foundation, including text from Wikipedia, Linked Open Data (LOD) from Wikidata, and images and other media from Wikimedia Commons
3. **Support and promote the responsible use of web resources**  All resources used in a visual essay include attribution when required and clearly define reuse rights. 
3. **Minimal setup and administration by a user.**  Some initial work is needed by a user to create a home for the content to be rendered by Juncture.  That's where Github comes in.  To get started a user must signup for a Github account and link it to the Juncture editor.  For many users.that's it.  There is no on-going administration required of a user.  No cloud infrastructure provisioning, no server management, nothing of that sort. A user is able to focus time and energy on creating great content. The only exception to this would be the setup of a custom domain for a Juncture web site if that was desired.  A step-by-step build is provided for custom domain setup. It would typically require no more than a few minutes of time.   

The Juncture tools and services are designed to work together to provide an integrated and easy-to-use work-flow for web page definition and rendering.  These tools are based on web standards and may also be used separately.

The definition of a Juncture web page is performed using plain text.

- Web page creation and hosting
- IIIF services

Uses of Juncture include:

- Creation of a web site containing themed essayy
- 
