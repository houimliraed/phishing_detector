from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def root():
    return {"hello":"world"}

@app.get('/url_test')
def url_test():
    pass



