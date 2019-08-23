# !/usr/bin/python
# -* coding decoding -*-

# Get the list of x_genes
x_gene_list = []
f = open('/home/lss/cat/x_gene.txt')
lines = f.readlines()
for line in lines:
    x_gene_list.append(line.split('\n')[0])
f.close()

# Get the list of genes
gene_list = []
f = open('/home/lss/cat/gene.txt')
lines = f.readlines()
for line in lines:
    gene_list.append(line.split('\n')[0])
f.close()

# Get the list of cats and genes
cat_gene_list = []
f = open('/home/lss/cat/cat.txt')
lines = f.readlines()
for line in lines:
    cat_gene_list.append(line.split('\n')[0])
f.close()

# Record the number of cats per gene
f = open('/home/lss/cat/gene_num.txt', 'w')
for gene in gene_list:
    cat_num = 0
    for cat_gene in cat_gene_list:
        if gene in cat_gene:
            cat_num += 1
    # if gene in x_gene_list:
    # 	gene = '*' + gene
    f.write('{}:{}\n'.format(gene, cat_num))
f.close()

# Get the number of cats per gene
gene_num_dict = {}
f = open('/home/lss/cat/gene_num.txt')
lines = f.readlines()
for line in lines:
    line = line.split('\n')[0]
    gene = line.split(':')[0]
    gene_n = line.split(':')[1]
    gene_num_dict.update({gene: gene_n})
f.close()

# Record the number of score per cat
f = open('/home/lss/cat/cat_score.txt', 'w')
for cat_gene in cat_gene_list:
    cat = cat_gene.split(':')[0]
    one_cat_gene_list = cat_gene.split(':')[1].split('+')
    cat_score = 0
    for gene in one_cat_gene_list:
        if gene in x_gene_list:
            cat_score += 2
        if int(gene_num_dict[gene]) < 2:
            cat_score += 2
    # elif int(gene_num_dict[gene]) == 2 :
    # 	cat_score += 1
    # print cat, cat_score
    f.write('{}:{}\n'.format(cat, cat_score))
f.close()
