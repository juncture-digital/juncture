# General Scripts

Custom JavaScript may be applied to a Juncture essay in two ways.

- Reference an external file
- Script tag in essay

## Reference an external stylesheet

The `.ve-script` tag can be used to link to an external javascript file.  The .ve-style tag requires a `href` attribute defining the script URL.  The href attribute may be included using positional or key-value notation.  The URL may be absolute or relative.

<ve-snippet collapsible label="Using external style sheet" prefix="rsnyder/essays" path="styling">

    .ve-script ./custom.js

</ve-snippet>

## Style tag in essay

An HTML `script` tag with JavaScript may be added in the essay text.

<ve-snippet collapsible label="Custom styling using HTML style tag">

<script>
    // JavaScript placed here will also work.
    console.log("This log was generated as an example of inline JavaScript in a Juncture essay.");
</script>
</ve-snippet>

In these examples a script is used to generate a console log.