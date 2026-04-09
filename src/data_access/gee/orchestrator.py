from src.data_access.base.source import ImagerySource


class Orchestrator:
    def __init__(self):
        self.source = None

    def set_source(self, source: ImagerySource):
        self.source = source

    def run_process(self):
        image_id = self.source.search()
        metadata = self.source.get_metadata(image_id)  # noqa F841
