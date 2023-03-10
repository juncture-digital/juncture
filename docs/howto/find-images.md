<style>
    .markdown-section h3 span {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .markdown-section h3 span img {
        height: 40px;
    }

</style>

# Finding Images

This page collects information for finding IIIF resources.  These are typically images but some sites, such as Wikimedia Commons, also contain audio and video content that can be dynamically wrapped in an IIIF manifest for easy use in a Juncture essay.  In most cases an image or media file found on a site listed below can be added to a Juncture essay by dragging the image from the hosting site into the Juncture essay editor.  When using the drag-and-drop or copy-paste method of adding a IIIF resource to a Juncture essay the corresponding `.ve-media` or `.ve-header` tag with the correct IIIF URL is automatically created.

## Sites providing IIIF resources

The [IIIF website](https://iiif.io/) provides a brief guide to finding IIIF resources from a list of collections, which you can find [here](https://iiif.io/guides/finding_resources/).

## Media sharing sites

In addition to using IIIF resources exposed by the sites mentioned above, Juncture is able to dynamically create IIIF images from a number of image hosting sites that do not currently provide IIIF versions of hosted content.  In most cases these sites do provide a public API that can be used to obtain metadata that can be used to construct an IIIF manifest. 

### ![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/80px-Commons-logo.svg.png) Wikimedia Commons

 [Wikimedia Commons](https://commons.wikimedia.org/wiki/Main_Page) is an online repository of free-to-use images, audio, and video files.  Much of the content hosted by Wikimedia Commons is either public domain or available with an open Creative Commons license providing flexible reuse.  Wikimedia Commons provides a IIIF image server which is used to render the IIIF images.  Juncture uses the Wikimedia Commons API to obtain metadata for dynamically constructing the IIIF presentation manifest.

Wikimedia Commons IIIF URLs are formed by combining the `wc:` prefix with the Wikimedia Commons file name.  For example, the image found at [https://commons.wikimedia.org/wiki/File:Holy_SURP_Hovhannes_Church.jpg](https://commons.wikimedia.org/wiki/File:Holy_SURP_Hovhannes_Church.jpg) has the file name "Holy_SURP_Hovhannes_Church.jpg" (note that spaces in the file name are converted to underscores).  In this example the resulting IIIF URL would be [https://iiif.juncture-digital.org/wc:Holy_SURP_Hovhannes_Church.jpg/manifest.json](https://iiif.juncture-digital.org/wc:Holy_SURP_Hovhannes_Church.jpg/manifest.json).  A short-form version of the URL with just the prefix and file name can be used in a Juncture essay, for instance - `wc:Holy_SURP_Hovhannes_Church.jpg`.

<ve-snippet collapsible label="Wikimedia Commons - Image example">
    .ve-media wc:Holy_SURP_Hovhannes_Church.jpg right

    [Holy SURP Hovhannes Church](https://commons.wikimedia.org/wiki/File:Holy_SURP_Hovhannes_Church.jpg)

    Saint John Church of Sohrol, a 5th or 6th century Armenian Catholic church in Sohrol, Iran, rebuilt by Samson Makintsev (Sam Khan) in 1840

    [Wikimedia Commons](https://commons.wikimedia.org/wiki/Main_Page) [Picture of the Year](https://commons.wikimedia.org/wiki/Commons:Picture_of_the_Year) for 2021
</ve-snippet>

<ve-snippet collapsible label="Wikimedia Commons - Audio example">
    .ve-media wc:Interview_with_Warren_Hanson_regarding_Hundred_Flowers.ogg right

    [Interview with Warren Hanson regarding Hundred Flowers](https://commons.wikimedia.org/wiki/File:Interview_with_Warren_Hanson_regarding_Hundred_Flowers.ogg)

    This is an oral history interview with Warren Hanson conducted as part of a West Bank oral history project. He recalls the challenges of getting the Hundred Flowers underground newspaper printed in 1969 at a time when small town newspaper presses in Minnesota were unwilling to print the anti-war, civil rights, counter-culture publication, forcing the paper to be printed in Milwaukee, until one civil libertarian owned press in Minnesota finally volunteered their services in the spirit of free speech.
</ve-snippet>

<ve-snippet collapsible label="Wikimedia Commons - Video example">
    .ve-media wc:Aerial_views_of_Shoalhaven_Heads,_NSW,_Australia_in_June_2016.webm right autoplay

    [Aerial views of Shoalhaven Heads, NSW, Australia in June 2016](https://commons.wikimedia.org/wiki/File:Aerial_views_of_Shoalhaven_Heads,_NSW,_Australia_in_June_2016.webm)
</ve-snippet>

<ve-snippet collapsible label="Wikimedia Commons - GIF example">
    .ve-media wc:DART-impact-SAAO-Lesedi-Mookodi.gif right

    [DART impact SAAO-Lesedi-Mookodi](https://commons.wikimedia.org/wiki/Template:Motd/2022-12#/media/File:DART-impact-SAAO-Lesedi-Mookodi.gif)

    The impact of Double Asteroid Redirection Test (DART) spacecraft's intentional collision with asteroid Dimorphos and its corresponding plumule as seen by using the Mookodi instrument on the SAAO's 1-m Lesedi telescope. NASA's first flight mission for planetary defense, DART seeks to test and validate a method to protect Earth in case of an asteroid impact threat.
</ve-snippet>

### ![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Flickr.svg/256px-Flickr.svg.png) Flickr

[Flickr](https://www.flickr.com/) is an image and video hosting service, as well as an online community, founded in Canada and headquartered in the United States. It was created by Ludicorp in 2004 and was a popular way for amateur and professional photographers to host high-resolution photos. It has changed ownership several times and has been owned by SmugMug since April 20, 2018.

Flickr IIIF URLs are formed by combining the `flickr:` prefix with the Flickr image ID.  For example, the image found at [https://www.flickr.com/photos/mgaylard/52736840054/](https://www.flickr.com/photos/mgaylard/52736840054/) has the image ID "52736840054".  In this example the resulting IIIF URL would be [https://iiif.juncture-digital.org/flickr:52736840054/manifest.json](https://iiif.juncture-digital.org/flickr:52736840054/manifest.json).  The short-form IIIF URL for use in Juncture essays would be `flickr:52736840054`  

<ve-snippet collapsible label="Flickr image">
    .ve-media flickr:52736840054 right

    [Yarmouth Ferry Terminal](https://www.flickr.com/photos/mgaylard/52736840054/)
</ve-snippet>

### ![](https://about.jstor.org/wp-content/themes/aboutjstor2017/static/JSTOR_Logo2017_90.png) JSTOR

[JSTOR](https://jstor.org) is a digital library of academic journals, books, and primary sources. JSTOR hosts both restricted access and open content. Open access images on JSTOR can be queried using this [open content search expression](https://www.jstor.org/action/doBasicSearch?Query=cc_reuse_license%3A%22public+domain%22+OR+cc_reuse_license%3A%22Creative+Commons%22+-cc_reuse_license%3A%28NonCommercial+OR+NoDerivs%29&efqs=eyJjdHkiOlsiWTI5dWRISnBZblYwWldSZmFXMWhaMlZ6Il0sImRpc2MiOltdfQ%3D%3D&searchkey=1677864936160&pagemark=eyJwYWdlIjoyLCJzdGFydHMiOnsiSlNUT1JCYXNpYyI6MjV9fQ%253D%253D).  A more targeted search can then be performed using the Search Bar in the navigation menu on the left side of the page.

JSTOR IIIF URLs are formed by combining the `jstor:` prefix with the JSTOR content ID.  For example, the image found at [https://www.jstor.org/stable/community.18615405](https://www.jstor.org/stable/community.18615405) has the content ID "community.18615405".  In this example the resulting IIIF URL would be [https://iiif.juncture-digital.org/jstor:community.18615405/manifest.json](https://iiif.juncture-digital.org/jstor:community.18615405/manifest.json).  The short-form IIIF URL for use in Juncture essays would be `jstor:community.18615405` 

<ve-snippet collapsible label="JSTOR image">
    .ve-media jstor:community.18615405 right

    [Portal of a Venetian Palace](https://www.jstor.org/stable/community.18615405)
</ve-snippet>

### ![](https://upload.wikimedia.org/wikipedia/commons/9/93/Internet_Archive_logotype.png) Internet Archive

The [Internet Archive](https://archive.org/) ...


[MET]()

[OpenVerse]()

[Wikidata]()

[Edison Papers]()


### Personal Images and Github Repositories

You can use any image from your personal GitHub repository in a Juncture essay and a IIIF manifest will be generated by Juncture for your GitHub hosted image. A helpful tool in managing your images is the [Juncture Media Tool](https://www.juncture-digital.org/#/embedded-media). [Here](https://www.juncture-digital.org/howto/setup-media-collection) is a guide to using the media tool to set up a personal media collection.
