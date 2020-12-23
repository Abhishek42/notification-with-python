from plyer import notification

# =====================================================
#     notificationbar

def notf(title,message):
    notification.notify(title=title
    ,message=message
    ,timeout=5
    ,app_icon="C:\\python\\python notification\\images.png"
    )
# ========================================================

if __name__ == "__main__":
    notf("abhishek","Abhishek sharma")
    input()
