// script.js
const gameboard = document.getElementById('gameboard');
const info = document.getElementById('info');
const restartBtn = document.getElementById('restartBtn');
const modal = document.getElementById('winModal');
const modalMessage = document.getElementById('modalMessage');
const modalRestartBtn = document.getElementById('modalRestartBtn');
const closeBtn = document.querySelector('.closeBtn');
let currentPlayer = 'X';
let gameActive = true;
let board = ['', '', '', '', '', '', '', '', ''];

const winningCombinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
];

function checkWin() {
    for (let combination of winningCombinations) {
        const [a, b, c] = combination;
        if (board[a] && board[a] === board[b] && board[a] === board[c]) {
            modalMessage.innerText = `Player ${currentPlayer} wins!`;
            modal.style.display = "block";
            gameActive = false;
            return;
        }
    }

    if (!board.includes('')) {
        modalMessage.innerText = "It's a draw!";
        modal.style.display = "block";
        gameActive = false;
        setTimeout(() => {
            restartGame();
            modal.style.display = "none";
        }, 2000);
    }
}

function boxClicked(index) {
    if (!gameActive || board[index] !== '') return;

    board[index] = currentPlayer;
    const box = document.querySelector(`[data-index='${index}']`);
    box.innerText = currentPlayer;
    box.classList.add(currentPlayer === 'X' ? 'playerX' : 'playerO');

    checkWin();
    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    if (gameActive) {
        info.innerText = `Player ${currentPlayer}'s turn`;
    }
}

function restartGame() {
    board = ['', '', '', '', '', '', '', '', ''];
    gameActive = true;
    currentPlayer = 'X';
    info.innerText = `Player ${currentPlayer}'s turn`;
    document.querySelectorAll('.box').forEach(box => {
        box.innerText = '';
        box.classList.remove('playerX', 'playerO');
    });
}

gameboard.addEventListener('click', (event) => {
    if (event.target.classList.contains('box')) {
        boxClicked(event.target.dataset.index);
    }
});

restartBtn.addEventListener('click', () => {
    restartGame();
    modal.style.display = "none";
});

modalRestartBtn.addEventListener('click', () => {
    restartGame();
    modal.style.display = "none";
});

closeBtn.addEventListener('click', () => {
    modal.style.display = "none";
});

info.innerText = `Player ${currentPlayer}'s turn`;