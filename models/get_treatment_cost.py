# def get_treatment_cost(patients_collection, department_name=None, disease_name=None):

#     query = {}
#     if department_name:
#         query["department"] = department_name
#     if disease_name:
#         query["disease"] = disease_name

#     patients = patients_collection.find({}, {"treatment_cost": 1, "_id": 0})
#     cost_groups = {
#         "100 - 500": 0,
#         "501 - 1000": 0,
#         "1001 - 2000": 0,
#         "2001 - 3000": 0,
#         "3001 - 4000": 0,
#         "4001 - 5000": 0,
#     }

#     for patient in patients:
#         treatment_cost = patient["treatment_cost"]
#         if 100 <= treatment_cost <= 500:
#             cost_groups["100 - 500"] += 1
#         elif 501 <= treatment_cost <= 1000:
#             cost_groups["501 - 1000"] += 1
#         elif 1001 <= treatment_cost <= 2000:
#             cost_groups["1001 - 2000"] += 1
#         elif 2001 <= treatment_cost <= 3000:
#             cost_groups["2001 - 3000"] += 1
#         elif 3001 <= treatment_cost <= 4000:
#             cost_groups["3001 - 4000"] += 1
#         else:
#             cost_groups["4001 - 5000"] += 1

#     data = cost_groups
#     custom_title = f"Biểu đồ chi phí điều trị{(" bệnh " + disease_name) if disease_name else ""} {department_name if department_name else ""}"
#     return data, custom_title


# models/treatment_cost.py


def get_treatment_cost_by_department(patients_collection, department_name=None):
    """
    Lấy tổng chi phí điều trị theo từng loại bệnh trong một khoa.
    :param patients_collection: MongoDB collection chứa thông tin bệnh nhân.
    :param department_name: Tên phòng ban (khoa), nếu không có sẽ lấy toàn bộ bệnh viện.
    :return: data chứa tổng chi phí điều trị theo từng loại bệnh và tiêu đề biểu đồ.
    """
    query = {}
    if department_name:
        query["department"] = department_name

    # Lấy thông tin bệnh nhân và chi phí điều trị
    patients = patients_collection.find(
        query, {"disease": 1, "treatment_cost": 1, "_id": 0}
    )

    # Tạo nhóm chi phí theo loại bệnh
    cost_by_disease = {}
    for patient in patients:
        disease = patient.get("disease", "Unknown")
        treatment_cost = patient.get("treatment_cost", 0)

        if disease in cost_by_disease:
            cost_by_disease[disease] += treatment_cost
        else:
            cost_by_disease[disease] = treatment_cost

    # Tạo tiêu đề cho biểu đồ
    if department_name:
        custom_title = f"Tổng chi phí điều trị theo từng bệnh tại {department_name}"
    else:
        custom_title = "Tổng chi phí điều trị theo từng bệnh tại toàn bệnh viện"

    return cost_by_disease, custom_title
