from django.urls import include, path
from rest_framework import routers
from . import api
router = routers.DefaultRouter()
router.register(r'project-comment', api.ProjectCommentViewSet)
router.register(r'country-project-comment', api.CountryProjectCommentViewSet)
router.register(r'region-project-comment', api.RegionProjectCommentViewSet)

router.register(r'wereda-project-comment', api.WeredaProjectCommentViewSet)
router.register(r'city-project-comment', api.CityProjectCommentViewSet)
router.register(r'kebele-project-comment', api.KebeleProjectCommentViewSet)
router.register(r'user-region-project-comment', api.UserRegionProjectComment)

router.register(r'user-wereda-project-comment', api.UserWeredaProjectComment)
router.register(r'user-city-project-comment', api.UserCityProjectComment)
router.register(r'user-kebele-project-comment', api.UserKebeleProjectComment)
#router.register(r'all', api.ProjectList)






# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [path('all', api.ProjectCommentList),
               path('all-user-comments', api.UserProjectCommentList),path('all-user-comments-1', api.UserProjectCommentList1),
    path('', include(router.urls)),
]