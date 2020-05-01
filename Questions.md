# Questions
Here I want to collect some nice questions for some easy/complex 
tasks that can be solved via commandline or with small scripts.
The goal is to answer them using one-liners. If you have some 
cool tasks yourself feel free to share them with me.

## Question 1: How to generate unigram counts of a corpus?

Input: text file
output: unigrams with their frequency in descending ordering

## Question 2: Can you count N-grams with variable size of N?
Input: text file and N
output: N-grams with their frequency in descending ordering

# Solutions

## Question 1: How to generate unigram counts of a corpus?

```
cat ulysses.txt | tr " " "\n" | sort | uniq -c | sort -nr
```
We first cat some file and then replace all whitespaces by newline (simple whitespace tokenization).
After that step we just need to sort and use uniq with parameter -c to count. With sort, we sort the
file for numbers (-n) in descending ordering (-r)


## Question 2: Can you count N-grams with variable size of N?

This is a tricky question and it took me some days to find a one-liner for this problem. 
The solution for this one is first to use lookahead for regular expressions and second 
to use Perl that support lookahead. Here, is the command for trigrams:

```
cat ulysses.txt | perl -ne 'chomp;print "$3\n" while /(?=(( |^)(([^ ]+( |$)){3})))/g;'| sort | uniq -c
```
The perl command does the following:
1) split the text into tokens
2) we iterate through the tokens and then we have the regular expressions that does a 
   lookahead for the next {3} (here we can specify the N for the ngram length) tokens
   
