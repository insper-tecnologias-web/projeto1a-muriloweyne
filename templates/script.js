const validateForm = () => {
    let titleInput = document.getElementsByTagName('input')[0].value;
    let descriptionInput = document.getElementsByTagName('textarea')[0].value;
    if (titleInput.length === 0) {
        alert('Preencha o campo do título do post it!');
    } if (descriptionInput.length === 0) {
        alert('Preencha o campo da descrição do post it!');
    }
}