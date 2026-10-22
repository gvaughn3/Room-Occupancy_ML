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
      { id: "2", label: "Floor 2"},
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
  panel.hidden = false;
  map.invalidateSize();
  renderFloors(building);
}

function closePanel() {
  panel.hidden = true;
  map.invalidateSize();
}

panelClose.addEventListener("click", closePanel);

// TEMPORARY: fake predictions until the back end is connected
function getCurrentOccupancy(building) {
  const predictions = {};
  for (const floor of building.floors) {
    predictions[floor.id] = Math.round(Math.random() * 100);
  }
  return predictions;
}

function renderFloors(building) {
  panelFloors.textContent = "";

  const predictions = getCurrentOccupancy(building);

  for (const floor of building.floors) {
    const percent = predictions[floor.id];
    const row = document.createElement("p");
    row.textContent = floor.label + ": " + percent + "% full";
    panelFloors.appendChild(row);
  }
}

// ---- Add every building to the map ----
for (const building of buildings) {
  addBuilding(building);
}

// ---- TEMPORARY: print coordinates when you click (remove before submitting) ----
map.on("click", function (event) {
  console.log(event.latlng);
});

