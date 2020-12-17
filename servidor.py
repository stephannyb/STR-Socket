from socket import *
import msvcrt
import arcade
import threading

class Game(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.quadro_velocidades = threading.Thread(target=self.q_velocidades).start()
        self.verde = 235.46
        self.roxo = 235.46
        self.amarelo = 109.46
        self.azul = 109.46
        self.v_verde = 0
        self.v_roxo = 0
        self.v_amarelo = 0
        self.v_azul = 0

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("S : + ", start_x=50, start_y=500, font_size=14, color=arcade.color.GREEN)
        arcade.draw_text("T : + ", start_x=50, start_y=475, font_size=14, color=arcade.color.VIOLET)
        arcade.draw_text("E : + ", start_x=50, start_y=450, font_size=14, color=arcade.color.ORANGE)
        arcade.draw_text("P : + ", start_x=50, start_y=425, font_size=14, color=arcade.color.BLUE)

        arcade.draw_text("R : - ", start_x=300, start_y=500, font_size=14, color=arcade.color.GREEN)
        arcade.draw_text("A : - ", start_x=300, start_y=475, font_size=14, color=arcade.color.VIOLET)
        arcade.draw_text("F : - ", start_x=300, start_y=450, font_size=14, color=arcade.color.ORANGE)
        arcade.draw_text("L : - ", start_x=300, start_y=425, font_size=14, color=arcade.color.BLUE)

        arcade.draw_text("VELOCIDADE PERMITIDA ENTRE 0 KM/H E 100 KM/H", start_x=50, start_y=350, font_size=14,color=arcade.color.WHITE)

        arcade.draw_text("TREM VERDE", start_x=50, start_y=300, font_size=18, color=arcade.color.GREEN)
        arcade.draw_rectangle_outline(100,260,15,60,arcade.color.GREEN,border_width=3)
        arcade.draw_rectangle_filled(100, self.verde, 50, 3, arcade.color.GREEN)


        arcade.draw_text("TREM ROXO", start_x=300, start_y=300, font_size=18, color=arcade.color.VIOLET)
        arcade.draw_rectangle_outline(350, 260, 15, 60, arcade.color.PURPLE, border_width=3)
        arcade.draw_rectangle_filled(350, self.roxo, 50, 3, arcade.color.VIOLET)

        arcade.draw_text("TREM AMARELO", start_x=50, start_y=175, font_size=18, color=arcade.color.ORANGE)
        arcade.draw_rectangle_outline(100, 135, 15, 60, arcade.color.YELLOW, border_width=3)
        arcade.draw_rectangle_filled(100, self.amarelo, 50, 3, arcade.color.YELLOW)

        arcade.draw_text("TREM AZUL", start_x=300, start_y=175, font_size=18, color=arcade.color.BLUE)
        arcade.draw_rectangle_outline(350, 135, 15, 60, arcade.color.BLUE, border_width=3)
        arcade.draw_rectangle_filled(350, self.azul, 50, 3, arcade.color.BLUE)


    def q_velocidades(self):
        serverName = ''
        serverPort = 61000
        serverSocket = socket(AF_INET, SOCK_DGRAM)
        serverSocket.bind((serverName, serverPort))
        cmd = ""
        update = ""
        while cmd != "b'z'":
            cmd = msvcrt.getch()
            cmd = str(cmd)
            print(cmd)

            if cmd == "b'S'":
                print("VERDE++")
                update = "vel_+_verde"
                self.verde += 1.364

            elif cmd == "b'T'":
                print("ROXO++")
                update = "vel_+_roxo"
                self.roxo += 1.364

            elif cmd == "b'E'":
                print("AMARELO++")
                update = "vel_+_amarelo"
                self.amarelo+=1.364
            elif cmd == "b'P'":
                print("AZUL++")
                update = "vel_+_azul"
                self.azul += 1.364
            elif cmd == "b'R'":
                print("VERDE--")
                update = "vel_-_verde"
                self.verde -= 1.364
            elif cmd == "b'A'":
                print("ROXO--")
                update = "vel_-_roxo"
                self.roxo -= 1.364
            elif cmd == "b'F'":
                print("AMARELO--")
                update = "vel_-_amarelo"
                self.amarelo -= 1.364
            elif cmd == "b'L'":
                print("AZUL--")
                update = "vel_-_azul"
                self.azul -= 1.364
            else:
                print("NENHUM")

            if self.verde >= 290:
                self.verde = 290

            if self.verde <= 230:
                self.verde = 230

            if self.roxo >= 290:
                self.roxo = 290

            if self.roxo <= 230:
                self.roxo = 230

            if self.amarelo >= 165:
                self.amarelo = 165

            if self.amarelo <= 105:
                self.amarelo = 105

            if self.azul >= 165:
                self.azul = 165

            if self.azul <= 105:
                self.azul = 105

            message, clientAddress = serverSocket.recvfrom(2048)
            message = message.decode('utf-8')
            # print(message)
            if message == "waiting":
                serverSocket.sendto(update.encode('utf-8'), clientAddress)
        serverSocket.close()

window = Game(500, 550)
arcade.run()