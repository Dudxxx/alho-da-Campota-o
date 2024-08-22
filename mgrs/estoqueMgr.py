from dvos import estoqueDvo
from daos import estoqueDao
 

class EstoqueMgr:
    def consultarEstoque(self, nomeOuEan13):
        if estoqueDvo().isEan13(nomeOuEan13):
            return estoqueDao().listByEan13(nomeOuEan13)
        else:
            return estoqueDao().listByNome(nomeOuEan13)

    def cadastrarProduto(self, produto):
        estoqueDao().update(produto)

    def entradaProduto(self, produto): #entidade produto
        estoqueDao().update(produto)
        return produto #mostrar posteriormente nome e quantidade do produto atualizado
