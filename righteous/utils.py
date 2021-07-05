import os
from uuid import uuid4

def rename_imagefile_to_uuid(instance, filename):
        upload_to = f'media/foods/{instance.food.slug}'
        ext = filename.split('.')[-1]
        uuid = uuid4().hex

        if instance:
            filename = '{}_{}.{}'.format(uuid, instance, ext)
        else:
            filename = '{}.{}'.format(uuid, ext)
        
        return os.path.join(upload_to, filename)