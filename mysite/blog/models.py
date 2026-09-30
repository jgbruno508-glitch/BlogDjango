from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    # campos do post
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    body = models.TextField()

    # preenchido automaticamente
    Publish = models.DateField(default=timezone.now) # timezone.now retorna a data e a hora atuais em um formato ciente do fuso horário (timezone-aware).
    created = models.DateField(auto_now_add=True) # Instrução que preenche o campo automaticamente com a data atual apenas no momento em que o registro é criado pela primeira vez. Esse valor não é alterado em edições futuras.
    update = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-publish"] # Define a ordenação padrão com a qual os posts serão recuperados do banco de dados quando nenhuma ordenação específica for solicitada na consulta O sinal de hífen (-) antes do campo publish indica ordem decrescente, garantindo que os posts sejam retornados em ordem cronológica reversa (do mais recente para o mais antigo) por padrão
        indexes = [
            models.Index(fields=["-publish"]),
        ] # Define a criação de um índice de banco de dados para o campo publish Índices no banco de dados servem para melhorar o desempenho de buscas, filtros e ordenações Como o blog consulta e ordena posts frequentemente pela data de publicação, a criação deste índice faz com que essas operações sejam executadas de forma rápida O hífen também cria o índice otimizado especificamente para a ordem decrescente
    def __str__(self):
        return self.title
