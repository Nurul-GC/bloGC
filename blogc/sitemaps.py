from django.contrib.sitemaps import Sitemap

from blogc.forms import Publicacao


class PublicacaoSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Publicacao.publicados.all()

    def lastmod(self, obj):
        return obj.data_atualizacao
