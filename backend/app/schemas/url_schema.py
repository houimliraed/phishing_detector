
from pydantic import BaseModel, HttpUrl

class UrlRequest(BaseModel):
    url : HttpUrl
    
    
    