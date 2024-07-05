# from django.shortcuts import render
# from .models import shows
# # Create your views here.
# def index(request):
#     show=shows.objects.all()
#     if show:
#         return render(request,"index.html",context={'show':show})
#     else:
#         return render(request,"index.html",context={'message':"No shows avilable at the moment"})
# def vid(request,pk):
#     show=shows.objects.get(id=pk)
#     return render(request,"play_vid.html",context={"show":show})
# myapp/views.py

from django.shortcuts import render, get_object_or_404
from django.http import StreamingHttpResponse, HttpResponse, Http404
from django.views import View
import os
import re
from netflix_clone import settings
from .models import shows as Show
from itertools import groupby
from operator import itemgetter

def index(request):
    shows = Show.objects.all().order_by('category')
    if shows:
        grouped_shows={}
        for key, group in groupby(shows, key=lambda x: getattr(x, 'category')):
            grouped_shows[key] = list(group)
        return render(request,"index.html",{'grouped_shows': grouped_shows})
    else:
        return render(request, "index.html", context={'message': "No shows available at the moment"})

def vid_desc(request, pk):
    show = get_object_or_404(Show, id=pk)
    return render(request, "play_vid.html", context={"show": show})

class StreamVideoView(View):
    def get(self, request, pk):
        show = get_object_or_404(Show, id=pk)
        filename=show.name
        filepath= show.videos.path

        if not os.path.exists(filepath):
            raise Http404("File not found")

        range_header = request.headers.get('Range', None)
        size = os.path.getsize(filepath)
        content_type = 'video/mp4'

        if range_header:
            range_match = re.match(r'bytes=(\d+)-(\d*)', range_header)
            if range_match:
                start = int(range_match.group(1))
                end = range_match.group(2)
                if end:
                    end = int(end)
                else:
                    end = size - 1
            else:
                return HttpResponse(status=400, content="Invalid Range Header")

            length = end - start + 1
            response = StreamingHttpResponse(
                self.file_iterator(filepath, start, length),
                status=206,
                content_type=content_type
            )
            response['Content-Length'] = str(length)
            response['Content-Range'] = f'bytes {start}-{end}/{size}'
        else:
            response = StreamingHttpResponse(
                self.file_iterator(filepath, 0, size),
                content_type=content_type
            )
            response['Content-Length'] = str(size)

        response['Accept-Ranges'] = 'bytes'
        return response

    def file_iterator(self, filepath, offset, length, chunk_size=8192):
        with open(filepath, 'rb') as f:
            f.seek(offset)
            remaining = length
            while remaining > 0:
                chunk_size = min(chunk_size, remaining)
                data = f.read(chunk_size)
                if not data:
                    break
                yield data
                remaining -= len(data)
