from abc import ABC, abstractmethod


class Figure(ABC):
    html_config = {
        'config': {
            'displaylogo': False
        },
        'full_html': False
    }
    pdf_config = {
        'config': {
            'displaylogo': False
        },
        'full_html': False
    }

    @staticmethod
    @abstractmethod
    def get_html(cfg):
        pass
