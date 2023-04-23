# Even Doubler Odd Tripler (EDOT)
Takes in a file input, distinguishes odd from even, and then double or triple them.
*Note to avoid confusion:*
*This program takes the square of even numbers, the cube of odd numbers, and stores them into separate files.*
*In hindsight, a better descriptive title would be Even Squared Odd Cubed. The current one has a nice ring to it though, so it was kept anyway.*

1. Take a file input
2. Iterate through all the numbers from file input
    - If even, then double and append to even.txt file
    - If odd, then triple and append to odd.txt file
3. Remember to close the txt file! (Use with operator for a foolproof execution!)

## To Clone And Run This Project In Your Local Machine
```
git clone https://github.com/ryesgit/odd_and_even_extractor
cd ./odd_and_even_extractor
pip install -r requirements.txt
python extractor_ui.py
```