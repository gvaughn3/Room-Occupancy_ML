// ---- Map setup ----
const imageWidth = 2746;
const imageHeight = 2583;

const normalStyle = { color: "green", opacity: 0.4, fillOpacity: 0.15 };
const hoverStyle = { color: "green", opacity: 1, fillOpacity: 0.5 };

const map = L.map("map", { crs: L.CRS.Simple, minZoom: -2 });
const bounds = [[0, 0], [imageHeight, imageWidth]];

const panel = document.getElementById("panel");
const panelName = document.getElementById("panel-name");
const panelClose = document.getElementById("panel-close");
const panelFloors = document.getElementById("panel-floors");

L.imageOverlay("campus-map.png", bounds).addTo(map);
map.fitBounds(bounds);

// ---- Building data ----
const buildings = [
  {
    id: "04",
    name: "Atkins Library",
    floors: [
      { id: "G", label: "Ground Floor" },
      { id: "1", label: "Floor 1" },
      { id: "2", label: "Floor 2" },
      { id: "3", label: "Floor 3" },
      { id: "4", label: "Floor 4" },
      { id: "5", label: "Floor 5" },
      { id: "6", label: "Floor 6" },
      { id: "7", label: "Floor 7" },
      { id: "8", label: "Floor 8" },
      { id: "9", label: "Floor 9" },
      { id: "10", label: "Floor 10" }
    ],
    corners: [[1205, 1528], [1400, 1524], [1390, 1774], [1300, 1772], [1296, 1914], [1194, 1912]]
  },

  {
    id: "46",
    name: "Student Activity Center",
    floors: [
      { id: "1", label: "Arena/Food Court"},
      { id: "2", label: "Gym"}
    ],
    corners: [
      [1288, 990],
      [1566, 997],
      [1567, 1054],
      [1656, 1057],
      [1651, 1256],
      [1563, 1255],
      [1561, 1275],
      [1281, 1268]
    ]
  },

  {
    id: "17",
    name: "Belk Gym",
    floors: [
      { id: "G", label: "Ground Floor"},
      { id: "2", label: "Floor 2"}
    ],
    corners: [
      [1046, 768],
      [1121, 770],
      [1122, 674],
      [1217, 674],
      [1216, 770],
      [1289, 773],
      [1284, 926],
      [1043, 920]
    ]
  },

  {
    id: "96",
    name: "REC Center",
    floors: [
      { id: "1", label: "Floor 1"},
      { id: "2", label: "Floor 2"},
      { id: "G", label: "Ground Floor"},
      { id: "4", label: "Floor 4"},
      { id: "5", label: "Floor 5"}
    ],
    corners: [
      [2125, 772],
      [2126, 1005],
      [2113, 1030],
      [2100, 1117],
      [2069, 1150],
      [2022, 1144],
      [1998, 1090],
      [2020, 1016],
      [2012, 1004],
      [2016, 773]
    ]
  },

  {
    id: "69",
    name: "Student Union",
    floors: [
      { id: "LL", label: "Lower Level"},
      { id: "1", label: "Floor 1"},
      { id: "M", label: "Mezzanine Level"},
      { id: "2", label: "Floor 2"},
      { id: "3", label: "Floor 3"}
    ],
    corners: [
      [2217, 1187],
      [2277, 1258],
      [2274, 1406],
      [2206, 1407],
      [2124, 1491],
      [2044, 1407],
      [2076, 1376],
      [2080, 1278],
      [2045, 1246],
      [2128, 1164],
      [2173, 1221]
    ]
  },

  {
    id: "05",
    name: "Cone center",
    floors: [
      { id: "G", label: "Ground Floor"},
      { id: "2", label: "Floor 2"},
      { id: "3", label: "Floor 3"}
    ],
    corners: [
    [1226, 1368],
    [1225, 1536],
    [1083, 1531],
    [1081, 1441],
    [995, 1439],
    [989, 1509],
    [923, 1513],
    [933, 1349],
    [1064, 1352],
    [1064, 1414],
    [1082, 1415],
    [1088, 1368]
    ]
  },

  {
    id: "34",
    name: "Prospector",
    floors: [
      { id: "G", label: "Ground Floor"},
      { id: "2", label: "Floor 2"}
    ],
    corners: [
    [1705, 1982],
    [1700, 2085],
    [1482, 2086],
    [1487, 1968]
    ]
  },

  {
    id: "82",
    name: "South Village Crossing",
    floors: [
      { id: "G", label: "Ground Floor"},
      { id: "2", label: "Floor 2"}
    ],
    corners: [
    [416, 923],
    [473, 1035],
    [367, 1105],
    [342, 1064],
    [291, 1095],
    [256, 1041],
    [269, 976],
    [328, 937],
    [348, 970]
    ]
  },

  {
    id: "56",
    name: "Woodward Hall",
    floors: [
      { id: "G", label: "Ground Floor"},
      { id: "2", label: "Floor 2"},
      { id: "3", label: "Floor 3"},
      { id: "4", label: "Floor 4"}
    ],
    corners: [
    [1878, 774],
    [1868, 1083],
    [1780, 1073],
    [1779, 851],
    [1606, 857],
    [1610, 758]
    ]
  }

];

// ---- Draw one building and give it hover behavior ----
function addBuilding(building) {
  const shape = L.polygon(building.corners, normalStyle).addTo(map);

  shape.on("mouseover", function () {
    shape.setStyle(hoverStyle);
  });

  shape.on("mouseout", function () {
    shape.setStyle(normalStyle);
  });

  shape.bindTooltip(building.name);

  shape.on("click", function () {
    openPanel(building);
  });
}

function openPanel(building) {
  panelName.textContent = building.name;
  selectedBuilding = building;
  selectedFloor = building.floors[0];
  selectedDay = todayIndex();
  selectedHour = currentHour();
  panel.hidden = false;
  map.invalidateSize();
  renderFloors(building);
}

function closePanel() {
  panel.hidden = true;
  map.invalidateSize();
}

panelClose.addEventListener("click", closePanel);

// ---- Fake occupancy data (TEMPORARY: replace with back end predictions) ----
const DAYS = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"];
const DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
const FIRST_HOUR = 8;   // 8 AM
const LAST_HOUR = 22;   // 10 PM

// Small seeded random generator so the fake numbers stay the same
// for a given building/floor/day instead of changing on every click.
function seededRandom(seedText) {
  let h = 1779033703 ^ seedText.length;
  for (let i = 0; i < seedText.length; i++) {
    h = Math.imul(h ^ seedText.charCodeAt(i), 3432918353);
    h = (h << 13) | (h >>> 19);
  }
  let a = h >>> 0;
  return function () {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

// Returns { 8: 35, 9: 42, ... 22: 20 } for one floor on one day (0 = Monday)
function getDayData(building, floor, dayIndex) {
  const random = seededRandom(building.id + "-" + floor.id + "-" + dayIndex);
  const weekend = dayIndex >= 5;
  const peakHour = 12 + Math.floor(random() * 6);        // busiest around 12pm-5pm
  const peakHeight = (weekend ? 40 : 65) + random() * 35;
  const data = {};

  for (let hour = FIRST_HOUR; hour <= LAST_HOUR; hour++) {
    const distance = Math.abs(hour - peakHour);
    const curve = Math.exp(-(distance * distance) / 24);
    const noise = (random() - 0.5) * 20;
    const value = peakHeight * curve + 8 + noise;
    data[hour] = Math.max(2, Math.min(100, Math.round(value)));
  }
  return data;
}

function todayIndex() {
  return (new Date().getDay() + 6) % 7;   // JS has Sunday = 0, we want Monday = 0
}

function currentHour() {
  return Math.max(FIRST_HOUR, Math.min(LAST_HOUR, new Date().getHours()));
}

function formatHour(hour) {
  const suffix = hour >= 12 ? "PM" : "AM";
  const twelveHour = hour % 12 === 0 ? 12 : hour % 12;
  return twelveHour + " " + suffix;
}

function busyLabel(percent) {
  if (percent < 25) return "Not busy";
  if (percent < 50) return "A little busy";
  if (percent < 75) return "Busy";
  return "Very busy";
}

// ---- Side panel state ----
let selectedBuilding = null;
let selectedFloor = null;
let selectedDay = todayIndex();
let selectedHour = currentHour();

function renderFloors(building) {
  panelFloors.textContent = "";

  // Floor picker (shows the current occupancy for each floor)
  const floorList = document.createElement("div");
  floorList.className = "floor-list";

  for (const floor of building.floors) {
    const percent = getDayData(building, floor, todayIndex())[currentHour()];
    const button = document.createElement("button");
    button.type = "button";
    button.className = "floor-button" + (floor === selectedFloor ? " active" : "");
    button.textContent = floor.label + ": " + percent + "% full";
    button.addEventListener("click", function () {
      selectedFloor = floor;
      renderFloors(building);
    });
    floorList.appendChild(button);
  }
  panelFloors.appendChild(floorList);

  panelFloors.appendChild(buildChart(building, selectedFloor));
}

function buildChart(building, floor) {
  const data = getDayData(building, floor, selectedDay);
  const isToday = selectedDay === todayIndex();
  const nowHour = currentHour();

  const wrapper = document.createElement("div");
  wrapper.className = "popular-times";

  const title = document.createElement("h3");
  title.textContent = "Popular times: " + floor.label;
  wrapper.appendChild(title);

  // Day tabs
  const tabs = document.createElement("div");
  tabs.className = "day-tabs";
  DAYS.forEach(function (dayLabel, index) {
    const tab = document.createElement("button");
    tab.type = "button";
    tab.className = "day-tab" + (index === selectedDay ? " active" : "");
    tab.textContent = dayLabel;
    tab.addEventListener("click", function () {
      selectedDay = index;
      // Default to the current hour on today, noon on other days
      selectedHour = index === todayIndex() ? currentHour() : 12;
      renderFloors(building);
    });
    tabs.appendChild(tab);
  });
  wrapper.appendChild(tabs);

  // Message above the chart
  const message = document.createElement("div");
  message.className = "chart-message";
  const percent = data[selectedHour];
  const verb = isToday && selectedHour === nowHour ? "Currently" : "Predicted";
  message.innerHTML =
    "<strong>" + verb + " " + percent + "% occupancy at " + formatHour(selectedHour) + "</strong>" +
    "<span>" + busyLabel(percent) + " · " + DAY_NAMES[selectedDay] + "</span>";
  wrapper.appendChild(message);

  // Bars
  const chart = document.createElement("div");
  chart.className = "chart";

  for (let hour = FIRST_HOUR; hour <= LAST_HOUR; hour++) {
    const bar = document.createElement("button");
    bar.type = "button";
    bar.className = "bar";
    if (hour === selectedHour) bar.classList.add("selected");
    else if (isToday && hour === nowHour) bar.classList.add("now");
    bar.style.height = data[hour] + "%";
    bar.setAttribute("aria-label", data[hour] + "% at " + formatHour(hour));
    bar.addEventListener("click", function () {
      selectedHour = hour;
      renderFloors(building);
    });
    chart.appendChild(bar);
  }
  wrapper.appendChild(chart);

  // Hour labels every 3 hours
  const axis = document.createElement("div");
  axis.className = "chart-axis";
  for (let hour = FIRST_HOUR; hour <= LAST_HOUR; hour++) {
    const label = document.createElement("span");
    if ((hour - FIRST_HOUR) % 3 === 0) {
      label.textContent = formatHour(hour).replace(" ", "").toLowerCase().replace("m", "");
    }
    axis.appendChild(label);
  }
  wrapper.appendChild(axis);

  return wrapper;
}

// ---- Add every building to the map ----
for (const building of buildings) {
  addBuilding(building);
}

// ---- TEMPORARY: print coordinates when you click (remove before submitting) ----
map.on("click", function (event) {
  console.log(event.latlng);
});