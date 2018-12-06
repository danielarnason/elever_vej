import pandas as pd

def read_data(path):
    df = pd.read_csv(path, sep=';', encoding='latin1')
    return df

if __name__ == '__main__':
    data = read_data('test_data.csv')

    data['vejnavn'] = data['adresse1'].str.extract(r'^(\D+)\s')

    elever_vej = data.groupby('vejnavn').size()
    vej_skole = data.groupby(['vejnavn', 'skolenavn']).size().unstack(fill_value=0)
    vej_klassetrin = data.groupby(['vejnavn', 'klassetrin']).size().unstack(fill_value=0)

    test = pd.concat([elever_vej, vej_skole, vej_klassetrin], axis=1)
    test.to_csv('test.csv')