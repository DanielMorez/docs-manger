from grappelli.dashboard import Dashboard as GrappelliDashboard
from grappelli.dashboard import modules


class Dashboard(GrappelliDashboard):
    def __init__(self, **kwargs):
        GrappelliDashboard.__init__(self, **kwargs)
        self.children.append(
            modules.ModelList(
                title="Абонентская база",
                column=1,
                collapsible=True,
                models=(
                    "manager.models.Customer",
                    "manager.models.Order",
                ),
            )
        )
        self.children.append(
            modules.ModelList(
                title="Справочная информация",
                column=1,
                collapsible=True,
                models=(
                    "manager.models.Sector",
                    "manager.models.Resource",
                    "manager.models.Equipment",
                    "manager.models.TechnicalProcess",
                ),
            )
        )
        self.children.append(
            modules.ModelList(
                title="Пользовательские данные",
                column=2,
                collapsible=True,
                models=(
                    "django.contrib.auth.models.Group",
                    "django.contrib.auth.models.User"
                ),
            )
        )
        self.children.append(
            modules.RecentActions(
                "Последние действия", limit=10, collapsible=True, column=3
            )
        )
