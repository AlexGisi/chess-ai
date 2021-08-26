# chess-ai
The goal of this project is to create a chess engine that learns from self-play similar to Giraffe as presented in [Lai (2015)](https://arxiv.org/pdf/1509.01549.pdf), using chess-python as a basis.

# To-Do
1. Identify a [Python neural network library](https://analyticsindiamag.com/top-7-python-neural-network-libraries-for-developers/) with the requisite features to replicate Giraffe's evaluation function's architecture, such as restricted connectivity.
2. Write code to convert a python-chess board object to a feature vector as described in pages 18-19.
3. Define a three-layer network as described on page 21.
4. Collect 5 million positions randomly from an online chess database, and write code to convert them to python-chess representations. Write code to process the positions as described in p. 22.
5. Write code to bootstrap the NN training process with a simple linear evaluation function.
6. Implement TD-Leaf algorithm in p. 23. 
7. Test using the [Strategic Test Suite](https://www.chessprogramming.org/Strategic_Test_Suite).
8. Implement UCI protocol.
