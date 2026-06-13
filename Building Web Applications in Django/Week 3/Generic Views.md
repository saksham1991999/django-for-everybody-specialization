# Generic Views

### 1. In the class django.views.generic.list.ListView, which of the following methods is called earliest in the process?

- [x] get_template_names()
- [ ] get_queryset()
- [ ] get_context_data()
- [ ] render_to_response()

### 2. In the class django.views.generic.list.ListView, which of the following methods is called latest in the process?

- [ ] get_template_names()
- [ ] get_queryset()
- [ ] get_context_data()
- [x] render_to_response()

### 3. In the class django.views.generic.detail.Detailview, which of the following methods is called earliest in the process?

- [x] dispatch()
- [ ] get_queryset()
- [ ] get_object()
- [ ] render_to_response()

### 4. In the class django.views.generic.detail.DetailView, which of the following methods is called latest in the process?

- [ ] dispatch()
- [ ] get_queryset()
- [ ] get_object()
- [x] render_to_response()

### 5. By convention when using an app_name of "abc" and a model of "Dog", if you use a View that extends django.views.generic.detail.Detailview, what is the file name that will be used for the template?

- [x] templates/abc/dog_detail.html
- [ ] templates/abc/dog_detail.djtl
- [ ] templates/dog_detail.djtl
- [ ] templates/doc/abc_detail.djtl

### 6. If you want to override the template name chosen by convention in a View that extends django.views.generic.detail.Detailview, what is the name of the class attribute variable that you use?

- [x] template_name
- [ ] template
- [ ] template_override
- [ ] template_extend

### 7. By convention when using an app_name of "abc" and a model of "Dog", if you use a View that extends django.views.generic.list.ListView, what is the name of the context variable that will include all the Dog objects in the template when it is being rendered?

- [x] dog_list
- [ ] dogs
- [ ] dogs_select
- [ ] dogs.values()

### 8. For the following line in a views.py file, what is the best description of "Listview"?

`class ArticleListView(Listview):`

- [x] The class that is being extended
- [ ] The class that is being created
- [ ] The name of a view function
- [ ] The first parameter to the renderQ() method

### 9. For the following line in a views.py file, what is the best description of "ArticleListView"?

`class ArticleListView(Listview):`

- [ ] The class that is being extended
- [x] The class that is being created
- [ ] The name of a view function
- [ ] The first parameter to the render() method

### 10. For the following line in a urls.py file, where would you find the actual code for TemplateView?

```python
urlpatterns = [
    path('', Templateview.as_view(template_name='gview/main.html'))
]
```

- [x] In the Django source
- [ ] In views.py
- [ ] In settings.py
- [ ] In urls.py
