# What is Juncture?

Juncture is a suite of tools and services that enable anyone to easily create engaging web pages with rich visualizations, including interactive images, videos, maps, and more.  

Juncture is developed and maintained by the friendly folks at JSTOR Labs and grew out of a project that used visual essays in a form of visual story telling.  The visual essays consisted of a text narrative augmented with interactive visualizations providing depth and context for the narrative.  

This version of Juncture represents the second generation of the Juncture concept.  It's a complete rewrite of the code base and documentation.  Juncture version 2 is backwards compatible with visual essays written for version 1, so if you're an existing Juncture user, no worries, your Juncture essays will continue to work.  If you came to this page looking for documetation for version 1 that can be found [here](https://github.com/jstor-labs/juncture/wiki).

In its current form Juncture is still well-suited for the type of digital story telling emphasized in version 1 but this new version can more be easily used for generating web pages that are less text-centric, such as an image exhibitions.

A few examples are provided to help explain what Junture is.  Press any of the buttons below for a quick demo.

<ve-modal button-label="Hello, Juncture" src="juncture-digital/juncture/examples/hello-juncture"></ve-modal> <ve-modal button-label="A Travelogue" src="juncture-digital/juncture/examples/travelogue"></ve-modal> <ve-modal button-label="Bedroom in Arles" src="juncture-digital/juncture/examples/bedroom-in-arles"></ve-modal>

# What problem does Juncture solve?

To be honest, all of the capabilities provided by Juncture can be found in any number of existing web services and tools, and often with better feature sets and polish than provided by Juncture.  Juncture aims to be a platform that lowers the bar in using some great features like deep-zoom images and interactive maps in easy to create web pages, without the overhead often involved in using many of these tools. 

Juncture's primary goal is to make great technology accessible to any user with an interest in sharing something on the web.  In the [Quick Start](#quick-start) section below you can give it spin and see for yourself.  All that is required is Github account.  If you already have one the "hard" part is done.  If not, you'll need to take a take a couple minutes to do the sign-up.  Signing up is free and painless.  

If you're looking for best of breed capabilities in image display, map rendering, etc, then Juncture may not be the best fit.  On the other hand, if you're looking for a tool set that hits the sweet-spot of providing a really nice set of tools for quickly creating web pages with engaging and interactive content with minimal setup and zero on-going administration, Juncture may be worth considering.

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
3. **Minimal setup and administration by a user.**  This could have been "_Zero_ setup and administration" but some initial work is needed by a user to create a home for the content to be rendered by Juncture.  When Juncture is used to render custom content a user must signup for a Github account and populate a Github repository (workspace) with page definition files.  Other than creating the page definition files and providing a home for them in Github, there is nothing required by a user long-term.  No cloud infrastrcture provisioning, no server management, nothing of that sort. A user is able to focus time and energy on creating great content. 

The Juncture tools and services are designed to work together to provide an integrated and easy-to-use work-flow for web page definition and rendering.  These tools are based on web standards and may also be used separately.

The definition of a Juncture web page is performed using plain text.

- Web page creation and hosting
- IIIF services

Uses of Juncture include:

- Creation of a web site containing themed essayy
- 


# Quick Start

In this Quick Start guide you'll create your own version of the `Hello, Juncture` demo essay, also linked in the [What is Juncture?](#what-is-juncture) section.  While this is a simple essay it illustrates the basic steps in creating and "publishing" and essay.  The generated essay could also be used as a starting point for more  involved essays.

### First things, first...

If you haven't already done so, you'll need to,

- [Signup for a Free Github account](https://github.com/join), and 
- **Login to Github** with Juncture.  There's a login button at the top left of this page that can be used to login to Github.  In the initial login you will be asked to authorize Juncture to make changes on your behalf (via the Juncture Editor tool).  This short video clip demonstrates the steps involved in this initial login.  After the initial login has been performed, the login/logout process is a single button click.

### Open the Juncture Editor

Once you've successfully logged in with Github (and authorized Juncture access), open the Github Editor in a new window. <ve-window href="/editor" button-label="Open Juncture Editor"></ve-window>

### Create a new essay file in Github

In the Github navigation tool at the top of the Editor window (located just below the header), select the `Add File` icon and enter the name of the essay to be created (for example, `hello-juncture`) in the input dialog that appears.  Press the `Add` button to create the new essay.  

When a file extension (such as `.md`) is not included in the name entered into the dialog, a folder with the specified named is created with a single child file named `README.md`.  _README.md_ is the Github convention for naming index files in a folder.  While we could have used the file name `hello-juncture.md` for our new essay (which would have worked perfectly fine), creating a parent folder for the essay has advantages and is generally recommended.  The main advantage is that is folder provides a convenient location for storing other files that may eventually be assocaiated with the essay.  This could include annotation files and map overlays, among others.

### Add some content

<ve-snippet>
    # Hello, Juncture

    This example illustrates the use of a few Markdown formatting tags and the incorporation of an image and a map into a Juncture  essay.

    ## Aulacophora indica

    .ve-media wc:The_Bug_Peek.jpg right

    The image depicts a leaf beetle (Aulacophora indica) (Family: Chrysomelidae; subfamily: Galerucinae) looking out from a leaf hole of Alnus nepalensis tree. Adult leaf beetles make holes in host plant leaves while feeding. They camouflage themselves with these holes.

    This image is hosted on [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:The_Bug_Peek.jpg) and was runner-up for Wikimedia Commons Picture of the Year for 2021.

    Image controls are located in the top-right corner of the image and can be seen when hovering over the image.  Controls are available for image zoom, rotation, full-screen viewing, and image repositioning.  Panning can be performed with keyboard arrow keys or by mouse click-and-drag.

    Image information can be seen when hovering the cursor over the info icon located in the top-right corner of the image.  The Image information popover includes image title, description, attribution statement, and reuse rights.

    ## Chitwan National Park, Nepal

    .ve-map Q1075023 right

    The map is centered on the Chitwan National Park in Nepal, which is the location associated with the image above.  The Wikidata identifier for Chitwan National Park is `Q1075023`.  When a map location is specified using a Wikidata ID (or QID) Juncture can automatically retrieve the geographic coordinates for map centering.

    An alternative to using a Wikidata identifier for map positioning is to use regular latitude and longitude coordinates.  In that approach the QID would be replaced with the coordinates `27.5,84.333`, resulting in an identical map.

</ve-snippet>
