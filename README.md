# celery_on_gke

### steps:
1. build the docker and push into the GCR

```
gcloud builds submit 
```

2. create the celery deployment 
```
kubectl apply -f ./gke/celery_gke.yaml 
kubectl get deployments
kubectl get pods
```

3. create the hpa
```
kubectl apply -f ./gke/celery_hpa.yaml 
kubectl get hpa
```

4. test from client
```
python3 producer.py
```
