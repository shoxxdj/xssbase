# XSSBase 

## One and only shell to XSS 

- Why ? I'm tired of opening X terms just to trigg an XSS

## How does it works ? 
``` 
poetry install
poetry run xssbase 
``` 
### Start a webserver : 
``` 
webserver start <port>
```
### Expose : 
#### Ngrok : 

```
expose ngork <port of local webserver> 
```

### Get payloads : 
```
payload
```

#### Exemple : 
```
payload generic exposed 
```
Will return a generic xss payload with exposed url inside
```
payload firebase exposed minified
```

Will return a payload to trigg an xss in firebase with exposed url and minified version. 

## What's comming next ? 

- [ ] Encoding
- [ ] More paylods
- [ ] Other expose functions 

