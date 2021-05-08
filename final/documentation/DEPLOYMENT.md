<h1>Deployment Information</h1>
<h2>Docker Images</h2>
<p>In the Makefile directory, use:</p>

    make build-all

<p>Then, push the images using:</p>

    docker push benjamintan1/Image_Name:latest
  
<p>For example:</p>

    docker push benjamintan1/final-api:latest
    docker push benjamintan1/final-wrk:latest
    docker push benjamintan1/final-db:latest
  
<h2>Kubernetes Execution</h2>
<p>In the deploy directory, run the commands:</p>

    kubectl apply -f ./api
    kubectl apply -f ./redis
    kubectl apply -f ./worker

<p>To verify, you can run commands:</p>

    kubectl get pods
    kubectl get services
    kubectl get pvc

<p>To debug, run the commands:</p>

    kubectl logs POD_NAME

<p>After running these commands and ensuring the pods are working, copy the IP_ADDRESS of the redis service and paste it into the files:</p>
    
    /deploy/api/final-flask-deployment.yml
    /deploy/worker/final-worker-deployment.yml
