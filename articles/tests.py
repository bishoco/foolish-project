from django.test import TestCase
from .utils import *

class ContentApiTests(TestCase):
    def test_article_with_slug(self):
        slug = "10-promise"

        article_no_slug_10 = {"headline":"This one has slug 10-promise","modified":"2017-11-10T15:05:53Z","tags":[{"uuid":"78aa4c44-d4f4-11e5-86ff-0050569d32b9","slug":"msn","name":"MSN","tag_type":{"name":"Syndication Partner","slug":"syndication-partner"},"links":{"content":"http://api.fool.com/api/content?tag_uuids=78aa4c44-d4f4-11e5-86ff-0050569d32b9","self":"http://api.fool.com/api/tags/78aa4c44-d4f4-11e5-86ff-0050569d32b9"}},{"uuid":"342ec714-9adf-11e6-bdf0-0050569d32b9","slug":"default-partners","name":"Default Partners","tag_type":{"name":"Syndication Partner","slug":"syndication-partner"},"links":{"content":"http://api.fool.com/api/content?tag_uuids=342ec714-9adf-11e6-bdf0-0050569d32b9","self":"http://api.fool.com/api/tags/342ec714-9adf-11e6-bdf0-0050569d32b9"}},{"uuid":"89038dfe-5db3-11e3-8416-0050569d32b9","slug":"10-promise","name":"10% Promise","tag_type":{"name":"Personalized Email","slug":"personalized-email"},"links":{"content":"http://api.fool.com/api/content?tag_uuids=89038dfe-5db3-11e3-8416-0050569d32b9","self":"http://api.fool.com/api/tags/89038dfe-5db3-11e3-8416-0050569d32b9"}},{"uuid":"603e544a-1f53-11e5-a69e-0050569d4be0","slug":"yahoo-money","name":"Yahoo","tag_type":{"name":"Syndication Partner","slug":"syndication-partner"},"links":{"content":"http://api.fool.com/api/content?tag_uuids=603e544a-1f53-11e5-a69e-0050569d4be0","self":"http://api.fool.com/api/tags/603e544a-1f53-11e5-a69e-0050569d4be0"}}],"byline":"Scott Levine"}
        self.assertIs(article_has_slug(article_no_slug_10, slug), True)

        article_with_slug_10 = {"headline":"This one does not have slug 10-promise","modified":"2017-11-10T15:05:53Z","tags":[{"uuid":"78aa4c44-d4f4-11e5-86ff-0050569d32b9","slug":"msn","name":"MSN","tag_type":{"name":"Syndication Partner","slug":"syndication-partner"},"links":{"content":"http://api.fool.com/api/content?tag_uuids=78aa4c44-d4f4-11e5-86ff-0050569d32b9","self":"http://api.fool.com/api/tags/78aa4c44-d4f4-11e5-86ff-0050569d32b9"}},{"uuid":"342ec714-9adf-11e6-bdf0-0050569d32b9","slug":"default-partners","name":"Default Partners","tag_type":{"name":"Syndication Partner","slug":"syndication-partner"},"links":{"content":"http://api.fool.com/api/content?tag_uuids=342ec714-9adf-11e6-bdf0-0050569d32b9","self":"http://api.fool.com/api/tags/342ec714-9adf-11e6-bdf0-0050569d32b9"}},{"uuid":"603e544a-1f53-11e5-a69e-0050569d4be0","slug":"yahoo-money","name":"Yahoo","tag_type":{"name":"Syndication Partner","slug":"syndication-partner"},"links":{"content":"http://api.fool.com/api/content?tag_uuids=603e544a-1f53-11e5-a69e-0050569d4be0","self":"http://api.fool.com/api/tags/603e544a-1f53-11e5-a69e-0050569d4be0"}}],"byline":"Scott Levine"}
        self.assertIs(article_has_slug(article_with_slug_10, slug), False)

    def test_get_main_article(self):
        slug = "10-promise"
        #this is the uuid of the first article with slug = 10-promise in content_api.json
        main_article_uuid = "a7acd8c8-c5ce-11e7-9fa6-0050569d4be0"

        article_list = get_articles_from_api()

        main_article = get_main_article(article_list, slug)
        self.assertEquals(main_article.uuid, main_article_uuid)

        first_article = get_main_article(article_list, "bad slug")
        first_article_uuid = "f52c15f2-c5a9-11e7-8889-0050569d4be0"
        self.assertEquals(first_article.uuid, first_article_uuid)
    
    def test_get_sub_articles(self):
        article_list = get_articles_from_api()
        main_article_uuid = "a7acd8c8-c5ce-11e7-9fa6-0050569d4be0"
        count = 3;

        sub_article_list = get_sub_articles (article_list, count, main_article_uuid)
        self.assertEquals(len(sub_article_list), count)
        
        filtered_list = [x for x in sub_article_list if x.uuid == main_article_uuid]
        self.assertEquals(len(filtered_list), 0)
    
    def test_convert_raw_article_to_article(self):
        slug = "10-promise"
        main_article_uuid = "a7acd8c8-c5ce-11e7-9fa6-0050569d4be0"
        image_url = "https://g.foolcdn.com/editorial/images/463206/gold_bar_2.jpg"
        byline = "Scott Levine"

        article_list = get_articles_from_api()
        article = get_main_article(article_list, slug)
        
        self.assertEquals(article.uuid, main_article_uuid)
        self.assertEquals(article.byline, byline)
        self.assertEquals(article.image_url, image_url)