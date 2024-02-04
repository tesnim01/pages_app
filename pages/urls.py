from django.urls import path
from .views import HomePageView, AboutPageView
urlpatterns = [
 path("about/", AboutPageView.as_view(), name="about"), # define location and name
 path("", HomePageView.as_view(), name="home"),
]
#we set urls to call the templates by "name" in the testing
#we only tested our url (locations and names) and not our templates
#we use assertions methods to test our templates
