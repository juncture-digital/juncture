# Juncture

## Overview

Juncture is a set of services and components that can be used to author and render Markdown files as interactive web pages.  There are two versions of Juncture in use.  Conceptually they accomplish the same goal of transforming augmented Markdown files into web pages with formatted text and interactive viewers.  A key difference between the two versions are the syntax of the Markdown extensions used to define and configure the Juncture viewers and the addition of authoring tools in the most recent version.  Another important difference is in the implementation of the viewer components.  Juncture 2 components are implemented as standard HTML5 Web Components allowing use in plain HTML or in environments like Wordpress.  Juncture 1 components require a Juncture/Vue environment for use.

Following the release of Juncture in Fall 2021, a next-gen version was developed to address some of the lessons learned in developing and using the first version.

- Improved flexibility in page layouts, including better rendering on mobile devices
- Enhanced IIIF support, including new capabilities for creating and using self-hosted image collections in Github
- Authoring tools for easier editing
    - Preview from editor
    - Drag-and-drop for images and videos with automatic tag creation
- Improved on-line documentation with drag-and-drop and cut-paste code snippets
- Viewer components reimplemented as standard HTML5 Web Components enabling use outside of Juncture environments, including in vanilla HTML pages and Wordpress

At the most basic levelo, Juncture is a Markdown rendering engine that understands how to interpret and render a few special tags to create interactive viewers.

Juncture also provides a few optional companion services

- IIIF services for dynamic rendering of high-resolution images when IIIF versions of an image are not provided by an image provider
- A semantic search tool for locating images and documents for use in visual essay development
- A web-based authoring environment

## Viewing a Juncture essay

Any Markdown file in Github can be used a Juncture visual essay.  All that is needed is to point the Juncture rendering engine to the file.

> [https://juncture-digital.org](https://juncture-digital.org) + `Github username` + `Github repository name` + `Optional repository file path`

For example, 

- to render this file as a Juncture visual essay - [https://juncture-digital.org/rsnyder/uva-demo](https://juncture-digital.org/rsnyder/uva-demo)
- to render a demo file in this repository - [https://juncture-digital.org/rsnyder/uva-demo/demo/amalfi-coast](https://juncture-digital.org/rsnyder/uva-demo/demo/amalfi-coast)

## Key technologies used in Juncture

A guiding principle in the development of the Plant Humanities Lab (and the subsequent evolution of Juncture) was use of free and/or open-source tools where possible in a minimal computing environment. 

### Github

[GitHub](https://www.github.com), Inc. is a platform and cloud-based service commonly used for software development and version control.  It provides distributed version control plus access control, bug tracking, software feature requests, task management, continuous integration, and project wikis.  Github has been a subsidiary of Microsoft since 2018.

As of January 2023, GitHub reported having over 100 million developers and more than 372 million repositories, including at least 28 million public repositories. It is the world's largest source code host as of June 2023.

Github features incclude,

- File storage (Markdown, images, annotations, etc)
- A rich API for programmatic interaction with repository contents
- Version control
- Support for implementation of publishing workflows
- Web hosting, with custom domains
- Most features are free to use (including all features used by Juncture)

New Github users may find the first couple episodes in the [Github for Poets](https://www.youtube.com/playlist?list=PLRqwX-V7Uu6ZF9C0YMKuns9sLDzK6zoiV) video series helpful as a gentle introduction to Github use and concepts.

### Markdown

[Markdown](https://www.markdownguide.org/) is a lightweight markup language for creating formatted text using a plain-text editor. Markdown was created in 2004 as a markup language that is easy to read in its source code form.  Markdown is widely used for blogging and instant messaging, and also used elsewhere in online forums, collaborative software, documentation pages, and readme files.

### Wikidata

[Wikidata](https://www.wikidata.org) is a collaboratively edited multilingual knowledge graph hosted by the Wikimedia Foundation.It is a common source of open data that Wikimedia projects such as Wikipedia, and anyone else, can use under the CC0 public domain license. Wikidata is a wiki powered by the software MediaWiki, including its extension for semi-structured data, the Wikibase.

### International Image Interoperability Framework (IIIF)

[The International Image Interoperability Framework](https://iiif.io) (IIIF, spoken as 'triple-I-eff') defines several application programming interfaces that provide a standardised method of describing and delivering images over the web, as well as "presentation based metadata" (that is, structural metadata) about structured sequences of images. If institutions holding artworks, books, newspapers, manuscripts, maps, scrolls, single sheet collections, and archival materials provide IIIF endpoints for their content, any IIIF-compliant viewer or application can consume and display both the images and their structural and presentation metadata.

### Leaflet

[Leaflet](https://leafletjs.com/) is an open source JavaScript library used to build web mapping applications. First released in 2011, it supports most mobile and desktop platforms, supporting HTML5 and CSS3. Among its users are FourSquare, Pinterest and Flickr.

Leaflet allows developers without a GIS background to very easily display tiled web maps hosted on a public server, with optional tiled overlays. It can load feature data from GeoJSON files, style it and create interactive layers, such as markers with popups when clicked.

### GeoJSON

[GeoJSON](https://geojson.org/) is an open standard format designed for representing simple geographical features, along with their non-spatial attributes. It is based on the JSON format.

The features include points (addresses and locations), line strings (streets, highways and boundaries), polygons (countries, provinces, tracts of land), and multi-part collections of these types.

## Juncture Github Repositories

Juncture code is hosted in repositories found in the Github [juncture-digital](https://github.com/juncture-digital) organization account.

- **[juncture](https://github.com/juncture-digital/juncture)** (this repository) - The main Juncture web and API services.  The web and API are implemented as a python ASGI service using [FastAPI](https://fastapi.tiangolo.com/).
- **[web-components](https://github.com/juncture-digital/web-components)** - Juncture v2 Web Components implemented using [Vue 3 Custom Elements](https://vuejs.org/guide/extras/web-components.html).
- **[iiif](https://github.com/juncture-digital/iiif)** - Juncture implementation of IIIF Presentation API.  Includes helper tools for creating TIFF pyramids for use by Juncture IIIF Image API.  The Juncture IIIF Presentation API is implemented as a python ASGI service using [FastAPI](https://fastapi.tiangolo.com/).
- **[juncture-ghp](https://github.com/juncture-digital/juncture-ghp)** - Juncture self-hosting setup for Github pages.  This is the recommended configuration for hosting a Juncture-powered web site with a custom domain.
- **[search](https://github.com/juncture-digital/search)** - Juncture semantic search companion tool.  Helpful for locating high-resolution images that are public domain or licenseable.  This is still under active development.
- **[serverless-iiif](https://github.com/juncture-digital/serverless-iiif)** - Juncture implementation of IIIF Image API.  It is a forked copy of the [Samvera](https://samvera.org/) [serverless-iiif](https://github.com/samvera/serverless-iiif) code.
- **[mdx-outline](https://github.com/juncture-digital/mdx-outline)** - Lightly modified version of [aleray/mdx_outline](https://github.com/aleray/mdx_outline) Python-Markdown extension to wrap the document logical sections (as implied by h1-h6 headings).
- **[markdown-customblocks](https://github.com/juncture-digital/markdown-customblocks)** - Lightly modified version of [vokimon/markdown-customblocks](https://github.com/vokimon/markdown-customblocks) Python-Markdown extension for defining custom blocks.

## Juncture Web/API Service

The most common use of Juncture by users is to host Markdown files in a personal Github repository and use Juncture services hosted by JSTOR Labs to render the Markdown files as web pages.  When using Juncture services to render a Markdown file the Github account, repository and path to the Markdown file are included as path elements on the `juncture-digital.org` domain, for example [https://juncture-digital.org/rsnyder/essays/demo](https://juncture-digital.org/rsnyder/essays/demo)

The `www.juncture-digital.org` domain hosts the Juncture web and API servers.  The web server handles requests for the Juncture home and documentation pages as well as content hosted in user Github repositories.  The code for the web and API service is maintained in this repository.

#### Local development

The Juncture web/api server may be run in local mode for development and testing.  The server may also be run as a stand-alone server or may be used in conjunction with a local development setups for the web components server.  In local development mode the server may serve local content or content hosted in Github.

When running the server locally a python virtual environment is recommended.  Below is an example of the one time setup of the virtual environment on a Mac.

```bash
> python3 -m venv .venv
> source .venv/bin/activate
> pip install -r requirements.txt
```

Once the virtual environment has been activated the server is started by running the `serve.py` python script.  A couple of shell "run" scripts are also available as conveniences for different situations.

In the default use (running the serve.py script with no options) the server mimics the behavior of the juncture-digital.org web site, serving content from the juncture-digital/juncture Github repository.  

```bash
> ./serve.py
```

To serve local content the `--content` option may be used with a path to the local content root.  For instance, to serve content from the local directory.

```bash
> ./serve.py --content .
```

#### Deployment

A `deploy.sh` script is found in the `aws` folder for deploying code to both production and development servers.  The deployments are built as Lambda container images.  The deploy.sh script assumes the Docker image is being compiled on a computer with an Apple Silicon (M*) architecture.  Changes in the script would be needed for other build environments.  The script builds the Docker image, uploads the image to ECR, and activates the new image.  All deployments take place on the JSTOR Labs AWS account.

**Deploying to development (default behavior)**

```bash
> ./aws/deploy.sh
```
or  
```bash
> ./aws/deploy.sh juncture-webapp-dev
```

**Deploying to production**
```bash
> ./aws/deploy.sh juncture-webapp
```

#### API Endpoints

The OpenAPI documentation for the Juncture endpoints can be seen at [https://api.juncture-digital.org/docs](https://api.juncture-digital.org/docs).  These API endpoints are not typically used by users.  The endpoints are primarily used by the Juncture web host or in some self-hosting configurations when custom domains are needed.