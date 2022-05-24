from django.db import models

class Plus500(models.Model):
    url_from = models.CharField(max_length=250, blank=True)
    url_to = models.CharField(max_length=250, blank=True)
    ahrefs_rank = models.IntegerField()
    domain_rating = models.IntegerField()
    title = models.CharField(max_length=900, blank=True)
    competitor = models.CharField(max_length=250, blank=True)
    refdomains = models.IntegerField(blank=True, null=True)
    traffic = models.IntegerField(blank=True, null=True)
    refdomains_backlinks_ratio = models.FloatField(blank=True, null=True)
    category_options = (
        ('news', 'news'),
        ('finance', 'finance'),
        ('crypto', 'crypto'),
        ('forex', 'forex'),
        ('commodities', 'commodities'),
        ('leisure', 'leisure'),
    )
    category =  models.CharField(max_length=50, blank=True, choices=category_options)
    #contact_email = models.EmailField()

    def __str__(self):
        return self.url_from

class Settings_table(models.Model):
    #id - the key of the object
    id = models.IntegerField(primary_key=True)
    #the min values to filter on these fields
    domain_rating = models.IntegerField(null=True)
    domain_traffic = models.IntegerField(null=True)
    #organic_keywords = models.IntegerField(null=True)
    referringDomains_backlinks_ratio = models.IntegerField(null=True)
    #sorting priorities of the fields:
    domain_rating_priority = models.IntegerField(null=True)
    domain_traffic_priority = models.IntegerField(null=True)
    organic_keywords_priority = models.IntegerField(null=True)
    referringDomains_backlinks_ratio_priority = models.IntegerField(null=True)
    #cometitors bolean fields (True if selected, else False):
    avatrae = models.BooleanField(default=False)
    robinhood = models.BooleanField(default=False)
    etoro = models.BooleanField(default=False)
    IG = models.BooleanField(default=False)
    CMC_markets = models.BooleanField(default=False)
    #the email template
    email_template = models.CharField(max_length=10000, null=True)
    #last number of links:
    links_num = models.IntegerField(null=True)

    #is_news = models.BooleanField(default=False)
    #is_finance = models.BooleanField(default=False)
    #is_crypto = models.BooleanField(default=False)
    #is_forex = models.BooleanField(default=False)
    #is_commodities = models.BooleanField(default=False)
    #is_leisure = models.BooleanField(default=False)

    def __int__(self):
        return self.id
