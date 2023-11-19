from django_elasticsearch_dsl import Index, Document, Date, Text,fields
from django_elasticsearch_dsl.registries import registry
from logingest.models import Log

PUBLISHER_INDEX=Index('logs_search')


PUBLISHER_INDEX.settings(
   number_of_shards=1,
   number_of_replicas=1
)

@PUBLISHER_INDEX.doc_type
class LogsDocument(Document):
   id=fields.IntegerField(attr="id")
   message = fields.TextField(
      type='text',
      fields={
        'raw': fields.KeywordField(),           
    }
   )
   timestamp = Date(
   default_timezone='UTC'
)
   metadata = fields.ObjectField(properties={
      'parentResourceId': fields.KeywordField(),
   })

   class Django(object):
      model=Log
      fields=["level","resourceId","traceId","spanId","commit"]

