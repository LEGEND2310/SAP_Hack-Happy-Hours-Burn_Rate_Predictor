//get data



// listen for auth status changes
auth.onAuthStateChanged(client => {
  if (client) {
    db.collection('users').onSnapshot(snapshot => {
      showData(snapshot.docs);
      setupUI(client);
    });
  } else {
    setupUI();
    showData([]);
  }
})



// signup
const signupForm = document.querySelector('#signup-form');
signupForm.addEventListener('submit', (e) => {
  e.preventDefault();

  // get user info
  const email = signupForm['signup-email'].value;
  const password = signupForm['signup-password'].value;

  // sign up the user
  auth.createUserWithEmailAndPassword(email, password).then(cred => {
    return db.collection('users').doc(cred.user.uid).set({
      bio: signupForm['signup-bio'].value,
      Name: signupForm['signup-name'].value,
      Age: signupForm['signup-age'].value
    });
  }).then(() => {
    // close the signup modal & reset form
    const modal = document.querySelector('#modal-signup');
    M.Modal.getInstance(modal).close();
    signupForm.reset();
    window.location.href = "./index.html";
  });
});

// logout
const logout = document.querySelector('#logout');
logout.addEventListener('click', (e) => {
  e.preventDefault();
  auth.signOut();
});

// login
const loginForm = document.querySelector('#signup-form');
loginForm.addEventListener('submit', (e) => {
  e.preventDefault();

  // get user info
  const email = loginForm['username'].value;
  const password = loginForm['password'].value;

  // log the user in
  auth.signInWithEmailAndPassword(email, password).then((cred) => {
    // close the signup modal & reset form
    const modal = document.querySelector('#signupForm');
    M.Modal.getInstance(modal).close();
    loginForm.reset();
    window.location.href = "./index.html";
  });

});