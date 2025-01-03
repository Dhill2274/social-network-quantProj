# Bristol In House Quantum Hackathon
> [!INFO]
**This is an asynchronous challenge to decide teams for iQu Hack**

- [Challenge Details](#overview)
- - [Prep](#setting-up-your-environment)
- [Scoring](#judging-criteria)
------

## **Overview**

We've entered a new era of quantum computing - The Quantum Utility era.

Quantum utility is what we get when a quantum computer can perform reliable computations at a scale beyond brute force classical computing methods that provide exact solutions to computational problems.

Now, computational scientists and other researchers can tackle these large-scale problems using quantum computers with IBM's 100+ qubits backends accessible to everybody. That's an enormous milestone in the field's history because, until recently, all quantum computers were small, experimental devices primarily used to advance the study of quantum computing. Entering the era of quantum utility is, in other words, the quantum computers we have today are valuable tools researchers can use to explore meaningful scientific problems. Now it is your turn to tackle and explore issues with this leading-edge computational resource.

This challenge aims to design and build a quantum-powered application that addresses a real-world problem and is accessible to end users. This includes applications of quantum algorithms that can have practical usage and, in theory, be exposed to businesses or individual users on the internet for consumption. Teams should identify a problem that can be solved (not necessarily more efficiently) with quantum computers.

We encourage contestants to be creative and to leverage their existing quantum knowledge to develop new applications and experiments. To get you started, we offer some suggestions and prompts that may lead to interesting projects.

Beginner
- An implementation of [Quantum Key Distribution](https://en.wikipedia.org/wiki/BB84)
- **An application involving the [Quantum Approximate Optimization Algorithm (QAOA)](https://learning.quantum.ibm.com/tutorial/quantum-approximate-optimization-algorithm)**
- A simulation probing the [dynamics](https://docs.quantum.ibm.com/api/qiskit/qiskit.synthesis.SuzukiTrotter) of a [chemical](https://www.youtube.com/watch?v=DWOfMWPKHDU)

Intermediate
- A realization of [Quantum Signal Processing (QSP)](https://github.com/ichuang/pyqsp)
- An implementation of [amplitude estimation](https://arxiv.org/abs/1912.05559)

Advanced
- A realization of [port-based quantum teleportation](https://arxiv.org/abs/0807.4568)
- An experiment involving [holographic quantum states](https://arxiv.org/abs/2110.14691)

Open-Ended
- A cryprographically secure quantum random number generator
- **A quantum game illustrating the weirdness of quantum mechanics**
- A quantum calculator using reversible arithmetic

> [!NOTE]
The idea is that it serves a practical use case and can be accessed by anyone without special tooling that is not already included in a typical computer installation (or minimal installation)

## **Requirement**

There is no requirement to have you solution hosted on the cloud or have it run on quantum hardware. For this reason there is no support here for setup, however, this does not mean you can't do it.
If you will work locally or in a cloud environment, all users' first step is installing Qiskit.

### Setting up the repo

```bash
git clone git@github.com:TumCucTom/bristol-quantum-hackathon-async.git
cd bristol-quantum-hackathon-async
````

## Setting up your environment

### MacOS /Linux
Make and enter your environment for this project
```bash
python3 -m venv quantum_env
source /path/to/virtual/environment/bin/activate
```

### Windows

Make and enter your environment for this project
```bash
python3 -m venv c:\path\to\project\quantum_env
source /path/to/project/quantum_env/Scripts/activate
```

### Setup

All our prep has been with qiskit but you are no constrained to it.
```bash
pip install qiskit
```

For your report and if you plan to make a jupyter notebook for users:
```bash
pip install 'qiskit[visualization]'
pip install jupyter
```

You can open a notebook with:
```bash
jupyter notebook path/to/project/bristol-quantum-hackathon-async/notebook.ipynb
```

## Submitting the tasks

> [!IMPORTANT]
Submission Due: 3h after your slot starts</br>
If you don't know when your slot is, you should email hf23482@bristol.ac.uk

Submit by:
- sending a .zip of your entire folder including docs to hf23482@bristol.ac.uk
- adding tumcuctom to your **private** repo

Please also see [documentation info](#tips) in the tips.

## **Judging Criteria**

1. **Technical Aspects (30%)** : This category includes the following subcategories:
    - Quantum Complexity : How complex is the quantum algorithm? How optimized is it?
    - Architecture :  Can the architecture serve users at a reasonable scale?
    - Accessibility/User Experience : How accessible is the end user application? Is it easy to use and intuitive for end users?
2. **Originality and Uniqueness (20%)** : How unique is this project compared to others? How interesting is it? Did the team attempt something new or difficult?
3. **Usefulness and Complexity (20%)** : How useful is the project and how well-designed is it? How functional is it at the time of judging? Can it be used in real-world business applications or serve as a valuable tool for individuals?
4. **Presentation (30%)** : How well did the team present their project? Were they able to explain their decisions? Did the entire team have a chance to speak?


## Tips

Most people expressed they wanted to do a formal writeup - a guide format can be found for a program that leverages QAOA in the [pdf](guide.pdf). The LaTeX for this is [here](guide.tex)

Also linked is a portion of an [IBM notebook](qaoa-example.ipynb) that you might like to use a a guide for your own.

This challenge requires a write-up/documentation portion that is heavily considered during
judging. The write-up is a chance for you to be creative in describing your approach and describing
your process. It should be in one of the following forms:
- Formal PDF academic style write up
  - submitted with your code
- Lighthearted prerecorded video
  - submitted linked in the README
- Formal prerecorded video
  - submitted linked in the README
- Presentation
  - submitted:
    - slides in the folder
    - present to team after submissions


Make sure to clearly link the documentation into the `README.md` and to include a link to the original challenge
repository from the documentation.

## Resources

### Learning Materials

#### Quantum Computing and Algorithms

- [Basics of quantum information](https://learning.quantum.ibm.com/course/basics-of-quantum-information) by John Watrous (Award Badge Available)
- [Fundamentals of quantum algorithms](https://learning.quantum.ibm.com/course/fundamentals-of-quantum-algorithms) by John Watrous
- [Variational algorithm design](https://learning.quantum.ibm.com/course/variational-algorithm-design)

#### Workflow Example Tutorials

- [Qiskit Runtime Lab](https://github.com/JavaFXpert/qiskit-runtime-lab) by [James Weaver](https://github.com/JavaFXpert)
- [Variational quantum eigensolver](https://learning.quantum.ibm.com/tutorial/variational-quantum-eigensolver)
- [Quantum approximate optimization algorithm](https://learning.quantum.ibm.com/tutorial/quantum-approximate-optimization-algorithm)
- [CHSH inequality](https://learning.quantum.ibm.com/tutorial/chsh-inequality)
- [Max-Cut](https://learning.quantum.ibm.com/tutorial/max-cut)
- [Heisenberg chain](https://learning.quantum.ibm.com/tutorial/heisenberg-chain)
- [And More!](https://learning.quantum.ibm.com/catalog/tutorials)


### API Reference

- [Qiskit](https://docs.quantum.ibm.com/api/qiskit)
- [Qiskit Runtime IBM Client](https://docs.quantum.ibm.com/api/qiskit-ibm-runtime)
- [Qiskit IBM Runtime REST API](https://docs.quantum.ibm.com/api/runtime/tags/jobs)
- [Qiskit IBM Provider](https://docs.quantum.ibm.com/api/qiskit-ibm-provider)


