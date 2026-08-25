# WebResourceHandler

WebResourceHandler是自定义scheme拦截场景中用于向Web组件返回拦截请求结果的处理器。当WebSchemeHandler决定拦截一个请求后，开发者通过WebResourceHandler向Web组件提供自定义 的响应头（didReceiveResponse）、响应体数据（didReceiveResponseBody），并通知请求完成（didFinish）或失败（didFail）。其中didFail支持重载方法（API version 2 0+）以简化错误处理流程。该接口实现了应用层对网络请求的完全自定义响应。WebResourceHandler与[WebSchemeHandler](arkts-arkweb-webview-webschemehandler-c.md)、 [WebSchemeHandlerResponse](arkts-arkweb-webview-webschemehandlerresponse-c.md)配合使用：WebSchemeHandler的onRequestStart回调中接收 WebResourceHandler实例，开发者构造WebSchemeHandlerResponse对象，通过WebResourceHandler的didReceiveResponse和didReceiveResponseBody 传入响应头和响应体数据，最后调用didFinish或didFail结束请求。

**起始版本：** 12

**系统能力：** SystemCapability.Web.Webview.Core

## 导入模块

```TypeScript
import { webview } from 'kits/@kit.ArkWeb';
```

## didFail

```TypeScript
didFail(code: WebNetErrorList): void
```

通知ArkWeb内核被拦截请求将返回失败，并结束该网络请求，调用前需调用[didReceiveResponse](#didreceiveresponse)传入响应 头。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | [WebNetErrorList](arkts-arkweb-web-neterrorlist-webneterrorlist-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100021](../errorcode-webview.md#17100021-webresourcehandler已经失效) |

## didFail

```TypeScript
didFail(code: WebNetErrorList, completeIfNoResponse: boolean): void
```

通知ArkWeb内核，被拦截请求将返回失败。若completeIfNoResponse为false，调用前需调用 [didReceiveResponse](#didreceiveresponse)传入响应头。若completeIfNoResponse为true，且调用前未调用 [didReceiveResponse](#didreceiveresponse)，则自动生成一个响应头，网络错误码为-104，详情参见 [WebNetErrorList](arkts-arkweb-web-neterrorlist-webneterrorlist-e.md)。

**起始版本：** 20

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | [WebNetErrorList](arkts-arkweb-web-neterrorlist-webneterrorlist-e.md) | 是 |
| completeIfNoResponse | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100101](../errorcode-webview.md#17100101-使用了错误的网络错误码) |
| [17100021](../errorcode-webview.md#17100021-webresourcehandler已经失效) |

## didFail

```TypeScript
didFail(code: WebNetErrorList, completeIfNoResponse: boolean, customErrorCode: number): void
```

通知ArkWeb内核，被拦截请求应返回失败，并携带自定义错误码。

**起始版本：** 26.1.0

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | [WebNetErrorList](arkts-arkweb-web-neterrorlist-webneterrorlist-e.md) | 是 |
| completeIfNoResponse | boolean | 是 |
| customErrorCode | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100021](../errorcode-webview.md#17100021-webresourcehandler已经失效) |

## didFinish

```TypeScript
didFinish(): void
```

通知Web组件被拦截的请求已经完成，并且没有更多的数据可用，调用前需调用[didReceiveResponse](#didreceiveresponse)传入响应 头。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100021](../errorcode-webview.md#17100021-webresourcehandler已经失效) |

## didReceiveResponse

```TypeScript
didReceiveResponse(response: WebSchemeHandlerResponse): void
```

将构造的响应头传递给被拦截的请求。需在调用didFinish或didFail之前调用。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| response | [WebSchemeHandlerResponse](arkts-arkweb-webview-webschemehandlerresponse-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100021](../errorcode-webview.md#17100021-webresourcehandler已经失效) |

## didReceiveResponseBody

```TypeScript
didReceiveResponseBody(data: ArrayBuffer): void
```

将构造的响应体传递给被拦截的请求。需在调用didFinish或didFail之前调用。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | ArrayBuffer | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100021](../errorcode-webview.md#17100021-webresourcehandler已经失效) |
