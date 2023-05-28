from ursina import *

app = Ursina()


def toggle_bool(arr):
    index = arr.index(True)
    arr[index] = False
    arr[(index + 1) % len(arr)] = True
    return arr


def toggle_visibility():
    vis = toggle_bool(model_visible)
    for i, model in enumerate(models):
        model.visible = vis[i]


model_visible = [True, False, False]

models = [
    Entity(
        model="./assets/models/scene.gltf",
        position=(40, -90, 0),
        scale=1.0,
        collider="mesh",
        visible=model_visible[0],
    ),
    Entity(
        model="./assets/models/skull.gltf",
        collider="mesh",
        position=(-25, -13, -17),
        scale=10.0,
        visible=model_visible[1],
    ),
    Entity(
        model="./assets/models/space.gltf",
        collider="mesh",
        position=(-10, -10, -14),
        scale=2.0,
        visible=model_visible[2],
    ),
]

Entity(
    model="./assets/models/mushroom.gltf",
    position=(0, 37, -50),
    scale=2.0,
    parent=models[0],
)

Sky(texture="sky_sunset")

camera.fov = 110
camera.rotation_x = 19
camera.rotation_y = 80
camera.rotation_z = 0
camera.x = -45

scene.fog_density = 0.001
scene.fog_color = color.rgb(50, 68, 168)


button = Button(
    text="Change",
    scale=(0.15, 0.1),
    origin=(0, 0),
    x=0,
    y=-0.4,
)

button.on_click = toggle_visibility


def update():
    for model in models:
        model.rotation_y += time.dt * 10

    if held_keys["right arrow"]:
        for model in models:
            model.rotation_y += time.dt * 50
    elif held_keys["left arrow"]:
        for model in models:
            model.rotation_y -= time.dt * 50


# EditorCamera()


app.run()
