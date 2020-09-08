from ads.models import Ad
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


class AdListView(OwnerListView):
    model = Ad


class AdDetailView(OwnerDetailView):
    model = Ad


class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'text', 'price']


class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'text', 'price']


class AdDeleteView(OwnerDeleteView):
    model = Ad
