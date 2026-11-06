document.addEventListener('DOMContentLoaded', () => {
    // Variables de contenedores
    const wrapper = document.querySelector('.wrapper');
    const modal_overlay = document.querySelector('.modal-overlay');
    const icon_close = document.querySelector('.icon-close');

    // Botones de apertura (Header + Hero)
    const btn_login_popup = document.querySelector('.btn-login-header');
    const btn_register_popup = document.querySelector('.btn-register-header');
    const hero_login_btn = document.querySelector('.hero-login-btn');

    // Enlaces de navegación interna del modal
    const login_link = document.querySelector('.login-link');
    const register_link = document.querySelector('.register-link');
    const forgot_password_link = document.querySelector('.forgot-password-link');
    const forgot_login_link = document.querySelector('.forgot-login-link');
    const verification_login_link = document.querySelector('.verification-login-link');
    const new_password_login_link = document.querySelector('.new-password-login-link');

    // Formularios
    const forgot_password_form = document.querySelector('.forgot-password form');
    const verification_form = document.querySelector('.verification-code form');
    const new_password_form = document.querySelector('.new-password form');
    const register_form = document.querySelector('.form-box.register form');

    const documentInput = document.querySelector('#register-num-document');

    // =========================
    // UTILIDADES
    // =========================
    function resetWrapper() {
        if (wrapper) {
            wrapper.classList.remove(
                'active',
                'forgot-active',
                'verification-active',
                'new-password-active'
            );
        }
    }

    function isSenaEmail(email) {
        return /^[a-zA-Z0-9._%+-]+@soy\.sena\.edu\.co$/.test(email);
    }

    function isValidDocument(documentNumber) {
        return /^\d{10}$/.test(documentNumber);
    }

    // =========================
    // MOSTRAR FORMULARIOS
    // =========================
    function showLogin() {
        resetWrapper();
        if (modal_overlay) modal_overlay.classList.add('active');
    }

    function showRegister() {
        resetWrapper();
        if (wrapper) wrapper.classList.add('active');
        if (modal_overlay) modal_overlay.classList.add('active');
    }

    function showForgotPassword() {
        resetWrapper();
        if (wrapper) wrapper.classList.add('forgot-active');
        if (modal_overlay) modal_overlay.classList.add('active');
    }

    function showVerificationCode() {
        resetWrapper();
        if (wrapper) wrapper.classList.add('verification-active');
        if (modal_overlay) modal_overlay.classList.add('active');
    }

    function showNewPassword() {
        resetWrapper();
        if (wrapper) wrapper.classList.add('new-password-active');
        if (modal_overlay) modal_overlay.classList.add('active');
    }

    // =========================
    // BOTONES QUE ABREN EL MODAL
    // =========================
    btn_login_popup?.addEventListener('click', (e) => {
        e.preventDefault();
        showLogin();
    });

    btn_register_popup?.addEventListener('click', (e) => {
        e.preventDefault();
        showRegister();
    });

    hero_login_btn?.addEventListener('click', (e) => {
        e.preventDefault();
        showLogin();
    });

    // =========================
    // NAVEGACIÓN ENTRE FORMULARIOS
    // =========================
    register_link?.addEventListener('click', (e) => {
        e.preventDefault();
        showRegister();
    });

    login_link?.addEventListener('click', (e) => {
        e.preventDefault();
        showLogin();
    });

    forgot_password_link?.addEventListener('click', (e) => {
        e.preventDefault();
        showForgotPassword();
    });

    forgot_login_link?.addEventListener('click', (e) => {
        e.preventDefault();
        showLogin();
    });

    verification_login_link?.addEventListener('click', (e) => {
        e.preventDefault();
        showLogin();
    });

    new_password_login_link?.addEventListener('click', (e) => {
        e.preventDefault();
        showLogin();
    });

    // =========================
    // CERRAR MODAL (ÚNICAMENTE CON SU BOTÓN)
    // =========================
    icon_close?.addEventListener('click', () => {
        if (modal_overlay) modal_overlay.classList.remove('active');
        resetWrapper();
    });

    // =========================
    // VALIDACIONES DE FORMULARIO
    // =========================
    if (documentInput) {
        documentInput.addEventListener('input', () => {
            documentInput.value = documentInput.value
                .replace(/\D/g, '')
                .slice(0, 10);
        });
    }

    forgot_password_form?.addEventListener('submit', (e) => {
        e.preventDefault();
        const emailInput = document.querySelector('#recovery-email');
        if (emailInput) {
            const email = emailInput.value.trim();
            if (!isSenaEmail(email)) {
                alert('Debes utilizar un correo institucional @soy.sena.edu.co');
                return;
            }
        }
        showVerificationCode();
    });

    verification_form?.addEventListener('submit', (e) => {
        e.preventDefault();
        const codeInput = document.querySelector('#verification-code');
        if (codeInput) {
            const code = codeInput.value;
            if (!/^\d{6}$/.test(code)) {
                alert('El código debe contener exactamente 6 cifras.');
                return;
            }
        }
        showNewPassword();
    });

    const btnResendCode = document.querySelector('.btn-resend-code');
    btnResendCode?.addEventListener('click', (e) => {
        e.preventDefault();
        alert('El código se ha reenviado correctamente a tu correo institucional.');
    });

    new_password_form?.addEventListener('submit', (e) => {
        e.preventDefault();
        const passwordInput = document.querySelector('#new-password');
        const confirmPasswordInput = document.querySelector('#confirm-new-password');
        
        if (passwordInput && confirmPasswordInput) {
            if (passwordInput.value !== confirmPasswordInput.value) {
                alert('Las contraseñas no coinciden.');
                return;
            }
            if (passwordInput.value.length < 8) {
                alert('La contraseña debe tener mínimo 8 caracteres.');
                return;
            }
        }

        alert('Has cambiado la contraseña exitosamente. Ahora inicia sesión.');
        new_password_form.reset();
        showLogin();
    });
});