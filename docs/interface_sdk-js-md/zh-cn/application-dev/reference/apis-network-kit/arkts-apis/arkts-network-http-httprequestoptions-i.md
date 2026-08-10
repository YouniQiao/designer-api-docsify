# HttpRequestOptions

Specifies the type and value range of the optional parameters in the HTTP request.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-http-export interface HttpRequestOptions--><!--Device-http-export interface HttpRequestOptions-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { http } from 'kits/@kit.NetworkKit';
```

## addressFamily

```TypeScript
addressFamily?: AddressFamily
```

Address family option.

**类型：** [AddressFamily](arkts-network-http-addressfamily-e.md)

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-HttpRequestOptions-addressFamily?: AddressFamily--><!--Device-HttpRequestOptions-addressFamily?: AddressFamily-End-->

**系统能力：** SystemCapability.Communication.NetStack

## body

```TypeScript
body?: string | Object | ArrayBuffer
```

The body content of the HTTP request.

This parameter explicitly specifies the payload to be sent in the request body.When this field is set, the framework forces the data into the body, regardless of the HTTP request method (GET, POST, etc.).

Serialization rules:  
- string: sent directly as the request body.  
- Object: serialized to a JSON string before being sent.  
- ArrayBuffer: sent as raw binary data without additional serialization.

If both body and extraData are specified, body takes precedence, and extraData will be ignored.

**类型：** string \| Object \| ArrayBuffer

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HttpRequestOptions-body?: string | Object | ArrayBuffer--><!--Device-HttpRequestOptions-body?: string | Object | ArrayBuffer-End-->

**系统能力：** SystemCapability.Communication.NetStack

## caData

```TypeScript
caData?: string
```

A PEM representation of a certificate. The system will create an X.509 certificate object in the SSL process.If the caPath option is set, the caData option will be ignored.Certificate chain is not supported.Maxium length is 8000 Bytes.

**类型：** string

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为20。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequestOptions-caData?: string--><!--Device-HttpRequestOptions-caData?: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

## caPath

```TypeScript
caPath?: string
```

If this parameter is set, the system will use ca path specified by user, or else use preset ca by the system.

**类型：** string

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequestOptions-caPath?: string--><!--Device-HttpRequestOptions-caPath?: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

## certificatePinning

```TypeScript
certificatePinning?: CertificatePinning | CertificatePinning[]
```

Certificate pinning option. If server certificate's digest does not match{@link CertificatePinning.publicKeyHash}, request will fail.

**类型：** [CertificatePinning](arkts-network-http-certificatepinning-i.md) \| CertificatePinning[]

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-HttpRequestOptions-certificatePinning?: CertificatePinning | CertificatePinning[]--><!--Device-HttpRequestOptions-certificatePinning?: CertificatePinning | CertificatePinning[]-End-->

**系统能力：** SystemCapability.Communication.NetStack

## clientCert

```TypeScript
clientCert?: ClientCert
```

Support the application to pass in client certificates, allowing the server to verify the client's identity.

**类型：** [ClientCert](arkts-network-websocket-clientcert-i.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-HttpRequestOptions-clientCert?: ClientCert--><!--Device-HttpRequestOptions-clientCert?: ClientCert-End-->

**系统能力：** SystemCapability.Communication.NetStack

## clientEncCert

```TypeScript
clientEncCert?: ClientCert
```

Support the application to pass in client certificates, allowing the server to verify the client's encryption identity.

**类型：** [ClientCert](arkts-network-websocket-clientcert-i.md)

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为20。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequestOptions-clientEncCert?: ClientCert--><!--Device-HttpRequestOptions-clientEncCert?: ClientCert-End-->

**系统能力：** SystemCapability.Communication.NetStack

## connectTimeout

```TypeScript
connectTimeout?: int
```

Connection timeout interval. The default value is 60,000, in ms.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequestOptions-connectTimeout?: int--><!--Device-HttpRequestOptions-connectTimeout?: int-End-->

**系统能力：** SystemCapability.Communication.NetStack

## customMethod

```TypeScript
customMethod?: string
```

Supports specifying the user custom defined http request method

**类型：** string

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

<!--Device-HttpRequestOptions-customMethod?: string--><!--Device-HttpRequestOptions-customMethod?: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

## dnsOverHttps

```TypeScript
dnsOverHttps?: string
```

If this parameter is set, incoming DNS resolution server URL for the DoH server to use for name resolving.The parameter must be URL-encoded in the following format: "https://host:port/path".It MUST specify an HTTPS URL.

**类型：** string

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-HttpRequestOptions-dnsOverHttps?: string--><!--Device-HttpRequestOptions-dnsOverHttps?: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

## dnsServers

```TypeScript
dnsServers?: Array<string>
```

If this parameter is set, use the specified DNS server for DNS resolution.Multiple DNS resolution servers can be set up, with a maximum of 3 servers.Only take the first three if there are more than three.

**类型：** Array&lt;string&gt;

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-HttpRequestOptions-dnsServers?: Array<string>--><!--Device-HttpRequestOptions-dnsServers?: Array<string>-End-->

**系统能力：** SystemCapability.Communication.NetStack

## enablePartialChain

```TypeScript
enablePartialChain?: boolean
```

Indicates whether to enable partial chain verification.The default value is true when SslType is set to TLS, and false when SslType is set to TLCP.If set to false, the certificate chain must verify up to a trusted root CA.If set to true, the verification succeeds if the chain builds to a trusted intermediate CA,without requiring a path to a trusted root CA.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HttpRequestOptions-enablePartialChain?: boolean--><!--Device-HttpRequestOptions-enablePartialChain?: boolean-End-->

**系统能力：** SystemCapability.Communication.NetStack

## expectDataType

```TypeScript
expectDataType?: HttpDataType
```

Data type to be returned. If this parameter is set, the system preferentially returns the specified type.

**类型：** [HttpDataType](arkts-network-http-httpdatatype-e.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequestOptions-expectDataType?: HttpDataType--><!--Device-HttpRequestOptions-expectDataType?: HttpDataType-End-->

**系统能力：** SystemCapability.Communication.NetStack

## extraData

```TypeScript
extraData?: string | Object | ArrayBuffer
```

Additional data of the request.extraData can be a string or an Object (API 6) or an ArrayBuffer(API 8).

**类型：** string \| Object \| ArrayBuffer

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequestOptions-extraData?: string | Object | ArrayBuffer--><!--Device-HttpRequestOptions-extraData?: string | Object | ArrayBuffer-End-->

**系统能力：** SystemCapability.Communication.NetStack

## header

```TypeScript
header?: Object
```

HTTP request header. default is 'content-type': 'application/json'

**类型：** Object

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequestOptions-header?: Object--><!--Device-HttpRequestOptions-header?: Object-End-->

**系统能力：** SystemCapability.Communication.NetStack

## inactivityMs

```TypeScript
inactivityMs?: int
```

Maximum HTTP idle time (unit: ms)

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HttpRequestOptions-inactivityMs?: int--><!--Device-HttpRequestOptions-inactivityMs?: int-End-->

**系统能力：** SystemCapability.Communication.NetStack

## maxLimit

```TypeScript
maxLimit?: int
```

The maximum limit of the response body. The default value is 5 * 1024 * 1024, in Byte.The maximum value is 100 * 1024 *1024, in Byte.

**类型：** int

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-HttpRequestOptions-maxLimit?: int--><!--Device-HttpRequestOptions-maxLimit?: int-End-->

**系统能力：** SystemCapability.Communication.NetStack

## maxRedirects

```TypeScript
maxRedirects?: int
```

Support specifying the configuration of maximum redirect count

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

<!--Device-HttpRequestOptions-maxRedirects?: int--><!--Device-HttpRequestOptions-maxRedirects?: int-End-->

**系统能力：** SystemCapability.Communication.NetStack

## method

```TypeScript
method?: RequestMethod
```

Request method,default is GET.

**类型：** [RequestMethod](arkts-network-http-requestmethod-e.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequestOptions-method?: RequestMethod--><!--Device-HttpRequestOptions-method?: RequestMethod-End-->

**系统能力：** SystemCapability.Communication.NetStack

## multiFormDataList

```TypeScript
multiFormDataList?: Array<MultiFormData>
```

The data fields which is supported by the HTTP protocol to post forms and by the SMTP and IMAP protocols to provide the email data to send/upload.

**类型：** Array&lt;MultiFormData&gt;

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-HttpRequestOptions-multiFormDataList?: Array<MultiFormData>--><!--Device-HttpRequestOptions-multiFormDataList?: Array<MultiFormData>-End-->

**系统能力：** SystemCapability.Communication.NetStack

## pathPreference

```TypeScript
pathPreference?: PathPreference
```

Support specifying a preferred network when making HTTP requests.If the specified network is unavailable, the default network will be selected to send the request.

**类型：** [PathPreference](arkts-network-http-pathpreference-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

<!--Device-HttpRequestOptions-pathPreference?: PathPreference--><!--Device-HttpRequestOptions-pathPreference?: PathPreference-End-->

**系统能力：** SystemCapability.Communication.NetStack

## priority

```TypeScript
priority?: int
```

[1, 1000], default is 1.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequestOptions-priority?: int--><!--Device-HttpRequestOptions-priority?: int-End-->

**系统能力：** SystemCapability.Communication.NetStack

## queryParams

```TypeScript
queryParams?: string | QueryParamObject
```

Query parameters to append to the request URL.Supports two input forms:  
- `string`: a pre-encoded query string provided by the caller. It is appended  
to the URL as-is and is not encoded again by the system.  
- `QueryParamObject`: a key-value object. The system encodes keys and values  
and serializes them into the URL query string automatically.

Notes:1. For `string`, do not include the leading `?`(for example, use `"key=value"`, not `"?key=value"`).2. For `string`, the caller is responsible for encoding special characters.3. For `string`, use `&` to separate multiple parameters.

If both `queryParams` and `extraData` are specified, `queryParams` takes precedence for URL construction, and `extraData` will be ignored.

**类型：** string \| QueryParamObject

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HttpRequestOptions-queryParams?: string | QueryParamObject--><!--Device-HttpRequestOptions-queryParams?: string | QueryParamObject-End-->

**系统能力：** SystemCapability.Communication.NetStack

## readTimeout

```TypeScript
readTimeout?: int
```

Read timeout period. The default value is 60,000, in ms.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequestOptions-readTimeout?: int--><!--Device-HttpRequestOptions-readTimeout?: int-End-->

**系统能力：** SystemCapability.Communication.NetStack

## remoteValidation

```TypeScript
remoteValidation?: RemoteValidation
```

Certificate authority(CA) which is used to verify the remote server's identification.

**类型：** [RemoteValidation](arkts-network-http-remotevalidation-t.md)

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequestOptions-remoteValidation?: RemoteValidation--><!--Device-HttpRequestOptions-remoteValidation?: RemoteValidation-End-->

**系统能力：** SystemCapability.Communication.NetStack

## resumeFrom

```TypeScript
resumeFrom?: long
```

Used to set to uploading or downloading the start bytes. The default value is 0.HTTP standard (RFC 7233 section 3.1) allows servers to ignore range requests.For HTTP PUT uploads this option should not be used, since it may conflict with other options.

**类型：** long

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-HttpRequestOptions-resumeFrom?: long--><!--Device-HttpRequestOptions-resumeFrom?: long-End-->

**系统能力：** SystemCapability.Communication.NetStack

## resumeTo

```TypeScript
resumeTo?: long
```

Used to set to uploading or downloading the end bytes. Translate to the end if not set.HTTP standard (RFC 7233 section 3.1) allows servers to ignore range requests.For HTTP PUT uploads this option should not be used, since it may conflict with other options.

**类型：** long

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-HttpRequestOptions-resumeTo?: long--><!--Device-HttpRequestOptions-resumeTo?: long-End-->

**系统能力：** SystemCapability.Communication.NetStack

## reuseConnections

```TypeScript
reuseConnections?: boolean
```

Supports forbidding reuse of HTTP/HTTPS connections

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HttpRequestOptions-reuseConnections?: boolean--><!--Device-HttpRequestOptions-reuseConnections?: boolean-End-->

**系统能力：** SystemCapability.Communication.NetStack

## serverAuthentication

```TypeScript
serverAuthentication?: ServerAuthentication
```

HTTP server authentication settings. No authentication by default.

**类型：** [ServerAuthentication](arkts-network-http-serverauthentication-i.md)

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequestOptions-serverAuthentication?: ServerAuthentication--><!--Device-HttpRequestOptions-serverAuthentication?: ServerAuthentication-End-->

**系统能力：** SystemCapability.Communication.NetStack

## sniHostName

```TypeScript
sniHostName?: string
```

Support specifying an SNI domain name to include the SNI field during the TLS connection process

**类型：** string

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

<!--Device-HttpRequestOptions-sniHostName?: string--><!--Device-HttpRequestOptions-sniHostName?: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

## sslType

```TypeScript
sslType?: SslType
```

Which secure communication protocol is used, TLS (by defaul) or TLCP.If TLCP is used, all TLS related options, such as caPath, caData and clientCert, are ignored.

**类型：** [SslType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-cachedownload-ssltype-e.md)

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为20。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequestOptions-sslType?: SslType--><!--Device-HttpRequestOptions-sslType?: SslType-End-->

**系统能力：** SystemCapability.Communication.NetStack

## tlsOptions

```TypeScript
tlsOptions?: TlsOptions
```

TLS option.

**类型：** [TlsOptions](arkts-network-http-tlsoptions-t.md)

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequestOptions-tlsOptions?: TlsOptions--><!--Device-HttpRequestOptions-tlsOptions?: TlsOptions-End-->

**系统能力：** SystemCapability.Communication.NetStack

## usingCache

```TypeScript
usingCache?: boolean
```

default is true

**类型：** boolean

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequestOptions-usingCache?: boolean--><!--Device-HttpRequestOptions-usingCache?: boolean-End-->

**系统能力：** SystemCapability.Communication.NetStack

## usingProtocol

```TypeScript
usingProtocol?: HttpProtocol
```

default is automatically specified by the system.

**类型：** [HttpProtocol](arkts-network-http-httpprotocol-e.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequestOptions-usingProtocol?: HttpProtocol--><!--Device-HttpRequestOptions-usingProtocol?: HttpProtocol-End-->

**系统能力：** SystemCapability.Communication.NetStack

## usingProxy

```TypeScript
usingProxy?: boolean | HttpProxy
```

If this parameter is set as type of boolean, the system will use default proxy or not use proxy.If this parameter is set as type of HttpProxy, the system will use the specified HttpProxy.

**类型：** boolean \| HttpProxy

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-HttpRequestOptions-usingProxy?: boolean | HttpProxy--><!--Device-HttpRequestOptions-usingProxy?: boolean | HttpProxy-End-->

**系统能力：** SystemCapability.Communication.NetStack

## usingSocks5Proxy

```TypeScript
usingSocks5Proxy?: Socks5Proxy
```

Specifies the use of a SOCKS5 proxy. Note that this configuration takes precedence over usingProxy.It is recommend not to configure both simultaneously.

**类型：** [Socks5Proxy](arkts-network-connection-socks5proxy-i.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HttpRequestOptions-usingSocks5Proxy?: Socks5Proxy--><!--Device-HttpRequestOptions-usingSocks5Proxy?: Socks5Proxy-End-->

**系统能力：** SystemCapability.Communication.NetStack

