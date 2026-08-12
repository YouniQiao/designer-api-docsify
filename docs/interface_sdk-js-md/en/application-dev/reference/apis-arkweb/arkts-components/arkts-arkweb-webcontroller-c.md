# WebController

Defines the Web controller.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [WebviewController](ohos.web.webview.webview.WebviewController)

<!--Device-unnamed-declare class WebController--><!--Device-unnamed-declare class WebController-End-->

**System capability:** SystemCapability.Web.Webview.Core

## accessBackward

```TypeScript
accessBackward(): boolean
```

Checks whether the web page can go back.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [accessBackward](ohos.web.webview.webview.WebviewController#accessBackward)

<!--Device-WebController-accessBackward(): boolean--><!--Device-WebController-accessBackward(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the web page can go back. |

## accessForward

```TypeScript
accessForward(): boolean
```

Checks whether the web page can go forward.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [accessForward](ohos.web.webview.webview.WebviewController#accessForward)

<!--Device-WebController-accessForward(): boolean--><!--Device-WebController-accessForward(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## accessStep

```TypeScript
accessStep(step: number): boolean
```

Checks whether the web page can go back or forward the given number of steps.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [accessStep](ohos.web.webview.webview.WebviewController#accessStep)

<!--Device-WebController-accessStep(step: number): boolean--><!--Device-WebController-accessStep(step: number): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| step | number | Yes | The number of steps. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## backward

```TypeScript
backward()
```

Goes back in the history of the web page.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [backward](ohos.web.webview.webview.WebviewController#backward)

<!--Device-WebController-backward()--><!--Device-WebController-backward()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## clearHistory

```TypeScript
clearHistory(): void
```

Clears the history in the Web.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [clearHistory](ohos.web.webview.webview.WebviewController#clearHistory)

<!--Device-WebController-clearHistory(): void--><!--Device-WebController-clearHistory(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

Constructor.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [constructor](ohos.web.webview.webview.WebviewController#constructor)

<!--Device-WebController-constructor()--><!--Device-WebController-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## deleteJavaScriptRegister

```TypeScript
deleteJavaScriptRegister(name: string)
```

Deletes a registered JavaScript object with given name.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [deleteJavaScriptRegister](ohos.web.webview.webview.WebviewController#deleteJavaScriptRegister)

<!--Device-WebController-deleteJavaScriptRegister(name: string)--><!--Device-WebController-deleteJavaScriptRegister(name: string)-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | The name of a registered JavaScript object to be deleted. |

## forward

```TypeScript
forward()
```

Goes forward in the history of the web page.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [forward](ohos.web.webview.webview.WebviewController#forward)

<!--Device-WebController-forward()--><!--Device-WebController-forward()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## getCookieManager

```TypeScript
getCookieManager(): WebCookie
```

Gets network cookie manager

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 9

**Substitutes:** [WebCookieManager](../arkts-apis/arkts-arkweb-webview-webcookiemanager-c.md#WebCookieManager)

<!--Device-WebController-getCookieManager(): WebCookie--><!--Device-WebController-getCookieManager(): WebCookie-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [WebCookie](arkts-arkweb-webcookie-c.md) |  |

## getHitTest

```TypeScript
getHitTest(): HitTestType
```

Gets the type of HitTest.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [getHitTest](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#getHitTest)

<!--Device-WebController-getHitTest(): HitTestType--><!--Device-WebController-getHitTest(): HitTestType-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [HitTestType](arkts-arkweb-hittesttype-e.md) | The type of HitTest. |

## loadData

```TypeScript
loadData(options: { data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string })
```

Loads the data or URL.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [loadData](ohos.web.webview.webview.WebviewController#loadData)

<!--Device-WebController-loadData(options: { data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string })--><!--Device-WebController-loadData(options: { data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string })-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | { data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string } | Yes | The options with the data or URL and other information. |

## loadUrl

```TypeScript
loadUrl(options: { url: string | Resource, headers?: Array<Header> })
```

Loads the given URL.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [loadUrl](ohos.web.webview.webview.WebviewController#loadUrl)

<!--Device-WebController-loadUrl(options: { url: string | Resource, headers?: Array<Header> })--><!--Device-WebController-loadUrl(options: { url: string | Resource, headers?: Array<Header> })-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | { url: string \| Resource, headers?: Array&lt;[Header](arkts-arkweb-header-i.md)&gt; } | Yes | The options with the URL and other information. |

## onActive

```TypeScript
onActive(): void
```

Called when the **Web** component enters the active state.This API is supported since API version 8 and deprecated since API version 9. You are advised to use  
[onActive&lt;sup&gt;9+&lt;/sup&gt;](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#onActive) instead.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [onActive](ohos.web.webview.webview.WebviewController#onActive)

<!--Device-WebController-onActive(): void--><!--Device-WebController-onActive(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## onInactive

```TypeScript
onInactive(): void
```

Called when the **Web** component enters the inactive state.This API is supported since API version 8 and deprecated since API version 9. You are advised to use  
[onInactive&lt;sup&gt;9+&lt;/sup&gt;](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#onInactive) instead.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [onInactive](ohos.web.webview.webview.WebviewController#onInactive)

<!--Device-WebController-onInactive(): void--><!--Device-WebController-onInactive(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## refresh

```TypeScript
refresh()
```

refreshes the current URL.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [refresh](ohos.web.webview.webview.WebviewController#refresh)

<!--Device-WebController-refresh()--><!--Device-WebController-refresh()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## registerJavaScriptProxy

```TypeScript
registerJavaScriptProxy(options: { object: object, name: string, methodList: Array<string> })
```

Registers the JavaScript object and method list.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [registerJavaScriptProxy](ohos.web.webview.webview.WebviewController#registerJavaScriptProxy)

<!--Device-WebController-registerJavaScriptProxy(options: { object: object, name: string, methodList: Array<string> })--><!--Device-WebController-registerJavaScriptProxy(options: { object: object, name: string, methodList: Array<string> })-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | { object: object, name: string, methodList: Array&lt;string&gt; } | Yes | The option with the JavaScript object and method list. |

## requestFocus

```TypeScript
requestFocus()
```

Gets the request focus.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [requestFocus](ohos.web.webview.webview.WebviewController#requestFocus)

<!--Device-WebController-requestFocus()--><!--Device-WebController-requestFocus()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## runJavaScript

```TypeScript
runJavaScript(options: { script: string, callback?: (result: string) => void })
```

Asynchronously execute JavaScript in the context of the currently displayed page.The result of the script execution will be returned through an asynchronous callback.This method must be used on the UI thread, and the callback will also be invoked on the UI thread.&lt;p&gt;&lt;strong&gt;API Note&lt;/strong&gt;:&lt;br&gt;The state of JavaScript is no longer persisted across navigations like loadUrl.For example, global variables and functions defined before calling loadUrl will not exist in the loaded page.It is recommended that applications use registerJavaScriptProxy to ensure that the JavaScript state can be persisted across page navigations.&lt;p&gt;

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [runJavaScript](ohos.web.webview.webview.WebviewController#runJavaScript)

<!--Device-WebController-runJavaScript(options: { script: string, callback?: (result: string) => void })--><!--Device-WebController-runJavaScript(options: { script: string, callback?: (result: string) => void })-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | { script: string, callback?: (result: string) =&gt; void } | Yes | The options with a piece of code and a callback. |

## stop

```TypeScript
stop()
```

Stops the current load.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [stop](ohos.web.webview.webview.WebviewController#stop)

<!--Device-WebController-stop()--><!--Device-WebController-stop()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## zoom

```TypeScript
zoom(factor: number): void
```

Let the Web zoom by.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [zoom](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#zoom)

<!--Device-WebController-zoom(factor: number): void--><!--Device-WebController-zoom(factor: number): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factor | number | Yes | The zoom factor. |

