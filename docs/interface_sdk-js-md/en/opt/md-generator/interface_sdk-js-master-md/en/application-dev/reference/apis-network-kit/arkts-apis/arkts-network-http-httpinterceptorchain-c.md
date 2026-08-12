# HttpInterceptorChain

Defines an HTTP Interceptor chain.

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

Add an interceptor chain to the HTTP client.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-HttpInterceptorChain-public addChain(chain: HttpInterceptor[]): boolean--><!--Device-HttpInterceptorChain-public addChain(chain: HttpInterceptor[]): boolean-End-->

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
| 2300802 |
| 2300801 |
| [2300999](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-http.md#2300999-internal-error) |

## apply

```TypeScript
public apply(httpRequest: HttpRequest): boolean
```

Attach the chain to the target http request.Only one chain can be attached to a given request.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-HttpInterceptorChain-public apply(httpRequest: HttpRequest): boolean--><!--Device-HttpInterceptorChain-public apply(httpRequest: HttpRequest): boolean-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| httpRequest | [HttpRequest](arkts-network-http-httprequest-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| 2300801 |
| [2300999](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-http.md#2300999-internal-error) |

## getChain

```TypeScript
public getChain(): HttpInterceptor[]
```

The method to get the chain of interceptors.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-HttpInterceptorChain-public getChain(): HttpInterceptor[]--><!--Device-HttpInterceptorChain-public getChain(): HttpInterceptor[]-End-->

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [HttpInterceptor](arkts-network-http-httpinterceptor-i.md)[] |
