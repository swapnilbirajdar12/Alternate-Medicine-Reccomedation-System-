
let Redmedicines = my_list2;
let meds = my_list;

function recommendedmed() {
  let redmeds = document.getElementById("redmeds");
  let nam = flag;
  let inht = "<h3>Recommended Medicines for " + nam + "</h3>";
  for (let i in Redmedicines) {
    inht += "<h2>" + Redmedicines[i] + "</h2>" + "<a href='https://pharmeasy.in/search/all?name=" + Redmedicines[i] + "'>Click Here</a>" + "<p>Purchase Link from pharmacy</p>";
  }
  redmeds.innerHTML = inht;
}

if (flag != "None")
  recommendedmed();

function addmedicine() {
  let medicines = document.getElementById("medicines");
  let inht = "<option value='' selected disabled>Search Medicine</option>";
  for (let i in meds) {
    inht += "<option value='" + meds[i] + "' id='med" + i + "'>" + meds[i] + "</option>";
  }
  medicines.innerHTML = inht;
}

addmedicine();



