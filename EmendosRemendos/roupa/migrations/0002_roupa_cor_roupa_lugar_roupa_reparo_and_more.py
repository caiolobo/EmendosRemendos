# Generated by Django 4.2.1 on 2023-05-04 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roupa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roupa',
            name='cor',
            field=models.CharField(choices=[('branco', 'Branco'), ('preto', 'Preto'), ('cinza', 'Cinza'), ('verde', 'Verde'), ('azul', 'Azul'), ('marrom', 'Marrom'), ('amarelo', 'Amarelo'), ('rosa', 'Rosa'), ('roxo', 'Roxo'), ('laranja', 'Laranja'), ('bege', 'Bege'), ('lilas', 'Lilás'), ('verazu', 'Verde-Azulado')], default='branco', max_length=8),
        ),
        migrations.AddField(
            model_name='roupa',
            name='lugar',
            field=models.CharField(choices=[('cos', 'Cós'), ('barra', 'Barra'), ('manga', 'Manga'), ('lados', 'Lados'), ('gola', 'Gola'), ('bolso', 'Bolso'), ('ziperc', 'Zíper Comum'), ('ziperi', 'Zíper Invisível'), ('ziperr', 'Zíper Reforçado')], default='cos', max_length=8),
        ),
        migrations.AddField(
            model_name='roupa',
            name='reparo',
            field=models.CharField(choices=[('ajuste', 'Ajuste'), ('barra', 'Barra'), ('reforma', 'Reforma'), ('folgar', 'Folgar'), ('trocar', 'Trocar')], default='barra', max_length=8),
        ),
        migrations.AlterField(
            model_name='roupa',
            name='categoria',
            field=models.CharField(choices=[('calca', 'Calça'), ('short', 'Short'), ('camisa', 'Camisa'), ('camiseta', 'Camiseta'), ('moletom', 'Moletom'), ('saia', 'Saia'), ('vestido', 'Vestido'), ('blusa', 'Blusa'), ('bermuda', 'Bermuda')], default='calca', max_length=8),
        ),
    ]
