import unittest
from app import app
import datetime


class BasicTestCase(unittest.TestCase):

    def setUp(self):
        """Executado antes de cada teste. Configura um cliente de teste."""
        self.app = app.test_client()
        self.app.testing = True

    def test_index_status_code(self):
        """Verifica se a rota '/' retorna o status code 200 OK."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        print("Teste 1: Status code da página inicial é 200.")

    def test_index_content_type(self):
        """Verifica se o cabeçalho 'Content-Type' é 'text/html'."""
        response = self.app.get('/')
        self.assertIn('text/html', response.content_type)
        print("Teste 2: O conteúdo da página é HTML.")

    def test_page_has_correct_title(self):
        """Verifica se a tag <title> contém 'Recycling Manager'."""
        response = self.app.get('/')
        html_content = response.data.decode('utf-8')
        self.assertIn('<title>Recycling Manager</title>', html_content)
        print("Teste 3: O título da página está correto.")

    def test_page_has_main_heading(self):
        """Verifica se o H1 'Tech Recycling' está na página."""
        response = self.app.get('/')
        html_content = response.data.decode('utf-8')
        self.assertIn('Tech Recycling</h1>', html_content)
        print("Teste 4: O cabeçalho principal H1 foi encontrado.")

    def test_footer_contains_author_name(self):
        """Verifica se o nome 'Luiz Gasparino' está no rodapé."""
        response = self.app.get('/')
        html_content = response.data.decode('utf-8')
        self.assertIn('Luiz Gasparino', html_content)
        print("Teste 5: O nome do autor está no rodapé.")

    def test_footer_contains_current_year(self):
        """Verifica se o ano no rodapé corresponde ao ano corrente."""
        current_year = datetime.date.today().year
        response = self.app.get('/')
        html_content = response.data.decode('utf-8')
        self.assertIn(str(current_year), html_content)
        print(f"Teste 6: Ano do rodapé ({current_year}) está correto.")


if __name__ == '__main__':
    unittest.main()
