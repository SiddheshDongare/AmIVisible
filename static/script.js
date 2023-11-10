document.getElementById('portCheckForm').addEventListener('submit', function(event) {
    var ip = document.getElementById('ip').value;
    var port = document.getElementById('port').value;

    if (!ip || !port) {
        alert('Please fill all the fields.');
        event.preventDefault();
    }
});
function updatePortInput() {
   var dropdown = document.getElementById('portDropdown');
   var portInput = document.getElementById('port');
   portInput.value = dropdown.value;
}
