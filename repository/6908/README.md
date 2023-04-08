# Student Management System - 6908

**Language**: `Java`

**Lines of code**: `132`

## Description

This program is a student management system that allows users to add, delete, and view student records. It uses JavaFX for the user interface and SQLite for the database.

## Code

``` Java
import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;
import java.sql.*;

public class StudentManagementSystem extends Application {

    private TextField nameField, ageField, emailField, idField;

    private Connection connection;

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("Student Management System");

        GridPane grid = new GridPane();
        grid.setAlignment(Pos.CENTER);
        grid.setHgap(10);
        grid.setVgap(10);
        grid.setPadding(new Insets(25, 25, 25, 25));

        Label nameLabel = new Label("Name:");
        grid.add(nameLabel, 0, 1);
        nameField = new TextField();
        grid.add(nameField, 1, 1);

        Label ageLabel = new Label("Age:");
        grid.add(ageLabel, 0, 2);
        ageField = new TextField();
        grid.add(ageField, 1, 2);

        Label emailLabel = new Label("Email:");
        grid.add(emailLabel, 0, 3);
        emailField = new TextField();
        grid.add(emailField, 1, 3);

        Label idLabel = new Label("ID:");
        grid.add(idLabel, 0, 4);
        idField = new TextField();
        grid.add(idField, 1, 4);

        Button addButton = new Button("Add");
        addButton.setOnAction(event -> addStudent());
        grid.add(addButton, 1, 5);

        Button deleteButton = new Button("Delete");
        deleteButton.setOnAction(event -> deleteStudent());
        grid.add(deleteButton, 2, 5);

        Button viewButton = new Button("View");
        viewButton.setOnAction(event -> viewStudents());
        grid.add(viewButton, 3, 5);

        Scene scene = new Scene(grid, 500, 275);
        primaryStage.setScene(scene);
        primaryStage.show();

        // Connect to the database
        try {
            Class.forName("org.sqlite.JDBC");
            connection = DriverManager.getConnection("jdbc:sqlite:students.db");
            Statement statement = connection.createStatement();
            statement.executeUpdate("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, email TEXT)");
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        }
    }

    private void addStudent() {
        try {
            PreparedStatement statement = connection.prepareStatement("INSERT INTO students (name, age, email) VALUES (?, ?, ?)");
            statement.setString(1, nameField.getText());
            statement.setInt(2, Integer.parseInt(ageField.getText()));
            statement.setString(3, emailField.getText());
            statement.executeUpdate();
            clearFields();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private void deleteStudent() {
        try {
            PreparedStatement statement = connection.prepareStatement("DELETE FROM students WHERE id = ?");
            statement.setInt(1, Integer.parseInt(idField.getText()));
            statement.executeUpdate();
            clearFields();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private void viewStudents() {
        try {
            Statement statement = connection.createStatement();
            ResultSet resultSet = statement.executeQuery("SELECT * FROM students");
            while (resultSet.next()) {
                System.out.println("ID: " + resultSet.getInt
            ("id") + ", Name: " + resultSet.getString("name") + ", Age: " + resultSet.getInt("age") + ", Email: " + resultSet.getString("email"));
        }
        resultSet.close();
    } catch (SQLException e) {
        e.printStackTrace();
    }
}

private void clearFields() {
    nameField.clear();
    ageField.clear();
    emailField.clear();
    idField.clear();
}

@Override
public void stop() {
    // Close the database connection when the program is stopped
    try {
        connection.close();
    } catch (SQLException e) {
        e.printStackTrace();
    }
}

```

## Prompt

```
Make me a program in java that is more than 20 lines of code long and is complex and interesting.

When you create the program make a title for it and a short description of what it does.
```