
<script>
function check() {
    if (document.getElementById('password').value ==
            document.getElementById('confirm').value) {
        document.getElementById('submit').disabled = false;
    } else {
        document.getElementById('submit').disabled = true;
    }
}

</script>