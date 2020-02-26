from django.db import models
from django.db.models.signals import pre_save , post_delete
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    STATUS_CHOICIS=(
        ('draft','Draft'),
        ('puzblished','published'),    
        )
    title = models.CharField(max_length=50 , null= False , blank = False)
    body = models.TextField()
    #tags = models.ManyToManyField('Tag')
    #category = models.ForeignKey(Category, on_delete = models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='../media',null=True , blank = True)
    date_published=models.DateTimeField(auto_now_add=True,verbose_name="date published")
    date_updated=models.DateTimeField(auto_now =True,verbose_name="date updated")
    slug_url = models.SlugField(blank=True,unique=True)
    #comment = models.ManyToManyField
    status=models.CharField(max_length=10,choices=STATUS_CHOICIS,default='published')
    likes = models.ManyToManyField(User,related_name="post_likes",blank=True)
    dislikes= models.ManyToManyField(User,related_name="post_dislikes",blank=True)
    class Meta:
        ordering = ('-date_published',)
    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("list", kwargs={"id": self.id})    

    def get_absolute_url(self):
        return reverse('posts:post_detail', args=[self.id])


#to show the image in the post 
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url  

#delete img from file media within the post 
@receiver(post_delete,sender = Post) 
def submission_delete(sender, instance,**kwargs):
    instance.image.delete(False) 

#slug concat username with post title to be more readable in url & to be unique 
def pre_save_post_receiver(sender,instance,*args,**kwargs):
    if not instance.slug_url:
        instance.slug_url = slugify(instance.user.username+"_"+instance.title) 

pre_save.connect(pre_save_post_receiver, sender=Post)        




