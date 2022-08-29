// Change the icons inside the button based on previous settings
if (localStorage.getItem('theme') === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    document.querySelector("#theme-toggle-light-icon").classList.remove("hidden")
    document.querySelector("#tooltip-span").innerHTML = "Light"
}
else {
    document.querySelector("#theme-toggle-dark-icon").classList.remove("hidden")
    document.querySelector("#tooltip-span").innerHTML = "Dark"
}

document.querySelector('#theme-toggle').addEventListener('click', function () {

    // toggle icons inside button
    document.querySelector('#theme-toggle-dark-icon').classList.toggle('hidden');
    document.querySelector('#theme-toggle-light-icon').classList.toggle('hidden');

    // if set via local storage previously
    if (localStorage.getItem('theme')) {
        if (localStorage.getItem('theme') === 'light') {
            document.documentElement.classList.add('dark');
            document.querySelector("#tooltip-span").innerHTML = "Light"
            localStorage.setItem('theme', 'dark');
        } else {
            document.documentElement.classList.remove('dark');
            document.querySelector("#tooltip-span").innerHTML = "Dark"
            localStorage.setItem('theme', 'light');
        }

        // if NOT set via local storage previously
    } else {
        if (document.documentElement.classList.contains('dark')) {
            document.documentElement.classList.remove('dark');

            document.querySelector("#tooltip-span").innerHTML = "Light"
            localStorage.setItem('theme', 'light');
        } else {
            document.documentElement.classList.add('dark');

            document.querySelector("#tooltip-span").innerHTML = "Dark"
            localStorage.setItem('theme', 'dark');
        }
    }

});

