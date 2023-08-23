console.log("BABABABABA");

// const article = document.querySelector("article");


// // `document.querySelector` may return null if the selector doesn't match anything.
// if (article) {
//   const badge = document.createElement("p");
//   // Use the same styling as the publish information in an article's header
//   badge.classList.add("color-secondary-text", "type--caption");

//   // Support for API reference docs
//   const heading = article.querySelector("h1");
//   // Support for article docs with date
//   const date = article.querySelector("time")?.parentNode;

//   (date ?? heading).insertAdjacentElement("afterend", badge);
// }

function make_icon() {
  // const image = document.createElement('img');
  // image.src  = '../images/panther.png';
  // return image;
  const icon = document.createElement("p");
  icon.classList.add("color-secondary-text", "type--caption");
  icon.textContent = `✅`;
  return icon;
}

// function add_icon_to_link(link) {
//   let link_parent = link?.parentNode;
  
//   let link_dd = document.createElement("dd");
//   link_dd.style.cssText += "display:inline-block;";
//   link_dd.appendChild(link);

//   let icon_dd = document.createElement("dd");
//   icon_dd.style.cssText += "display:inline-block;";
//   icon_dd.appendChild(make_icon());
//   let dl = document.createElement("dl");
//   dl.style.cssText += "list-style-type:none;";
//   dl.appendChild(link_dd);
//   dl.appendChild(icon_dd);

//   link_parent.appendChild(dl);
// }

function get_grade(link) {
  //TODO: add logic options
  return "(✅    90%)";
}

function is_link_relevant_google(link) {
  return link.className == "" &&
    link.querySelector("h3") != null &&
    !link.href.startsWith("https://www.google.com");
}

function add_icon_to_link(link) {
  title = link.querySelector("h3");
  grade = get_grade(link);
  title.textContent = title.textContent + "   " + grade;
  // title?.parentNode.removeChild(title);
}

function mess_up(link) {
  title = link.querySelector("h3");
  title?.parentNode.removeChild(title);
}

// find all relevant links
// const links = Array.from(document.links).filter((link) => link.className == "");
const links = Array.from(document.links).filter(is_link_relevant_google);

links.forEach(add_icon_to_link);

console.log("YUPIDIDUP");