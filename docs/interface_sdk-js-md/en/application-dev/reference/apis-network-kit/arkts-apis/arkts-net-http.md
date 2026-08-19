# @ohos.net.http

The **http** module provides APIs for implementing HTTP data request capabilities. An application can initiate a data request over HTTP. Common HTTP methods include **GET**, **POST**, **OPTIONS**, **HEAD**, **PUT**, **DELETE**, **PATCH**, **TRACE**, and **CONNECT**.

**Since:** 23

<!--Device-unnamed-declare namespace http--><!--Device-unnamed-declare namespace http-End-->

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { http } from '@kit.NetworkKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createHttp](arkts-network-http-createhttp-f.md) | Creates an HTTP request. You can use this API to initiate or destroy an HTTP request, or enable or disable listening for HTTP Response Header events. To initiate multiple HTTP requests, you must create an **HttpRequest** object for each HTTP request. An **HttpRequest** object corresponds to an HTTP request. &gt; **NOTE：**&gt; &gt; When the request is no longer needed, call destroy() to release resources. Otherwise, memory leaks may occur. |
| [createHttpResponseCache](arkts-network-http-createhttpresponsecache-f.md) | Creates an **HttpResponseCache** object that stores the response data of HTTP requests. You can call [flush](arkts-network-http-httpresponsecache-i.md#flush) and [delete](arkts-network-http-httpresponsecache-i.md#delete) in the object. |

### Classes

| Name | Description |
| --- | --- |
| [HttpInterceptorChain](arkts-network-http-httpinterceptorchain-c.md) | Defines HTTP interceptor chain. |

### Interfaces

| Name | Description |
| --- | --- |
| [CertificatePinning](arkts-network-http-certificatepinning-i.md) | Defines the dynamic configuration of certificate pinning. |
| [ClientCert](arkts-network-http-clientcert-i.md) | Defines the client certificate type. |
| [ConnectionExtraInfo](arkts-network-http-connectionextrainfo-i.md) | Defines the detailed information about the HTTP request interaction. |
| [Credential](arkts-network-http-credential-i.md) | Represents the credential used for server identity verification in a session, including the user name and password. |
| [DataReceiveProgressInfo](arkts-network-http-datareceiveprogressinfo-i.md) | Defines the data receiving progress information. |
| [DataSendProgressInfo](arkts-network-http-datasendprogressinfo-i.md) | Defines the data sending progress information. |
| [HttpInterceptor](arkts-network-http-httpinterceptor-i.md) | Defines the HTTP interceptor API, which is used to define the interception processing function. |
| [HttpRequest](arkts-network-http-httprequest-i.md) | Defines an HTTP request task. Before invoking APIs provided by **HttpRequest**, you must call [createHttp()](arkts-network-http-createhttp-f.md) to create an **HttpRequestTask** object. |
| [HttpRequestContext](arkts-network-http-httprequestcontext-i.md) | Defines HTTP request context data. The object instance is passed as a parameter in the [interceptorHandle](arkts-network-http-httpinterceptor-i.md#interceptorhandle) method of the interceptor. You can use this object to obtain and modify the information about the HTTP request. |
| [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) | Defines the options for initiating an HTTP request. |
| [HttpResponse](arkts-network-http-httpresponse-i.md) | Defines the response to an HTTP request. |
| [HttpResponseCache](arkts-network-http-httpresponsecache-i.md) | Defines an object that stores the response to an HTTP request. Before invoking APIs provided by **HttpResponseCache**, you must call [createHttpResponseCache()](arkts-network-http-createhttpresponsecache-f.md) to create an **HttpRequestTask** object. **Usage of Keywords in the Response Header** - **`Cache-Control`**: specifies the cache policy, for example, `no-cache`, `no-store`, `max-age`, `public`, or `private`. - **`Expires`**: specifies the expiration time of a resource. The value is in the GMT format. - **`ETag`**: identifies the resource version. The client can use the `If-None-Match` request header to check whether the resource has been modified. - **`Last-Modified`**: specifies the last modification time of a resource. The client can use the `If-Modified-Since` request header to check whether a resource has been modified. - **`Vary`**: specifies the parts of the request header that affect the cached response. This field is used to distinguish different cache versions. When using these keywords, ensure that the response header is correctly configured on the server. The client determines whether to use the cached resource and how to verify whether the resource is the latest based on the response header. Correct cache policies help to improve application performance and user experience. **How to Set the Cache-Control Header** `Cache-Control` is a common header, but it is usually used on the server. It allows you to define when, how, and how long a response should be cached. The following are some common `Cache-Control` directives: - **`no-cache`**: indicates that the response can be stored in the cache, but it must be verified with the origin server before each reuse. If the resource remains unchanged, the response status code is 304 (Not Modified). In this case, the resource content is not sent, and the resource in the cache is used. If the resource has expired, the response status code is 200 and the resource content is sent. - `no-store`: indicates that resources cannot be cached. Resources must be obtained from the server for each request. - `max-age`: specifies the maximum cache duration, in seconds. For example, `Cache-Control: max-age=3600` indicates that the valid cache duration is 3,600 seconds (that is, 1 hour). - `public`: indicates that the response can be cached by any object, for example, the client that sends the request or the proxy server. - `private`: indicates that the response can be cached only by a single user and cannot be used as a shared cache ( that is, the response cannot be cached by the proxy server). - `must-revalidate`: indicates that a resource must be revalidated with the origin server once it has become stable. - **`no-transform`**: indicates that the proxy server is not allowed to modify the response content. - **`proxy-revalidate`**: works in a way similar to `must-revalidate`, but applies only to shared caches. - **`s-maxage`**: works in a way similar to `max-age`, but applies only to shared caches. |
| [MultiFormData](arkts-network-http-multiformdata-i.md) | Defines the type of multi-form data. |
| [PerformanceTiming](arkts-network-http-performancetiming-i.md) | Configures the timing for performance tracing, in ms. |
| [ServerAuthentication](arkts-network-http-serverauthentication-i.md) | Defines HTTP server identity verification information. |
| [TlsConfig](arkts-network-http-tlsconfig-i.md) | Defines the TLS configuration, including the version and cipher suite. |
| [ValidationContext](arkts-network-http-validationcontext-i.md) | The validation context of [ValidationCallback](arkts-network-http-validationcallback-t.md) |

### Enums

| Name | Description |
| --- | --- |
| [AddressFamily](arkts-network-http-addressfamily-e.md) | Enumerates IP address families of the target domain name. |
| [CertType](arkts-network-http-certtype-e.md) | Enumerates certificate types. |
| [HttpDataType](arkts-network-http-httpdatatype-e.md) | Enumerates HTTP data types. \| Name\| Value\| Description \| \| ------------------ \| -- \| ----------- \| \| STRING \| 0 \| String type.\| \| OBJECT \| 1 \| Object type. \| \| ARRAY_BUFFER \| 2 \| Binary array type.\| |
| [HttpProtocol](arkts-network-http-httpprotocol-e.md) | Enumerates HTTP protocol versions. |
| [InterceptorType](arkts-network-http-interceptortype-e.md) | Enumerates the types of HTTP interceptors. \| Name \| Value\|Description \| \| ------ \| --\|-------------------------------------- \| \| INITIAL_REQUEST \|'INITIAL_REQUEST' \|Intercepts after the initial HTTP request is assembled.\| \| REDIRECTION \| 'REDIRECTION' \|Intercepts when a redirection response is received.\| \| CACHE_CHECKED \| 'READ_CACHE' \|Intercepts when the HTTP cache is checked and hit.\| \| NETWORK_CONNECT \| 'CONNECT_NETWORK' \|Intercepts before the network request is sent.\| \| FINAL_RESPONSE \| 'FINAL_RESPONSE' \|Intercepts when the final HTTP response is obtained.\| |
| [RequestMethod](arkts-network-http-requestmethod-e.md) | Defines an HTTP request method. |
| [ResponseCode](arkts-network-http-responsecode-e.md) | Enumerates the response codes for an HTTP request. |
| [TlsVersion](arkts-network-http-tlsversion-e.md) | Enumerates TLS versions. |

### Types

| Name | Description |
| --- | --- |
| [AuthenticationType](arkts-network-http-authenticationtype-t.md) | Enumerates server authentication modes in a session. |
| [ChainContinue](arkts-network-http-chaincontinue-t.md) | Specifies whether to continue to process the interceptor chain. |
| [CipherSuite](arkts-network-http-ciphersuite-t.md) | Declares the cipher suite. |
| [HttpProxy](arkts-network-http-httpproxy-t.md) | Defines the network proxy configuration. |
| [PathPreference](arkts-network-http-pathpreference-t.md) | Enumerates the types of networks specified in an HTTP request. &gt; **NOTE：**&gt; &gt; It is recommended that this parameter be used in scenarios such as network concurrency. &gt; If the specified network is not activated, the system uses the default network. |
| [QueryParamObject](arkts-network-http-queryparamobject-t.md) | Defines the key-value object type used to construct URL query parameters. &gt; **NOTE：**&gt; &gt; (1) The property name is used as the key of the **QueryParamObject** parameter. The corresponding property value &gt; can be a single **QueryParamValue** or a **QueryParamValue** array. &gt; (2) The array will be expanded into multiple parameters with the same name. For example, **{ tag: ['a', 'b'] }** &gt; will be serialized into **tag=a&tag=b**. &gt; (3) The key and value are automatically URL-encoded by the system. You should pass the original, unencoded &gt; content. &gt; (4) To strictly control the parameter sequence or repeat the key sequence, you are advised to use the **string** &gt; of **queryParams**. |
| [QueryParamValue](arkts-network-http-queryparamvalue-t.md) | Defines the single-value type that can be used in **QueryParamObject**. |
| [RemoteValidation](arkts-network-http-remotevalidation-t.md) | Enumerates the identity verification modes of the remote server. |
| [Socks5Proxy](arkts-network-http-socks5proxy-t.md) | Socks5 Proxy Configuration Information. |
| [SslType](arkts-network-http-ssltype-t.md) | Defines the secure communications protocol. |
| [TlsOptions](arkts-network-http-tlsoptions-t.md) | Defines the TLS configuration. |
| [TlsV10CipherSuite](arkts-network-http-tlsv10ciphersuite-t.md) | Declares the cipher suite for TLS 1.0. |
| [TlsV10SpecificCipherSuite](arkts-network-http-tlsv10specificciphersuite-t.md) | Enumerates cipher suites supported by TLS 1.0 or later. |
| [TlsV11CipherSuite](arkts-network-http-tlsv11ciphersuite-t.md) | Declares the cipher suite for TLS 1.1, which is the same as that for TLS1.0. |
| [TlsV12CipherSuite](arkts-network-http-tlsv12ciphersuite-t.md) | Declares the cipher suite for TLS 1.2, which is also compatible with TLS 1.1. |
| [TlsV12SpecificCipherSuite](arkts-network-http-tlsv12specificciphersuite-t.md) | Enumerates cipher suites supported by TLS 1.2 or later. |
| [TlsV13CipherSuite](arkts-network-http-tlsv13ciphersuite-t.md) | Declares the cipher suite for TLS 1.3, which is also compatible with TLS 1.2. |
| [TlsV13SpecificCipherSuite](arkts-network-http-tlsv13specificciphersuite-t.md) | Enumerates cipher suites supported by TLS 1.3 or later. |
| [ValidationCallback](arkts-network-http-validationcallback-t.md) | Self defined remote validation. This API uses a promise to return the result. |
| [X509Cert](arkts-network-http-x509cert-t.md) | X509 certificate. |

