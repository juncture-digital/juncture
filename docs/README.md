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

1. **Juncture will not retain user data** **  It's your data, we just want to make it easier to create and share.
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

### Create new essay

<ve-snippet>
    .ve-header "Farmhouse in Provence" wc:Farmhouse_in_Provence,_1888,_Vincent_van_Gogh,_NGA.jpg sticky

    # Farmhouse in Provence

    Farmhouse in Provence, also known as Entrance Gate to a Farm with Haystacks, is an oil-on-canvas painting produced in 1888 by Dutch painter ==Vincent van Gogh=={Q5582} in Arles, Provence, at the height of his career. Partially due to having been inspired by painter Adolphe Monticelli, Van Gogh sought the Provence region of France to further expand his painting skill and experience. Van Gogh used several pairs of complementary colors in the Farmhouse in Provence, the color contrast bringing an intensity to his work. The painting is owned by the National Gallery of Art in Washington, D.C.[^1]

    ## The painting

    .ve-media wc:Farmhouse_in_Provence,_1888,_Vincent_van_Gogh,_NGA.jpg right

    Van Gogh used three pairs of complementary, or contrasting, colors which when sat together intensified the brilliance and intensity of one another's colors. One pair is orange and blue. Another would be the red and green of the plants. Last, pink clouds against the turquoise sky.

    Van Gogh used complementary, contrasting colors to bring an intensity to his work, which evolved over the periods of his work. Two complementary colors of the same degree of vividness and brightness placed next to one another produce an intense reaction, called the "law of simultaneous contrast."

    Van Gogh mentioned the liveliness and interplay of "a wedding of two complementary colors, their mingling and opposition, the mysterious vibrations of two kindred souls."

    While in Nuenen Van Gogh became familiar with Michel Eugène Chevreul's laws in weaving to maximize the intensity of colors through their contrast to adjacent colors.

    In Paris he was exposed through his brother Theo to Adolphe Monticelli's still life work with flowers, which he admired. First, he saw Monticelli's use of color as an expansion of Delacroix's theories of color and contrast. Secondly he admired the effect Monticelli created by heavy application of paint. It was partially Monticelli, from Marseilles, who inspired Van Gogh's southerly move to Provence. He felt such kinship for the man, and desire to emulate his style, that he wrote in a letter to his sister Wil that he felt as if he were "Monticelli's son or his brother."

    ## Arles

    .ve-map Q48292 5 left
        - Q48292

    At the time that Van Gogh painted Farmhouse in Provence, he was 35 years old. Living in Arles, in southern France, he was at the height of his career, producing some of his best work,[1] such as fields, farmhouses and people of the Arles, Nîmes and Avignon area.

    The area was quite different from what he'd known in the Netherlands and Paris. The climate was hot and dry. People had dark hair and skin and spoke a different language than Parisian French. The colors were vivid. The terrain varied from plains to mountains. Here Van Gogh found a "brilliance and light that would wash out details and simplify forms, reducing the world around him to the sort of pattern he admired in Japanese woodblocks" and where the "effect of the sun would strengthen the outlines of composition and reduce nuances of color to a few vivid contrasts."

    A prolific time, in less than 444 days Vincent made about 100 drawings and produced more than 200 paintings Yet, he still wrote more than 200 letters. He described a series of seven studies of wheat fields as, "landscapes, yellow—old gold—done quickly, quickly, quickly, and in a hurry just like the harvester who is silent under the blazing sun, intent only on the reaping."

    In a letter to his brother, Theo, he wrote, "Painting as it is now, promises to become more subtle—more like music and less like sculpture—and above all, it promises color."

    [^1]: Wikipedia contributors. (2021, November 9). Farmhouse in Provence. In Wikipedia, The Free Encyclopedia. Retrieved 01:09, January 20, 2023, from https://en.wikipedia.org/w/index.php?title=Farmhouse_in_Provence&oldid=1054303646

    .ve-footer
        - CC0
</ve-snippet>
