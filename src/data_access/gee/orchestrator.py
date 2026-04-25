from src.data_access.base.source import ImagerySource
from dataclasses import asdict


class Orchestrator:
    def __init__(self):
        self.source = None

    def set_source(self, source: ImagerySource):
        self.source = source

    def run_process(self):
        image_id = self.source.search()
        metadata = self.source.get_metadata(image_id)
        image_request = self.source.build_image_request(image_id)

        return {
            "image_id": image_id,
            "metadata": asdict(metadata),
            "image_request": asdict(image_request),
        }

    def download(self):
        self.source.download(image_request=self.run_process()["image_request"])
