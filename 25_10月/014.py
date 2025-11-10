cmd = ['reset','mv','rotate','set_pattern','set_color','stamp']
class Stamp:
    def __init__(self):
        self.pos:list[float]= [0,0]
        self.angle:float= 0
        self.pattern:str = "no_pattern"
        self.color:str= "black"
    def reset(cls):
        cls.pos = [0.0,0.0]
        cls.angle = 00.
        cls.pattern = "no_pattern"
        cls.color = "black"
    def mv(cls,x,y):
        cls.pos = [cls.pos[0]+x,cls.pos[1]+y]
    def rotate(cls,angle):
        angle = float(angle)
        cls.angle += angle
        cls.angle %= 360
    def set_pattern(cls,pattern):
        cls.pattern = pattern
    def set_color(cls,color):
        cls.color = color
    def stamp(cls):
        print(f"Stamping... [position: ({cls.pos[0]:.2f}, {cls.pos[1]:.2f}), rotation: {cls.angle:.2f} degrees, pattern: {cls.pattern}, color: {cls.color}]")
    def execute(cls,command:str):
        cmd_list = command.split()
        if cmd_list[0] in cmd:
            if len(cmd_list) == 1:
                getattr(cls,cmd_list[0])()
            elif len(cmd_list) == 2:
                getattr(cls,cmd_list[0])(cmd_list[1])
            elif len(cmd_list) == 3:
                getattr(cls,cmd_list[0])(float(cmd_list[1]),float(cmd_list[2]))

if __name__ == "__main__":
    s = Stamp()
    no_opt = True
    for _ in range(6):
        command = input("")
        if command.lower() == 'stamp':
            no_opt = False
        s.execute(command)
    if no_opt:
        print("Stamping canceled")
