# AtomicServiceWebController

Implements an **AtomicServiceWebController** object for controlling the behavior of the **AtomicServiceWeb** component. An **AtomicServiceWebController** can control only one **AtomicServiceWeb** component, and the APIs on the **AtomicServiceWebController** can be called only after it has been bound to the target **AtomicServiceWeb** component.

**Since:** 12

<!--Device-unnamed-export declare class AtomicServiceWebController--><!--Device-unnamed-export declare class AtomicServiceWebController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## accessBackward

```TypeScript
accessBackward(): boolean
```

Checks whether going to the previous page can be performed on this page.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceWebController-accessBackward(): boolean--><!--Device-AtomicServiceWebController-accessBackward(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## accessForward

```TypeScript
accessForward(): boolean
```

Checks whether going to the next page can be performed on this page.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceWebController-accessForward(): boolean--><!--Device-AtomicServiceWebController-accessForward(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## accessStep

```TypeScript
accessStep(step: number): boolean
```

Checks whether this page can navigate forward or backward by the specified number of steps.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceWebController-accessStep(step: number): boolean--><!--Device-AtomicServiceWebController-accessStep(step: number): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| step | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## backward

```TypeScript
backward(): void
```

Moves to the previous page based on the history stack. This API is generally used together with [accessBackward](#accessbackward).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceWebController-backward(): void--><!--Device-AtomicServiceWebController-backward(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## forward

```TypeScript
forward(): void
```

Moves to the next page based on the history stack. This API is generally used together with [accessForward](#accessforward).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceWebController-forward(): void--><!--Device-AtomicServiceWebController-forward(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## getCustomUserAgent

```TypeScript
getCustomUserAgent(): string
```

Obtains a custom user agent.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceWebController-getCustomUserAgent(): string--><!--Device-AtomicServiceWebController-getCustomUserAgent(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## getUserAgent

```TypeScript
getUserAgent(): string
```

Obtains the default user agent of this web page.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceWebController-getUserAgent(): string--><!--Device-AtomicServiceWebController-getUserAgent(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## loadUrl

```TypeScript
loadUrl(url: string | Resource, headers?: Array<WebHeader>): void
```

Loads a specified URL.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceWebController-loadUrl(url: string | Resource, headers?: Array<WebHeader>): void--><!--Device-AtomicServiceWebController-loadUrl(url: string | Resource, headers?: Array<WebHeader>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |
| headers | Array&lt;[WebHeader](arkts-arkui-atomicservice-atomicserviceweb-webheader-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-incorrect-url-format) |
| [17100003](../../apis-arkweb/errorcode-webview.md#17100003-incorrect-resource-path) |

## refresh

```TypeScript
refresh(): void
```

Refreshes the web page.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceWebController-refresh(): void--><!--Device-AtomicServiceWebController-refresh(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## setCustomUserAgent

```TypeScript
setCustomUserAgent(userAgent: string): void
```

Sets a custom user agent, which will override the default user agent. Set the user agent in the **onControllerAttached** callback to ensure that it takes effect. For details about the setting, see the example. Avoid setting the user agent in **onLoadIntercept**. Otherwise, the setting may fail occasionally. > **NOTE：**> > If a URL is set for the **Web** component **src** and **UserAgent** is not set in the **onControllerAttached** > callback, calling **setCustomUserAgent** may cause mismatches between the loaded page and the intended user > agent.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceWebController-setCustomUserAgent(userAgent: string): void--><!--Device-AtomicServiceWebController-setCustomUserAgent(userAgent: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userAgent | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |
