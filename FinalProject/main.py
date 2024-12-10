import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QFileDialog, QCheckBox, QComboBox, QMessageBox, QScrollArea)
from actionControllerClass import ActionController
from fileManagerClass import extensions


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Organizer")
        self.initUI()
        self.controller = ActionController()

    def initUI(self):
        layout = QVBoxLayout()

        # Directory source input
        self.source_label = QLabel("Source Directory:")
        self.source_input = QLineEdit()
        self.source_browse = QPushButton("Browse")
        
        self.source_browse.clicked.connect(self.select_source)
        
        src_layout = QHBoxLayout()
        
        src_layout.addWidget(self.source_label)
        src_layout.addWidget(self.source_input)
        src_layout.addWidget(self.source_browse)

        # Directory destination input
        self.dest_label = QLabel("Destination Directory:")
        self.dest_input = QLineEdit()
        self.dest_browse = QPushButton("Browse")
        
        self.dest_browse.clicked.connect(self.select_destination)
        
        dest_layout = QHBoxLayout()
        
        dest_layout.addWidget(self.dest_label)
        dest_layout.addWidget(self.dest_input)
        dest_layout.addWidget(self.dest_browse)

        # New file name input
        self.file_label = QLabel("New File Name Prefix:")
        self.file_input = QLineEdit()

        # New folder name input
        self.folder_label = QLabel("New Folder Name:")
        self.folder_input = QLineEdit()

        # Checkbox list for file types
        self.filetype_label = QLabel("Select File Types:")
        self.checkboxes = []
        
        scroll_area = QScrollArea()
        checkbox_widget = QWidget()
        checkbox_layout = QVBoxLayout()
        
        for ext in extensions.keys():
            checkbox = QCheckBox(ext)
            self.checkboxes.append(checkbox)
            checkbox_layout.addWidget(checkbox)
        
        checkbox_widget.setLayout(checkbox_layout)
        scroll_area.setWidget(checkbox_widget)
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedHeight(200)

        # Action dropdown
        self.action_label = QLabel("Select Action:")
        self.action_dropdown = QComboBox()
        self.action_dropdown.addItems([
            "Copy Only", "Sort Only", "Rename Only",
            "Copy & Sort", "Sort & Rename", "Copy & Sort & Rename"
        ])

        # Run button
        self.run_button = QPushButton("Run")
        self.run_button.clicked.connect(self.run_action)

        # Add widgets to the layout
        layout.addLayout(src_layout)
        layout.addLayout(dest_layout)
        layout.addWidget(self.file_label)
        layout.addWidget(self.file_input)
        layout.addWidget(self.folder_label)
        layout.addWidget(self.folder_input)
        layout.addWidget(self.filetype_label)
        layout.addWidget(scroll_area)
        layout.addWidget(self.action_label)
        layout.addWidget(self.action_dropdown)
        layout.addWidget(self.run_button)

        self.setLayout(layout)

    def select_source(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Source Directory")
        if directory:
            self.source_input.setText(directory)

    def select_destination(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Destination Directory")
        if directory:
            self.dest_input.setText(directory)

    def run_action(self):
        source = self.source_input.text()
        dest = self.dest_input.text()
        file_prefix = self.file_input.text()
        selected_ext = [cb.text() for cb in self.checkboxes if cb.isChecked()]
        action = self.action_dropdown.currentText()

        if not source or not dest:
            QMessageBox.warning(self, "Error", "Please select both source and destination directories.")
            return

        self.controller.execute_action(action, source, dest, selected_ext, file_prefix)
        QMessageBox.information(self, "Success", f"Action '{action}' completed successfully.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
