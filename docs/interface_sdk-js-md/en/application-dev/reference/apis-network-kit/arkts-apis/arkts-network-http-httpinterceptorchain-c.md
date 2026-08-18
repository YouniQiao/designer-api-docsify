# HttpInterceptorChain

Defines HTTP interceptor chain.

**Since:** 22

<!--Device-http-export class HttpInterceptorChain--><!--Device-http-export class HttpInterceptorChain-End-->

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { http } from '@kit.NetworkKit';
```

## addChain

```TypeScript
public addChain(chain: HttpInterceptor[]): boolean
```

Adds an interceptor to the HTTP client. > **NOTE：**> > An interceptor chain cannot contain interceptor instances of the same type. If interceptors of the same type > are passed in, the error code **2300802** (Duplicated interceptor type in the chain) is reported.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-HttpInterceptorChain-public addChain(chain: HttpInterceptor[]): boolean--><!--Device-HttpInterceptorChain-public addChain(chain: HttpInterceptor[]): boolean-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| chain | [HttpInterceptor](arkts-network-http-httpinterceptor-i.md)[] | Yes | Interception chain composed of interceptor instances. A single interceptor or multiple interceptors of different types can be passed in. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the interceptor is added successfully. The value **true** indicates that the interceptor is successfully added, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 2300802 | Duplicated interceptor type in the chain. |
| 2300801 | Parameter type not supported by the interceptor. |
| [2300999](../errorcode-net-http.md#2300999-internal-error) | Internal error. |

## apply

```TypeScript
public apply(httpRequest: HttpRequest): boolean
```

Adds an interceptor chain to the target HTTP request. Each HTTP request instance can have only one interceptor chain attached. > **NOTE：**> > After an interceptor chain is attached to an [HttpRequest](arkts-network-http-httprequest-i.md) instance, when the instance > initiates an HTTP request, interceptors of the corresponding type in the attached interceptor chain are > triggered. > For more information about how to trigger interceptors using HTTP requests, see > [HTTP Interceptor Function Code Example](../../../network/http-request.md#http-interceptor). > The HTTP interceptor feature is supported only by > [HttpRequest.request](arkts-network-http-httprequest-i.md#request) APIs, > and is not supported by > [HttpRequest.requestInStream](arkts-network-http-httprequest-i.md#requestinstream) > APIs (streaming transmission).

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-HttpInterceptorChain-public apply(httpRequest: HttpRequest): boolean--><!--Device-HttpInterceptorChain-public apply(httpRequest: HttpRequest): boolean-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| httpRequest | HttpRequest | Yes | [HttpRequest](arkts-network-http-httprequest-i.md) that initiates an HTTP request. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the interceptor is attached successfully. The value **true** indicates that the interceptor is successfully added, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 2300801 | Parameter type not supported by the interceptor. |
| [2300999](../errorcode-net-http.md#2300999-internal-error) | Internal error. |

## getChain

```TypeScript
public getChain(): HttpInterceptor[]
```

Obtains all interceptor instances in the current interceptor chain.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-HttpInterceptorChain-public getChain(): HttpInterceptor[]--><!--Device-HttpInterceptorChain-public getChain(): HttpInterceptor[]-End-->

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| Type | Description |
| --- | --- |
| [HttpInterceptor](arkts-network-http-httpinterceptor-i.md)[] | Returns all interceptor instances added by the [addChain]{ |

