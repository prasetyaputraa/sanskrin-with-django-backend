class SubmissionRouter:

    route_app_label = 'submitted_translations'

    def db_for_read(self, model, **hints):
        if model._meta.app_label == self.route_app_label:
            return 'mongo'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == self.route_app_label:
            return 'mongo'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == self.route_app_label:
            return db == 'mongo'
        return None