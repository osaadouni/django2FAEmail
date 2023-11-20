from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_otp.plugins.otp_email.models import EmailDevice


@receiver(post_save, sender=User)
def create_user_2fa_device(sender, instance, created, **kwargs):
    """
    Signal receiver to create or update a user profile when a user is created or updated.
    """
    print("User created/updated. Create/Update 2FA device!!")
    email_device, created = EmailDevice.objects.get_or_create(user=instance)
    email_device.confirmed = True
    email_device.name = "default" # Do not change this value !
    email_device.save()


@receiver(post_delete,sender=User)
def delete_user_2fa_device(sender, instance, *args, **kwargs):
    print("User deleted. Delete 2FA device !")
    EmailDevice.objects.filter(user=instance).delete()

# Connect the signal
# post_save.connect(create_user_emaildevice, sender=User)
