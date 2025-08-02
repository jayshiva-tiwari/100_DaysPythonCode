## What are Flask Templates?
Flask uses Jinja2 templating engine to render dynamic HTML pages.
Instead of hardcoding HTML in Python, we can write separate .html files and inject data dynamically using curly braces like {{ name }}.
#
### first create templates
 
` templates/index.html `
check in templates folder,
how to use templates.
#
### second Update app.py to render HTML
` return render_template("index.html", name="Shiva") `
#
### At the last check on web.
check your website on port `http://127.0.0.1:5000/`
#