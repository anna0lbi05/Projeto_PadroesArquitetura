# Análise Inicial do Sistema Legado

O sistema legado fornecido apresenta diversos problemas arquiteturais relacionados aos princípios SOLID, Clean Code e organização em camadas.

O objetivo desta análise é identificar violações arquiteturais existentes, compreender os impactos dessas decisões no processo de manutenção e preparar o sistema para uma futura refatoração orientada por testes.

Antes de iniciar qualquer modificação estrutural, foram criados testes de caracterização (Golden Master Tests) com o objetivo de preservar o comportamento original do sistema e evitar regressões funcionais durante o processo de refatoração.

# Violação do Princípio SRP (Single Responsibility Principle)

A classe `Sis` concentra múltiplas responsabilidades dentro de uma única estrutura, violando o princípio da responsabilidade única.

Responsabilidades identificadas:
- Persistência de dados em SQLite
- Processamento de pagamentos
- Cálculo de descontos
- Controle de status de pedidos
- Geração de relatórios
- Validação de estoque
- Envio de notificações

Trechos relacionados:
- `add_ped`
- `proc_pag`
- `gerar_rel`
- `validar_estoque`

Impacto arquitetural:
Alterações em funcionalidades específicas aumentam o risco de efeitos colaterais em partes não relacionadas do sistema, dificultando manutenção, testes e reutilização de código.

Exemplo:
Uma mudança no sistema de notificações exige alteração direta dentro da classe principal do sistema.

Solução planejada:
Separação das responsabilidades em camadas independentes utilizando:
- Services
- Repositories
- Notification Services
- Payment Strategies

# Violação do Princípio OCP (Open/Closed Principle)

O sistema atual depende fortemente de estruturas condicionais (`if/elif`) para definir comportamentos relacionados a pagamentos, descontos e tipos de cliente.

Trechos relacionados:
- Método `proc_pag`
- Método `add_ped`

Exemplo identificado:

```python
if m == 'cartao':
    ...
elif m == 'pix':
    ...
elif m == 'boleto':
    ...
```

Problema:
Sempre que um novo método de pagamento for adicionado, será necessário modificar o código existente, aumentando o risco de regressões.

Impacto arquitetural:
A arquitetura atual dificulta extensão do sistema sem alteração direta de classes existentes.

Solução planejada:
Aplicação do padrão Strategy para encapsular métodos de pagamento e descontos em estratégias independentes.

# Violação do Princípio LSP (Liskov Substitution Principle)

A classe `PedEspecial` herda da classe `Sis`, porém altera comportamentos fundamentais esperados da classe pai.

Trechos relacionados:
- Método `add_ped`
- Método `upd_st`

Problema identificado:
A subclasse modifica regras importantes do sistema original, como o fluxo de atualização de status e cálculo de valores, sem preservar o comportamento esperado da classe base.

Exemplo:
O método `upd_st` em `PedEspecial` ignora completamente validações e transições existentes na implementação original.

Impacto arquitetural:
Objetos da subclasse não podem substituir objetos da classe pai de forma segura, podendo gerar inconsistências no sistema.

Solução planejada:
Substituir herança inadequada por composição e estratégias específicas para comportamentos especiais.

# Violação do Princípio ISP (Interface Segregation Principle)

A estrutura atual concentra múltiplos comportamentos em uma única classe monolítica, obrigando clientes do sistema a dependerem de funcionalidades que não utilizam diretamente.

Problema identificado:
A classe `Sis` possui métodos relacionados a:
- pagamentos
- relatórios
- estoque
- notificações
- persistência
- pedidos

Impacto arquitetural:
A ausência de segregação aumenta acoplamento, dificulta manutenção e reduz reutilização de componentes específicos.

Exemplo:
Uma funcionalidade que necessita apenas de geração de relatórios depende indiretamente de métodos relacionados a pagamento e estoque.

Solução planejada:
Separação das responsabilidades em interfaces menores e especializadas, como:
- PaymentService
- ReportService
- InventoryService
- NotificationService

# Violação do Princípio DIP (Dependency Inversion Principle)

O sistema atual depende diretamente de implementações concretas, dificultando extensibilidade e testes isolados.

Trechos relacionados:
- SQLite diretamente na classe principal
- Impressões via `print`
- Regras de pagamento implementadas diretamente em condicionais

Problema identificado:
A classe `Sis` controla diretamente detalhes de infraestrutura e implementação, sem abstrações intermediárias.

Impacto arquitetural:
Mudanças em banco de dados, notificações ou pagamentos exigem alteração direta da lógica principal do sistema.

Exemplo:
A substituição do SQLite por outro banco exigiria modificações internas na classe principal.

Solução planejada:
Introdução de abstrações utilizando:
- Repositories
- Interfaces
- Injeção de dependência
- Serviços desacoplados

# Refatoração Arquitetural Inicial

Após a criação dos Golden Master Tests e estabilização do comportamento legado, iniciou-se o processo de refatoração incremental da aplicação.

A estratégia adotada priorizou:
- preservação do comportamento original
- baixo risco de regressão
- desacoplamento gradual
- separação de responsabilidades

## Estrutura Arquitetural Criada

Foram introduzidas novas camadas arquiteturais:

- `models`
- `repositories`
- `services`
- `strategies`
- `factories`
- `observers`

## Repository Pattern

O acesso ao banco SQLite foi parcialmente desacoplado da classe principal através da criação do `PedidoRepository`.

Responsabilidades extraídas:
- persistência de pedidos
- busca por identificadores
- atualização de status
- listagem de pedidos

Benefícios obtidos:
- redução de acoplamento
- isolamento de persistência
- melhor testabilidade

## Service Layer

Foi criada a camada `PedidoService` para centralizar regras de negócio anteriormente distribuídas na classe `Sis`.

Responsabilidades migradas:
- criação de pedidos
- cálculo de descontos
- processamento de pagamentos
- atualização de status

Benefícios obtidos:
- centralização da lógica de negócio
- separação entre infraestrutura e domínio
- melhoria de coesão

## Strategy Pattern

O processamento de pagamentos foi refatorado utilizando o padrão comportamental Strategy.

Strategies implementadas:
- `CartaoPaymentStrategy`
- `PixPaymentStrategy`
- `BoletoPaymentStrategy`

Benefícios obtidos:
- eliminação parcial de estruturas condicionais
- extensibilidade para novos métodos de pagamento
- aderência ao princípio Open/Closed

## Factory Pattern

Foi criada a `PaymentFactory` para centralizar a criação de estratégias de pagamento.

Benefícios obtidos:
- desacoplamento de criação de objetos
- simplificação da lógica de seleção
- organização arquitetural

## Refatoração Incremental

A integração da nova arquitetura ocorreu gradualmente, mantendo o sistema legado funcional durante todo o processo.

Métodos parcialmente refatorados:
- `get_ped`
- `proc_pag`
- `add_ped`

Durante o processo, os Golden Master Tests foram utilizados continuamente para validação de regressões.

Resultado atual:
- 17 testes automatizados
- 85% de cobertura
- comportamento legado preservado
- integração gradual entre sistema legado e nova arquitetura

## Observer Pattern

O sistema de notificações iniciou processo de desacoplamento através da aplicação do padrão comportamental Observer.

Observers implementados:
- `EmailNotifier`
- `SMSNotifier`
- `CorporateNotifier`

Também foi criado o componente:
- `NotificationManager`

Objetivos da refatoração:
- remover notificações da lógica principal
- reduzir acoplamento
- facilitar extensibilidade
- centralizar eventos de comunicação

Benefícios obtidos:
- separação entre domínio e infraestrutura
- maior flexibilidade para novos canais
- aderência aos princípios SOLID