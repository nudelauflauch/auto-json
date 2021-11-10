def fence_gate(modname, model):
      return '''{  "variants" : {    "facing=east,in_wall=false,open=false" : {      "uvlock" : true,      "y" : 270,      "model" : "'''+modname+''':block/'''+model+'''_fence_gate"    },    "facing=east,in_wall=false,open=true" : {      "uvlock" : true,      "y" : 270,      "model" : "'''+modname+''':block/'''+model+'''_fence_gate_open"    },    "facing=east,in_wall=true,open=false" : {      "uvlock" : true,      "y" : 270,      "model" : "'''+modname+''':block/'''+model+'''_fence_gate_wall"   },    "facing=east,in_wall=true,open=true" : {      "uvlock" : true,      "y" : 270,      "model" : "'''+modname+''':block/'''+model+'''_fence_gate_wall_open"    },    "facing=north,in_wall=false,open=false" : {      "uvlock" : true,      "y" : 180,      "model" : "'''+modname+''':block/'''+model+'''_fence_gate"    },    "facing=north,in_wall=false,open=true" : {      "uvlock" : true,      "y" : 180,
        "model" : "'''+modname+''':block/'''+model+'''_fence_gate_open"
      },
      "facing=north,in_wall=true,open=false" : {
        "uvlock" : true,
        "y" : 180,
        "model" : "'''+modname+''':block/'''+model+'''_fence_gate_wall"
      },
      "facing=north,in_wall=true,open=true" : {
        "uvlock" : true,
        "y" : 180,
        "model" : "'''+modname+''':block/'''+model+'''_fence_gate_wall_open"
      },
      "facing=south,in_wall=false,open=false" : {
        "uvlock" : true,
        "model" : "'''+modname+''':block/'''+model+'''_fence_gate"
      },
      "facing=south,in_wall=false,open=true" : {
        "uvlock" : true,
        "model" : "'''+modname+''':block/'''+model+'''_fence_gate_open"
      },
      "facing=south,in_wall=true,open=false" : {
        "uvlock" : true,
        "model" : "'''+modname+''':block/'''+model+'''_fence_gate_wall"
      },
      "facing=south,in_wall=true,open=true" : {
        "uvlock" : true,
        "model" : "'''+modname+''':block/'''+model+'''_fence_gate_wall_open"
      },
      "facing=west,in_wall=false,open=false" : {
        "uvlock" : true,
        "y" : 90,
        "model" : "'''+modname+''':block/'''+model+'''_fence_gate"
      },
      "facing=west,in_wall=false,open=true" : {
        "uvlock" : true,
        "y" : 90,
        "model" : "'''+modname+''':block/'''+model+'''_fence_gate_open"
      },
      "facing=west,in_wall=true,open=false" : {
        "uvlock" : true,
        "y" : 90,
        "model" : "'''+modname+''':block/'''+model+'''_fence_gate_wall"
      },
      "facing=west,in_wall=true,open=true" : {
        "uvlock" : true,
        "y" : 90,
        "model" : "'''+modname+''':block/'''+model+'''_fence_gate_wall_open"
          }
      }
      }'''

def fence(modname, model):
      return ''' {
      "multipart" : [ {
          "apply" : {
          "model" : "'''+modname+''':block/'''+model+'''_fence_post"
          }
      }, {
          "when" : {
          "north" : "true"
          },
          "apply" : {
          "model" : "'''+modname+''':block/'''+model+'''_fence_side",
          "uvlock" : true
          }
      }, {
          "when" : {
          "east" : "true"
          },
          "apply" : {
          "model" : "'''+modname+''':block/'''+model+'''_fence_side",
          "y" : 90,
          "uvlock" : true
          }
      }, {
          "when" : {
          "south" : "true"
          },
          "apply" : {
          "model" : "'''+modname+''':block/'''+model+'''_fence_side",
          "y" : 180,
          "uvlock" : true
          }
      }, {
          "when" : {
          "west" : "true"
          },
          "apply" : {
          "model" : "'''+modname+''':block/'''+model+'''_fence_side",
          "y" : 270,
          "uvlock" : true
          }
          } ]
          }'''

def button(modname, model):
    return '''{
    "variants" : {
        "face=ceiling,facing=east,powered=false" : {
      "model" : "'''+modname+''':block/'''+model+'''_button",
      "y" : 270,
      "x" : 180
    },
    "face=ceiling,facing=east,powered=true" : {
      "model" : "'''+modname+''':block/'''+model+'''_button_pressed",
      "y" : 270,
      "x" : 180
    },
    "face=ceiling,facing=north,powered=false" : {
      "model" : "'''+modname+''':block/'''+model+'''_button",
      "y" : 180,
      "x" : 180
    },
    "face=ceiling,facing=north,powered=true" : {
      "model" : "'''+modname+''':block/'''+model+'''_button_pressed",
      "y" : 180,
      "x" : 180
    },
    "face=ceiling,facing=south,powered=false" : {
      "model" : "'''+modname+''':block/'''+model+'''_button",
      "x" : 180
    },
    "face=ceiling,facing=south,powered=true" : {
      "model" : "'''+modname+''':block/'''+model+'''_button_pressed",
      "x" : 180
    },
    "face=ceiling,facing=west,powered=false" : {
      "model" : "'''+modname+''':block/'''+model+'''_button",
      "y" : 90,
      "x" : 180
    },
    "face=ceiling,facing=west,powered=true" : {
      "model" : "'''+modname+''':block/'''+model+'''_button_pressed",
      "y" : 90,
      "x" : 180
    },
    "face=floor,facing=east,powered=false" : {
      "model" : "'''+modname+''':block/'''+model+'''_button",
      "y" : 90
    },
    "face=floor,facing=east,powered=true" : {
      "model" : "'''+modname+''':block/'''+model+'''_button_pressed",
      "y" : 90
    },
    "face=floor,facing=north,powered=false" : {
      "model" : "'''+modname+''':block/'''+model+'''_button"
    },
    "face=floor,facing=north,powered=true" : {
      "model" : "'''+modname+''':block/'''+model+'''_button_pressed"
    },
    "face=floor,facing=south,powered=false" : {
      "model" : "'''+modname+''':block/'''+model+'''_button",
      "y" : 180
    },
    "face=floor,facing=south,powered=true" : {
      "model" : "'''+modname+''':block/'''+model+'''_button_pressed",
      "y" : 180
    },
    "face=floor,facing=west,powered=false" : {
      "model" : "'''+modname+''':block/'''+model+'''_button",
      "y" : 270
    },
    "face=floor,facing=west,powered=true" : {
      "model" : "'''+modname+''':block/'''+model+'''_button_pressed",
      "y" : 270
    },
    "face=wall,facing=east,powered=false" : {
      "model" : "'''+modname+''':block/'''+model+'''_button",
      "y" : 90,
      "x" : 90,
      "uvlock" : true
    },
    "face=wall,facing=east,powered=true" : {
      "model" : "'''+modname+''':block/'''+model+'''_button_pressed",
      "y" : 90,
      "x" : 90,
      "uvlock" : true
    },
    "face=wall,facing=north,powered=false" : {
      "model" : "'''+modname+''':block/'''+model+'''_button",
      "x" : 90,
      "uvlock" : true
    },
    "face=wall,facing=north,powered=true" : {
      "model" : "'''+modname+''':block/'''+model+'''_button_pressed",
      "x" : 90,
      "uvlock" : true
    },
    "face=wall,facing=south,powered=false" : {
      "model" : "'''+modname+''':block/'''+model+'''_button",
      "y" : 180,
      "x" : 90,
      "uvlock" : true
    },
    "face=wall,facing=south,powered=true" : {
      "model" : "'''+modname+''':block/'''+model+'''_button_pressed",
      "y" : 180,
      "x" : 90,
      "uvlock" : true
    },
    "face=wall,facing=west,powered=false" : {
      "model" : "'''+modname+''':block/'''+model+'''_button",
      "y" : 270,
      "x" : 90,
      "uvlock" : true
    },
    "face=wall,facing=west,powered=true" : {
      "model" : "'''+modname+''':block/'''+model+'''_button_pressed",
      "y" : 270,
      "x" : 90,
      "uvlock" : true
    }
    }
    }'''
def pressure_plate(modname, model):
      return '''{
      "variants" : {
          "powered=false" : {
          "model" : "'''+modname+''':block/'''+model+'''_pressure_plate"
          },
          "powered=true" : {
          "model" : "'''+modname+''':block/'''+model+'''_pressure_plate_down"
          }
      }
      }'''

def stairs(modname, model):
      return '''{
      "variants": {
          "facing=east,half=bottom,shape=inner_left": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_inner",
        "y": 270,
        "uvlock": true
      },
      "facing=east,half=bottom,shape=inner_right": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_inner"
      },
      "facing=east,half=bottom,shape=outer_left": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_outer",
        "y": 270,
        "uvlock": true
      },
      "facing=east,half=bottom,shape=outer_right": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_outer"
      },
      "facing=east,half=bottom,shape=straight": {
        "model": "'''+modname+''':block/'''+model+'''_stairs"
      },
      "facing=east,half=top,shape=inner_left": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_inner",
        "x": 180,
        "uvlock": true
      },
      "facing=east,half=top,shape=inner_right": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_inner",
        "x": 180,
        "y": 90,
        "uvlock": true
      },
      "facing=east,half=top,shape=outer_left": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_outer",
        "x": 180,
        "uvlock": true
      },
      "facing=east,half=top,shape=outer_right": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_outer",
        "x": 180,
        "y": 90,
        "uvlock": true
      },
      "facing=east,half=top,shape=straight": {
        "model": "'''+modname+''':block/'''+model+'''_stairs",
        "x": 180,
        "uvlock": true
      },
      "facing=north,half=bottom,shape=inner_left": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_inner",
        "y": 180,
        "uvlock": true
      },
      "facing=north,half=bottom,shape=inner_right": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_inner",
        "y": 270,
        "uvlock": true
      },
      "facing=north,half=bottom,shape=outer_left": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_outer",
        "y": 180,
        "uvlock": true
      },
      "facing=north,half=bottom,shape=outer_right": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_outer",
        "y": 270,
        "uvlock": true
      },
      "facing=north,half=bottom,shape=straight": {
        "model": "'''+modname+''':block/'''+model+'''_stairs",
        "y": 270,
        "uvlock": true
      },
      "facing=north,half=top,shape=inner_left": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_inner",
        "x": 180,
        "y": 270,
        "uvlock": true
      },
      "facing=north,half=top,shape=inner_right": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_inner",
        "x": 180,
        "uvlock": true
      },
      "facing=north,half=top,shape=outer_left": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_outer",
        "x": 180,
        "y": 270,
        "uvlock": true
      },
      "facing=north,half=top,shape=outer_right": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_outer",
        "x": 180,
        "uvlock": true
      },
      "facing=north,half=top,shape=straight": {
        "model": "'''+modname+''':block/'''+model+'''_stairs",
        "x": 180,
        "y": 270,
        "uvlock": true
      },
      "facing=south,half=bottom,shape=inner_left": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_inner"
      },
      "facing=south,half=bottom,shape=inner_right": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_inner",
        "y": 90,
        "uvlock": true
      },
      "facing=south,half=bottom,shape=outer_left": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_outer"
      },
      "facing=south,half=bottom,shape=outer_right": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_outer",
        "y": 90,
        "uvlock": true
      },
      "facing=south,half=bottom,shape=straight": {
        "model": "'''+modname+''':block/'''+model+'''_stairs",
        "y": 90,
        "uvlock": true
      },
      "facing=south,half=top,shape=inner_left": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_inner",
        "x": 180,
        "y": 90,
        "uvlock": true
      },
      "facing=south,half=top,shape=inner_right": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_inner",
        "x": 180,
        "y": 180,
        "uvlock": true
      },
      "facing=south,half=top,shape=outer_left": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_outer",
        "x": 180,
        "y": 90,
        "uvlock": true
      },
      "facing=south,half=top,shape=outer_right": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_outer",
        "x": 180,
        "y": 180,
        "uvlock": true
      },
      "facing=south,half=top,shape=straight": {
        "model": "'''+modname+''':block/'''+model+'''_stairs",
        "x": 180,
        "y": 90,
        "uvlock": true
      },
      "facing=west,half=bottom,shape=inner_left": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_inner",
        "y": 90,
        "uvlock": true
      },
      "facing=west,half=bottom,shape=inner_right": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_inner",
        "y": 180,
        "uvlock": true
      },
      "facing=west,half=bottom,shape=outer_left": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_outer",
        "y": 90,
        "uvlock": true
      },
      "facing=west,half=bottom,shape=outer_right": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_outer",
        "y": 180,
        "uvlock": true
      },
      "facing=west,half=bottom,shape=straight": {
        "model": "'''+modname+''':block/'''+model+'''_stairs",
        "y": 180,
        "uvlock": true
      },
      "facing=west,half=top,shape=inner_left": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_inner",
        "x": 180,
        "y": 180,
        "uvlock": true
      },
      "facing=west,half=top,shape=inner_right": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_inner",
        "x": 180,
        "y": 270,
        "uvlock": true
      },
      "facing=west,half=top,shape=outer_left": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_outer",
        "x": 180,
        "y": 180,
        "uvlock": true
      },
      "facing=west,half=top,shape=outer_right": {
        "model": "'''+modname+''':block/'''+model+'''_stairs_outer",
        "x": 180,
        "y": 270,
        "uvlock": true
      },
      "facing=west,half=top,shape=straight": {
        "model": "'''+modname+''':block/'''+model+'''_stairs",
        "x": 180,
        "y": 180,
        "uvlock": true
          }
      }
      }'''

def slab(modname, model):
      return '''
          {
        "variants": {
          "type=bottom": {
            "model": "'''+modname+''':block/'''+model+'''_slab"
          },
          "type=double": {
            "model": "'''+modname+''':block/'''+model+'''"
          },
          "type=top": {
            "model": "'''+modname+''':block/'''+model+'''_slab_top"
          }
        }
      } '''

def trapdoor(modname, model):
      return '''{
      "variants": {
      "facing=east,half=bottom,open=false": {
        "model": "'''+modname+''':block/'''+model+'''_trapdoor_bottom",
        "y": 90
      },
      "facing=east,half=bottom,open=true": {
        "model": "'''+modname+''':block/'''+model+'''_trapdoor_open",
        "y": 90
      },
      "facing=east,half=top,open=false": {
        "model": "'''+modname+''':block/'''+model+'''_trapdoor_top",
        "y": 90
      },
      "facing=east,half=top,open=true": {
        "model": "'''+modname+''':block/'''+model+'''_trapdoor_open",
        "x": 180,
        "y": 270
      },
      "facing=north,half=bottom,open=false": {
        "model": "'''+modname+''':block/'''+model+'''_trapdoor_bottom"
      },
      "facing=north,half=bottom,open=true": {
        "model": "'''+modname+''':block/'''+model+'''_trapdoor_open"
      },
      "facing=north,half=top,open=false": {
        "model": "'''+modname+''':block/'''+model+'''_trapdoor_top"
      },
      "facing=north,half=top,open=true": {
        "model": "'''+modname+''':block/'''+model+'''_trapdoor_open",
        "x": 180,
        "y": 180
      },
      "facing=south,half=bottom,open=false": {
        "model": "'''+modname+''':block/'''+model+'''_trapdoor_bottom",
        "y": 180
      },
      "facing=south,half=bottom,open=true": {
        "model": "'''+modname+''':block/'''+model+'''_trapdoor_open",
        "y": 180
      },
      "facing=south,half=top,open=false": {
        "model": "'''+modname+''':block/'''+model+'''_trapdoor_top",
        "y": 180
      },
      "facing=south,half=top,open=true": {
        "model": "'''+modname+''':block/'''+model+'''_trapdoor_open",
        "x": 180,
        "y": 0
      },
      "facing=west,half=bottom,open=false": {
        "model": "'''+modname+''':block/'''+model+'''_trapdoor_bottom",
        "y": 270
      },
      "facing=west,half=bottom,open=true": {
        "model": "'''+modname+''':block/'''+model+'''_trapdoor_open",
        "y": 270
      },
      "facing=west,half=top,open=false": {
        "model": "'''+modname+''':block/'''+model+'''_trapdoor_top",
        "y": 270
      },
      "facing=west,half=top,open=true": {
        "model": "'''+modname+''':block/'''+model+'''_trapdoor_open",
        "x": 180,
        "y": 90
          }
        }
      }'''

def wall(modname, model):
      return '''{
      "multipart": [
      {
        "when": {
          "up": "true"
        },
        "apply": {
          "model": "'''+modname+''':block/'''+model+'''_wall_post"
        }
      },
      {
        "when": {
          "north": "low"
        },
        "apply": {
          "model": "'''+modname+''':block/'''+model+'''_wall_side",
          "uvlock": true
        }
      },
      {
        "when": {
          "east": "low"
        },
        "apply": {
          "model": "'''+modname+''':block/'''+model+'''_wall_side",
          "y": 90,
          "uvlock": true
        }
      },
      {
        "when": {
          "south": "low"
        },
        "apply": {
          "model": "'''+modname+''':block/'''+model+'''_wall_side",
          "y": 180,
          "uvlock": true
        }
      },
      {
        "when": {
          "west": "low"
        },
        "apply": {
          "model": "'''+modname+''':block/'''+model+'''_wall_side",
          "y": 270,
          "uvlock": true
        }
      },
      {
        "when": {
          "north": "tall"
        },
        "apply": {
          "model": "'''+modname+''':block/'''+model+'''_wall_side_tall",
          "uvlock": true
        }
      },
      {
        "when": {
          "east": "tall"
        },
        "apply": {
          "model": "'''+modname+''':block/'''+model+'''_wall_side_tall",
          "y": 90,
          "uvlock": true
        }
      },
      {
        "when": {
          "south": "tall"
        },
        "apply": {
          "model": "'''+modname+''':block/'''+model+'''_wall_side_tall",
          "y": 180,
          "uvlock": true
        }
      },
      {
        "when": {
          "west": "tall"
        },
        "apply": {
          "model": "'''+modname+''':block/'''+model+'''_wall_side_tall",
          "y": 270,
          "uvlock": true
            }
          }
        ]
      }'''

def door(modname, model):
    return '''{
    "variants": {
      "facing=east,half=lower,hinge=left,open=false": {
        "model": "'''+modname+''':block/'''+model+'''_door_bottom"
      },
      "facing=east,half=lower,hinge=left,open=true": {
        "model": "'''+modname+''':block/'''+model+'''_door_bottom_hinge",
        "y": 90
      },
      "facing=east,half=lower,hinge=right,open=false": {
        "model": "'''+modname+''':block/'''+model+'''_door_bottom_hinge"
      },
      "facing=east,half=lower,hinge=right,open=true": {
        "model": "'''+modname+''':block/'''+model+'''_door_bottom",
        "y": 270
      },
      "facing=east,half=upper,hinge=left,open=false": {
        "model": "'''+modname+''':block/'''+model+'''_door_top"
      },
      "facing=east,half=upper,hinge=left,open=true": {
        "model": "'''+modname+''':block/'''+model+'''_door_top_hinge",
        "y": 90
      },
      "facing=east,half=upper,hinge=right,open=false": {
        "model": "'''+modname+''':block/'''+model+'''_door_top_hinge"
      },
      "facing=east,half=upper,hinge=right,open=true": {
        "model": "'''+modname+''':block/'''+model+'''_door_top",
        "y": 270
      },
      "facing=north,half=lower,hinge=left,open=false": {
        "model": "'''+modname+''':block/'''+model+'''_door_bottom",
        "y": 270
      },
      "facing=north,half=lower,hinge=left,open=true": {
        "model": "'''+modname+''':block/'''+model+'''_door_bottom_hinge"
      },
      "facing=north,half=lower,hinge=right,open=false": {
        "model": "'''+modname+''':block/'''+model+'''_door_bottom_hinge",
        "y": 270
      },
      "facing=north,half=lower,hinge=right,open=true": {
        "model": "'''+modname+''':block/'''+model+'''_door_bottom",
        "y": 180
      },
      "facing=north,half=upper,hinge=left,open=false": {
        "model": "'''+modname+''':block/'''+model+'''_door_top",
        "y": 270
      },
      "facing=north,half=upper,hinge=left,open=true": {
        "model": "'''+modname+''':block/'''+model+'''_door_top_hinge"
      },
      "facing=north,half=upper,hinge=right,open=false": {
        "model": "'''+modname+''':block/'''+model+'''_door_top_hinge",
        "y": 270
      },
      "facing=north,half=upper,hinge=right,open=true": {
        "model": "'''+modname+''':block/'''+model+'''_door_top",
        "y": 180
      },
      "facing=south,half=lower,hinge=left,open=false": {
        "model": "'''+modname+''':block/'''+model+'''_door_bottom",
        "y": 90
      },
      "facing=south,half=lower,hinge=left,open=true": {
        "model": "'''+modname+''':block/'''+model+'''_door_bottom_hinge",
        "y": 180
      },
      "facing=south,half=lower,hinge=right,open=false": {
        "model": "'''+modname+''':block/'''+model+'''_door_bottom_hinge",
        "y": 90
      },
      "facing=south,half=lower,hinge=right,open=true": {
        "model": "'''+modname+''':block/'''+model+'''_door_bottom"
      },
      "facing=south,half=upper,hinge=left,open=false": {
        "model": "'''+modname+''':block/'''+model+'''_door_top",
        "y": 90
      },
      "facing=south,half=upper,hinge=left,open=true": {
        "model": "'''+modname+''':block/'''+model+'''_door_top_hinge",
        "y": 180
      },
      "facing=south,half=upper,hinge=right,open=false": {
        "model": "'''+modname+''':block/'''+model+'''_door_top_hinge",
        "y": 90
      },
      "facing=south,half=upper,hinge=right,open=true": {
        "model": "'''+modname+''':block/'''+model+'''_door_top"
      },
      "facing=west,half=lower,hinge=left,open=false": {
        "model": "'''+modname+''':block/'''+model+'''_door_bottom",
        "y": 180
      },
      "facing=west,half=lower,hinge=left,open=true": {
        "model": "'''+modname+''':block/'''+model+'''_door_bottom_hinge",
        "y": 270
      },
      "facing=west,half=lower,hinge=right,open=false": {
        "model": "'''+modname+''':block/'''+model+'''_door_bottom_hinge",
        "y": 180
      },
      "facing=west,half=lower,hinge=right,open=true": {
        "model": "'''+modname+''':block/'''+model+'''_door_bottom",
        "y": 90
      },
      "facing=west,half=upper,hinge=left,open=false": {
        "model": "'''+modname+''':block/'''+model+'''_door_top",
        "y": 180
      },
      "facing=west,half=upper,hinge=left,open=true": {
        "model": "'''+modname+''':block/'''+model+'''_door_top_hinge",
        "y": 270
      },
      "facing=west,half=upper,hinge=right,open=false": {
        "model": "'''+modname+''':block/'''+model+'''_door_top_hinge",
        "y": 180
      },
      "facing=west,half=upper,hinge=right,open=true": {
        "model": "'''+modname+''':block/'''+model+'''_door_top",
        "y": 90
          }
        }
      }'''
      
# def rest(name):
#     name_fence_gate_open = '''{
#         "parent": "minecraft:block/template_fence_gate_open",
#         "textures": {
#             "texture": "'''+modname+''':block/'''+model+'''"
#         }
#         }'''
#     name_fence_gate_wall_open = '''{
#         "parent": "minecraft:block/template_fence_gate_wall_open",
#         "textures": {
#             "texture": "'''+modname+''':block/'''+model+'''"
#         }
#         }'''
#     name_fence_gate_wall = '''{
#     "parent": "minecraft:block/template_fence_gate_wall",
#     "textures": {
#         "texture": "'''+modname+''':block/'''+model+'''"
#     }
#     }'''

#     name_fence_gate = '''{
#     "parent": "minecraft:block/template_fence_gate",
#     "textures": {
#         "texture": "'''+modname+''':block/'''+model+'''"
#     }
#     }'''
#     name_button_inventory = '''{
#     "parent": "minecraft:block/button_inventory",
#     "textures": {
#         "texture": "'''+modname+''':block/'''+model+'''"
#     }
#     }'''

#     name_button_pressed = '''{
#     "parent": "minecraft:block/button_pressed",
#     "textures": {
#         "texture": "'''+modname+''':block/'''+model+'''"
#     }
#     }'''
#     name_button = '''{
#     "parent": "minecraft:block/button",
#     "textures": {
#         "texture": "'''+modname+''':block/'''+model+'''"
#     }
#     }'''    
#     name_fence_inventory = ''' {
#     "parent": "minecraft:block/fence_inventory",
#     "textures": {
#         "texture": "'''+modname+''':block/'''+model+'''"
#         }
#         }'''
#     name_fence_post = '''{
#     "parent": "minecraft:block/fence_post",
#     "textures": {
#         "texture": "'''+modname+''':block/'''+model+'''"
#         }
#         }'''
#     name_fence_side = '''{
#     "parent": "minecraft:block/fence_side",
#     "textures": {
#         "texture": "'''+modname+''':block/'''+model+'''"
#         }
#         }'''

#     name_pressure_plate_down = '''{
#     "parent": "minecraft:block/pressure_plate_down",
#     "textures": {
#         "texture": "'''+modname+''':block/'''+model+'''"
#         }
#         }'''
#     name_pressure_plate = '''{
#         "parent": "minecraft:block/pressure_plate_up",
#         "textures": {
#         "texture": "'''+modname+''':block/'''+model+'''"
#         }
#         }'''
        
#     name_pressure_plate_inv = '''{
#       //ACHTUNG SELBER MACHEN
#         "parent": "'''+modname+''':block/pressure_plate_inv",
#         "textures": {
#         "texture": "'''+modname+''':block/'''+model+'''"
#         }
#         }'''
        
#     name_stairs_inner = '''{
#     "parent": "minecraft:block/inner_stairs",
#     "textures": {
#         "bottom": "'''+modname+''':block/'''+model+'''",
#         "top": "'''+modname+''':block/'''+model+'''",
#         "side": "'''+modname+''':block/'''+model+'''"
#         }
#         }'''
#     name_stairs_outer = '''{
#     "parent": "minecraft:block/outer_stairs",
#     "textures": {
#         "bottom": "'''+modname+''':block/'''+model+'''",
#         "top": "'''+modname+''':block/'''+model+'''",
#         "side": "'''+modname+''':block/'''+model+'''"
#         }
#         }'''
#     name_stairs = '''{
#     "parent": "minecraft:block/stairs",
#     "textures": {
#         "bottom": "'''+modname+''':block/'''+model+'''",
#         "top": "'''+modname+''':block/'''+model+'''",
#         "side": "'''+modname+''':block/'''+model+'''"
#         }
#         }'''

#     name_slab_top = '''{
#     "parent": "minecraft:block/slab_top",
#     "textures": {
#       "bottom": "'''+modname+''':block/'''+model+'''",
#       "top": "'''+modname+''':block/'''+model+'''",
#       "side": "'''+modname+''':block/'''+model+'''"
#       }
#     }'''

#     name_slab = '''{
#       "parent": "minecraft:block/slab",
#       "textures": {
#         "bottom": "'''+modname+''':block/'''+model+'''",
#         "top": "'''+modname+''':block/'''+model+'''",
#         "side": "'''+modname+''':block/'''+model+'''"
#       }
#     }'''
    
#     name_trapdoor_bottom = '''{
#       "parent": "minecraft:block/template_orientable_trapdoor_bottom",
#       "textures": {
#         "texture": "'''+modname+''':block/'''+model+'''_trapdoor"
#       }
#     }'''
    
#     name_trapdoor_open = '''{
#       "parent": "minecraft:block/template_orientable_trapdoor_open",
#       "textures": {
#         "texture": "'''+modname+''':block/'''+model+'''_trapdoor"
#       }
#     }'''
    
#     name_trapdoor_top = '''
#     {
#       "parent": "minecraft:block/template_orientable_trapdoor_top",
#       "textures": {
#         "texture": "'''+modname+''':block/'''+model+'''_trapdoor"
#       }
#     }'''
    
#     name_wall_side = '''{
#       "parent": "minecraft:block/template_wall_side",
#       "textures": {
#         "wall": "'''+modname+''':block/'''+model+'''"
#       }
#     }'''
    
#     name_wall_side_tall = '''{
#       "parent": "minecraft:block/template_wall_side_tall",
#       "textures": {
#         "wall": "'''+modname+''':block/'''+model+'''"
#       }
#     }'''
    
#     name_wall_post = '''{
#       "parent": "minecraft:block/template_wall_post",
#       "textures": {
#         "wall": "'''+modname+''':block/'''+model+'''"
#       }
#     }'''
    
#     name_wall_inventory = '''{
#       "parent": "minecraft:block/wall_inventory",
#       "textures": {
#         "wall": "'''+modname+''':block/'''+model+'''"
#       }
#     }'''
    
#     name_list = ["stairs", "fence_gate" , "fence_gate_open", "fence_gate_wall_open", "fence_gate_wall", "fence_gate_wall", "button_inventory", "button_pressed", "button", "fence_inventory", "fence_post", "fence_side", "pressure_plate_down","pressure_plate_inv", "pressure_plate", "stairs_inner", "stairs_outer", "stairs", "slab_top", "slab", "trapdoor_bottom", "trapdoor_open", "trapdoor_top", "wall_side", "wall_side_tall", "wall_post", "wall_inventory"]
#     eingabeliste = [name_stairs, name_fence_gate, name_fence_gate_open, name_fence_gate_wall_open, name_fence_gate_wall, name_fence_gate_wall, name_button_inventory, name_button_pressed, name_button, name_fence_inventory, name_fence_post, name_fence_side, name_pressure_plate_down,  name_pressure_plate, name_pressure_plate_inv, name_stairs_inner,name_stairs_outer, name_stairs, name_slab_top, name_slab, name_trapdoor_bottom, name_trapdoor_open, name_trapdoor_top, name_wall_side, name_wall_side_tall, name_wall_post, name_wall_inventory]

#     for write, names in zip(eingabeliste, name_list):
#         file  = open(f"./ausgabe/{name}_{names}.json","w")
#         file.write(write)

# def door(name):
#     door = '''{
#   "variants": {
#     "facing=east,half=lower,hinge=left,open=false": {
#       "model": "'''+modname+''':block/'''+model+'''_door_bottom"
#     },
#     "facing=east,half=lower,hinge=left,open=true": {
#       "model": "'''+modname+''':block/'''+model+'''_door_bottom_hinge",
#       "y": 90
#     },
#     "facing=east,half=lower,hinge=right,open=false": {
#       "model": "'''+modname+''':block/'''+model+'''_door_bottom_hinge"
#     },
#     "facing=east,half=lower,hinge=right,open=true": {
#       "model": "'''+modname+''':block/'''+model+'''_door_bottom",
#       "y": 270
#     },
#     "facing=east,half=upper,hinge=left,open=false": {
#       "model": "'''+modname+''':block/'''+model+'''_door_top"
#     },
#     "facing=east,half=upper,hinge=left,open=true": {
#       "model": "'''+modname+''':block/'''+model+'''_door_top_hinge",
#       "y": 90
#     },
#     "facing=east,half=upper,hinge=right,open=false": {
#       "model": "'''+modname+''':block/'''+model+'''_door_top_hinge"
#     },
#     "facing=east,half=upper,hinge=right,open=true": {
#       "model": "'''+modname+''':block/'''+model+'''_door_top",
#       "y": 270
#     },
#     "facing=north,half=lower,hinge=left,open=false": {
#       "model": "'''+modname+''':block/'''+model+'''_door_bottom",
#       "y": 270
#     },
#     "facing=north,half=lower,hinge=left,open=true": {
#       "model": "'''+modname+''':block/'''+model+'''_door_bottom_hinge"
#     },
#     "facing=north,half=lower,hinge=right,open=false": {
#       "model": "'''+modname+''':block/'''+model+'''_door_bottom_hinge",
#       "y": 270
#     },
#     "facing=north,half=lower,hinge=right,open=true": {
#       "model": "'''+modname+''':block/'''+model+'''_door_bottom",
#       "y": 180
#     },
#     "facing=north,half=upper,hinge=left,open=false": {
#       "model": "'''+modname+''':block/'''+model+'''_door_top",
#       "y": 270
#     },
#     "facing=north,half=upper,hinge=left,open=true": {
#       "model": "'''+modname+''':block/'''+model+'''_door_top_hinge"
#     },
#     "facing=north,half=upper,hinge=right,open=false": {
#       "model": "'''+modname+''':block/'''+model+'''_door_top_hinge",
#       "y": 270
#     },
#     "facing=north,half=upper,hinge=right,open=true": {
#       "model": "'''+modname+''':block/'''+model+'''_door_top",
#       "y": 180
#     },
#     "facing=south,half=lower,hinge=left,open=false": {
#       "model": "'''+modname+''':block/'''+model+'''_door_bottom",
#       "y": 90
#     },
#     "facing=south,half=lower,hinge=left,open=true": {
#       "model": "'''+modname+''':block/'''+model+'''_door_bottom_hinge",
#       "y": 180
#     },
#     "facing=south,half=lower,hinge=right,open=false": {
#       "model": "'''+modname+''':block/'''+model+'''_door_bottom_hinge",
#       "y": 90
#     },
#     "facing=south,half=lower,hinge=right,open=true": {
#       "model": "'''+modname+''':block/'''+model+'''_door_bottom"
#     },
#     "facing=south,half=upper,hinge=left,open=false": {
#       "model": "'''+modname+''':block/'''+model+'''_door_top",
#       "y": 90
#     },
#     "facing=south,half=upper,hinge=left,open=true": {
#       "model": "'''+modname+''':block/'''+model+'''_door_top_hinge",
#       "y": 180
#     },
#     "facing=south,half=upper,hinge=right,open=false": {
#       "model": "'''+modname+''':block/'''+model+'''_door_top_hinge",
#       "y": 90
#     },
#     "facing=south,half=upper,hinge=right,open=true": {
#       "model": "'''+modname+''':block/'''+model+'''_door_top"
#     },
#     "facing=west,half=lower,hinge=left,open=false": {
#       "model": "'''+modname+''':block/'''+model+'''_door_bottom",
#       "y": 180
#     },
#     "facing=west,half=lower,hinge=left,open=true": {
#       "model": "'''+modname+''':block/'''+model+'''_door_bottom_hinge",
#       "y": 270
#     },
#     "facing=west,half=lower,hinge=right,open=false": {
#       "model": "'''+modname+''':block/'''+model+'''_door_bottom_hinge",
#       "y": 180
#     },
#     "facing=west,half=lower,hinge=right,open=true": {
#       "model": "'''+modname+''':block/'''+model+'''_door_bottom",
#       "y": 90
#     },
#     "facing=west,half=upper,hinge=left,open=false": {
#       "model": "'''+modname+''':block/'''+model+'''_door_top",
#       "y": 180
#     },
#     "facing=west,half=upper,hinge=left,open=true": {
#       "model": "'''+modname+''':block/'''+model+'''_door_top_hinge",
#       "y": 270
#     },
#     "facing=west,half=upper,hinge=right,open=false": {
#       "model": "'''+modname+''':block/'''+model+'''_door_top_hinge",
#       "y": 180
#     },
#     "facing=west,half=upper,hinge=right,open=true": {
#       "model": "'''+modname+''':block/'''+model+'''_door_top",
#       "y": 90
#         }
#       }
#     }'''
    
#     door_bottom_hinge = '''{
#       "parent": "minecraft:block/door_bottom_rh",
#       "textures": {
#         "top": "'''+modname+''':block/'''+model+'''_door_top",
#         "bottom": "'''+modname+''':block/'''+model+'''_door_bottom"
#       }
#     }'''
    
#     door_top = '''{
#       "parent": "minecraft:block/door_top",
#       "textures": {
#         "top": "'''+modname+''':block/'''+model+'''_door_top",
#         "bottom": "'''+modname+''':block/'''+model+'''_door_bottom"
#       }
#     }'''
#     door_top_hinge = '''{
#         "parent": "minecraft:block/door_top_rh",
#         "textures": {
#           "top": "'''+modname+''':block/'''+model+'''_door_top",
#           "bottom": "'''+modname+''':block/'''+model+'''_door_bottom"
#         }
#       }'''
#     door_bottom = '''{
#       "parent": "minecraft:block/door_bottom",
#       "textures": {
#         "top": "'''+modname+''':block/'''+model+'''_door_top",
#         "bottom": "'''+modname+''':block/'''+model+'''_door_bottom"
#       }
#     }'''
    
#     names = ["door", "door_bottom_hinge", "door_top", "door_top_hinge", "door_bottom"]
#     writes = [door, door_bottom_hinge, door_top, door_top_hinge, door_bottom]
    
#     for namee, write in zip(names,writes):
#         file  = open(f"./ausgabe/{name}_{namee}.json","w")
#         file.write(write)