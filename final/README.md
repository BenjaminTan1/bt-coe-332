<h1>Austin Animal Center Outcome Analyses</h1>
<h4>Benjamin Tan</h4>

<p>Uses data from the Austin Animal Center due to their data being already formatted into a json format. Runs analyses on the outcomes of animals that enter the center. See "documentation" for instructions on deployments, etc. Data can be found in the "src" folder.</p>

<h3>Instructions</h3>
<p>Look through DEPLOYMENT.md under the directory "documentation", then to get instructions for routes, run the command below after execing into an interactive python shell.</p>

    curl host:flask_port/</p>
    
<p>Example:</p>

    root@py-debug-deployment-5cc8cdd65f-ttl84:/# curl 10.103.197.163:5000/

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
