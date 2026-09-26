const todosContainer = document.getElementById('todos');
const searchInput = document.getElementById('searchInput');
const userFilter = document.getElementById('userFilter');
const statusFilter = document.getElementById('statusFilter');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const pageInfo = document.getElementById('pageInfo');

const modal = document.getElementById('modal');
const modalBody = document.getElementById('modalBody');
const closeModal = document.getElementById('closeModal');

let allTodos = [];
let currentPage = 1;
const itemsPerPage = 10;

fetch('https://jsonplaceholder.typicode.com/todos')
    .then(response => response.json())
    .then(todos => {
        allTodos = todos;
        populateUserDropdown(todos);
        render();
    })
    .catch(error => console.log(error));

function populateUserDropdown(todos) {
    const userIds = [...new Set(todos.map(t => t.userId))];
    userIds.forEach(id => {
        const option = document.createElement('option');
        option.value = id;
        option.textContent = `User ${id}`;
        userFilter.appendChild(option);
    });
}

function getFilteredTodos() {
    const searchValue = searchInput.value.toLowerCase();
    const selectedUser = userFilter.value;
    const selectedStatus = statusFilter.value;

    return allTodos.filter(todo => {
        const matchesSearch = todo.title.toLowerCase().includes(searchValue);
        const matchesUser = selectedUser === '' || todo.userId.toString() === selectedUser;
        const matchesStatus = selectedStatus === '' || todo.completed.toString() === selectedStatus;

        return matchesSearch && matchesUser && matchesStatus;
    });
}

function render() {
    const filtered = getFilteredTodos();
    const startIndex = (currentPage - 1) * itemsPerPage;
    const paginatedTodos = filtered.slice(startIndex, startIndex + itemsPerPage);

    todosContainer.innerHTML = '';

    paginatedTodos.forEach(todo => {
        const todoElement = document.createElement('p');
        todoElement.classList.add('todo');
        todoElement.textContent = todo.title;

        todoElement.addEventListener('click', () => {
            showDetails(todo);
        });

        todosContainer.appendChild(todoElement);
    });

    const totalPages = Math.ceil(filtered.length / itemsPerPage) || 1;
    pageInfo.textContent = `${currentPage} / ${totalPages}`;
    prevBtn.disabled = currentPage === 1;
    nextBtn.disabled = currentPage >= totalPages;
}

function showDetails(todo) {
    modalBody.innerHTML = `
        <p><strong>ID:</strong> ${todo.id}</p>
        <p><strong>User ID:</strong> ${todo.userId}</p>
        <p><strong>Title:</strong> ${todo.title}</p>
        <p><strong>Completed:</strong> ${todo.completed ? 'Yes' : 'No'}</p>
    `;
    modal.style.display = 'flex';
}

closeModal.addEventListener('click', () => {
    modal.style.display = 'none';
});

window.addEventListener('click', (event) => {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});

searchInput.addEventListener('input', () => { currentPage = 1; render(); });
userFilter.addEventListener('change', () => { currentPage = 1; render(); });
statusFilter.addEventListener('change', () => { currentPage = 1; render(); });

prevBtn.addEventListener('click', () => {
    if (currentPage > 1) {
        currentPage--;
        render();
    }
});

nextBtn.addEventListener('click', () => {
    currentPage++;
    render();
});