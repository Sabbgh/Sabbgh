from flet import *
def main(flash:Page):
    flash.window.width=390
    flash.window.height=700
    f=Flashlight()
    flash.overlay.append(f)
    per=PermissionHandler()
    flash.overlay.append(per)
    def openSetting(e):
        per.open_app_settings()
    flash.add(
          AppBar(
              title=Text('FlashLight ',size=12),
              color='white',bgcolor='red',
              toolbar_height=35,
              actions=[
                  IconButton(Icons.SETTINGS,on_click=openSetting)
              ]
          ),
           Row([Text('Flashlight',size=30)],alignment=MainAxisAlignment.CENTER),
           Row([Image(src='../l.jpg')],alignment=MainAxisAlignment.CENTER),
           Row([
               ElevatedButton(
                   "on",icon=Icons.PLAY_ARROW,color='white',bgcolor='green',on_click=lambda _:Flashlight.turn_on()
               ),
                ElevatedButton(
                   "off",icon=Icons.STOP ,color='white',bgcolor='red',on_click=lambda _:Flashlight.turn_off
               )
           ],alignment=MainAxisAlignment.CENTER),
           Row([Text('\n\n\n\nby:MAHMOUD EL SABBAGH',size=16,color='blue')],alignment=MainAxisAlignment.CENTER)
    )
    Page.update(flash)
app(main)
