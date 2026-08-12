# WebController

Defines the Web controller.

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [WebviewController](ohos.web.webview.webview.WebviewController)

<!--Device-unnamed-declare class WebController--><!--Device-unnamed-declare class WebController-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## accessBackward

```TypeScript
accessBackward(): boolean
```

Checks whether the web page can go back.

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [accessBackward](ohos.web.webview.webview.WebviewController#accessBackward)

<!--Device-WebController-accessBackward(): boolean--><!--Device-WebController-accessBackward(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## accessForward

```TypeScript
accessForward(): boolean
```

Checks whether the web page can go forward.

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [accessForward](ohos.web.webview.webview.WebviewController#accessForward)

<!--Device-WebController-accessForward(): boolean--><!--Device-WebController-accessForward(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## accessStep

```TypeScript
accessStep(step: number): boolean
```

Checks whether the web page can go back or forward the given number of steps.

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [accessStep](ohos.web.webview.webview.WebviewController#accessStep)

<!--Device-WebController-accessStep(step: number): boolean--><!--Device-WebController-accessStep(step: number): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| step | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## backward

```TypeScript
backward()
```

Goes back in the history of the web page.

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [backward](ohos.web.webview.webview.WebviewController#backward)

<!--Device-WebController-backward()--><!--Device-WebController-backward()-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## clearHistory

```TypeScript
clearHistory(): void
```

Clears the history in the Web.

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [clearHistory](ohos.web.webview.webview.WebviewController#clearHistory)

<!--Device-WebController-clearHistory(): void--><!--Device-WebController-clearHistory(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

Constructor.

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [constructor](ohos.web.webview.webview.WebviewController#constructor)

<!--Device-WebController-constructor()--><!--Device-WebController-constructor()-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## deleteJavaScriptRegister

```TypeScript
deleteJavaScriptRegister(name: string)
```

Deletes a registered JavaScript object with given name.

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [deleteJavaScriptRegister](ohos.web.webview.webview.WebviewController#deleteJavaScriptRegister)

<!--Device-WebController-deleteJavaScriptRegister(name: string)--><!--Device-WebController-deleteJavaScriptRegister(name: string)-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

## forward

```TypeScript
forward()
```

Goes forward in the history of the web page.

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [forward](ohos.web.webview.webview.WebviewController#forward)

<!--Device-WebController-forward()--><!--Device-WebController-forward()-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## getCookieManager

```TypeScript
getCookieManager(): WebCookie
```

Gets network cookie manager

**起始版本：** 9

**废弃版本：** 9

**替代接口：** [WebCookieManager](../arkts-apis/arkts-arkweb-webview-webcookiemanager-c.md#WebCookieManager)

<!--Device-WebController-getCookieManager(): WebCookie--><!--Device-WebController-getCookieManager(): WebCookie-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [WebCookie](arkts-arkweb-webcookie-c.md) |

## getHitTest

```TypeScript
getHitTest(): HitTestType
```

获取点击测试类型。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getHitTest](ohos.web.webview.webview.WebviewController#getHitTest)

<!--Device-WebController-getHitTest(): HitTestType--><!--Device-WebController-getHitTest(): HitTestType-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [HitTestType](arkts-arkweb-hittesttype-e.md) |

## loadData

```TypeScript
loadData(options: { data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string })
```

Loads the data or URL.

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [loadData](ohos.web.webview.webview.WebviewController#loadData)

<!--Device-WebController-loadData(options: { data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string })--><!--Device-WebController-loadData(options: { data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string })-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | { data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string } | 是 |

## loadUrl

```TypeScript
loadUrl(options: { url: string | Resource, headers?: Array<Header> })
```

Loads the given URL.

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [loadUrl](ohos.web.webview.webview.WebviewController#loadUrl)

<!--Device-WebController-loadUrl(options: { url: string | Resource, headers?: Array<Header> })--><!--Device-WebController-loadUrl(options: { url: string | Resource, headers?: Array<Header> })-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | { url: string \| Resource, headers?: Array&lt;[Header](arkts-arkweb-header-i.md)&gt; } | 是 |

## onActive

```TypeScript
onActive(): void
```

Let the Web active.It is no longer maintained since API version 9, and it is recommended to use [onActive](#onActive) instead.

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [onActive](ohos.web.webview.webview.WebviewController#onActive)

<!--Device-WebController-onActive(): void--><!--Device-WebController-onActive(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## onInactive

```TypeScript
onInactive(): void
```

Let the Web inactive.It is no longer maintained since API version 9, and it is recommended to use [onInactive](#onInactive) instead.

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [onInactive](ohos.web.webview.webview.WebviewController#onInactive)

<!--Device-WebController-onInactive(): void--><!--Device-WebController-onInactive(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## refresh

```TypeScript
refresh()
```

refreshes the current URL.

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [refresh](ohos.web.webview.webview.WebviewController#refresh)

<!--Device-WebController-refresh()--><!--Device-WebController-refresh()-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## registerJavaScriptProxy

```TypeScript
registerJavaScriptProxy(options: { object: object, name: string, methodList: Array<string> })
```

Registers the JavaScript object and method list.

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [registerJavaScriptProxy](ohos.web.webview.webview.WebviewController#registerJavaScriptProxy)

<!--Device-WebController-registerJavaScriptProxy(options: { object: object, name: string, methodList: Array<string> })--><!--Device-WebController-registerJavaScriptProxy(options: { object: object, name: string, methodList: Array<string> })-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | { object: object, name: string, methodList: Array & lt;string & gt; } | 是 |

## requestFocus

```TypeScript
requestFocus()
```

Gets the request focus.

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [requestFocus](ohos.web.webview.webview.WebviewController#requestFocus)

<!--Device-WebController-requestFocus()--><!--Device-WebController-requestFocus()-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## runJavaScript

```TypeScript
runJavaScript(options: { script: string, callback?: (result: string) => void })
```

Asynchronously execute JavaScript in the context of the currently displayed page.The result of the script execution will be returned through an asynchronous callback.This method must be used on the UI thread, and the callback will also be invoked on the UI thread.&lt;p&gt;&lt;strong&gt;API Note&lt;/strong&gt;:&lt;br&gt;The state of JavaScript is no longer persisted across navigations like loadUrl.For example, global variables and functions defined before calling loadUrl will not exist in the loaded page.It is recommended that applications use registerJavaScriptProxy to ensure that the JavaScript state can be persisted across page navigations.&lt;p&gt;

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [runJavaScript](ohos.web.webview.webview.WebviewController#runJavaScript)

<!--Device-WebController-runJavaScript(options: { script: string, callback?: (result: string) => void })--><!--Device-WebController-runJavaScript(options: { script: string, callback?: (result: string) => void })-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | { script: string, callback?: (result: string) = & gt; void } | 是 |

## stop

```TypeScript
stop()
```

Stops the current load.

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [stop](ohos.web.webview.webview.WebviewController#stop)

<!--Device-WebController-stop()--><!--Device-WebController-stop()-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## zoom

```TypeScript
zoom(factor: number): void
```

对网页进行缩放。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [zoom](ohos.web.webview.webview.WebviewController#zoom)

<!--Device-WebController-zoom(factor: number): void--><!--Device-WebController-zoom(factor: number): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [factor](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-materialproperty-i.md) | number | 是 |
