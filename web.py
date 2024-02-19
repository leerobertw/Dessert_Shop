from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse

from MenuItems import Candy


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.display_page(self.display_menu)

    def do_POST(self):
        length = int(self.headers.get('content-length'))
        field_data = self.rfile.read(length)
        fields = parse.parse_qs(str(field_data, "UTF-8"))
        self.handle_post(fields)

    def handle_post(self, fields):
        field = fields.get('menuItemMenu')
        if field is None:
            self.display_page(self.display_menu)
        else:
            menu_item_menu = field[0]
            menu_item_method = self.display_menu
            match menu_item_menu:
                case 'candy':
                    menu_item_method = self.display_candy
                case 'cookies':
                    menu_item_method = self.display_cookies
                case 'ice_cream':
                    menu_item_method = self.display_ice_cream
                case 'sundae':
                    menu_item_method = self.display_sundae
            self.display_page(menu_item_method)

    def display_page(self, display_function):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head>", "utf-8"))
        self.javascript_code()
        self.wfile.write(bytes("<title>Dessert Shop</title>", "utf-8"))
        self.button_styles()
        self.wfile.write(bytes("</head><body>", "utf-8"))
        display_function()
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def button_styles(self):
        self.wfile.write(bytes(
            '''
<style>
.button {
    border: none;
    color: white;
    padding: 25px 55px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
}

.candy_button
{background-color:  #04AA6D;} /* Green */
.cookies_button
{background-color:  #008CBA;} /* Blue */
.ice_cream_button
{background-color:  #FC0303;} /* Red */
.sundae_button
{background-color:  #F403FC;} /* Purple */
</style>
                    ''', 'utf-8'))

    def javascript_code(self):
        self.wfile.write(bytes('''
    <script>
        function setMenuItemMenu(value) {
            document.getElementById("menuItemMenu").value = value
        }
    </script>
        ''', 'utf-8'))

    def display_menu(self):
        self.wfile.write(bytes("<h1>Welcome to the Dessert Shop Ordering Application</h1>", "utf-8"))
        self.wfile.write(bytes('''
        <h2>Select a menu item</h2>
        <form method="post">
            <input type="hidden" name="menuItemMenu" id="menuItemMenu" value="main_menu"/>
            <button type="submit" class="button candy_button" onclick="setMenuItemMenu('candy')">Candy</button>
            <button type="submit" class="button cookies_button" onclick="setMenuItemMenu('cookies')">Cookies</button><br>
            <button type="submit" class="button ice_cream_button" onclick="setMenuItemMenu('ice_cream')">Ice Cream</button>
            <button type="submit" class="button sundae_button" onclick="setMenuItemMenu('sundae')">Sundae</button>
        </form>
        ''', 'utf-8'))

    def display_candy(self):
        self.wfile.write(bytes('''
         <h1>Candy Menu</h1>
         <form method="post">
         <p>Enter amount of candy in lbs<br>
         <input type="hidden" name="menu_item" value="candy" />
         <input type="text" name="amount" /> <input type="submit" /></p>
        ''', 'utf-8'))

    def display_cookies(self):
        self.wfile.write(bytes('''
         <h1>Cookies Menu</h1>
         <form method="post">
         <p>Enter the number of dozen of cookies<br>
         <input type="hidden" name="menu_item" value="cookies" />
         <input type="text" name="amount" /> <input type="submit" /></p>
        ''', 'utf-8'))

    def display_ice_cream(self):
        self.wfile.write(bytes('''
         <h1>Ice Cream Menu</h1>
         <form method="post">
         <p>Enter number of scoops<br>
         <input type="hidden" name="menu_item" value="ice_cream" />
         <input type="text" name="amount" /> <input type="submit" /></p>
        ''', 'utf-8'))

    def display_sundae(self):
        pass


def run(server_class=HTTPServer, handler_class=MyServer):
    server_address = ('', 8082)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Server stopped.")


if __name__ == "__main__":
    run()

