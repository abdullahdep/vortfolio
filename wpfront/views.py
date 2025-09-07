from django.shortcuts import render
import requests

def wp_page(request, slug='home'):
    # Use your WordPress site URL 
    wp_url = "http://wordpress.vortfolio.icu"  # Update this to your actual WordPress URL
    page_url = f"{wp_url}/{slug}"
    
    try:
        res = requests.get(page_url)
        if res.status_code == 200:
            full_page_content = res.text
        else:
            # Return a proper 404 page
            return render(request, "app/404.html", status=404)
            
    except Exception as e:
        return render(request, "app/404.html", {
            "error_message": f"Error connecting to WordPress: {str(e)}"
        }, status=500)

    return render(request, "wpfront/page.html", {
        "full_page_content": full_page_content,
    })
