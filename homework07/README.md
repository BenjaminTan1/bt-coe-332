<h1>HOMEWORK 07 README</h1>

<h2>PA</h2>
<h3>1.</h3>
<p>docker build -f Dockerfile -t benjamintan1/hw7:latest .</p>
<p>docker push benjamintan1/hw7:latest</p>
<h3>2.</h3>
<p>[btan9967@isp02 api]$ kubectl apply -f btan9967-hw7-flask-deployment.yml</p>
<p>[btan9967@isp02 api]$ kubectl apply -f btan9967-hw7-flask-service.yml</p>
<p>[btan9967@isp02 db]$ kubectl apply -f btan9967-hw7-redis-deployment.yml</p>
<p>[btan9967@isp02 db]$ kubectl apply -f btan9967-hw7-redis-pvc.yml</p>
<p>[btan9967@isp02 db]$ kubectl apply -f btan9967-hw7-redis-service.yml</p>
<p>[btan9967@isp02 worker]$ kubectl apply -f btan9967-hw7-worker-deployment.yml</p>
---
<p>Ouput Sample: deployment.apps/btan9967-hw7-worker-deployment created </p>
---
<p>This output is then repeated for all the kubectl apply commands.</p>
<h3>3.</h3>
<p> Then, we want to determine the IP address of our flask and redis and put it into our deployment files using: </p>
<p>[btan9967@isp02 homework07]$ kubectl get service
<p>NAME                    TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE</p>
<p>btan9967-hw07-flask     ClusterIP   10.96.24.170   <none>        5000/TCP   165m</p>
<p>btan9967-test-service   ClusterIP   10.102.161.2   <none>        6379/TCP   129m</p>
<h2>PB</h2>
  
<h2>PC</h2>
