import random
import os.path

if not os.path.isfile("/etc/django_secret_key.txt"):
    with open('/etc/django_secret_key.txt', 'w') as f:
        secret_key = ''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50))
        f.write(secret_key)