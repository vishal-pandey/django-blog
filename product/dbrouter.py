
class ProductDBRouter(object):
    """
    A router to control app1 db operations
    """
    def db_for_read(self, model, **hints):
        from django.conf import settings
        if 'product' not in settings.DATABASES:
            return None
        if model._meta.app_label == 'product':
            return 'product'
        return None

    def db_for_write(self, model, **hints):
        from django.conf import settings
        if 'product' not in settings.DATABASES:
            return None
        if model._meta.app_label == 'product':
            return 'product'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        from django.conf import settings
        if 'product' not in settings.DATABASES:
            return None
        if obj1._meta.app_label == 'app1' or obj2._meta.app_label == 'app1':
            return True
        return None

    def allow_syncdb(self, db, model):
        from django.conf import settings
        if 'product' not in settings.DATABASES:
            return None
        if db == 'product':
            return model._meta.app_label == 'app1'
        elif model._meta.app_label == 'product':
            return False
        return None