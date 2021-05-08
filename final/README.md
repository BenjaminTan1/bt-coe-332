<h1>Austin Animal Center Outcome Analyses</h1>
<h4>Benjamin Tan</h4>

<p>Uses data from the Austin Animal Center due to their data being already formatted into a json format. Runs analyses on the outcomes of animals that enter the center. See "documentation" for instructions on deployments, etc. Data can be found in the "src" folder.</p>

<h3>Instructions</h3>
<p>Look through DEPLOYMENT.md under the directory "documentation", then to get instructions for routes, run the command below after execing into an interactive python shell.</p>

    curl host:flask_port/</p>
    
<p>Example:</p>

    root@py-debug-deployment-5cc8cdd65f-ttl84:/# curl 10.103.197.163:5000/
    
Output:

    The routes are as follows:
    curl <host>:<flask_port>/                                                                                General info.
    curl <host>:<flask_port>/load                                                                            Adds data.json info to the database.
    curl <host>:<flask_port>/getAll                                                                          Returns the database.
    curl <host>:<flask_port>/getAnimal/?animal_id=...                                                        Query an animal ID.
    curl <host>:<flask_port>/outcomeType/<outcome_type>                                                      Sort by animal type.
    curl <host>:<flask_port>/updateAnimal/?animal_id=...                                                     Updates an animal with an animal ID specified.
    curl -X POST -H "content-type: application/json" -d '{<Animal>} <host>:<flask_port>/addAnimal            Add an animal.
    curl <host>:<flask_port>/delete/?animal_id=...                                                           Deletes an animal with an animal ID specified.
    curl -X POST -d <host>:<flask_port>/jobs                                                                 Lists jobs.
    curl <host>:<flask_port>/download/<jobuuid>                                                              Obtains image from a job.

Then, make sure to load in the data from data.json into redis first before executing other commands.

    root@py-debug-deployment-5cc8cdd65f-ttl84:/# curl 10.103.197.163:5000/load
    The file data.json was imported into database.

<h1>Sample trial curl commands include...</h1>
<p>An animal_id used for debuggin is A833556</p>
<h3>getAll</h3>

    root@py-debug-deployment-5cc8cdd65f-ttl84:/# curl 10.103.197.163:5000/getAll
    [
      {
      "animal_id": "A464421",
      "name": "Cairo",
      "datetime": "2021-05-06T18:10:00.000",
      "monthyear": "2021-05-06T18:10:00.000",
      "date_of_birth": "2007-01-19T00:00:00.000",
      "outcome_type": "Adoption",
      "animal_type": "Cat",
      "sex_upon_outcome": "Spayed Female",
      "age_upon_outcome": "14 years",
      "breed": "Siamese Mix",
      "color": "Lynx Point"
    },
    ...
 
<h3>getAnimal</h3>

    root@py-debug-deployment-5cc8cdd65f-ttl84:/# curl 10.103.197.163:5000/getAnimal/?animal_id=A833556
    {
      "animal_id": "A833556",
      "datetime": "2021-05-03T16:30:00.000",
      "monthyear": "2021-05-03T16:30:00.000",
      "date_of_birth": "2021-04-14T00:00:00.000",
      "outcome_type": "Transfer",
      "outcome_subtype": "Partner",
      "animal_type": "Cat",
      "sex_upon_outcome": "Intact Female",
      "age_upon_outcome": "2 weeks",
      "breed": "Domestic Medium Hair",
      "color": "Brown Tabby"
    }

<h3>updateAnimal</h3>
<p>Code below doesn't declare information for the animal, so it is left default as null. To update individual values, put in /?name=value, for example /?animal_id=testID into the URL.</p>

    root@py-debug-deployment-5cc8cdd65f-ttl84:/# curl 10.103.197.163:5000/updateAnimal/?animal_id=A833556
    {
      "animal_id": "A833556",
      "datetime": null,
      "monthyear": null,
      "date_of_birth": null,
      "outcome_type": null,
      "outcome_subtype": null,
      "animal_type": null,
      "sex_upon_outcome": null,
      "age_upon_outcome": null,
      "breed": null,
      "color": null,
      "name": null
    }

<h1>Post Curl Commands</h1>
<p>For routes that include POST such as the addAnimal or jobs methods, input the command as given.</p>

    curl -X POST -H "content-type: application/json" -d '{<Animal_Type_Name>=<Animal_Type_Value} <host>:<flask_port>/addAnimal
