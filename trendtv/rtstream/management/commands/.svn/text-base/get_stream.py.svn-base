from django.core.management.base import BaseCommand, CommandError
from trendtv.rtstream.models import Consumable
from trendtv.data_stream.streamer import streamer
from trendtv.data_analysis.info_pull import get_content

class Command(BaseCommand):
    def _streamer_callback(p):
        contents = get_content(p.get("word"))
        for content in contents:
            entry = {"term":p.get("word"),"content":content}
            c = Consumable(buzzword=p.get("word"),source=p.get("source"),type=content['type'],created_date=datetime.datetime.now())
            c.save



	help = 'This command gets a real time stream of data and indexes it to create consumable content'

	def handle(self, *args, **options):
		self.stdout.write(str(args))
        st = streamer(_streamer_callback) 
