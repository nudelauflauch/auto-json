import blockstate as bl

def gen_special_model(model, modname, parent, super_secial):
    if super_secial:
        aus_block_model = '{\n  "parent": "'+parent+'",\n  "textures": {\n    "top": "'+modname+':block/'+model+'_top"\n   "bottom": "'+modname+':block/'+model+'_bottom"\n  }\n}'
    else:
        aus_block_model = '{\n  "parent": "'+parent+'",\n  "textures": {\n    "bottom": "'+modname+':block/'+model+'"\n   "top": "'+modname+':block/'+model+'"\n  "side": "'+modname+':block/'+model+'"}\n}'
    
    file  = open("output/"+modname+"/assets/"+modname+"/model/block/"+model+".json","w")
    file.write(aus_block_model)

def gen_block_model(model, modname, parent = ""):
    #aus_blockstate = '{\n	"variants": {\n		"": {\n			"model": "'+modname+':block/'+model+'"\n		}\n	}\n}'
    
    if parent:
        aus_block_model = '{"parent": "'+parent+'","textures": {"texture": "'+modname+'":block/'+model+'"}}'
    else:
        aus_block_model = '{\n  "parent": "minecraft:block/cube_all",\n  "textures": {\n    "all": "'+modname+':block/'+model+'"\n  }\n}'
    
    file  = open("output/"+modname+"/assets/"+modname+"/model/block/"+model+".json","w")
    file.write(aus_block_model)

def gen_item_model(model, modname, is_block_item = False):
    #item model for only item
    if is_block_item:
        aus_item = '{\n	"parent": "'+modname+':block/'+model+'"\n}'
        file  = open("output/"+modname+"/assets/"+modname+"/model/item/"+model+".json","w")
        
        file.write(aus_item)
    #itemmodel for a block item
    else:
        file  = open("output/"+modname+"/assets/"+modname+"/model/item/"+model+".json","w")
        aus_item = '{\n	"parent":"item/generated",\n	"textures": {\n		"layer0": "'+modname+':item/'+model+'"\n	}\n}'
        
        file.write(aus_item)
    
    file.close()

def gen_pres(modname):
    pressure_plate = """{
    "parent" : "minecraft:block/thin_block",
    "display" : {
            "gui" : {
            "rotation" : [ 30, 135, 0 ],
            "translation" : [ 0, 0, 0 ],
            "scale" : [ 0.625, 0.625, 0.625 ]
            },
            "fixed" : {
            "rotation" : [ 0, 90, 0 ],
            "translation" : [ 0, 0, 0 ],
            "scale" : [ 0.5, 0.5, 0.5 ]
            }
        },
        "elements" : [ {
            "from" : [ 1, 0, 1 ],
            "to" : [ 15, 1, 15 ],
            "faces" : {
            "down" : {
                "uv" : [ 1, 1, 15, 15 ],
                "texture" : "#texture",
                "cullface" : "down"
            },
            "up" : {
                "uv" : [ 1, 1, 15, 15 ],
                "texture" : "#texture"
            },
            "north" : {
                "uv" : [ 1, 15, 15, 16 ],
                "texture" : "#texture"
            },
            "south" : {
                "uv" : [ 1, 15, 15, 16 ],
                "texture" : "#texture"
            },
            "west" : {
                "uv" : [ 1, 15, 15, 16 ],
                "texture" : "#texture"
            },
            "east" : {
                "uv" : [ 1, 15, 15, 16 ],
                "texture" : "#texture"
            }
            }
        } ]
        }"""
    file  = open("output/"+modname+"/assets/"+modname+"/model/block/pressure_plate_inventory.json","w")
    file.write(pressure_plate)
    
def generates_drop(block, modname):
    ausgabe = '{"type": "minecraft:block","pools": [{"rolls": 1,"entries": [{"type": "minecraft:item","name": "'+modname+':'+block+'"}]}]}'
    
    file = open("output/"+modname+"/data/"+modname+"/loot_table/"+block+".json","w")
    file.write(ausgabe)