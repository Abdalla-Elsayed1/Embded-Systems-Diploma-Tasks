import webbrowser
import os
favourite_links= {"chatgpt":"https://chat.openai.com/",
                  "pythonorg":"https://www.python.org/",
                  "w3school":"https://www.w3schools.com/",
                  "github":"https://github.com/"
                }

def open_link(url_key):
    url_key = favourite_links[url_key]
    ## one way to get the firefox path using r and \\
    # firefox_path = r"C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    
    #another one is using os module \ function .join()
    firefox_path = os.path.join("C:", "Program Files",  "Mozilla Firefox", "firefox.exe")

    webbrowser.register("firefox", None, webbrowser.BackgroundBrowser(firefox_path))
    try:
        webbrowser.get('firefox').open(url_key)
    except:
        print(f"Error: URL key '{url_key}' not found in favourite_links.")
        return


