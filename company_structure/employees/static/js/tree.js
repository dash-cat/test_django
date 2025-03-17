document.addEventListener("DOMContentLoaded", function () {
  fetch("/api/departments/")
    .then((response) => response.json())
    .then((data) => {
      function createTree(data) {
        let html = "<ul>";
        data.forEach((dept) => {
          html += `<li>${dept.name} (Сотрудников: ${dept.employees.length})`;
          if (dept.employees.length > 0) {
            html += "<ul>";
            dept.employees.forEach((emp) => {
              html += `<li>${emp.full_name} - ${emp.position} - ${emp.salary} руб.</li>`;
            });
            html += "</ul>";
          }
          if (dept.children.length > 0) {
            html += createTree(dept.children);
          }
          html += "</li>";
        });
        html += "</ul>";
        return html;
      }
      document.getElementById("tree").innerHTML = createTree(data);
    })
    .catch((error) => console.error("Ошибка загрузки данных: ", error));
});
