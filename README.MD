# AUDIT RANDOM SAMPLER

This is the open source version of an audit random sampler, I wrote for a client.

The usecase is that there are a lot of for example ticket numbers. It is impossible to audit all of them, so you need to sample a random subset of them.

The program is going to generate 2 sequences of these numbers completely randomly.

The second sequence is just incase the first sequence does not work for some reason.

The header file is nessesary for the program to fully go through.

to run the program do a pip install -r req.txt and just run the main script.

## Possible issues:

- If the values are too big the text goes off screen:change font size or edit the grid
