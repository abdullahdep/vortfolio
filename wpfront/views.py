from django.shortcuts import render
import requests

def wp_page(request, slug='home'):
    page_url = f"http://vortfolio.icu/{slug}"  # Fetch the full rendered page
    try:
        res = requests.get(page_url)
        if res.status_code == 200:
            full_page_content = res.text  # Get the full HTML content
        else:
            full_page_content = "<p>Page not found.</p>"
    except Exception as e:
        full_page_content = f"<p>Error fetching page: {e}</p>"

    return render(request, "wpfront/page.html", {
        "full_page_content": full_page_content,
    })
