import cv2
import os

# Количество фотографий для съемки
NUM_IMAGES = 30

# Создаем директорию, если ее нет
if not os.path.exists('images'):
    os.makedirs('images')

# Инициализируем камеру
cap = cv2.VideoCapture(0)

# Создаем пустой список для хранения изображений
images = []

# Запускаем цикл для съемки фотографий
for i in range(NUM_IMAGES):
    # Захватываем изображение с камеры
    ret, frame = cap.read()

    # Отображаем изображение
    cv2.imshow('frame', frame)

    # Сохраняем изображение в папке "images"
    filename = os.path.join('images', f'image_{i}.jpg')
    cv2.imwrite(filename, frame)

    # Добавляем изображение в список
    images.append(frame)

    # Ожидаем 100 мс между съемками фотографий
    cv2.waitKey(500)

# Останавливаем камеру и закрываем окна
cap.release()
cv2.destroyAllWindows()

# Обрабатываем список изображений, как в вашем текущем коде
