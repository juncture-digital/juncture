# General Styling

Custom styles may be applied to a Juncture essay in few ways.

## Link to external stylesheet

The `.ve-style` tag can be used to link to an external stylesheet.

## Embed style information in an essay using the HTML `<style>` tag

<ve-snippet label="Custom styling using HTML style tag">

<style>
    @import url(//fonts.googleapis.com/css?family=Montserrat);
    #juncture { font-family: Montserrat; }
    #juncture h1 { color: red; }
</style>

    # Heading

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

</ve-snippet>

## Add in-line styling to Juncture tags or paragraphs