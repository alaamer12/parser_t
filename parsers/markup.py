from .base import BaseParser

class MarkupParser(BaseParser):
    def __init__(self, markup_source):
        self.markup_source = markup_source
        self.parsed_markup = None

    def parse(self):
        self._preprocess_markup()
        self._parse_markup()
        self._postprocess_markup()
        return self.parsed_markup

    def _preprocess_markup(self):
        # Perform preprocessing steps
        pass

    def _parse_markup(self):
        # Parse markup from self.markup_source
        pass

    def _postprocess_markup(self):
        # Perform postprocessing steps
        pass
