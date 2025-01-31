import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://127.0.0.1:5000", // Địa chỉ API Flask
  headers: {
    "Content-Type": "application/json",
  },
});

export default {
  getDepartments() {
    return apiClient.get("/api/departments");
  },

  getChartData({ chart_type, data_type, department_name, disease_name }) {
    return apiClient.post(
      "/api/chart",
      {
        chart_type,
        data_type,
        department_name,
        disease_name,
      },
      {
        responseType: "blob", // Thiết lập responseType là blob
      }
    );
  },

  getBedOccupancy({
    chart_type = "line",
    time_range,
    department_name,
    disease_name,
  }) {
    return apiClient.post(
      "/api/bed-occupancy",
      {
        chart_type,
        time_range,
        department_name,
        disease_name,
      },
      {
        responseType: "arraybuffer", // Nhận dữ liệu hình ảnh dưới dạng mảng byte
      }
    );
  },

  getPatients({ department_name, disease_name }) {
    return apiClient.post("/api/patients", {
      department_name,
      disease_name,
    });
  },

  getDiseaseRatio({ department_name, chart_type }) {
    return apiClient.post(
      "/api/disease-ratio",
      {
        department_name,
        chart_type,
      },
      {
        responseType: "blob", // Thiết lập responseType là blob
      }
    );
  },

  getPatientCount({ department_name, chart_type }) {
    return apiClient.post(
      "/api/patient-count",
      {
        department_name,
        chart_type,
      },
      {
        responseType: "blob", // Thiết lập responseType là blob
      }
    );
  },

  getTreamentCost({ department_name, chart_type }) {
    return apiClient.post(
      "/api/treatment-cost-by-department",
      {
        department_name,
        chart_type,
      },
      {
        responseType: "blob", // Thiết lập responseType là blob
      }
    );
  },
};
