import numpy as np

def evaluation(y_test, predictions):
    y_pred = predictions.toarray()
    y_test = y_test.to_numpy()

    acc_list1 = []
    acc_list2 = []
    acc_list3 = []
    for i in range(len(y_test)):
        if(y_test[i, 0] == y_pred[i, 0]):
            temp_acc1 = 100
            acc_list1.append(temp_acc1)
            if(y_test[i, 1] == y_pred[i, 1]):
                temp_acc2 = 100
                acc_list2.append(temp_acc2)
                if(y_test[i, 2] == y_pred[i, 2]):
                    temp_acc3 = 100
                    acc_list3.append(temp_acc3)
                else:
                    temp_acc3 = 67
                    acc_list3.append(temp_acc3)
            else:
                temp_acc2 = 67
                acc_list2.append(temp_acc2)

                temp_acc3 = 33
                acc_list3.append(temp_acc3)
        else:
            temp_acc1 = 0
            acc_list1.append(temp_acc1)

            temp_acc2 = 0
            acc_list2.append(temp_acc2)

            temp_acc3 = 0
            acc_list3.append(temp_acc3)

    acc1 = np.mean(acc_list1)
    acc2 = np.mean(acc_list2)
    acc3 = np.mean(acc_list3)

    print(f'Accuracy using Chain Multi-Outputs on Type2: {acc1:.2f}%')
    print(f'Accuracy using Chain Multi-Outputs on Type2 + Type3: {acc2:.2f}%')
    print(f'Accuracy using Chain Multi-Outputs on Type2 + Type3 + Type4: {acc3:.2f}%')

