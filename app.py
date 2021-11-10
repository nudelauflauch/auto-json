import tkinter as tk
from tkinter.constants import END
from PIL import Image, ImageTk
import blockstate as bl
import models, os


class switches():
    posx = 0
    posy = 0
    state = False
    tkinter = tk.Toplevel()
    beschirftung = ""
    name = ""
    switch_on = ImageTk.PhotoImage(Image.open("switch_on.png").resize((90, 50), Image.ANTIALIAS))
    switch_off = ImageTk.PhotoImage(Image.open('switch_off.png').resize((90, 50), Image.ANTIALIAS))
    
    def __init__(self, posx, posy, tkinter, beschirftung, name):
        self.posx = posx
        self.posy = posy
        self.tkinter = tkinter
        self.beschirftung = beschirftung
        self.name = name
            
        self.beschreibung = tk.Label(self.tkinter, bg="green",text=self.beschirftung, font=('arial', 12, 'bold'))
        self.beschreibung.place(relx=self.posx, rely=self.posy)
        
        self.switch = tk.Button(self.tkinter, command=self.change, image=self.switch_off)
        self.switch.place(relx=self.posx+0.29, rely=self.posy-0.03)
    
    def change(self):
        
        if self.state:
            self.switch.config(image=self.switch_off)
            self.state = False
        else:
            self.switch.config(image=self.switch_on)
            self.state = True
    
    def getstate(self):
        return self.state
    
    def getname(self):
        return self.name


class add ():
    ausgabe = []
    modname = ""
    filename = ""
    
    haupt = tk.Toplevel()
    haupt.geometry('600x600')
    
    switch_off = tk.PhotoImage()
    switch_on = tk.PhotoImage()
    
    def __init__(self, modname):
        self.modname = modname
        self.main = tk.Frame(self.haupt, bg='green')
        self.main.place(relwidth=1, relheight=1)
        
        self.switch_on = ImageTk.PhotoImage(Image.open("switch_on.png").resize((90, 50), Image.ANTIALIAS))
        self.switch_off = ImageTk.PhotoImage(Image.open('switch_off.png').resize((90, 50), Image.ANTIALIAS))
        
        try:
            file = open("output/settings", "r")
            for line in file:
                self.modname = line
        except:
            file = open("output/settings", "w")
            file.write("example_mod")
            self.modname = "example_mod"
        
        self.draw()


    def weiter(self):
        things = []
        exit_code = True
        for switch in self.switches:
            if switch.getname() == "item" and switch.getstate():
                things= ["item"]
                exit_code = False
                break
            
            if switch.getstate():
                things.append(switch.getname())
                exit_code = False
        
        if not exit_code:
            self.ausgabe.append([self.eingabe.get(), things])
            self.eingabe.delete(0, END)

    def start(self):
        if self.eingabe.get() != "":
            self.weiter()
        self.modname = self.modname_eingabe.get()
        
        file = open("output/settings", "w").write(self.modname)
        
        if self.ausgabe != [] or self.filename:
            print(self.ausgabe)
            
            if self.filename == "":
                write = ""
                for line in self.ausgabe:
                    write = write + str(line) + "\n"
                if not os.path.exists("output/"):
                    os.makedirs("output/")
                try:
                    if open("./output/"+ self.modname +"_mod.txt"):
                        file = open("./output/"+ self.modname +"_mod.txt", "a+")
                        file.write(write)
                except:
                    file = open("./output/"+ self.modname +"_mod.txt", "w+")
                    file.write(write)
                
                self.filename = "./output/"+ self.modname +"_mod.txt"
                file.close()
            create_files(self.haupt, self.filename, self.modname)
            self.main = self.main.destroy()
            
        else:
            print("ERROR: mindestens 1 datei")
    
    def read_in_file(self):
        from tkinter.filedialog import askopenfilename
        self.filename = askopenfilename()
        if self.filename.endswith(".txt"):
            print(self.filename)
        elif self.filename == "":
            pass
        elif not self.filename.endswith(".txt"):
            print("ERROR: DIE EINGELESENE DATEI MUSS EINE TXT DATEI SEIN")
            self.filename = ""
            self.read_in_file()
    
    def draw(self):        
        self.eingabe = tk.Entry(self.main, width=30,font=('arial', 20, 'bold'))
        self.eingabe.place(relx=0.0, rely=0.0, relwidth=0.5, relheight=0.1)

        self.start_button = tk.Button(self.main, command=self.start, text="Start", font=('arial', 20, 'bold'))
        self.start_button.place(relx=0.82, rely=0.0,relwidth=0.15, relheight=0.1)

        self.weiter_button = tk.Button(self.main, command=self.weiter, text="Weiter", font=('arial', 20, 'bold'))
        self.weiter_button.place(relx=0.5, rely=0.0,relwidth=0.15, relheight=0.1)
        
        self.weiter_button = tk.Button(self.main, command=self.read_in_file, text="Laden", font=('arial', 20, 'bold'))
        self.weiter_button.place(relx=0.66, rely=0.0,relwidth=0.15, relheight=0.1)

        self.modname_ueber = tk.Label(self.main, text="Modname", bg="green", font=('arial', 20, 'bold'))
        self.modname_ueber.place(relx=0.0, rely=0.15)

        self.modname_eingabe = tk.Entry(self.main, width=30,font=('arial', 20, 'bold'))
        self.modname_eingabe.place(relx=0.3, rely=0.13, relwidth=0.5, relheight=0.1)

        self.modname_eingabe.insert(10, self.modname)

        #unteren buttons
        self.isblock = switches(0.005, 0.3, self.main, "Block", "block")
        self.isitem = switches(0.005, 0.4, self.main, "Item", "item")
        self.isdoor = switches(0.005, 0.5, self.main, "Door", "door")
        self.istrapdoor = switches(0.005, 0.6, self.main, "Trappdoor", "trappdoor")
        self.isstair = switches(0.005, 0.7, self.main, "Stair", "stair")
        self.isslab = switches(0.005, 0.8, self.main, "Slab", "slab")
        self.isbutton = switches(0.005, 0.9, self.main, "Button", "button")
        self.ispersureplate = switches(0.5, 0.3, self.main, "Pressure_plate", "pressure_plate")
        self.isfencegate = switches(0.5, 0.4, self.main, "Fence Gate", "fence_gate")
        self.isfence = switches(0.5, 0.5, self.main, "Fence", "fence")
        self.iswall = switches(0.5, 0.6, self.main, "Wall", "wall")
        
        self.switches = [self.isblock, self.isitem, self.isdoor, self.istrapdoor, self.isstair, self.isslab, self.isbutton, self.ispersureplate, self.isfencegate, self.isfence, self.iswall]
        
class create_files():
    tkinter = tk.Tk()    
    filename = ""
    item_liste = []
    block_liste = []
    generel_list = []
    modname = ""
    
    def __init__(self, tkinter, filename, modname):
        self.tkinter = tkinter
        self.filename = filename
        self.modname = modname
        
        self.FENCE_GATE = ["minecraft:block/template_fence_gate_open", "minecraft:block/template_fence_gate_wall_open", "minecraft:block/template_fence_gate_wall", "minecraft:block/template_fence_gate"]
        self.BUTTON = ["minecraft:block/button_inventory", "minecraft:block/button_pressed", "minecraft:block/button"]
        self.FENCE = ["minecraft:block/fence_inventory", "minecraft:block/fence_post", "minecraft:block/fence_side"]
        self.PRESSURE_PLATE = ["minecraft:block/pressure_plate_down", "minecraft:block/pressure_plate_up", modname+":block/pressure_plate_inventory"]
        self.STAIR = ["minecraft:block/inner_stairs", "minecraft:block/outer_stairs", "minecraft:block/stairs"]
        self.SLAB = ["minecraft:block/slab_top", "minecraft:block/slab"]    
        self.TRAPDOOR = ["minecraft:block/template_orientable_trapdoor_bottom", "minecraft:block/template_orientable_trapdoor_open", "minecraft:block/template_orientable_trapdoor_top"]
        self.WALL = ["minecraft:block/template_wall_side", "minecraft:block/template_wall_side_tall", "minecraft:block/template_wall_post", "minecraft:block/wall_inventory"]
        self.DOOR = ["minecraft:block/door_bottom_rh", "minecraft:block/door_top", "minecraft:block/door_top_rh", "minecraft:block/door_bottom"]
        self.BLOCK = ["minecraft:block/cube_all"]
        
        self.NAME_FECE_GATE = ["fence_gate_open", "fence_gate_wall_open", "fence_gate_wall", "fence_gate_wall""fence_gate"]
        self.NAME_BUTTON = ["button_inventory", "button_pressed", "button"]
        self.NAME_FENCE = ["fence_inventory", "fence_post", "fence_side"]
        self.NAME_PRESURE_PLATE = ["pressure_plate_down", "pressure_plate", "pressure_plate_inv"]
        self.NAME_STAIR = ["stairs_inner", "stairs_outer", "stairs"]
        self.NAME_SLAB = ["slab_top", "slab"]
        self.NAME_TAPDOOR = ["trapdoor_bottom", "trapdoor_open", "trapdoor_top"]
        self.NAME_WALL = ["wall_side", "wall_side_tall", "wall_post", "wall_inventory"]
        self.NAME_DOOR = ["door", "door_bottom_hinge", "door_top", "door_top_hinge", "door_bottom"]
        
        self.main = tk.Frame(self.tkinter, bg='green')
        self.main.place(relwidth=1, relheight=1)
        
        self.draw()
        self.make_usfule_blocks()
        
    def make_usfule_blocks(self):
        
        file = open(self.filename, "r")
        for lines in file:
            line = self.str_to_list(lines)
            if line[1][0] == "item":
                self.item_liste.append(line)
            else:
                for model in line[1]:
                    self.block_liste.append([line[0], model])
            
            for model in line[1]:
                self.generel_list.append([line[0], model])
        file.close()

    def get_name(self, model):
        retrun_model = ""
        was_ = False
        for index, letter in enumerate(model):
            if index == 0:
                retrun_model += str(letter).upper()
            elif letter == "_":
                retrun_model += " "
                was_ = True
            elif was_:
                retrun_model += str(letter).upper()
                was_ = False
            else:
                retrun_model += str(letter)
        return retrun_model
    
    def model_gen(self):
        if not os.path.exists("output/"+self.modname+"/assets/"+self.modname+"/model/item"):
            os.makedirs("output/"+self.modname+"/assets/"+self.modname+"/model/item")
        if not os.path.exists("output/"+self.modname+"/assets/"+self.modname+"/model/block"):
            os.makedirs("output/"+self.modname+"/assets/"+self.modname+"/model/block")
        if not os.path.exists("output/"+self.modname+"/assets/"+self.modname+"/blockstates/"):
            os.makedirs("output/"+self.modname+"/assets/"+self.modname+"/blockstates/")
        
        for model in self.block_liste:
            if model[1] == "block":
                models.gen_block_model(model[0], self.modname)
                models.gen_item_model(model[0], self.modname, False)
            elif model[1] == "item":
                models.gen_item_model(model[0], self.modname, True)
            else:
                special = False
                if model[1] == "door":
                    aus = self.DOOR
                    name_end = self.NAME_DOOR
                    special = True
                    blockstate = bl.door(self.modname, f"{model[0]}_{model[1]}")
                elif model[1] == "trappdoor":
                    aus = self.TRAPDOOR
                    name_end = self.NAME_TAPDOOR
                    blockstate = bl.trapdoor(self.modname, f"{model[0]}_{model[1]}")
                elif model[1] == "stair":
                    aus = self.STAIR
                    name_end = self.NAME_STAIR
                    special = True
                    blockstate = bl.stairs(self.modname, f"{model[0]}_{model[1]}")
                elif model[1] == "slab":
                    name_end = self.NAME_SLAB
                    aus = self.SLAB
                    special = True
                    blockstate = bl.slab(self.modname, f"{model[0]}_{model[1]}")
                elif model[1] == "button":
                    aus = self.BUTTON
                    name_end = self.NAME_BUTTON
                    blockstate = bl.button(self.modname, f"{model[0]}_{model[1]}")
                elif model[1] == "pressure_plate":
                    aus = self.PRESSURE_PLATE
                    name_end = self.NAME_PRESURE_PLATE
                    models.gen_pres(self.modname)
                    blockstate = bl.pressure_plate(self.modname, f"{model[0]}_{model[1]}")
                elif model[1] == "fence_gate":
                    aus = self.FENCE_GATE
                    name_end = self.NAME_FECE_GATE
                    blockstate = bl.fence_gate(self.modname, f"{model[0]}_{model[1]}")
                elif model[1] == "fence":
                    aus = self.FENCE
                    name_end = self.NAME_FENCE
                    blockstate = bl.fence(self.modname, f"{model[0]}_{model[1]}")
                elif model[1] == "wall":
                    aus = self.WALL
                    name_end = self.NAME_WALL
                    blockstate = bl.wall(self.modname, f"{model[0]}_{model[1]}")
                
                for parent, end in zip(aus, name_end):
                    if special:
                        if model[1] == "door":
                            models.gen_special_model(f"{model[0]}_{end}", self.modname, parent, True)
                        else:
                            models.gen_special_model(f"{model[0]}_{end}", self.modname, parent, False)
                    else:
                        models.gen_block_model(f"{model[0]}_{end}", self.modname, parent)
                    models.gen_item_model(str(model[0]+"_"+model[1]), self.modname, True)
                
                file  = open("output/"+self.modname+"/assets/"+self.modname+"/blockstates/"+model[0]+"_"+model[1]+".json","w")
                file.write(blockstate)
        
        for item in self.item_liste:
            models.gen_item_model(item[0], self.modname)
                
    def lang_gen(self):
        if not os.path.exists("output/"+self.modname+"/assets/"+self.modname+"/lang"):
            os.makedirs("output/"+self.modname+"/assets/"+self.modname+"/lang")
            
        write = "{\n"
        for model in self.generel_list:
            if model[1] == "item":
                write += '  item.'+self.modname + '.' + model[0] + '" : "' + self.get_name(model[0]) + '",\n'
            elif model[1] == "block":
                write += '  block.'+self.modname + '.' + model[0] + '" : "' + self.get_name(model[0]) + '",\n'
            else:
                write += '  block.'+self.modname + '.' + model[0] + "_" + model[1] + '" : "' + self.get_name(model[0]) + '",\n'
        write += "}"
        
        file = open("output/"+self.modname+"/assets/"+self.modname+"/lang/en_us.json", "w")
        file.write(write)
        
    def drop_gen(self):
        if not os.path.exists("output/"+self.modname+"/data/"+self.modname+"/loot_table"):
            os.makedirs("output/"+self.modname+"/data/"+self.modname+"/loot_table")
        
        for block1 in self.block_liste:
            for block in block1:
                if block == "block":
                    models.generates_drop(str(block), self.modname)
                else:
                    models.generates_drop(f"{block1[0]}_{block}", self.modname)
    
    def draw(self):
        self.start_button = tk.Button(self.main, command=self.model_gen, text="Start Model/\nBlockstate/\nItem model Generaton", font=('arial', 25, 'bold'))
        self.start_button.place(relx=0.2, rely=0.0,relwidth=0.65, relheight=0.3)
        
        self.start_button = tk.Button(self.main, command=self.lang_gen, text="Start Lang\n Generaton", font=('arial', 25, 'bold'))
        self.start_button.place(relx=0.05, rely=0.4,relwidth=0.35, relheight=0.3)
        
        self.start_button = tk.Button(self.main, command=self.drop_gen, text="Start Drop\n Generaton", font=('arial', 25, 'bold'))
        self.start_button.place(relx=0.55, rely=0.4,relwidth=0.35, relheight=0.3)
        
    def str_to_list(self, beginn_list):
        str_1 = ""
        end_liste = []
        end_liste1 = []
        active_list = 0
        passt = False
        for i, letter  in enumerate(beginn_list):
            if letter == "[" and i != 0 :
                active_list += 1
                str_1 = ""
            if letter == "]":
                active_list -= 1
                if active_list == 0:
                    end_liste.append(end_liste1)
                    
            if letter == "'" and passt == True:
                passt = False
                if active_list == 0:
                    end_liste.append(str_1)
                elif active_list == 1:
                    end_liste1.append(str_1)
                str_1 = ""
            elif letter == "'":
                passt = True
            elif passt:
                str_1 = str_1 + letter
        return end_liste

add("ellada")

add.haupt.mainloop()