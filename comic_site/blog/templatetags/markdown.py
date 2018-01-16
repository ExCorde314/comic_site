from django.utils.safestring import mark_safe
from django import template
import mistune as md
import bleach

register = template.Library()

@register.filter
def markdown(value):
    return mark_safe(
        bleach.clean(
            md.markdown(value, escape=False), 
            attributes = {
                            u'a': [u'href', u'title', u'target'],
                            u'th': [u'align'],
                            u'td': [u'align'],
                            u'acronym': [u'title'],
                            u'abbr': [u'title'],
                            u'img': [u'src', u'alt', u'title']
                         }, 
            tags = [
                        u'h1',
                        u'h2',
                        u'h3',
                        u'h4',
                        u'h5',
                        u'h6',
                        u'tbody',
                        u'table',
                        u'thead',
                        u'tr',
                        u'th',
                        u'td',
                        u'img',
                        u'del',
                        u'pre',
                        u'blockquote',
                        u'p',
                        u'hr',
                        u'a',
                        u'abbr',
                        u'acronym',
                        u'b',
                        u'blockquote',
                        u'code',
                        u'em',
                        u'i',
                        u'li',
                        u'ol',
                        u'strong',
                        u'ul'
                   ]
            )
        )

