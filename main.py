import pandas as pd
import click

@click.command()
@click.option('--pricelist-filename', '-p')
@click.option('--catalogue-filename', '-c')
def main(pricelist_filename=None, catalogue_filename=None):
    pricelist = pd.read_excel(pricelist_filename)
    catalogue = pd.read_excel(catalogue_filename, sheet_name='Products')
    # print(catalogue)
    print(pricelist)


if __name__ == "__main__":
    main()