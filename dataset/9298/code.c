#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Define constants
#define ROWS 3
#define COLS 3

// Define game board
char board[ROWS][COLS];

// Print game board
void print_board() {
    printf("\n");
    printf(" %c | %c | %c \n", board[0][0], board[0][1], board[0][2]);
    printf("---+---+---\n");
    printf(" %c | %c | %c \n", board[1][0], board[1][1], board[1][2]);
    printf("---+---+---\n");
    printf(" %c | %c | %c \n\n", board[2][0], board[2][1], board[2][2]);
}

// Check if move is valid
bool is_valid_move(int row, int col) {
    if (row < 0 || row >= ROWS || col < 0 || col >= COLS) {
        return false;
    } else if (board[row][col] == 'X' || board[row][col] == 'O') {
        return false;
    }
    return true;
}

// Get player move
void get_move(char player, int* row, int* col) {
    printf("%c's turn: ", player);
    scanf("%d %d", row, col);
    while (!is_valid_move(*row, *col)) {
        printf("Invalid move. Try again.\n");
        printf("%c's turn: ", player);
        scanf("%d %d", row, col);
    }
}

// Check if game is over
bool is_game_over() {
    int i, j;
    // Check rows
    for (i = 0; i < ROWS; i++) {
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][0] != ' ') {
            return true;
        }
    }
    // Check columns
    for (j = 0; j < COLS; j++) {
        if (board[0][j] == board[1][j] && board[1][j] == board[2][j] && board[0][j] != ' ') {
            return true;
        }
    }
    // Check diagonals
    if ((board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[0][0] != ' ') ||
        (board[0][2] == board[1][1] && board[1][1] == board[2][0] && board[0][2] != ' ')) {
        return true;
    }
    // Check for tie
    for (i = 0; i < ROWS; i++) {
        for (j = 0; j < COLS; j++) {
            if (board[i][j] == ' ') {
                return false;
            }
        }
    }
    printf("It's a tie!\n");
    return true;
}

// Main function
int main() {
    int i, j;
    int row, col;
    char player = 'X';
    bool game_over = false;

    // Initialize game board
    for (i = 0; i < ROWS; i++) {
        for (j = 0; j < COLS; j++) {
            board[i][j] = ' ';
        }
    }

    // Game loop
    while (!game_over) {
        print_board();
        get_move(player, &row, &col);
        board[row][col] = player;
        game_over = is_game_over();
        player = (player == 'X') ? 'O' : 'X';
    }

    print_board();

    return 0;
}