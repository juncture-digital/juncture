<style>
    hr { clear: both; }
</style>

# Overview

This tutorial provides step-by-step instructions for creating a Juncture essay.  The created essay will incorporate a number of Juncture features including the use of an embedded media viewer for viewing a high-resolution image and the use of the media viewer for displaying an image grid and comparing two images.  The tutorial provides detailed instructions with accompanying videos and/or interactive images for each step.  

<ve-media src="wc:Polarlicht_2.jpg" right></ve-media>

Most of the <mark zoomto="1635,1500,376,246">tutorial</mark> sections include a short video clip demonstrating the actions that need to be accomplished.  Some sections also include links in the text for starting the video at specific points.

<ve-modal src="rsnyder/essays/bedroom-in-arles"></ve-modal>

<ve-window href="/editor">Open editor</ve-window>

---

# Prerequisites

The only true prerequisite for using Juncture is a Github account.  **Github is a free Internet hosting service** commonly used for software development projects.  It provides features for version control and work flow management for distributed teams.  Juncture uses Github for storing and managing essay files.  In addition to a Github account, some familiarity with Markdown and IIIF would be beneficial.

## Sign-up for Github account

If you don't already have a Github account one can be created at [https://github.com/signup](https://github.com/signup)

# Using the documentation

The documentation provides text snippets and live demonstrations of Juncture tags.  The text snippets can be copied and pasted into external documents and tools, including the Juncture web editor.  The snippet below provides a simple example of using the `.ve-media` tag.  Snippets are provide for both Markdown and HTML.

<ve-snippet>
    .ve-media gh:rsnyder/media/italy/amalfi-coast/Amalfi_Coast.jpg
</ve-snippet>

In addition to the embedded text snippets, pop-ups are sometimes used to demonstrate the use Juncture featues.  The pop-ups are triggered with a `Show me` (or similarily named) button.  For example, click the button below to see a rendered Juncture page with a `.ve-media` tag.

<ve-modal label="Juncture Demo" button-label="Show me" style="margin-bottom:2rem;">
    .ve-media gh:rsnyder/media/italy/amalfi-coast/Amalfi_Coast.jpg right
    A pop-up including a `.ve-media` viewer.
</ve-modal>
