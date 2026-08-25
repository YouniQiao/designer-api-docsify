# @ohos.net.http(数据请求)

本模块提供HTTP数据请求能力。应用可以通过HTTP发起一个数据请求，支持常见的GET、POST、OPTIONS、HEAD、PUT、DELETE、PATCH、TRACE、CONNECT方法。

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { http } from '@kit.NetworkKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [createHttp(数据请求)](arkts-network-http-createhttp-f.md) |
| [createHttpResponseCache(数据请求)](arkts-network-http-createhttpresponsecache-f.md) |

### 类

| 名称 |
| --- |
| [HttpInterceptorChain(数据请求)](arkts-network-http-httpinterceptorchain-c.md) |

### 接口

| 名称 |
| --- |
| [CertificatePinning(数据请求)](arkts-network-http-certificatepinning-i.md) |
| [ClientCert(数据请求)](arkts-network-http-clientcert-i.md) |
| [ConnectionExtraInfo(数据请求)](arkts-network-http-connectionextrainfo-i.md) |
| [Credential(数据请求)](arkts-network-http-credential-i.md) |
| [DataReceiveProgressInfo(数据请求)](arkts-network-http-datareceiveprogressinfo-i.md) |
| [DataSendProgressInfo(数据请求)](arkts-network-http-datasendprogressinfo-i.md) |
| [HttpInterceptor(数据请求)](arkts-network-http-httpinterceptor-i.md) |
| [HttpRequest(数据请求)](arkts-network-http-httprequest-i.md) |
| [HttpRequestContext(数据请求)](arkts-network-http-httprequestcontext-i.md) |
| [HttpRequestOptions(数据请求)](arkts-network-http-httprequestoptions-i.md) |
| [HttpResponse(数据请求)](arkts-network-http-httpresponse-i.md) |
| [HttpResponseCache(数据请求)](arkts-network-http-httpresponsecache-i.md) |
| [MultiFormData(数据请求)](arkts-network-http-multiformdata-i.md) |
| [PerformanceTiming(数据请求)](arkts-network-http-performancetiming-i.md) |
| [ServerAuthentication(数据请求)](arkts-network-http-serverauthentication-i.md) |
| [TlsConfig(数据请求)](arkts-network-http-tlsconfig-i.md) |
| [ValidationContext(数据请求)](arkts-network-http-validationcontext-i.md) |

### 枚举

| 名称 |
| --- |
| [AddressFamily(数据请求)](arkts-network-http-addressfamily-e.md) |
| [CertType(数据请求)](arkts-network-http-certtype-e.md) |
| [HttpDataType(数据请求)](arkts-network-http-httpdatatype-e.md) | HTTP的数据类型。  \| 名称 \| 值 \| 说明 \| \| ------------------ \| -- \| ----------- \| \| STRING \| 0 \| 字符串类型。 \| \| OBJECT \| 1 \| 对象类型。 \| \| ARRAY_BUFFER \| 2 \| 二进制数组类型。\|
| [HttpProtocol(数据请求)](arkts-network-http-httpprotocol-e.md) |
| [InterceptorType(数据请求)](arkts-network-http-interceptortype-e.md) | HTTP拦截器的类型枚举。  \| 名称 \| 值 \|说明 \| \| ------ \| --\|-------------------------------------- \| \| INITIAL_REQUEST \|'INITIAL_REQUEST' \|在初始HTTP请求组装完成后拦截。\| \| REDIRECTION \| 'REDIRECTION' \|当收到重定向响应时拦截。\| \| CACHE_CHECKED \| 'READ_CACHE' \|在检查并且命中HTTP缓存时拦截。\| \| NETWORK_CONNECT \| 'CONNECT_NETWORK' \|在网络请求将要发出前拦截。\| \| FINAL_RESPONSE \| 'FINAL_RESPONSE' \|在获取最终HTTP响应时拦截。\|
| [RequestMethod(数据请求)](arkts-network-http-requestmethod-e.md) |
| [ResponseCode(数据请求)](arkts-network-http-responsecode-e.md) |
| [TlsVersion(数据请求)](arkts-network-http-tlsversion-e.md) |

### 类型

| 名称 |
| --- |
| [AuthenticationType(数据请求)](arkts-network-http-authenticationtype-t.md) |
| [ChainContinue(数据请求)](arkts-network-http-chaincontinue-t.md) |
| [CipherSuite(数据请求)](arkts-network-http-ciphersuite-t.md) |
| [HttpProxy(数据请求)](arkts-network-http-httpproxy-t.md) |
| [PathPreference(数据请求)](arkts-network-http-pathpreference-t.md) |
| [QueryParamObject(数据请求)](arkts-network-http-queryparamobject-t.md) |
| [QueryParamValue(数据请求)](arkts-network-http-queryparamvalue-t.md) |
| [RemoteValidation(数据请求)](arkts-network-http-remotevalidation-t.md) |
| [Socks5Proxy(数据请求)](arkts-network-http-socks5proxy-t.md) |
| [SslType(数据请求)](arkts-network-http-ssltype-t.md) |
| [TlsOptions(数据请求)](arkts-network-http-tlsoptions-t.md) |
| [TlsV10CipherSuite(数据请求)](arkts-network-http-tlsv10ciphersuite-t.md) |
| [TlsV10SpecificCipherSuite(数据请求)](arkts-network-http-tlsv10specificciphersuite-t.md) |
| [TlsV11CipherSuite(数据请求)](arkts-network-http-tlsv11ciphersuite-t.md) |
| [TlsV12CipherSuite(数据请求)](arkts-network-http-tlsv12ciphersuite-t.md) |
| [TlsV12SpecificCipherSuite(数据请求)](arkts-network-http-tlsv12specificciphersuite-t.md) |
| [TlsV13CipherSuite(数据请求)](arkts-network-http-tlsv13ciphersuite-t.md) |
| [TlsV13SpecificCipherSuite(数据请求)](arkts-network-http-tlsv13specificciphersuite-t.md) |
| [ValidationCallback(数据请求)](arkts-network-http-validationcallback-t.md) |
| [X509Cert(数据请求)](arkts-network-http-x509cert-t.md) |
