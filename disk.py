#Используем модуль os и функцию os.statvfs для просмотра свободного места на диске
import os
def freespace(way):
    stat = os.statvfs(way)
    size_disk = stat.f_frsize
    free_place = stat.f_bavail
    freespace = free_place * size_disk
    return freespace
#Назначаем путь к диску, определяем и выводим количество свободного места на диске
disk_way = "/"
free_space_bytes = freespace(disk_way)
print(f"Свободного места на диске {disk_way}: {free_space_bytes} байт")


echo "Hello world"
