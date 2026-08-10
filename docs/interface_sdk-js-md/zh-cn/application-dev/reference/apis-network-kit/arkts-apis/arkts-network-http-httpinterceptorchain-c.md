# HttpInterceptorChain

Defines an HTTP Interceptor chain.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

<!--Device-http-export class HttpInterceptorChain--><!--Device-http-export class HttpInterceptorChain-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { http } from 'kits/@kit.NetworkKit';
```

## addChain

```TypeScript
public addChain(chain: HttpInterceptor[]): boolean
```

Add an interceptor chain to the HTTP client.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-HttpInterceptorChain-public addChain(chain: HttpInterceptor[]): boolean--><!--Device-HttpInterceptorChain-public addChain(chain: HttpInterceptor[]): boolean-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| chain | [HttpInterceptor](arkts-network-http-httpinterceptor-i.md)[] | 是 | The chain of interceptors. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Whether the chain is added successfully. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2300802 | Duplicated interceptor type in the chain. |
| 2300801 | Parameter type not supported by the interceptor. |
| 2300999 | Internal error. |

## apply

```TypeScript
public apply(httpRequest: HttpRequest): boolean
```

Attach the chain to the target http request.Only one chain can be attached to a given request.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-HttpInterceptorChain-public apply(httpRequest: HttpRequest): boolean--><!--Device-HttpInterceptorChain-public apply(httpRequest: HttpRequest): boolean-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| httpRequest | [HttpRequest](arkts-network-http-httprequest-i.md) | 是 | Initiates an HTTP request to a given URL. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Whether the interceptor chain is attached successfully. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2300801 | Parameter type not supported by the interceptor. |
| 2300999 | Internal error. |

## getChain

```TypeScript
public getChain(): HttpInterceptor[]
```

The method to get the chain of interceptors.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-HttpInterceptorChain-public getChain(): HttpInterceptor[]--><!--Device-HttpInterceptorChain-public getChain(): HttpInterceptor[]-End-->

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HttpInterceptor](arkts-network-http-httpinterceptor-i.md)[] | The chain of interceptors. |

