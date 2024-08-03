#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <random>
#include <set>

struct Data
{
    int dia;
    int mes;
    int ano;
};

Data converterParaData(const std::string &dataString)
{
    Data data;
    std::stringstream ss(dataString);
    char barra;

    data.dia = 0;
    data.mes = 0;
    data.ano = 0;

    if (!(ss >> data.dia >> barra >> data.mes >> barra >> data.ano) ||
        barra != '/' ||
        ss.fail())
    {
        std::cerr << "Formato de data inválido: " << dataString << std::endl;

        data.dia = 0;
        data.mes = 0;
        data.ano = 0;
    }

    return data;
}

struct Estudante
{
    int id;
    std::string nome;
    Data aniversario;
    long cpf;

    Estudante() {}

    Estudante(const std::string &nome, const Data &aniversario, long cpf)
        : nome(nome), aniversario(aniversario), cpf(cpf)
    {
        id = geradorId();
    }

private:
    static int geradorId()
    {
        return contadorId++;
    }

    static int contadorId;
};

int Estudante::contadorId = 1;

void imprimirData(const Data &d)
{
    std::cout << "Dia: " << d.dia << "\n";
    std::cout << "Mes: " << d.mes << "\n";
    std::cout << "Ano: " << d.ano << "\n";
}

void imprimirEstudante(const Estudante &e)
{
    std::cout << "ID: " << e.id << "\n";
    std::cout << "Nome: " << e.nome << "\n";
    std::cout << "CPF: " << e.cpf << "\n";
    imprimirData(e.aniversario);
    std::cout << "\n";
}

struct node
{
    Estudante estudante;
    node *next;
    node *previus;

    node(const Estudante &e)
        : estudante(e), next(nullptr), previus(nullptr) {}
};

struct ll
{
    node *head;
    int size;

    ll() : head(nullptr), size(0) {}

    void inserirNaFrente(const Estudante &e)
    {
        node *aux = new node(e);
        if (!head)
            head = aux;
        else
        {
            aux->next = head;
            head->previus = aux;
            head = aux;
        }
        size++;
    }

    int quantidadeDeNos()
    {
        return size;
    }

    node *procurarPeloId(int id)
    {
        node *cur = head;
        while (cur)
        {
            if (cur->estudante.id == id)
                return cur;
            cur = cur->next;
        }
        return nullptr;
    }

    void deletarPorId(int id)
    {
        node *atual = head;
        while (atual)
        {
            if (atual->estudante.id == id)
            {
                if (atual->previus)
                    atual->previus->next = atual->next;
                else
                    head = atual->next;

                if (atual->next)
                    atual->next->previus = atual->previus;

                delete atual;
                size--;
                return;
            }
            atual = atual->next;
        }
        size--;
    }

    void lerDadosDoArquivo(const std::string &nomeArquivo)
    {
        std::ifstream arquivo(nomeArquivo);
        if (!arquivo.is_open())
        {
            std::cerr << "Erro ao abrir o arquivo " << nomeArquivo << std::endl;
            return;
        }

        std::string linha;
        while (std::getline(arquivo, linha))
        {
            if (linha.empty())
                continue;

            std::string nome = linha;

            if (!std::getline(arquivo, linha))
            {
                std::cerr << "Formato de arquivo inválido. Dados incompletos para: " << nome << std::endl;
                break;
            }
            Data aniversario = converterParaData(linha);

            if (!std::getline(arquivo, linha))
            {
                std::cerr << "Formato de arquivo inválido. Dados incompletos para: " << nome << std::endl;
                break;
            }

            try
            {
                long cpf = std::stol(linha);
                Estudante est(nome, aniversario, cpf);
                inserirNaFrente(est);
            }
            catch (const std::invalid_argument &e)
            {
                std::cerr
                    << "Formato de CPF inválido: " << linha << std::endl;
            }

            catch (const std::out_of_range &e)
            {
                std::cerr
                    << "CPF fora do intervalo: " << linha << std::endl;
            }
        }

        arquivo.close();
    }

    void printList() const
    {
        node *cur = head;
        while (cur)
        {
            imprimirEstudante(cur->estudante);
            cur = cur->next;
        }
    }
};

struct ArvoreNo
{
    Estudante estudante;
    ArvoreNo *direito;
    ArvoreNo *esquerdo;

    ArvoreNo(Estudante e)
        : estudante(e), direito(nullptr), esquerdo(nullptr) {}
};

void printArvoreNo(ArvoreNo *no)
{
    if (!no)
    {
        std::cout << "No em branco" << std::endl;
        return;
    }
    std::cout << "Endereco: " << no << std::endl;
    std::cout << "Id: " << no->estudante.id << std::endl;
    std::cout << "CPF: " << no->estudante.cpf << std::endl;
    std::cout << "Nome: " << no->estudante.nome << std::endl;
    std::cout << "Aniversario: " << std::endl;
    imprimirData(no->estudante.aniversario);
}

void printNode(node *no)
{
    if (!no)
    {
        std::cout << "No em branco" << std::endl;
        return;
    }

    std::cout << "Endereco: " << no << std::endl;
    std::cout << "Id: " << no->estudante.id << std::endl;
    std::cout << "CPF: " << no->estudante.cpf << std::endl;
    std::cout << "Nome: " << no->estudante.nome << std::endl;
    std::cout << "Aniversario: " << std::endl;
    imprimirData(no->estudante.aniversario);
}

struct Arvore
{
    ArvoreNo *raiz;

    Arvore()
        : raiz(nullptr) {}

    ArvoreNo *insertHelper(ArvoreNo *n, const Estudante &val)
    {
        if (!n)
            return new ArvoreNo(val);

        if (val.id > n->estudante.id)
            n->direito = insertHelper(n->direito, val);
        else if (val.id < n->estudante.id)
            n->esquerdo = insertHelper(n->esquerdo, val);

        return n;
    }

    void insertRec(const Estudante &val) { raiz = insertHelper(raiz, val); }

    void inOrderTraversal(ArvoreNo *n)
    {
        if (n)
        {
            inOrderTraversal(n->esquerdo);
            std::cout << "ID: " << n->estudante.id << ", Nome: " << n->estudante.nome << ", CPF: " << n->estudante.cpf << std::endl;
            inOrderTraversal(n->direito);
        }
    }

    void printTree()
    {
        inOrderTraversal(raiz);
    }

    void inserirListaNaArvore(ll *ll)
    {
        node *current = ll->head;
        while (current)
        {
            insertRec(current->estudante);
            current = current->next;
        }
    }

    ArvoreNo *searchRec(ArvoreNo *n, int val)
    {
        if (!n)
            return nullptr;

        if (val == n->estudante.id)
            return n;

        if (val > n->estudante.id)
            return searchRec(n->direito, val);
        else
            return searchRec(n->esquerdo, val);
    }

    int max(int a, int b)
    {
        return a >= b ? a : b;
    }

    int height(ArvoreNo *n)
    {
        if (!n)
            return 0;
        return max(height(n->esquerdo), height(n->direito)) + 1;
    }

    int h()
    {
        return height(raiz);
    }

    void removerPorId(int key)
    {
        if (!raiz)
            return;

        ArvoreNo *cur = raiz, *pre = nullptr;

        while (cur)
        {
            if (cur->estudante.id == key)
                break;

            pre = cur;

            if (cur->estudante.id < key)
                cur = cur->direito;
            else
                cur = cur->esquerdo;
        }

        if (!cur)
            return;

        if (cur->esquerdo == nullptr || cur->direito == nullptr)
        {
            ArvoreNo *child = cur->esquerdo != nullptr ? cur->esquerdo : cur->direito;

            if (cur != raiz)
                if (pre->esquerdo == cur)
                    pre->esquerdo = child;
                else
                    pre->direito = child;
            else
                raiz = child;

            delete cur;
        }
        else
        {
            ArvoreNo *tmp = cur->direito;

            while (tmp->esquerdo)
                tmp = tmp->esquerdo;

            int tmpVal = tmp->estudante.id;
            removerPorId(tmp->estudante.id);
            cur->estudante.id = tmpVal;
        }
    }
};
int main()
{
    ll lista;
    lista.lerDadosDoArquivo("bla.txt");
    Arvore a;
    a.inserirListaNaArvore(&lista);
    lista.deletarPorId(19);
    lista.printList();
    a.printTree();
    ArvoreNo *no = a.searchRec(a.raiz, 4);
    node *n = lista.procurarPeloId(4);
    printArvoreNo(no);
    printNode(n);
    a.removerPorId(4);
    std::cout << "Altura arvore: " << a.h() << std::endl;
    lista.quantidadeDeNos();
    return 0;
}