# Hosting a Juncture website

In the most basic use of Juncture an essay is generated from a Markdown file stored in a Github repository.  Multiple essays can be connected by links creating a navigable network of resources.  This is often sufficient for many uses.  In some cases it may be desired to collect multiple essays into a website with a custom domain.

## Organizing the site content

When hosting a website of Juncture content the Markdown files for the site must be contained in a single Github repository.  By default Juncture creates an "essays" repository when linking a Github account.  Any repository may be used for the site but note that when using the simplest website hosting approach (Github Pages) the repository name becomes part of the website root url and should be named to reflect the website purpose or theme.

The README.md Markdown file at the root of the repository containing the website content will be used as the websites home (or landing) page.  Other website content is contained in Markdown files that are linked from the home page.  To create a nested content hierarchy Github folders may be used.    

## Hosting

There are two primary hosting strategies for a Juncture web site.  

The first strategy uses the hosting capability provided by Github called [Github Pages](https://pages.github.com/).  Github Pages is easy to setup and is free to use.  The only downside to using Github Pages for a Juncture site is suboptimal indexing by web search engines.  The Search Engine Optimization (SEO) in this approach is poor.  If site indexing is not important Github Pages would be a great option.

By default the root URL for a Github Pages hosted site is `https://GH_USERNAME/github.io/GH-REPOSITORY`.  For example, The base URL for a Github Pages hosted website in a repository named `website` for a user with the Github username `snagsby` would be `https://snagsby.github.io/website`.  If a custom domain is desired this can also be easily added to a Github Pages hosted site.

In the second strategy a simple web server is self-hosted.  There are any number of approaches for doing this.  A few are described [below](#using-a-self-hosted-web-server).  The key advantage of a self-hosted solution is improved SEO.  This is the recommended strategy if search engine indexing of site content is important.

### Hosting with Github Pages

Configuring a Github repository as a Github Pages hosted website is accomplished by copying a few files to the root of the repository to be used for the site content and activating the Github Pages option in the repository settings.

1. **Copy needed files**

    In the repository to be used for the Github Pages hosted site, add a copy of the following files located in the [juncture-digital/hosting](https://github.com/juncture-digital/hosting) repository.

    - [index.html](https://raw.githubusercontent.com/juncture-digital/hosting/main/index.html)
    - [404.html](https://raw.githubusercontent.com/juncture-digital/hosting/main/404.html)
    - [.nojekyll](https://raw.githubusercontent.com/juncture-digital/hosting/main/.nojekyll) - Note that this is an empty file, a file with this name just needs to exist in the repository root.

2. **Activate Github Pages**

    - Select the **Settings** menu option located at the top of the Github page for the repository to be used for the website content.  
    - From Settings main page select the **Pages** tab in the left sidebar menu to show the Github Pages setup panel.
    - In the Github Pages setup panel select **main** from the pulldown menu in the **Branch** section. 

That's it!  The repository is now configured for use as Github Pages hosted web site.  Note, that it can often take a few minutes for the site to become active after configuring it.

### Using a self-hosted web server

There are a variety of ways to host a Juncture web server, including Google Cloud, Amazon Web Services, pythonanywhere, and many more.  In this section instructions for hosting with [pythonanywehre](https://www.pythonanywhere.com/) are provided as it is probably the easiest to setup and is relatively inexpensive ($5/mo as of June 2023) to operate.

1. Signup for a $5/month "Hacker" account.  Note that the free account offered cannot be used as external API requests are not enabled at this level.
1. After signing up and logging in, select **Web** from the toolbar menu located at the top of the Dashboard page.
1. From the Web page click the **Add a mew web app** button.
    - In the "Your web app's domain name" form enter the domain name to be used for the site.
    - In the "Select a Python Web framework" form select **Flask**
    - In the "Select a Python version" form select **Python 3.9**
    - In the "Quickstart new Flask project" from use the default Path value
1. Select the **Files** option from the toolbar menu located at the top of the page.
1. From the Files page press the **mysite** entry in the **Directories** list.  In the next page press the **flask_app.py** entry in the **Files** list.
1. In the editor that is opened for the **flask_app.py** file, replace the current content with the contents of the [main.py](https://raw.githubusercontent.com/juncture-digital/hosting/main/main.py) file found in the [juncture-digital/hosting](https://github.com/juncture-digital/hosting) repository. 
1. In the replaced text, find the **CONTENT** variable located near the top of the file and replace the value with the Github username and repository that contains the content for the website.
1. Save the modified file by clicking the **Save** button at the top of the page.
1. After saving **flask_app.py** press the **Reload** icon located in the toolbar menu.  This will restart the web server with the new code that was just added to the **flask_app.py** file.
1. The web site should now be live at the domain name entered in the first **Add a mew web app** form.  This domain name can also be seen by selecting the **Dashboard** entry from the menu located at the top-right of the page.  On the Dashboard page the site domain/URL will be listed in the **Web apps** list.

## Using a custom domain name

A custom domain name may easily be associated with the configured website using either the Github Pages or self-hosted strategy.  Below are links to pages providing detailed instructions.

- [Setting up a custom domain on a Github Pages site](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
- [Setting up a custom domain on PythonAnywhere](https://help.pythonanywhere.com/pages/CustomDomains)
