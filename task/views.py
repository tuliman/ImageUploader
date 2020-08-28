from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages

from .models import Images, Size
from .forms import ImageForm, SizeForm
from .utlities import get_images


# Create your views here.


def index(request):
    data = Images.objects.all()
    context = {
        'data': data
    }
    return render(request, 'task/index.html', context)


class ImageView(View):
    def get(self, request):
        form = ImageForm(request.POST)

        context = {'form': form}
        return render(request, 'task/add_img.html', context)

    def post(self, request):
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            if (form.cleaned_data['url'] is '' and form.cleaned_data['image'] is not None) or (
                    form.cleaned_data['url'] is not '' and form.cleaned_data['image'] is None):

                if form['url'].value() != str(''):
                    if get_images(form.cleaned_data['url']) is not None:
                        data = Images.objects.create(image=get_images(form.cleaned_data['url']))
                        pk = data.id
                        return redirect(detail, pk=pk)
                    else:
                        form.add_error('url', 'Урл либо несодержит изображение либо несуществует')
                        return render(request, 'task/add_img.html', context={'form': form})

                elif form['image'] is not None:
                    data = Images.objects.create(image=form.cleaned_data['image'])

                    pk = data.id

                    return redirect(detail, pk=pk)

            elif form.cleaned_data['url'] is not '' and form.cleaned_data['image'] is not None:
                form.add_error('url', 'Обаполя немогут быть заполнены')
                print(form.errors)

                return render(request, 'task/add_img.html', context={'form': form})

            else:
                form.add_error('url', 'Хотябы одно поле должно быть заполнено')
                context = {
                    'form': form
                }
                return render(request, 'task/add_img.html', context)
        else:
            context = {
                'form': form
            }
            return render(request, 'task/add_img.html', context)


def detail(request, pk):
    get_data = get_object_or_404(Images, pk=pk)

    if request.method == 'POST':
        form = SizeForm(request.POST, instance=get_data)
        if form.is_valid():
            data = Size.objects.create(height=form.cleaned_data['height'], width=form.cleaned_data['width'], img=get_data)
            print(data.width,data.height)
            print(get_data.image.width)

            return redirect(detail, pk=pk)
    else:
        form = SizeForm(request.POST, instance=get_data)
        context = {
            'data': get_data,
            'form': form
        }
        return render(request, 'task/detail.html', context)
