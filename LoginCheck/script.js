document.addEventListener('DOMContentLoaded', function () {
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const submitBtn = document.getElementById('submitBtn');
    const passwordStrength = document.getElementById('passwordStrength');
    const toggleModeBtn = document.getElementById('toggleMode');
    const body = document.body;
    const container = document.querySelector('.container');

    function validateForm() {
        if (emailInput.value.trim() !== '' && passwordInput.value.trim() !== '') {
            submitBtn.removeAttribute('disabled');
        } else {
            submitBtn.setAttribute('disabled', 'disabled');
        }
    }

    function checkPasswordStrength() {
        const password = passwordInput.value;
        if (password.length < 3) {
            passwordStrength.textContent = 'Weak Password';
            passwordStrength.style.color = 'red';
        } else if (password.length <= 5) {
             passwordStrength.textContent = 'Medium Password';
            passwordStrength.style.color = 'orange';
        } else {
            passwordStrength.textContent = 'Strong Password';
            passwordStrength.style.color = 'green';
        }
    }

    emailInput.addEventListener('input', validateForm);
    passwordInput.addEventListener('input', function () {
        validateForm();
        checkPasswordStrength();
    });

    submitBtn.addEventListener('click', function (event) {
        event.preventDefault();
        const email = emailInput.value;
        const password = passwordInput.value;
        console.log('Email:', email, 'Password:', password);
    });

    toggleModeBtn.addEventListener('click', function () {
        body.classList.toggle('dark-mode');
    });
});