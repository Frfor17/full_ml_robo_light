import mujoco
import mujoco.viewer
import os

# Указываем путь к XML относительно текущей папки
model_path = "warehouse_ver2.xml"

# Проверяем, что файл существует
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Не найден файл: {model_path}")

# Загружаем модель и данные
model = mujoco.MjModel.from_xml_path(model_path)
data = mujoco.MjData(model)

# Запускаем viewer
with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        mujoco.mj_step(model, data)  # делаем шаг физики
        viewer.sync()               # синхронизируем камеру/рисование