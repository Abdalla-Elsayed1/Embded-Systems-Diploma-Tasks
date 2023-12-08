import webbrowser
import pyautogui
import os
import time
import cv2

vscode_link= {"vscode":"https://code.visualstudio.com/download"
                }
absloute_path = os.path.dirname(os.path.realpath(__file__))

def open_link(url_key):
    url_key = vscode_link[url_key]
    firefox_path = r"C:\Program Files\Mozilla Firefox\\firefox.exe"
    webbrowser.register("firefox", None, webbrowser.BackgroundBrowser(firefox_path))
    try:
        webbrowser.get('firefox').open(url_key)
    except:
        print(f"Error: URL key '{url_key}' not found in favourite_links.")
        return


def download_vs():
    absloute_path = os.path.dirname(os.path.realpath(__file__))+"/download_vs.png"
    isfind=None
    while isfind is None:
        isfind = pyautogui.locateCenterOnScreen(absloute_path, confidence=0.7)
    pyautogui.click(326, 611)

def install_vs():
    pyautogui.hotkey('win')
    time.sleep(0.3)
    pyautogui.write("VSCodeUserSetup-x64-")
    time.sleep(1)
    pyautogui.hotkey("Enter")
    
def install_vspackage():
    packages_lst = {
                    "clangd":"/clangd.png",
                   "c++ helper":"/cpphelper.png",
                   "cmake":"/cmake.png",
                   "cmake tools":"/cmaketools.png",
                   "c++ testmate":"/cpptestmate.png",
                }
    
    user_input = input("Enter package name: ").lower()
    
    if user_input in packages_lst.keys():
    
        package_name = user_input
        package_image_path = packages_lst[package_name]
        
        pyautogui.hotkey('win')
        time.sleep(0.3)
        pyautogui.write("VSCODE")
        time.sleep(1)
        pyautogui.hotkey("Enter")
        time.sleep(3)
        pyautogui.hotkey('Ctrl','Shift','X')
        pyautogui.write(package_name)
        time.sleep(15)
        absloute_path = os.path.dirname(os.path.realpath(__file__))+package_image_path
        isfind=None
        while isfind is None:
            isfind = pyautogui.locateCenterOnScreen(absloute_path, confidence=0.7)
       
        pyautogui.click(482, 165)


    
    else:
        print("unidentified extension name")
    
    
    