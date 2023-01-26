<div style="display:flex; align-items:center; width:100%; gap:18px; margin-bottom:2rem;">
    <div style="width:50%;">
        <div style="display:flex;align-items:center;">
            <img src="https://juncture-digital.github.io/juncture/static/images/favicon.svg" style="margin-left:-12px;height:90px">
            <div style="font-size:3rem;color:#455;margin-top:-10px;font-weight:bold;">Juncture</div>
        </div>
        <div style="padding-right:12px;">
            <h4><i>Create and share rich, interactive essays in minutes!</i></h4>
            <ul style="padding-right:1rem;">
                <li>Quickly create single visual essays and complete web sites (including using custom domains)</li>
                <li>Zero setup (all that is needed to get started is a free Github account)</li>
                <li>Zero ongoing administration</li>
                <li>Easy to use drag-n-drop essay editor</li>
                <li>Flexible content viewers for displaying images, video, audio, maps, diagrams, and more</li>
                <li>Use web-based resources as well as your own content</li>
                <li>Easy to use tools for image and essay annotation</li>
                <li>IIIF-enabled features for using high-quality, attributed digital objects</li>
                <li>Juncture components can be used outside of Juncture environment, for instance in vanilla HTML or WordPress site</li>
                <li>Open source and built on open tools and data formats</li>
            </ul>
        </div>
    </div>
    <!-- <img src="https://raw.githubusercontent.com/juncture-digital/juncture/dev/static/images/create-with-juncture.svg" style="width:40%;margin-left:12px;""> -->
    <img src="https://iiif-image.juncture-digital.org/iiif/2/3cfe1031e8afcb3b90b817fa4f2f937462786fd78f87954ca684152c42516675/full/500,/0/default.jpg" style="width:50%; height:100%;margin:auto; border-radius:3px; box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
">
</div>

# Welcome to Juncture

**Juncture** is a suite of tools and services that enable anyone to easily create engaging web pages with rich visualizations, including interactive images, videos, maps, and more.  

Juncture is developed and maintained by the friendly folks at JSTOR Labs and grew out of a project that used visual essays for a form of digital storytelling.  Visual essays are text narratives augmented with interactive visualizations providing depth and context.  

This version of Juncture represents the second generation of the Juncture concept.  It's a complete rewrite of the Juncture code base and documentation.  The rendering engine in version 2 is backwards compatible with visual essays written for version 1, so if you're an existing Juncture user, no worries, your Juncture essays will continue to work.  

?> If you came to this page looking for documentation for Juncture version 1, that can be found [here](https://github.com/jstor-labs/juncture/wiki).

In its current form Juncture is still well-suited for the type of digital story telling emphasized in version 1 but now can be more easily used for generating web pages that are less text-centric, such as an image exhibitions.

A few examples are provided to help explain what Juncture is.  Press any of the buttons below for a quick demo.

<ve-modal button-label="Hello, Juncture" src="juncture-digital/juncture/examples/hello-juncture"></ve-modal> <ve-modal button-label="Bedroom in Arles" src="juncture-digital/juncture/examples/bedroom-in-arles"></ve-modal>

# What problem does this solve?

Juncture's primary goal is to make the use of modern technology (like deep-zoom with high resolution images, interactive maps, etc) accessible to anyone with an interest in sharing something on the web, regardless of background or technical skills.  In the [Quick Start](/quick-start) section below you can give it try and see for yourself.  All that is required for this quick start (and to use Juncture generally) is an active Github account.  If you already have one the "hard" part is done.  If not, you'll need to take a take a couple minutes to signup with Github.  Signing up is free and painless, really.

If you're looking for leading edge capabilities in image display, map rendering, etc, then Juncture may not be the best fit.  On the other hand, if you're looking for a set of easy-to-use tools for quickly creating web pages with engaging and interactive content with minimal setup and zero on-going administration, Juncture might be exactly what you need.

# Juncture design principles

In developing Juncture we were guided by a few key principles.

1. **Juncture will not retain user data** **  It's your data, we just want to make it easier for you to use it to create and share great web content.
    - Many web hosting services store a copy of the source files used to render a web page or site.  Juncture does not.  It is principally a set of rendering engine and authoring tools.  User content is stored in a Github repository that is owned and managed by a user.  Juncture only requires read access to the Github repository to access the files for conversion and rendering.
    - The Juncture tool suite includes an optional browser-based editor that may be used to create and modify user files in Github.  When using the Juncture editor a user must authorize the editor to perform Github file updates on their behalf.  This authorization can be easily revoked by a user at any time.
    - ** The only caveat to the "Juncture does not retain user data" principle is that an optimized copy of user-hosted image files used in a rendered page are cached by the Juncture image server for a fixed period of time for performance reasons.
2. **Juncture will use open and non-proprietary tools and data where possible**.  This includes:
    - Markdown (with a few Juncture extensions) for page definitions
    - The International Image Interoperability Framework (IIIF) for media (image, video, audio) rendering
    - GeoJSON for map features and overlays
    - Various data and services provided by the Wikimedia Foundation, including text from Wikipedia, Linked Open Data (LOD) from Wikidata, and images and other media from Wikimedia Commons
3. **Promote the responsible use of web resources** ...
3. **Minimal setup and administration by a user.**  This could have been "_Zero_ setup and administration" but some initial work is needed by a user to create a home for the content to be rendered by Juncture.  When Juncture is used to render custom content a user must signup for a Github account and populate a Github repository (workspace) with page definition files.  Other than creating the page definition files and providing a home for them in Github, there is nothing required by a user long-term.  No cloud infrastructure provisioning, no server management, nothing of that sort. A user is able to focus time and energy on creating great content. 

The Juncture tools and services are designed to work together to provide an integrated and easy-to-use work-flow for web page definition and rendering.  These tools are based on web standards and may also be used separately.

The definition of a Juncture web page is performed using plain text.

- Web page creation and hosting
- IIIF services

Uses of Juncture include:

- Creation of a web site containing themed essayy
- 
