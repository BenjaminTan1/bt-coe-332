<h1>Deployment Information</h1>
<h2>Docker Images</h2>
<p>In the Makefile directory, use:</p>
---
<p>make build-all</p>
---
<p>Then, push the images using:</p>
---
<p>docker push benjamintan1/Image_Name:latest</p>
<p>For example:</p>
<p>docker push benjamintan1/final-api:latest</p>
<h2>Kubernetes Execution</h2>
<p>In the deploy directory, run the commands:</p>
---
<p>kubectl apply -f ./api</p>
<p>kubectl apply -f ./redis</p>
<p>kubectl apply -f ./worker</p>
---
<p>To verify, you can run commands:</p>
---
<p>kubectl get pods</p>
<p>kubectl get services</p>
<p>kubectl get pvc</p>
---
