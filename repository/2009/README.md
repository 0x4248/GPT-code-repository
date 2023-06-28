# Text-Based RPG Battle Simulator - 2009

**Language**: `Cpp`

**Lines of code**: `91`

## Description

This program simulates a text-based RPG battle between a player and a computer-controlled enemy. The player can choose their actions in each turn, and the program will output the results of the battle until one side wins.

To use this program, compile it with a C++ compiler (such as g++), and run the resulting executable. The program will simulate a text-based RPG battle between the player and a computer-controlled enemy. The player can choose between two actions each turn: attack or heal. The program will output the results of the battle until one side wins.

## Code

``` Cpp
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

const int PLAYER_HP = 100;
const int ENEMY_HP = 100;
const int MIN_DAMAGE = 10;
const int MAX_DAMAGE = 20;
const int MIN_HEAL = 10;
const int MAX_HEAL = 20;

int player_hp = PLAYER_HP;
int enemy_hp = ENEMY_HP;

void print_status() {
    cout << "Player HP: " << player_hp << endl;
    cout << "Enemy HP: " << enemy_hp << endl;
    cout << endl;
}

int get_player_input() {
    int input;
    cout << "1. Attack" << endl;
    cout << "2. Heal" << endl;
    cout << "Enter your choice: ";
    cin >> input;
    return input;
}

void player_attack() {
    int damage = rand() % (MAX_DAMAGE - MIN_DAMAGE + 1) + MIN_DAMAGE;
    enemy_hp -= damage;
    cout << "You attack the enemy for " << damage << " damage." << endl;
}

void player_heal() {
    int heal = rand() % (MAX_HEAL - MIN_HEAL + 1) + MIN_HEAL;
    player_hp += heal;
    cout << "You heal yourself for " << heal << " HP." << endl;
}

void enemy_attack() {
    int damage = rand() % (MAX_DAMAGE - MIN_DAMAGE + 1) + MIN_DAMAGE;
    player_hp -= damage;
    cout << "The enemy attacks you for " << damage << " damage." << endl;
}

bool is_game_over() {
    if (player_hp <= 0) {
        cout << "You lose!" << endl;
        return true;
    }
    if (enemy_hp <= 0) {
        cout << "You win!" << endl;
        return true;
    }
    return false;
}

int main() {
    srand(time(nullptr));

    cout << "Welcome to Text-Based RPG Battle Simulator!" << endl;
    cout << endl;

    while (!is_game_over()) {
        print_status();

        int player_choice = get_player_input();

        switch (player_choice) {
            case 1:
                player_attack();
                break;
            case 2:
                player_heal();
                break;
            default:
                cout << "Invalid choice. Try again." << endl;
        }

        if (enemy_hp > 0) {
            enemy_attack();
        }
    }

    return 0;
}

```

## Prompt

```
Make me a program in C++ that is more than 20 lines of code long and is complex and interesting.

When you create the program make a title for it and a short description of what it does.
```