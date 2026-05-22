document.addEventListener('DOMContentLoaded', () => {
    const term = document.getElementById('rpdev-terminal');
    const input = document.getElementById('term-input');
    const output = document.getElementById('term-output');

    if (!term) return;

    const commands = {
        'help': 'Available commands: whoami, projects, skills, clear',
        'whoami': 'RPDev | Security Analyst & Engineer | Cleveland, OH',
        'projects': 'Active: Blackhole Webserver, LuCI App, DNS Forge. See /projects/ for details.',
        'skills': 'Primary: Linux, PowerShell, RF/SDR, Enterprise Security, Low-level Systems.',
        'clear': ''
    };

    input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            const cmd = input.value.trim().toLowerCase();
            output.innerHTML += `<div><span class="prompt">root@RPDev:~#</span> ${input.value}</div>`;
            
            if (cmd === 'clear') {
                output.innerHTML = '';
            } else if (commands[cmd]) {
                output.innerHTML += `<div>${commands[cmd]}</div>`;
            } else if (cmd !== '') {
                output.innerHTML += `<div>command not found: ${cmd}</div>`;
            }
            
            input.value = '';
            term.scrollTop = term.scrollHeight;
        }
    });
});
