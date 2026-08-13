# WebSchemeHandler

This class is used to intercept requests for a specified scheme.

**起始版本：** 12

**废弃版本：** -1

<!--Device-webview-class WebSchemeHandler--><!--Device-webview-class WebSchemeHandler-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## onRequestStart

```TypeScript
onRequestStart(
      callback: (request: WebSchemeHandlerRequest, handler: WebResourceHandler) => boolean): void
```

当请求开始时的回调，在该回调函数中可以决定是否拦截该请求。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebSchemeHandler-onRequestStart(      callback: (request: WebSchemeHandlerRequest, handler: WebResourceHandler) => boolean): void--><!--Device-WebSchemeHandler-onRequestStart(      callback: (request: WebSchemeHandlerRequest, handler: WebResourceHandler) => boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (request: WebSchemeHandlerRequest, handler: WebResourceHandler) = & gt; boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## onRequestStop

```TypeScript
onRequestStop(callback: Callback<WebSchemeHandlerRequest>): void
```

请求完成时的回调。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebSchemeHandler-onRequestStop(callback: Callback<WebSchemeHandlerRequest>): void--><!--Device-WebSchemeHandler-onRequestStop(callback: Callback<WebSchemeHandlerRequest>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WebSchemeHandlerRequest](arkts-arkweb-webview-webschemehandlerrequest-c.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
