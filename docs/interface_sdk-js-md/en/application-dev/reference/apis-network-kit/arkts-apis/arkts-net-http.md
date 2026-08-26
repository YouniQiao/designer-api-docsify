# @ohos.net.http(Data Request)

The **http** module provides APIs for implementing HTTP data request capabilities. An application can initiate a data request over HTTP. Common HTTP methods include **GET**, **POST**, **OPTIONS**, **HEAD**, **PUT**, **DELETE**, **PATCH**, **TRACE**, and **CONNECT**.

**Since:** 6

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createHttp(Data Request)](arkts-network-http-createhttp-f.md) | Creates an HTTP request. You can use this API to initiate or destroy an HTTP request, or enable or disable listening for HTTP Response Header events. To initiate multiple HTTP requests, you must create an **HttpRequest** object for each HTTP request. An **HttpRequest** object corresponds to an HTTP request. |
| [createHttpResponseCache(Data Request)](arkts-network-http-createhttpresponsecache-f.md) | Creates an **HttpResponseCache** object that stores the response data of HTTP requests. You can call [flush](arkts-network-http-httpresponsecache-i.md#flush) and [delete](arkts-network-http-httpresponsecache-i.md#delete) in the object. |

### Classes

| Name | Description |
| --- | --- |
| [HttpInterceptorChain(Data Request)](arkts-network-http-httpinterceptorchain-c.md) | Defines HTTP interceptor chain. |

### Interfaces

| Name | Description |
| --- | --- |
| [CertificatePinning(Data Request)](arkts-network-http-certificatepinning-i.md) | Defines the dynamic configuration of certificate pinning. |
| [ClientCert(Data Request)](arkts-network-http-clientcert-i.md) | Defines the client certificate type. |
| [ConnectionExtraInfo(Data Request)](arkts-network-http-connectionextrainfo-i.md) | Defines the detailed information about the HTTP request interaction. |
| [Credential(Data Request)](arkts-network-http-credential-i.md) | Represents the credential used for server identity verification in a session, including the user name and password. |
| [DataReceiveProgressInfo(Data Request)](arkts-network-http-datareceiveprogressinfo-i.md) | Defines the data receiving progress information. |
| [DataSendProgressInfo(Data Request)](arkts-network-http-datasendprogressinfo-i.md) | Defines the data sending progress information. |
| [HttpInterceptor(Data Request)](arkts-network-http-httpinterceptor-i.md) | Defines the HTTP interceptor API, which is used to define the interception processing function. |
| [HttpRequest(Data Request)](arkts-network-http-httprequest-i.md) | Defines an HTTP request task. Before invoking APIs provided by **HttpRequest**, you must call [createHttp()](arkts-network-http-createhttp-f.md) to create an **HttpRequestTask** object. |
| [HttpRequestContext(Data Request)](arkts-network-http-httprequestcontext-i.md) | Defines HTTP request context data. The object instance is passed as a parameter in the [interceptorHandle](arkts-network-http-httpinterceptor-i.md#interceptorhandle) method of the interceptor. You can use this object to obtain and modify the information about the HTTP request. |
| [HttpRequestOptions(Data Request)](arkts-network-http-httprequestoptions-i.md) | Defines the options for initiating an HTTP request. |
| [HttpResponse(Data Request)](arkts-network-http-httpresponse-i.md) | Defines the response to an HTTP request. |
| [HttpResponseCache(Data Request)](arkts-network-http-httpresponsecache-i.md) | Defines an object that stores the response to an HTTP request. Before invoking APIs provided by **HttpResponseCache**, you must call [createHttpResponseCache()](arkts-network-http-createhttpresponsecache-f.md) to create an **HttpRequestTask** object.  **Usage of Keywords in the Response Header**  - **`Cache-Control`**: specifies the cache policy, for example, `no-cache`, `no-store`, `max-age`, `public`, or  `private`.  - **`Expires`**: specifies the expiration time of a resource. The value is in the GMT format.  - **`ETag`**: identifies the resource version. The client can use the `If-None-Match` request header to check  whether the resource has been modified.  - **`Last-Modified`**: specifies the last modification time of a resource. The client can use the  `If-Modified-Since` request header to check whether a resource has been modified.  - **`Vary`**: specifies the parts of the request header that affect the cached response. This field is used to  distinguish different cache versions.When using these keywords, ensure that the response header is correctly configured on the server. The client determines whether to use the cached resource and how to verify whether the resource is the latest based on the response header. Correct cache policies help to improve application performance and user experience.  **How to Set the Cache-Control Header** `Cache-Control` is a common header, but it is usually used on the server. It allows you to define when, how, and how number a response should be cached. The following are some common `Cache-Control` directives:  - **`no-cache`**: indicates that the response can be stored in the cache, but it must be verified with the origin  server before each reuse. If the resource remains unchanged, the response status code is 304 (Not Modified). In this case, the resource content is not sent, and the resource in the cache is used. If the resource has expired, the response status code is 200 and the resource content is sent.  - `no-store`: indicates that resources cannot be cached. Resources must be obtained from the server for each  request.  - `max-age`: specifies the maximum cache duration, in seconds. For example, `Cache-Control: max-age=3600` indicates  that the valid cache duration is 3,600 seconds (that is, 1 hour).  - `public`: indicates that the response can be cached by any object, for example, the client that sends the request  or the proxy server.  - `private`: indicates that the response can be cached only by a single user and cannot be used as a shared cache (  that is, the response cannot be cached by the proxy server).  - `must-revalidate`: indicates that a resource must be revalidated with the origin server once it has become  stable.  - **`no-transform`**: indicates that the proxy server is not allowed to modify the response content.  - **`proxy-revalidate`**: works in a way similar to `must-revalidate`, but applies only to shared caches.  - **`s-maxage`**: works in a way similar to `max-age`, but applies only to shared caches. |
| [MultiFormData(Data Request)](arkts-network-http-multiformdata-i.md) | Defines the type of multi-form data. |
| [PerformanceTiming(Data Request)](arkts-network-http-performancetiming-i.md) | Configures the timing for performance tracing, in ms. |
| [ServerAuthentication(Data Request)](arkts-network-http-serverauthentication-i.md) | Defines HTTP server identity verification information. |
| [TlsConfig(Data Request)](arkts-network-http-tlsconfig-i.md) | Defines the TLS configuration, including the version and cipher suite. |
| [ValidationContext(Data Request)](arkts-network-http-validationcontext-i.md) | The validation context of [ValidationCallback](arkts-network-http-validationcallback-t.md) |

### Enums

| Name | Description |
| --- | --- |
| [AddressFamily(Data Request)](arkts-network-http-addressfamily-e.md) | Enumerates IP address families of the target domain name. |
| [CertType(Data Request)](arkts-network-http-certtype-e.md) | Enumerates certificate types. |
| [HttpDataType(Data Request)](arkts-network-http-httpdatatype-e.md) | Enumerates HTTP data types.  \| Name\| Value\| Description \| \| ------------------ \| -- \| ----------- \| \| STRING \| 0 \| String type.\| \| OBJECT \| 1 \| Object type. \| \| ARRAY_BUFFER \| 2 \| Binary array type.\| |
| [HttpProtocol(Data Request)](arkts-network-http-httpprotocol-e.md) | Enumerates HTTP protocol versions. |
| [InterceptorType(Data Request)](arkts-network-http-interceptortype-e.md) | Enumerates the types of HTTP interceptors.  \| Name \| Value\|Description \| \| ------ \| --\|-------------------------------------- \| \| INITIAL_REQUEST \|'INITIAL_REQUEST' \|Intercepts after the initial HTTP request is assembled.\| \| REDIRECTION \| 'REDIRECTION' \|Intercepts when a redirection response is received.\| \| CACHE_CHECKED \| 'READ_CACHE' \|Intercepts when the HTTP cache is checked and hit.\| \| NETWORK_CONNECT \| 'CONNECT_NETWORK' \|Intercepts before the network request is sent.\| \| FINAL_RESPONSE \| 'FINAL_RESPONSE' \|Intercepts when the final HTTP response is obtained.\| |
| [RequestMethod(Data Request)](arkts-network-http-requestmethod-e.md) | Defines an HTTP request method. |
| [ResponseCode(Data Request)](arkts-network-http-responsecode-e.md) | Enumerates the response codes for an HTTP request. |
| [TlsVersion(Data Request)](arkts-network-http-tlsversion-e.md) | Enumerates TLS versions. |

### Types

| Name | Description |
| --- | --- |
| [AuthenticationType(Data Request)](arkts-network-http-authenticationtype-t.md) | Enumerates server authentication modes in a session. |
| [ChainContinue(Data Request)](arkts-network-http-chaincontinue-t.md) | Specifies whether to continue to process the interceptor chain. |
| [CipherSuite(Data Request)](arkts-network-http-ciphersuite-t.md) | Declares the cipher suite. |
| [HttpProxy(Data Request)](arkts-network-http-httpproxy-t.md) | Defines the network proxy configuration. |
| [PathPreference(Data Request)](arkts-network-http-pathpreference-t.md) | Enumerates the types of networks specified in an HTTP request. |
| [QueryParamObject(Data Request)](arkts-network-http-queryparamobject-t.md) | Defines the key-value object type used to construct URL query parameters. |
| [QueryParamValue(Data Request)](arkts-network-http-queryparamvalue-t.md) | Defines the single-value type that can be used in **QueryParamObject**. |
| [RemoteValidation(Data Request)](arkts-network-http-remotevalidation-t.md) | Enumerates the identity verification modes of the remote server. |
| [Socks5Proxy(Data Request)](arkts-network-http-socks5proxy-t.md) | Socks5 Proxy Configuration Information. |
| [SslType(Data Request)](arkts-network-http-ssltype-t.md) | Defines the secure communications protocol. |
| [TlsOptions(Data Request)](arkts-network-http-tlsoptions-t.md) | Defines the TLS configuration. |
| [TlsV10CipherSuite(Data Request)](arkts-network-http-tlsv10ciphersuite-t.md) | Declares the cipher suite for TLS 1.0. |
| [TlsV10SpecificCipherSuite(Data Request)](arkts-network-http-tlsv10specificciphersuite-t.md) | Enumerates cipher suites supported by TLS 1.0 or later. |
| [TlsV11CipherSuite(Data Request)](arkts-network-http-tlsv11ciphersuite-t.md) | Declares the cipher suite for TLS 1.1, which is the same as that for TLS1.0. |
| [TlsV12CipherSuite(Data Request)](arkts-network-http-tlsv12ciphersuite-t.md) | Declares the cipher suite for TLS 1.2, which is also compatible with TLS 1.1. |
| [TlsV12SpecificCipherSuite(Data Request)](arkts-network-http-tlsv12specificciphersuite-t.md) | Enumerates cipher suites supported by TLS 1.2 or later. |
| [TlsV13CipherSuite(Data Request)](arkts-network-http-tlsv13ciphersuite-t.md) | Declares the cipher suite for TLS 1.3, which is also compatible with TLS 1.2. |
| [TlsV13SpecificCipherSuite(Data Request)](arkts-network-http-tlsv13specificciphersuite-t.md) | Enumerates cipher suites supported by TLS 1.3 or later. |
| [ValidationCallback(Data Request)](arkts-network-http-validationcallback-t.md) | Self defined remote validation. This API uses a promise to return the result. |
| [X509Cert(Data Request)](arkts-network-http-x509cert-t.md) | X509 certificate. |
