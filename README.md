# AI Course Final Project: TAMA-48
In the next 30 years, by 2048, the population of Israel is projected to double, from 8.5M to 15M.
Land is a finite resource; while new towns and cities can be developed, the vast majority of citizens
will live in already existing cities. Therefore, new residences must conform to the constraints that
result from the geography of pre-existing towns and cities.

Our goal is to develop an AI based solution that will allow to add population to inhabit a specific neighborhood (TLV), while satisfying the social, environmental, and economic constraints, and maximizing the benefits from existing public buildings.

![Alt text](/figures/gui.png?raw=true "GUI")

## The project's main sections:

### 1. Data Preparation: 

how to extract a CAD file, process it into meaningful data and labels.

### 2. Data Structure & Defining ‘Solution’: 

how to represent the data to the algorithm in a meaningful and non-biased way. 

### 3. AI Algorithms
According to known parameters in the field of architecture and urban planning and given the number of people we would like to add to the neighbourhood we developed an
automatic solution to decide how many floors to add for each public and private buildings. We defined a cost function, an evaluation metric, and decided about two Classic Algorithms we learned at the course, these are:

   - Genetic Algorithm (Artificial Intelligence Algorithm #1)
   - Min-Conflict (Artificial Intelligence Algorithm #2)

### 4.  Graphic User Interface
user a 3D graphic representation on the algorithms’ output, displaying the added floors to each building in our map, along with the score, each one of
the algorithms outputted. After the user sets the amount of units he wishes to add and selects the algorithm to run, the added floors that are calculated are drawn in a different manner from the original buildings in order to ease the visual conception.

## My contribution to this work:
Sections #2 & #3, with Adi Yehezkely.

## Technologies:
- Algorithms: Python
- Visualization: JavaScript (p5.js library)
- Data Extruction: GIS map & Rhino
