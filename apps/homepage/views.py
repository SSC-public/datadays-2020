from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView

from apps.accounts.models import Profile
from apps.resources.models import Document

from .models import Intro, TimelineEvent, Prize, Stat
from .serializers import *


class HomepageView(GenericAPIView):

    def get(self, request):
        data = {
                'intro': IntroSerializer(Intro.objects.last()).data,
                'timeline': TimelineEventSerializer(TimelineEvent.objects.all().order_by('id').order_by('order'), many=True).data,
                'prizes': PrizeSerializer(Prize.objects.all().order_by('id'), many=True).data,
                'stats': {
                        'users': Profile.objects.all().count(),
                        'resources': Document.objects.all().count(),
                    },
                }
        return Response(data)


class TermsOfUseView(GenericAPIView):

    def get(self, request):
        data = {
                'term': Intro.objects.first().term_of_use
                }
        return Response(data)

