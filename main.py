from parsers.markup import MarkupParser
from parsers.log import LogParser
from parsers.nlp import NLPParser
from parsers.query import QueryParser
from parsers.data import DataParser
from parsers.config import ConfigParser



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    markup_parser = MarkupParser("markup.txt")
    print(markup_parser.parse())

    print("-" * 40)
    log_parser = LogParser("log.txt")
    print(log_parser.parse())

    print("-" * 40)
    nlp_parser = NLPParser("nlp.txt")
    print(nlp_parser.parse())

    print("-" * 40)
    query_parser = QueryParser("query.txt")
    print(query_parser.parse())

    print("-" * 40)
    data_parser = DataParser("data.txt")
    print(data_parser.parse())

    print("-" * 40)
    config_parser = ConfigParser("config.txt")
    print(config_parser.parse())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
