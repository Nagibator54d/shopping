from django .shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .forms import Productform, SignUpForm
from .models import Product, Category
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView,DetailView



class ProductListView(ListView):

    queryset=Product.published.all()
    template_name='shop/product_list.html'
    context_object_name='products'

    def get_context_data(self,**kwargs)->dict[str,Any]:
       context= super(ProductListView,self).get_context_data(**kwargs)
       context['categories']=Category.objects.all()
       return context



class ProductDetailView(DetailView):
    model= Product
    template_name='shop/product_detail.html'
    context_object_name='product'

    
# def product_list(request):
#     products=Product.objects.all()
#     categories=Category.objects.all()
#     context={
#         'products': products,
#         'categories': categories,
#     }
#     return render(request, 'shop/product_list.html', context)


# def product_detail(request, pk):
#     product=Product.objects.get(id=pk)
#     context={
#         'product': product,
#     }
#     return render(request, 'shop/product_detail.html', context)


def category_filter(request,pk):
    products=Product.objects.filter(category=pk)
    categories=Category.objects.all()
    context={
        'products': products,
        'categories': categories,
    }
    
    return render(request, 'shop/category.html', context)


def signup(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form=SignUpForm()

    return render(request, 'registration/signup.html', {'form':form})


def user_login(request):

    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            username=cd['username']
            password=cd['password']
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
            return redirect('product_list')
    else:
        form=AuthenticationForm()
    return render(request,'registration/login.html', {'form':form})
    

def create(request):
    if request.method =='POST':
        form = Productform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form=Productform()
    context={
        'form':form,
    }
    return render(request, 'shop/create.html', context)


def update(request,pk):
    product=Product.objects.get(id=pk)
    form=Productform(request.POST)
    if request.method == 'POST':
             form = Productform(request.POST, request.FILES)
             if form.is_valid():
                form.save()
                return redirect('product_list')
    context={
        'product': product,
        'form': form,
    }
    return render(request, 'shop/update.html', context)


def delete(request,pk):
    product=Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    context={
        'product':product,
    }
    return render(request,'shop/delete.html',context)