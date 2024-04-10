# FastAPI_DIO
## Desafio de projeto da DIO [Desenvolvendo sua Primeira API com FastAPI, Python e Docker](https://web.dio.me/lab/desenvolvendo-uma-api-assincrona-com-fastapi/learning/4058b4b5-1716-43fb-9bf6-121139c16227)
[Link repositório da DIO](https://github.com/digitalinnovationone/workout_api)

___
## [FastApi](https://fastapi.tiangolo.com/tutorial/first-steps/)

Para rodar a Api
````commandline
uvicorn workout_api.main:app --reload
````

___
## Docker
Para instalar o Docker no Windows, você geralmente tem duas opções principais: 
Docker Desktop para Windows e Docker Toolbox. Docker Desktop é a opção mais 
moderna e recomendada para máquinas que atendem aos requisitos mínimos de 
sistema, enquanto o Docker Toolbox é uma alternativa para sistemas mais 
antigos que não suportam a virtualização baseada em hardware ou o Hyper-V. 
Vou focar no Docker Desktop, que é a opção mais comum atualmente.

Requisitos do Sistema para Docker Desktop
Windows 10 64-bit: Pro, Enterprise, or Education (Build 16299 ou posterior).
Hyper-V e Containers Windows devem ser habilitados.
WSL 2 (Windows Subsystem for Linux version 2) para Windows 10 versões mais 
recentes. Isso é recomendado pela Docker para melhor desempenho e compatibilidade.
BIOS-level hardware virtualization support deve estar habilitado nas configurações
do BIOS.
Passos para a Instalação
1. Verifique se o Hyper-V está Habilitado
Abra o Painel de Controle.
Vá para "Programas" e depois "Ativar ou desativar recursos do Windows".
Verifique se as caixas para Hyper-V e Plataforma de Máquina Virtual estão 
marcadas. Se não estiverem, marque-as e reinicie o sistema.
2. Instalar o WSL 2 (para sistemas compatíveis)
Para sistemas que utilizam o WSL 2 (Windows Subsystem for Linux version 2), você
precisa garantir que o WSL 2 está instalado e funcionando. Você pode verificar a 
documentação oficial da Microsoft para as instruções mais recentes sobre como 
fazer isso.

3. Baixar e Instalar o Docker Desktop
Vá para o [site oficial do Docker](https://docs.docker.com/desktop/wsl/) e baixe 
a versão mais recente do Docker Desktop para Windows.
Execute o instalador baixado e siga as instruções. Durante a instalação, se 
solicitado, permita que o instalador habilite o WSL 2.
Após a conclusão da instalação, reinicie o computador se necessário.
4. Configuração Pós-instalação
Após reiniciar, inicie o Docker Desktop a partir do menu Iniciar.
Você pode ser solicitado a autorizar o Docker a fazer alterações no seu 
dispositivo, permita-o.
O Docker começará a inicialização e, uma vez concluído, você verá o ícone do 
Docker na bandeja do sistema, indicando que está rodando.
5. Verificar a Instalação
Abra um terminal ou prompt de comando e digite o seguinte comando para verificar 
se o Docker foi instalado corretamente:

````
docker --version
````

Você também pode executar o tradicional comando Hello World para verificar se o 
Docker está funcionando corretamente:

````
docker run hello-world
````

Se tudo estiver correto, você verá uma mensagem no terminal indicando que o 
Docker está funcionando e capaz de puxar e executar imagens.

Considerações Finais
Atualizações do WSL 2: Se você estiver utilizando o WSL 2, certifique-se de que 
sua distribuição Linux está configurada para usar o WSL 2. Isso pode ser feito 
através do PowerShell.
Configurações do Docker: Você pode ajustar as configurações do Docker Desktop, 
incluindo recursos alocados, compartilhamento de arquivos, e mais, acessando as 
configurações através do ícone da bandeja do sistema.
Seguindo estes passos, você deverá ter o Docker operacional no seu sistema 
Windows.

