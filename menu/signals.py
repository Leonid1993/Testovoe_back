from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Menu

@receiver(pre_save, sender=Menu)
def level_update_on_parent_id_change(sender, instance, **kwargs):
    if instance is not None:
        pre_save_state = Menu.objects.get(pk=instance.pk)
        if pre_save_state.parent_id != instance.parent_id:
            instance.level = Menu.objects.get(pk=instance.parent_id).level + 1

