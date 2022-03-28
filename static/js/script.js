function copyurl(id) {
    var url = document.getElementById(id);
    url.select();
    url.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(url.value);
    alert("Copied url: " + url.value);
    }

const navLinks = document.querySelectorAll('.nav-item')
const menuToggle = document.getElementById('navbarNavDropdown')
const bsCollapse = new bootstrap.Collapse(menuToggle, {toggle:false})
navLinks.forEach((l) => {
        l.addEventListener('click', () => { bsCollapse.toggle() })
    })

function download(id) {
    var imageurl = document.getElementById(id).value;
    let fileName = getFileName(imageurl);
    saveAs(imageurl, fileName);
}

function getFileName(str) {
        return str.substring(str.lastIndexOf('/') + 1)
    }

