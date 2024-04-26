from model.randomforest import RandomForest
from model.decisiontree import DecisionTree



def model_predict(data, df, name):
    '''
    results = []
    print("RandomForest")
    model = RandomForest("RandomForest", data.get_embeddings(), data.get_type())
    model.train(data)
    model.predict(data.X_test)
    model.print_results(data)

    results = []
    print("DecisionTree")
    model = DecisionTree("DecisionTree", data.get_embeddings(), data.get_type())
    model.train(data)
    model.predict(data.X_test)
    model.print_results(data)
    '''

    algorithms = [RandomForest, DecisionTree]
    names = ['RandomForest', 'DecisionTree']
    for i in range(len(algorithms)):
        results = []
        print(names[i])
        model = algorithms[i](names[i], data.get_embeddings(), data.get_type())
        model.train(data)
        model.predict(data.X_test)
        model.print_results(data)


def model_evaluate(model, data):
    model.print_results(data)


