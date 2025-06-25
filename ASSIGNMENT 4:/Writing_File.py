# Writing
initial_text = input("Enter text to write to the file: ")
_wfile = open('output.txt', 'w')
_wfile.write(initial_text + '\n')  # Add newline for better formatting
_wfile.close()
print("Data successfully written to output.txt.")

_adding_additional_text=input("Do you want to add additional text? (Y/n): ")
if _adding_additional_text == "Y":
    additional_text = input("\nEnter additional text to append: ")
    _afile = open('output.txt', 'a')
    _afile.write(additional_text + '\n')
    _afile.close()
    print("Data successfully appended.")
else:
    print("No additional text added.")

print("\nFinal content of output.txt:")
_rfile = open('output.txt', 'r')
print(_rfile.read())
_rfile.close()
