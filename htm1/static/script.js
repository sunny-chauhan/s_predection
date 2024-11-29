document.getElementById('uploadForm').addEventListener('submit', function (event) {
    const imageFile = document.getElementById('imageFile').files.length > 0;
    const videoFile = document.getElementById('videoFile').files.length > 0;

    if (imageFile && videoFile) {
        event.preventDefault();
        document.getElementById('errorMessage').textContent = "Error: Please upload only one file at a time!";
    }
});
