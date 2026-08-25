# @ohos.net.http(Data Request)

The **http** module provides APIs for implementing HTTP data request capabilities. An application can initiate a data request over HTTP. Common HTTP methods include **GET**, **POST**, **OPTIONS**, **HEAD**, **PUT**, **DELETE**, **PATCH**, **TRACE**, and **CONNECT**.

**Since:** 6

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { http } from 'kits/@kit.NetworkKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createHttp(Data Request)](arkts-network-http-createhttp-f.md) |
| [createHttpResponseCache(Data Request)](arkts-network-http-createhttpresponsecache-f.md) |

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [HttpInterceptorChain(Data Request)](arkts-network-http-httpinterceptorchain-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CertificatePinning(Data Request)](arkts-network-http-certificatepinning-i.md) |
| [ClientCert(Data Request)](arkts-network-http-clientcert-i.md) |
| [ConnectionExtraInfo(Data Request)](arkts-network-http-connectionextrainfo-i.md) |
| [Credential(Data Request)](arkts-network-http-credential-i.md) |
| [DataReceiveProgressInfo(Data Request)](arkts-network-http-datareceiveprogressinfo-i.md) |
| [DataSendProgressInfo(Data Request)](arkts-network-http-datasendprogressinfo-i.md) |
| [HttpInterceptor(Data Request)](arkts-network-http-httpinterceptor-i.md) |
| [HttpRequest(Data Request)](arkts-network-http-httprequest-i.md) |
| [HttpRequestContext(Data Request)](arkts-network-http-httprequestcontext-i.md) |
| [HttpRequestOptions(Data Request)](arkts-network-http-httprequestoptions-i.md) |
| [HttpResponse(Data Request)](arkts-network-http-httpresponse-i.md) |
| [HttpResponseCache(Data Request)](arkts-network-http-httpresponsecache-i.md) |
| [MultiFormData(Data Request)](arkts-network-http-multiformdata-i.md) |
| [PerformanceTiming(Data Request)](arkts-network-http-performancetiming-i.md) |
| [ServerAuthentication(Data Request)](arkts-network-http-serverauthentication-i.md) |
| [TlsConfig(Data Request)](arkts-network-http-tlsconfig-i.md) |
| [ValidationContext(Data Request)](arkts-network-http-validationcontext-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AddressFamily(Data Request)](arkts-network-http-addressfamily-e.md) |
| [CertType(Data Request)](arkts-network-http-certtype-e.md) |
| [HttpDataType(Data Request)](arkts-network-http-httpdatatype-e.md) | Enumerates HTTP data types.  \| Name\| Value\| Description \| \| ------------------ \| -- \| ----------- \| \| STRING \| 0 \| String type.\| \| OBJECT \| 1 \| Object type. \| \| ARRAY_BUFFER \| 2 \| Binary array type.\|
| [HttpProtocol(Data Request)](arkts-network-http-httpprotocol-e.md) |
| [InterceptorType(Data Request)](arkts-network-http-interceptortype-e.md) | Enumerates the types of HTTP interceptors.  \| Name \| Value\|Description \| \| ------ \| --\|-------------------------------------- \| \| INITIAL_REQUEST \|'INITIAL_REQUEST' \|Intercepts after the initial HTTP request is assembled.\| \| REDIRECTION \| 'REDIRECTION' \|Intercepts when a redirection response is received.\| \| CACHE_CHECKED \| 'READ_CACHE' \|Intercepts when the HTTP cache is checked and hit.\| \| NETWORK_CONNECT \| 'CONNECT_NETWORK' \|Intercepts before the network request is sent.\| \| FINAL_RESPONSE \| 'FINAL_RESPONSE' \|Intercepts when the final HTTP response is obtained.\|
| [RequestMethod(Data Request)](arkts-network-http-requestmethod-e.md) |
| [ResponseCode(Data Request)](arkts-network-http-responsecode-e.md) |
| [TlsVersion(Data Request)](arkts-network-http-tlsversion-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AuthenticationType(Data Request)](arkts-network-http-authenticationtype-t.md) |
| [ChainContinue(Data Request)](arkts-network-http-chaincontinue-t.md) |
| [CipherSuite(Data Request)](arkts-network-http-ciphersuite-t.md) |
| [HttpProxy(Data Request)](arkts-network-http-httpproxy-t.md) |
| [PathPreference(Data Request)](arkts-network-http-pathpreference-t.md) |
| [QueryParamObject(Data Request)](arkts-network-http-queryparamobject-t.md) |
| [QueryParamValue(Data Request)](arkts-network-http-queryparamvalue-t.md) |
| [RemoteValidation(Data Request)](arkts-network-http-remotevalidation-t.md) |
| [Socks5Proxy(Data Request)](arkts-network-http-socks5proxy-t.md) |
| [SslType(Data Request)](arkts-network-http-ssltype-t.md) |
| [TlsOptions(Data Request)](arkts-network-http-tlsoptions-t.md) |
| [TlsV10CipherSuite(Data Request)](arkts-network-http-tlsv10ciphersuite-t.md) |
| [TlsV10SpecificCipherSuite(Data Request)](arkts-network-http-tlsv10specificciphersuite-t.md) |
| [TlsV11CipherSuite(Data Request)](arkts-network-http-tlsv11ciphersuite-t.md) |
| [TlsV12CipherSuite(Data Request)](arkts-network-http-tlsv12ciphersuite-t.md) |
| [TlsV12SpecificCipherSuite(Data Request)](arkts-network-http-tlsv12specificciphersuite-t.md) |
| [TlsV13CipherSuite(Data Request)](arkts-network-http-tlsv13ciphersuite-t.md) |
| [TlsV13SpecificCipherSuite(Data Request)](arkts-network-http-tlsv13specificciphersuite-t.md) |
| [ValidationCallback(Data Request)](arkts-network-http-validationcallback-t.md) |
| [X509Cert(Data Request)](arkts-network-http-x509cert-t.md) |
