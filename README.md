# to_be_predictions
The verb "to be", in its different forms, is one of the most commonly used building blocks of the English language. Many examples and different forms of "to be" are demonstrated here.

You are provided a paragraph of text in which some of the derivates of this verb have been blanked out. At various points in the text, occurences of 'am','are','were','was','is','been','being','be' have been blanked out and replaced with a series of four consecutive hyphens (----). Your task is to identify which of these words can appropriately fill up these blanks.

## Input Format 
The input will contain two lines. The first line will contain only one integer N, which will equal the number of blanks in the text. The second line contains one paragraph of text. Several occurences of the words mentioned previously have been blanked out and replaced by four consecutive hyphens (----). These are the blanks which you need to fill up with one of the following words: 'am','are','were','was','is','been','being','be'

## Output Format 
The output should contain exactly N lines. This is followed, by the appropriate words which need to be filled up in the N blanks in the provided paragraph of text, in the same order as the blanks which they are intended for, respectively.

## Sample Input

6
When the modern Olympics began in 1896, the initiators and organizers ---- looking for a great popularizing event, recalling the ancient glory of Greece. The idea of a marathon race came from Michel Breal, who wanted the event to feature in the first modern Olympic Games in 1896 in Athens. This idea was heavily supported by Pierre de Coubertin, the founder of the modern Olympics, as well as by the Greeks. The Greeks staged a selection race for the Olympic marathon on 10 March 1896 that ---- won by Charilaos Vasilakos in 3 hours and 18 minutes (with the future winner of the introductory Olympic Games marathon coming in fifth). The winner of the first Olympic Marathon, on 10 April 1896 (a male-only race), was Spyridon "Spyros" Louis, a Greek water-carrier, in 2 hours 58 minutes and 50 seconds. The women's marathon ---- introduced at the 1984 Summer Olympics (Los Angeles, USA) and ---- won by Joan Benoit of the United States with a time of 2 hours 24 minutes and 52 seconds. Since the modern games were founded, it has become a tradition for the men's Olympic marathon to be the last event of the athletics calendar, with a finish inside the Olympic stadium, often within hours of, or even incorporated into, the closing ceremonies. The marathon of the 2004 Summer Olympics revived the traditional route from Marathon to Athens, ending at Panathinaiko Stadium, the venue for the 1896 Summer Olympics. Since the modern games ---- founded, it has become a tradition for the men's Olympic marathon to be the last event of the athletics calendar, with a finish inside the Olympic stadium, often within hours of, or even incorporated into, the closing ceremonies. The marathon of the 2004 Summer Olympics revived the traditional route from Marathon to Athens, ending at Panathinaiko Stadium, the venue for the 1896 Summer Olympics. The Olympic men's record ---- 2:06:32.  
Input Constraints 
1 <= N <= 20 The text chunk will not contain more than 5000 characters.

## Sample Output

were
was
was
was
were
is
Explanation

The blanks have been filled up with appropriate words as shown below:

When the modern Olympics began in 1896, the initiators and organizers were looking for a great popularizing event, recalling the ancient glory of Greece. The idea of a marathon race came from Michel Breal, who wanted the event to feature in the first modern Olympic Games in 1896 in Athens. This idea was heavily supported by Pierre de Coubertin, the founder of the modern Olympics, as well as by the Greeks. The Greeks staged a selection race for the Olympic marathon on 10 March 1896 that was won by Charilaos Vasilakos in 3 hours and 18 minutes (with the future winner of the introductory Olympic Games marathon coming in fifth). The winner of the first Olympic Marathon, on 10 April 1896 (a male-only race), was Spyridon "Spyros" Louis, a Greek water-carrier, in 2 hours 58 minutes and 50 seconds. The women's marathon was introduced at the 1984 Summer Olympics (Los Angeles, USA) and was won by Joan Benoit of the United States with a time of 2 hours 24 minutes and 52 seconds. Since the modern games were founded, it has become a tradition for the men's Olympic marathon to be the last event of the athletics calendar, with a finish inside the Olympic stadium, often within hours of, or even incorporated into, the closing ceremonies. The marathon of the 2004 Summer Olympics revived the traditional route from Marathon to Athens, ending at Panathinaiko Stadium, the venue for the 1896 Summer Olympics. Since the modern games were founded, it has become a tradition for the men's Olympic marathon to be the last event of the athletics calendar, with a finish inside the Olympic stadium, often within hours of, or even incorporated into, the closing ceremonies. The marathon of the 2004 Summer Olympics revived the traditional route from Marathon to Athens, ending at Panathinaiko Stadium, the venue for the 1896 Summer Olympics. The Olympic men's record is 2:06:32.

## Corpus of Text

You are provided with a corpus of text, which might assist you with the task at hand. This will also be available with the name “corpus.txt” in the same folder as the one where your program is executed, when you submit your solution. The corpus is located here.

## Scoring 
Each test carries a weightage proportional to the number of blanks in it. Score for each test case = M * C/N 
Where C = Number of correct answer N = Number of total blanks M is the maximum score for the test case.

After the contest, submissions will be re-run after adding five hidden test cases as well.
