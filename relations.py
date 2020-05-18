from sklearn.metrics import matthews_corrcoef
import data
import utils

endpoints_data = data.get_endpoints_data()


def stats(type_a, type_b):  # type_a & type_b: antipattern types
    for a_key in endpoints_data[type_a].keys():
        y_true_list = endpoints_data[type_a][a_key]

        for b_key in endpoints_data[type_b].keys():
            y_pred_list = endpoints_data[type_b][b_key]

            if (utils.all_zero(y_true_list) or utils.all_zero(y_pred_list)):
                print(a_key, "vs", b_key, "NA")
            else:
                result = matthews_corrcoef(y_true_list, y_pred_list)
                print(a_key, "vs", b_key, result)


stats("linguistic", "design")
stats("design", "linguistic")
