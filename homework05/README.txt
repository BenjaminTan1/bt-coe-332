A.
	1.
		[btan9967@isp02 homework05]$ kubectl apply -f pod-hello-name-A.yml
		pod/hello-name created
	2.
		[btan9967@isp02 homework05]$ kubectl get pods --selector "greetings=personalized"
		NAME         READY   STATUS    RESTARTS   AGE
		hello-name   1/1     Running   0          74s
	3. Logs executes as expected since name is only assigned a value in part B.
		[btan9967@isp02 homework05]$ kubectl logs hello-name
		Hello, !
	4.
		[btan9967@isp02 homework05]$ kubectl delete pods hello-name
B.
	1.
		[btan9967@isp02 homework05]$ kubectl get pods --selector "greetings=personalized"
		NAME         READY   STATUS    RESTARTS   AGE
		hello-name   1/1     Running   0          6s
	2.
		[btan9967@isp02 homework05]$ kubectl logs hello-name
		Hello, Benjamin!
	3.
		[btan9967@isp02 homework05]$ kubectl delete pods hello-name
		pod "hello-name" deleted
C.
	1.
		[btan9967@isp02 homework05]$ kubectl apply -f deployment-hello-name-C.yml
		deployment.apps/hello-deployment configured
	2. Removed irrelevant portions. Only copy pasted up until IP address is shown.
			[btan9967@isp02 homework05]$ kubectl get pods -o wide
		NAME                                READY   STATUS    RESTARTS   AGE     IP             NODE                         	
		hello-deployment-69bdb9bbb5-6xg97   1/1     Running   0          5m16s   10.244.6.176   c03                          
		hello-deployment-69bdb9bbb5-r5j25   1/1     Running   0          5m14s   10.244.10.23   c009.rodeo.tacc.utexas.edu   
		hello-deployment-69bdb9bbb5-rfhh2   1/1     Running   0          5m11s   10.244.5.137   c04                          
	3. This matches what is gotten in 2.
		[btan9967@isp02 homework05]$ kubectl logs hello-deployment-69bdb9bbb5-6xg97
		Hello, Benjamin from 10.244.6.176!
		[btan9967@isp02 homework05]$ kubectl logs hello-deployment-69bdb9bbb5-r5j25
		Hello, Benjamin from 10.244.10.23!
		[btan9967@isp02 homework05]$ kubectl logs hello-deployment-69bdb9bbb5-rfhh2
		Hello, Benjamin from 10.244.5.137!
		
