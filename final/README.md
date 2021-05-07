<h1>Austin Animal Center Outcome Analyses</h1>
<h4>Benjamin Tan</h4>

Uses data from the Austin Animal Center due to their data being already formatted into a json format. Runs analyses on the outcomes of animals that enter the center. See "documentation" for instructions on deployments, etc. Data can be found in the "src" folder.

<h3>File Structure</h3>
<p>data</p>
<p>- redis.conf</p>
<p>deploy</p>
<p>- api</p>
<p>--- final-flask-deployment.yml</p>
<p>--- final-flask-service.yml</p>
<p>- redis</p>
<p>--- final-redis-deployment.yml</p>
<p>--- final-redis-pvc.yml</p>
<p>--- final-redis-service.yml</p>
<p>- worker</p>
<p>--- final-worker-deployment.yml</p>
<p>docker</p>
<p>- docker-compose.yml</p>
<p>- Dockerfile.api</p>
<p>- Dockerfile.db</p>
<p>- Dockerfile.wrk</p>
<p>src</p>
<p>- data.json</p>
<p>- api.py</p>
<p>- worker.py</p>
<p>- jobs.py</p>
<p>documentation</p>
<p>- DEPLOYMENT.md</p>
<p>Makefile</p>
<p>README.md</p>




