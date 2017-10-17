# Http Server

### How to Run
---------

python server.py [port] <br />
Note : port is optional. if not provide server will run at 8081 port.

### Configurations
---------

Set `InputParamConsidered` Flag to `True`, if request is required to be handled based on request params. <br />
If `InputParamConsidered` Flag is `True`, by default only `http://localhost:8081/p1` request will be served.<br />
Modify `pathsAllowed` and `send_param_based_resp` func accordingly