import util
import read_csv
import charts


def run():
    data = read_csv.read_csv('data.csv') 
    data = list(filter(lambda item:item ['Continent'] == 'South America', data))
    
    country = list(map(lambda x:x ['Country/Territory'], data))
    porcentaje = list(map(lambda x:x ['World Population Percentage'], data))
    charts.generate_pie_chart(country, porcentaje)

    country = input('ingresar pais: ')
    print(country)

    result = util.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        print(country)
        labels, values = util.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)

if __name__ == '__main__':
    run()
        
