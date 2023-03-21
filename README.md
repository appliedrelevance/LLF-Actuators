# LLF Actuators

LLF Actuators is a ladder logic program that enables communication between the SequentMicrosystems Home Automation HAT for Raspberry PI and the MODBUS protocol that is used by many Human Machine Interface (HMI) and Programmable Logic Controller (PLC) devices. This project is licensed under the MIT license and is available on GitHub at <https://github.com/appliedrelevance/LLF-Actuators>.

The project is named LLF Actuators because it is the operational code behind the Logistics Learning Factory by Roots Education Company. It provides a software solution for controlling actuators and sensors using a Raspberry Pi, which is a popular platform for developing Internet of Things (IoT) applications.

## Getting Started

To get started with LLF Actuators, you will need to have a Raspberry Pi and a SequentMicrosystems Home Automation HAT installed on it. You will also need to have a basic understanding of ladder logic programming and the MODBUS protocol.

To install LLF Actuators, you can clone the GitHub repository to your Raspberry Pi using the following command:

```bash
git clone https://github.com/appliedrelevance/LLF-Actuators.git
```

Once you have cloned the repository, you can navigate to the directory and open the `plc.xml` file using the OpenPLC Editor. This will allow you to edit and build the ladder logic program.

## Usage

LLF Actuators uses ladder logic programming to control actuators and sensors connected to the SequentMicrosystems Home Automation HAT. The program communicates with HMI and PLC devices using the MODBUS protocol.

To use LLF Actuators, you will need to create a ladder logic program that maps inputs and outputs between the SequentMicrosystems Home Automation HAT and the MODBUS protocol. You can use the OpenPLC Editor to create and build your ladder logic program.

Once you have created your ladder logic program, you can generate the PLC program file for your program using the OpenPLC Editor. To do this, follow these steps:

1. Open the OpenPLC Editor and navigate to the "File" menu.
2. Select "Build PLC" from the dropdown menu.
3. The generated PLC program file will be saved in the "build" subfolder of your project.

Compile the generated PLC program file using the appropriate compiler for your target platform. Once you have compiled the file, you can upload it to the OpenPLC runtime using the OpenPLC web application's "Programs" page. Choose the generated_plc.st file and upload it. You can then start the PLC service built-in to OpenPLC with the "Start PLC" button.

## PSM Configuration

To create a PSM script to read the values from the LLF Actuator program, follow these steps:

1. Open the OpenPLC runtime web application and navigate to the "Hardware" page.
2. Select "Python on Linux (PSM)" from the OpenPLC Hardware Layer dropdown.
3. Edit the Python code directly in the editor provided. You can copy and paste from a more capable editor if you would like. There is example PSM code provided in the `llf_actuators_psm.py` file in the `LLF-Actuators` project on GitHub.

Your PSM script is now created, and you can start reading the values from the LLF Actuator program.

## Contributing

If you would like to contribute to LLF Actuators, please create a pull request on the GitHub repository at <https://github.com/appliedrelevance/LLF-Actuators>.


