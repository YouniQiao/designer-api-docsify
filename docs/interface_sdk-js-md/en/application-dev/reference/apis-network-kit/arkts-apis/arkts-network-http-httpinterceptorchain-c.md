# HttpInterceptorChain

Defines HTTP interceptor chain.

**Since:** 22

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { http } from 'kits/@kit.NetworkKit';
```

## addChain

```TypeScript
public addChain(chain: HttpInterceptor[]): boolean
```

Adds an interceptor to the HTTP client.

> **NOTE：**&gt;
> An interceptor chain cannot contain interceptor instances of the same type. If interceptors of the same type
> are passed in, the error code **2300802** (Duplicated interceptor type in the chain) is reported.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| chain | [HttpInterceptor](arkts-network-http-httpinterceptor-i.md)[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| 2300801 |
| 2300802 |
| [2300999](../errorcode-net-http.md#2300999-internal-error) |

## apply

```TypeScript
public apply(httpRequest: HttpRequest): boolean
```

Adds an interceptor chain to the target HTTP request. Each HTTP request instance can have only one interceptor chain attached.

> **NOTE：**&gt;
> After an interceptor chain is attached to an [HttpRequest](arkts-network-http-httprequest-i.md) instance, when the instance
> initiates an HTTP request, interceptors of the corresponding type in the attached interceptor chain are
> triggered.

> For more information about how to trigger interceptors using HTTP requests, see
> [HTTP Interceptor Function Code Example](../../../network/http-request.md#http-interceptor).

> The HTTP interceptor feature is supported only by
> [HttpRequest.request](arkts-network-http-httprequest-i.md#request) APIs,
> and is not supported by
> [HttpRequest.requestInStream](arkts-network-http-httprequest-i.md#requestinstream)
> APIs (streaming transmission).

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| httpRequest | [HttpRequest](arkts-network-connection-httprequest-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| 2300801 |
| [2300999](../errorcode-net-http.md#2300999-internal-error) |

## getChain

```TypeScript
public getChain(): HttpInterceptor[]
```

Obtains all interceptor instances in the current interceptor chain.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [HttpInterceptor](arkts-network-http-httpinterceptor-i.md)[] |
