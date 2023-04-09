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
