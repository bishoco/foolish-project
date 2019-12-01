from django.test import TestCase
from .utils import article_has_slug, get_articles_from_api, get_main_article

class ContentApiTests(TestCase):
    def test_article_with_slug(self):
        slug = "10-promise"

        article_no_slug_10 = {"headline":"This one has slug 10-promise","modified":"2017-11-10T15:05:53Z","tags":[{"uuid":"78aa4c44-d4f4-11e5-86ff-0050569d32b9","slug":"msn","name":"MSN","tag_type":{"name":"Syndication Partner","slug":"syndication-partner"},"links":{"content":"http://api.fool.com/api/content?tag_uuids=78aa4c44-d4f4-11e5-86ff-0050569d32b9","self":"http://api.fool.com/api/tags/78aa4c44-d4f4-11e5-86ff-0050569d32b9"}},{"uuid":"342ec714-9adf-11e6-bdf0-0050569d32b9","slug":"default-partners","name":"Default Partners","tag_type":{"name":"Syndication Partner","slug":"syndication-partner"},"links":{"content":"http://api.fool.com/api/content?tag_uuids=342ec714-9adf-11e6-bdf0-0050569d32b9","self":"http://api.fool.com/api/tags/342ec714-9adf-11e6-bdf0-0050569d32b9"}},{"uuid":"89038dfe-5db3-11e3-8416-0050569d32b9","slug":"10-promise","name":"10% Promise","tag_type":{"name":"Personalized Email","slug":"personalized-email"},"links":{"content":"http://api.fool.com/api/content?tag_uuids=89038dfe-5db3-11e3-8416-0050569d32b9","self":"http://api.fool.com/api/tags/89038dfe-5db3-11e3-8416-0050569d32b9"}},{"uuid":"603e544a-1f53-11e5-a69e-0050569d4be0","slug":"yahoo-money","name":"Yahoo","tag_type":{"name":"Syndication Partner","slug":"syndication-partner"},"links":{"content":"http://api.fool.com/api/content?tag_uuids=603e544a-1f53-11e5-a69e-0050569d4be0","self":"http://api.fool.com/api/tags/603e544a-1f53-11e5-a69e-0050569d4be0"}}],"byline":"Scott Levine"}
        self.assertIs(article_has_slug(article_no_slug_10, slug), True)

        article_with_slug_10 = {"headline":"This one does not have slug 10-promise","modified":"2017-11-10T15:05:53Z","tags":[{"uuid":"78aa4c44-d4f4-11e5-86ff-0050569d32b9","slug":"msn","name":"MSN","tag_type":{"name":"Syndication Partner","slug":"syndication-partner"},"links":{"content":"http://api.fool.com/api/content?tag_uuids=78aa4c44-d4f4-11e5-86ff-0050569d32b9","self":"http://api.fool.com/api/tags/78aa4c44-d4f4-11e5-86ff-0050569d32b9"}},{"uuid":"342ec714-9adf-11e6-bdf0-0050569d32b9","slug":"default-partners","name":"Default Partners","tag_type":{"name":"Syndication Partner","slug":"syndication-partner"},"links":{"content":"http://api.fool.com/api/content?tag_uuids=342ec714-9adf-11e6-bdf0-0050569d32b9","self":"http://api.fool.com/api/tags/342ec714-9adf-11e6-bdf0-0050569d32b9"}},{"uuid":"603e544a-1f53-11e5-a69e-0050569d4be0","slug":"yahoo-money","name":"Yahoo","tag_type":{"name":"Syndication Partner","slug":"syndication-partner"},"links":{"content":"http://api.fool.com/api/content?tag_uuids=603e544a-1f53-11e5-a69e-0050569d4be0","self":"http://api.fool.com/api/tags/603e544a-1f53-11e5-a69e-0050569d4be0"}}],"byline":"Scott Levine"}
        self.assertIs(article_has_slug(article_with_slug_10, slug), False)

    def test_get_main_article(self):
        slug = "10-promise"        
        main_article_uuid = "a7acd8c8-c5ce-11e7-9fa6-0050569d4be0"

        article_list = get_articles_from_api()
        main_article = get_main_article(article_list, slug)
        self.assertEquals(main_article.get("uuid"), main_article_uuid)


