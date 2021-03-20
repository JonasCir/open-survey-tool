from abc import ABC, abstractmethod


class Figure(ABC):
    html_config = {
        'config': {
            'displayModeBar': True
        },
        'full_html': False
    }
    pdf_config = {
        'config': {
            'displayModeBar': False
        },
        'full_html': False
    }

    @staticmethod
    @abstractmethod
    def get_html(cfg):
        pass
