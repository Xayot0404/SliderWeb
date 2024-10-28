from django.db import models


class WebDesignModel(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slide_file = models.FileField(upload_to="slides")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Web_Design(WebDesignModel):
    class Meta:
        db_table = 'slayd1_article_model'


class WebDesignModel2(WebDesignModel):
    class Meta:
        db_table = 'slayd2_article_model'

class WebDesignModel3(WebDesignModel):
    class Meta:
        db_table = 'slayd3_article_model'

class WebDesignModel4(WebDesignModel):
    class Meta:
        db_table = 'slayd4_article_model'

class WebDesignModel5(WebDesignModel):
    class Meta:
        db_table = 'slayd5_article_model'

class WebDesignModel6(WebDesignModel):
    class Meta:
        db_table = 'slayd6_article_model'

class Presentation(models.Model):
    title = models.CharField(max_length=100)
    ppt_file = models.FileField(upload_to='presentations/')
    html_file = models.FileField(upload_to='html_presentations/', blank=True, null=True)
    def str(self):
         return self.title