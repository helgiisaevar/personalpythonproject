# Personal Python Project.

## Tree API

The API holds information about different kind of data structures referred to as **_trees_** in computer science.
From this API you can control and see how different kinds of these trees work.
It can for example print out **Binary** tree in:

- Inorder
- Postorder
- Preorder

The plan is to gradually grow this API with information about various computer science subjects.

### Installing

Install the necessary requirements.

```
pip install -r requriements.txt
```

To run the API

```
flask run
```

and the API will be running on:

### http://localhost:5000/

---

## That is Flask?

Flask is a microframework for Python based on Werkzeug. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools. Extensions are updated far more regularly than the core Flask program

## API Requests

Send requests to different urls of the API

| HTTP METHOD        | POST                                                         | GET                              | PUT | DELETE |
| ------------------ | ------------------------------------------------------------ | -------------------------------- | --- | ------ |
| /                  | N/A                                                          | Get endpoint information (help)  | N/A | N/A    |
| /about             | N/A                                                          | Displays information             | N/A | N/A    |
| /about/:tree       | N/A                                                          | Displays information about trees | N/A | N/A    |
| /tree/:tree/:order | Prints out the specified kind of tree in the specified order | N/A                              | N/A | N/A    |

POST requests to `/tree/:tree/:order` require body like the following example shows.
`numbers` are values which will be stored in the tree.

    {
      "numbers": [12, 84, 34, 142]
    }

## Authors

- **Helgi Sævar Þorsteinsson** - _Initial work_
- **Eirikur** - _Initial work_
