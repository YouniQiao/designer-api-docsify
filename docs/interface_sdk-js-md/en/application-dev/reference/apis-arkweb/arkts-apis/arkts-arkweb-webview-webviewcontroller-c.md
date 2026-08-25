# WebviewController

WebviewController is the core controller for various behaviors of the **Web** component, providing extensive functions such as page loading and navigation control, JavaScript interaction, lifecycle management, scroll control, page zoom and content search, message port communication, and cache and certificate management. A WebviewController object can control only one **Web** component, and methods on WebviewController (except static methods) can be called only after the **Web** component is bound to WebviewController.

**Since:** 9

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from 'kits/@kit.ArkWeb';
```

## accessBackward

```TypeScript
accessBackward(): boolean
```

Checks whether going to the previous page can be performed on the current page.You can use [getBackForwardEntries](#getbackforwardentries) to obtain the historical information list of the current WebView and use [accessStep](#accessstep) to determine whether to move forward or backward based on the specified number of steps.

> **NOTE：**&gt;
> If [setCustomUserAgent](#setcustomuseragent) is called when the **Web**
> component is loaded for the first time, the value of **accessBackward** may be **false** when there are
> multiple historical entries. That is, there is no backward entry. You are advised to call the
> **setCustomUserAgent** method to set a user agent before using **loadUrl** to load a specific page.&gt;
> Causes: When the **Web** component is loaded for the first time, calling
> [setCustomUserAgent](#setcustomuseragent) causes the component to reload and
> retain the initial history entry. Then the new entry replaces the initial history entry and no new history
> entry is generated. As a result, the value of **accessBackward** is false.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## accessForward

```TypeScript
accessForward(): boolean
```

Checks whether going to the next page can be performed on the current page.You can use [getBackForwardEntries](#getbackforwardentries) to obtain the historical information list of the current WebView and use [accessStep](#accessstep) to determine whether to move forward or backward based on the specified number of steps.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## accessStep

```TypeScript
accessStep(step: number): boolean
```

Checks whether a specific number of steps forward or backward can be performed on the current page.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

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
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## addIntelligentTrackingPreventionBypassingList

```TypeScript
static addIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void
```

Adds a list of domain names that bypass intelligent tracking prevention.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hostList | Array & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## avoidVisibleViewportBottom

```TypeScript
avoidVisibleViewportBottom(avoidHeight: number): void
```

Sets the bottom avoidance height of the visible viewport on the web page.

> **NOTE：**&gt;
> - The valid value range of **avoidHeight** is [0, height of the **Web** component]. Values outside this range
> are adjusted to the nearest boundary.&gt;
> - When a non-zero value is specified for **avoidHeight**, the position and size of the **Web** component remain
> unchanged, but the visible viewport shift upwards by the specified height, lifting the web page content by the
> **avoidHeight**. This API is used to customize the avoidance area at the bottom of a web page. It is not
> recommended that this API be used when the editable area of the web page is tapped to pull up the keyboard. If
> this API is used in this scenario, the keyboard avoidance mode is set to **OVERLAYS_CONTENT**.&gt;
> - When the height of this API is set to **0**, the web page content can be restored, and the keyboard avoidance
> mode is specified by keyboardAvoidMode().

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| avoidHeight | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## backOrForward

```TypeScript
backOrForward(step: number): void
```

Performs a specific number of steps forward or backward on the current page based on the history stack. No redirection will be performed if the corresponding page does not exist in the history stack.Because the previously loaded web pages are used for the operation, no page reloading is involved.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| step | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## backward

```TypeScript
backward(): void
```

Moves to the previous page based on the history stack. This API is generally used together with [accessBackward](#accessbackward).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## clearBlanklessLoadingCache

```TypeScript
static clearBlanklessLoadingCache(keys?: Array<string>) : void
```

Clears the blankless loading cache of the page with a specified key value.In an applet or web application, when the content changes significantly during page loading, an obvious scene change may occur. If you are concerned about this change, you can use this API to clear the page cache.

> **NOTE：**&gt;
> - After the page is cleared, the optimization effect appears when the page is loaded for the third time.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keys | Array & lt;string & gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## clearClientAuthenticationCache

```TypeScript
clearClientAuthenticationCache(): void
```

Clears the user operation corresponding to the client certificate request event recorded by the **Web** component.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## clearHistory

```TypeScript
clearHistory(): void
```

Clears the browsing history. You are not advised to call **clearHistory()** in **onErrorReceive()** and **onPageBegin()**. Otherwise, abnormal exit occurs.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## clearHostIP

```TypeScript
static clearHostIP(hostName: string): void
```

Clears the IP address of a specified host after domain name resolution.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hostName | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## clearIntelligentTrackingPreventionBypassingList

```TypeScript
static clearIntelligentTrackingPreventionBypassingList(): void
```

Deletes all domain names from the list of domain names added through the **addIntelligentTrackingPreventionBypassingList** API.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## clearMatches

```TypeScript
clearMatches(): void
```

Clears the matches found through [searchAllAsync](#searchallasync).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## clearPrefetchedResource

```TypeScript
static clearPrefetchedResource(cacheKeyList: Array<string>): void
```

Clears the cache of prefetched resources based on the specified cache key list. The cache key in the input parameter must be the prefetched resource cache key specified by [prefetchResource](#prefetchresource).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| cacheKeyList | Array & lt;string & gt; | Yes |

## clearServiceWorkerWebSchemeHandler

```TypeScript
static clearServiceWorkerWebSchemeHandler(): void
```

Clears all WebSchemeHandlers that are set in the application and used to intercept ServiceWorker.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

## clearSslCache

```TypeScript
clearSslCache(): void
```

Clears the user operation corresponding to the SSL certificate error event recorded by the **Web** component.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## clearWebSchemeHandler

```TypeScript
clearWebSchemeHandler(): void
```

Clears all WebSchemeHandlers set for the **Web** component.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## closeAllMediaPresentations

```TypeScript
closeAllMediaPresentations(): void
```

Closes all full-screen videos on a web page.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## closeCamera

```TypeScript
closeCamera(): void
```

Disables the camera capture of the current web page.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## constructor

```TypeScript
constructor(webTag?: string)
```

Constructs a **WebviewController** object.

> **NOTE：**&gt;
> - No parameter: new webview.WebviewController() indicates an empty constructor. No parameter is required when
> the C API is not used.&gt;
> - Parameter is a valid string: new webview.WebviewController("xxx"), used for developers to distinguish
> multiple instances and call methods under the corresponding instance.&gt;
> - Empty parameter: new webview.WebviewController("") or new webview.WebviewController(undefined). In this
> scenario, the parameter is meaningless and cannot distinguish multiple instances. **undefined** is returned
> directly, and developers need to check whether the return value is normal.&gt;
> After the **Web** component is destroyed, it is unbound from WebViewController. Subsequently, calling non-
> static methods of WebviewController will throw a
> [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component)
> exception. Pay attention to the call timing and catch exceptions to prevent abnormal process exit.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| webTag | string | No |

## createPdf

```TypeScript
createPdf(configuration: PdfConfiguration, callback: AsyncCallback<PdfData>): void
```

Obtains the data stream of a specified web page using an asynchronous callback.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| configuration | [PdfConfiguration](arkts-arkweb-webview-pdfconfiguration-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PdfData](arkts-arkweb-webview-pdfdata-c.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## createPdf

```TypeScript
createPdf(configuration: PdfConfiguration): Promise<PdfData>
```

Obtains the data stream of a specified web page using a promise.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| configuration | [PdfConfiguration](arkts-arkweb-webview-pdfconfiguration-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PdfData](arkts-arkweb-webview-pdfdata-c.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## createWebMessagePorts

```TypeScript
createWebMessagePorts(isExtentionType?: boolean): Array<WebMessagePort>
```

Creates web message ports.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isExtentionType](arkts-arkweb-webview-webmessageport-i.md) | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[WebMessagePort](arkts-arkweb-webview-webmessageport-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createWebPrintDocumentAdapter

```TypeScript
createWebPrintDocumentAdapter(jobName: string): print.PrintDocumentAdapter
```

Creates a **PrintDocumentAdapter** instance to provide content for printing.

**Since:** 11

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [jobName](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-print-printjobdata-i.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| print.PrintDocumentAdapter |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## customizeSchemes

```TypeScript
static customizeSchemes(schemes: Array<WebCustomScheme>): void
```

Grants the cross-domain request and fetch request permissions for custom protocol URLs to the web kernel. When the Web performs a cross-domain fetch of a custom protocol URL, the fetch request can be intercepted by the [onInterceptRequest](../arkts-components/arkts-arkweb-web-attribute.md#oninterceptrequest) event API, so that developers can further process the request. It is recommended to call this API before any **Web** component is initialized.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| schemes | Array&lt;[WebCustomScheme](arkts-arkweb-webview-webcustomscheme-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100020](../errorcode-webview.md#17100020-failed-to-register-custom-schemes) |

## customizeSchemes

```TypeScript
static customizeSchemes(schemes: Array<WebCustomScheme>, lazyInitWebEngine: boolean): void
```

Grants the cross-domain request and fetch request permissions for custom protocol URLs to the web kernel. When the Web performs a cross-domain fetch of a custom protocol URL, the fetch request can be intercepted by the [onInterceptRequest](../arkts-components/arkts-arkweb-web-attribute.md#oninterceptrequest) event API, so that developers can further process the request. It is recommended to call this API before any **Web** component is initialized.

**Since:** 21

**Atomic service API:** This API can be used in atomic services since API version 21.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| schemes | Array&lt;[WebCustomScheme](arkts-arkweb-webview-webcustomscheme-i.md)&gt; | Yes |
| lazyInitWebEngine | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17100020](../errorcode-webview.md#17100020-failed-to-register-custom-schemes) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## deleteJavaScriptRegister

```TypeScript
deleteJavaScriptRegister(name: string): void
```

Deletes a JavaScript object with the specified name on the application side that is registered with the window using [registerJavaScriptProxy](#registerjavascriptproxy) or [javaScriptProxy](../arkts-components/arkts-arkweb-web-attribute.md#javascriptproxy). The deletion takes effect after the page is reloaded.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |
| [17100008](../errorcode-webview.md#17100008-deleting-a-javascriptproxy-that-does-not-exist) |

## enableAdsBlock

```TypeScript
enableAdsBlock(enable: boolean): void
```

Enables ad blocking.

> **NOTE：**&gt;
> - The ad blocking feature works only for the release-type application, not the debug-type application.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## enableAdvancedSecurityMode

```TypeScript
static enableAdvancedSecurityMode(securityParams: SecurityParams): void
```

Disables specific web engine capabilities by configuring security feature options to reduce the attack surface. Typical use cases include: apps with high security requirements (such as financial and government apps) should enable advanced security mode to disable unnecessary web engine capabilities.

> **NOTE：**&gt;
> - This API is a global static API. It only needs to be called once during the entire app lifecycle and does not
> need to be called repeatedly.&gt;
> - It must be called before [initializeWebEngine()](#initializewebengine).
> Otherwise, the setting does not take effect.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| securityParams | [SecurityParams](arkts-arkweb-webview-securityparams-i.md) | Yes |

## enableBackForwardCache

```TypeScript
static enableBackForwardCache(features: BackForwardCacheSupportedFeatures): void
```

Enables the back-forward cache of a **Web** component. You can specify whether to add a specific page to the back -forward cache.This API must be called before [initializeWebEngine()](#initializewebengine) initializes the kernel.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| features | [BackForwardCacheSupportedFeatures](arkts-arkweb-webview-backforwardcachesupportedfeatures-c.md) | Yes |

## enableIntelligentTrackingPrevention

```TypeScript
enableIntelligentTrackingPrevention(enable: boolean): void
```

Enables intelligent tracking prevention.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## enablePrivateNetworkAccess

```TypeScript
static enablePrivateNetworkAccess(enable: boolean): void
```

Sets the private network access check feature.After this feature is enabled, the **Web** component performs CORS preflight on private network requests (such as requests for accessing local servers or intranet resources). It sends an OPTIONS preflight request to obtain explicit authorization from the target server and then transmits the actual data. Disabling this feature will skip the security check.

> **NOTE：**&gt;
> The private network access check feature currently takes effect mainly for Web Worker scenarios.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

## enableSafeBrowsing

```TypeScript
enableSafeBrowsing(enable: boolean): void
```

Enables the safe browsing feature. This feature is forcibly enabled and cannot be disabled for identified untrusted websites.By default, this feature does not take effect. OpenHarmony provides only the malicious website blocking web UI. The website risk detection and web UI display features are implemented by the vendor. You are advised to listen for [DidStartNavigation](https://gitcode.com/openharmony-tpc/chromium_src/blob/master/content/public/browser/web_contents_observer.h) and [DidRedirectNavigation](https://gitcode.com/openharmony-tpc/chromium_src/blob/master/content/public/browser/web_contents_observer.h) in **WebContentsObserver** for detection.

> **NOTE：**&gt;
> This API does not take effect.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## enableWholeWebPageDrawing

```TypeScript
static enableWholeWebPageDrawing(): void
```

Enables the full drawing capability for the web page. This API works only during **Web** component initialization.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

## executeAIPageCommand

```TypeScript
executeAIPageCommand(command: string): Promise<string>
```

Executes `AIPageCommand` asynchronously. This API uses a promise to return the result. The command type and command parameters are specified through the `command` parameter in JSON string format.

> **NOTE：**&gt;
> - The return format varies for different commands. For details, see
> [AIPageCommand](../../../reference/apis-arkweb/arkts-apis-webview-AIPageCommand.md) and
> [AIPageInteraction](../../../reference/apis-arkweb/arkts-apis-webview-AIPageInteraction.md).&gt;
> - When a command cannot be dispatched or has no result to return, the promise may return an empty string.&gt;
> - When the return value is not empty, it is a JSON string. The app can parse it with `JSON.parse` before use.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| command | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |
| [17100024](../errorcode-webview.md#17100024-aipagecommand-format-error) |

## forward

```TypeScript
forward(): void
```

Moves forward by one page in the history stack. Generally used together with [accessForward](#accessforward).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## getActiveWebEngineVersion

```TypeScript
static getActiveWebEngineVersion(): ArkWebEngineVersion
```

Obtains the current ArkWeb kernel version.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArkWebEngineVersion](arkts-arkweb-webview-arkwebengineversion-e.md) |

## getAttachState

```TypeScript
getAttachState(): ControllerAttachState
```

Checks whether the current **WebViewController** is bound to a **Web** component.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ControllerAttachState](arkts-arkweb-webview-controllerattachstate-e.md) |

## getBackForwardEntries

```TypeScript
getBackForwardEntries(): BackForwardList
```

Obtains the historical information list of the current WebView.

> **NOTE：**&gt;
> onLoadIntercept is triggered when the loading starts. At this time, no
> historical node is generated. Therefore, the historical stack obtained by calling **getBackForwardEntries** in
> **onLoadIntercept** does not include the page that is being loaded.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BackForwardList](arkts-arkweb-webview-backforwardlist-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## getBlanklessInfoWithKey

```TypeScript
getBlanklessInfoWithKey(key: string) : BlanklessInfo
```

Obtains the prediction information about blankless loading (for details, see [BlanklessInfo](arkts-arkweb-webview-blanklessinfo-i.md)) and starts to generate the loading transition frame. The application determines whether to enable blankless loading based on the information. This API must be used together with the [setBlanklessLoadingWithKey](#setblanklessloadingwithkey) API before the page loading API is triggered or in **onLoadIntercept**, and after the **WebViewController** is bound to the **Web** component.

> **NOTE：**&gt;
> - The default size of the persistent cache capacity is 30 MB (about 30 pages). You can set the cache capacity
> by calling [setBlanklessLoadingCacheCapacity](#setblanklessloadingcachecapacity)
> . For details, see the description of this API. When the maximum capacity is exceeded, the cache is updated
> based on the Least Recently Used (LRU) mechanism. The persistent cache data that has been stored for more than
> seven days is automatically cleared. After the cache is cleared, the optimization effect appears when the page
> is loaded for the third time.&gt;
> - If the snapshot similarity (**similarity** in [BlanklessInfo](arkts-arkweb-webview-blanklessinfo-i.md))
> is extremely low, check whether the **key** value is correct.&gt;
> - After this API is called, page loading snapshot detection and transition frame generation calculation are
> enabled, which generates certain resource overhead.&gt;
> - Blankless loading consumes certain resources, which depends on the resolution of the **Web** component. When
> the width and height of the resolution are respectively **w** and **h**, the peak memory usage increases by
> about **12 × w × h** B in the page-opening phase. After the page is opened, the memory is reclaimed, which does
> not affect the stable memory usage. When the size of the solid-state application cache is increased, the
> increased cache of each page is about **w × h/10** B and the cache is located in the application cache.&gt;
> - Add the **ohos.permission.INTERNET** and **ohos.permission.GET_NETWORK_INFO** permissions to **module.json5**
> . For details, see
> [Declaring Permissions in the Configuration File](../../../security/AccessToken/declare-permissions.md#declaring-permissions-in-the-configuration-file).

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BlanklessInfo](arkts-arkweb-webview-blanklessinfo-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## getCertificate

```TypeScript
getCertificate(): Promise<Array<cert.X509Cert>>
```

Obtains the certificate information of this website. When the **Web** component is used to load an HTTPS website, SSL certificate verification is performed. This API uses a promise to return the [X.509 certificate](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-x509cert-i.md) of the current website.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;cert.X509Cert & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## getCertificate

```TypeScript
getCertificate(callback: AsyncCallback<Array<cert.X509Cert>>): void
```

Obtains the certificate information of the current website. When the **Web** component is used to load an HTTPS website, SSL certificate verification is performed. This API uses an asynchronous callback to return the X.509 certificate (for the X509Cert certificate type definition, see [X509Cert](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-x509cert-i.md)) of the current website, so that developers can display the website certificate information.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;cert.X509Cert&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## getCustomUserAgent

```TypeScript
getCustomUserAgent(): string
```

Obtains a custom user agent.For details about the default **User-Agent**, see [Developing User-Agent](../../../web/web-default-userAgent.md).

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## getDefaultUserAgent

```TypeScript
static getDefaultUserAgent(): string
```

Obtains the default user agent.This API can be called only in the UI thread.For details about the default **User-Agent**, see [Developing User-Agent](../../../web/web-default-userAgent.md).

**Since:** 14

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getErrorPageEnabled

```TypeScript
getErrorPageEnabled(): boolean
```

Queries whether the default error page is enabled.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## getFavicon

```TypeScript
getFavicon(): image.PixelMap
```

Obtains the favicon of this page.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| image.PixelMap |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## getHitTest

```TypeScript
getHitTest(): WebHitTestType
```

Obtains the element type of the area being clicked.

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [getLastHitTest](#getlasthittest)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WebHitTestType](arkts-arkweb-webview-webhittesttype-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## getHitTestValue

```TypeScript
getHitTestValue(): HitTestValue
```

Obtains the element information of the area being clicked.

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [getLastHitTest](#getlasthittest)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [HitTestValue](arkts-arkweb-webview-hittestvalue-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## getLastHitTest

```TypeScript
getLastHitTest(): HitTestValue
```

Obtains the element information of the area being clicked last time.

**Since:** 18

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [HitTestValue](arkts-arkweb-webview-hittestvalue-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## getLastJavascriptProxyCallingFrameUrl

```TypeScript
getLastJavascriptProxyCallingFrameUrl(): string
```

Injects a JavaScript object into the window object through [registerJavaScriptProxy](#registerjavascriptproxy) or [javaScriptProxy](../arkts-components/arkts-arkweb-web-attribute.md#javascriptproxy). This API obtains the URL of the frame that last called the injected object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## getMediaPlaybackState

```TypeScript
getMediaPlaybackState(): MediaPlaybackState
```

Queries the audio and video playback status of the current web page.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MediaPlaybackState](arkts-arkweb-webview-mediaplaybackstate-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## getOriginalUrl

```TypeScript
getOriginalUrl(): string
```

Obtains the original URL of the current page.Risk warning: If you want to obtain the URL for JavaScriptProxy communication API authentication, use [getLastJavascriptProxyCallingFrameUrl&lt;sup&gt;12+&lt;/sup&gt;](#getlastjavascriptproxycallingframeurl).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## getPageHeight

```TypeScript
getPageHeight(): number
```

Obtains the height of this web page. For details, see [Obtaining the Web Page Content Height](../../../web/web-getpage-height.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## getPageOffset

```TypeScript
getPageOffset(): ScrollOffset
```

Obtains the current scrolling offset of the web page (excluding the over-scrolling offset).

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ScrollOffset](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-scrolloffset-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## getPrintBackground

```TypeScript
getPrintBackground(): boolean
```

Obtains whether the web page background is printed.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## getProgress

```TypeScript
getProgress() : number
```

Obtains the loading progress of the current web page.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## getRenderProcessMode

```TypeScript
static getRenderProcessMode(): RenderProcessMode
```

Obtains the ArkWeb render subprocess mode.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RenderProcessMode](arkts-arkweb-webview-renderprocessmode-e.md) |

## getScrollable

```TypeScript
getScrollable(): boolean
```

Obtains whether this web page is scrollable.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## getScrollOffset

```TypeScript
getScrollOffset(): ScrollOffset
```

Obtains the current scrolling offset (including the over-scrolling offset) of the web page.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ScrollOffset](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-scrolloffset-i.md) |

## getSecurityLevel

```TypeScript
getSecurityLevel(): SecurityLevel
```

Obtains the security level of this web page.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SecurityLevel](../../apis-arkdata/arkts-apis/arkts-arkdata-distributedkvstore-securitylevel-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## getSiteIsolationMode

```TypeScript
static getSiteIsolationMode(): SiteIsolationMode
```

Queries the currently effective site isolation mode.

**Since:** 21

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SiteIsolationMode](arkts-arkweb-webview-siteisolationmode-e.md) |

## getSubframeErrorPageEnabled

```TypeScript
getSubframeErrorPageEnabled(): boolean
```

Queries whether the subframe error page feature is enabled.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## getSurfaceId

```TypeScript
getSurfaceId(): string
```

Obtains the ID of the surface corresponding to ArkWeb. The ID can be used to capture a screenshot of the web page.

> **NOTE：**&gt;
> This API is valid only when the **Web** component rendering mode is **ASYNC_RENDER**. The value of
> **getSurfaceId** can be obtained only after the **Web** component is initialized.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getTitle

```TypeScript
getTitle(): string
```

Obtains the title of the current web page.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## getUrl

```TypeScript
getUrl(): string
```

Obtains the URL of the current page.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## getUserAgent

```TypeScript
getUserAgent(): string
```

Obtains the default user agent of this web page.For details about the default **User-Agent**, see [Developing User-Agent](../../../web/web-default-userAgent.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## getUserAgentClientHintsEnabled

```TypeScript
static getUserAgentClientHintsEnabled(): boolean
```

Queries whether the User-Agent Client Hints feature is currently enabled.

**Since:** 24

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## getUserAgentMetadata

```TypeScript
getUserAgentMetadata(userAgent: string): UserAgentMetadata
```

Obtains the UserAgentMetadata information of a user agent.

**Since:** 24

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userAgent | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [UserAgentMetadata](arkts-arkweb-webview-useragentmetadata-c.md) |

## getWebId

```TypeScript
getWebId(): number
```

Obtains the index value of the **Web** component, which can be used for managing multiple **Web** components.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## hasImage

```TypeScript
hasImage(): Promise<boolean>
```

Checks whether this page contains images. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## hasImage

```TypeScript
hasImage(callback: AsyncCallback<boolean>): void
```

Checks whether this page contains images. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## initializeWebEngine

```TypeScript
static initializeWebEngine(): void
```

Loads the dynamic library file of the web engine through this API before the **Web** component is initialized, so as to improve startup performance. It also automatically preconnects to frequently visited websites in history.

> **NOTE：**&gt;
> - **initializeWebEngine** cannot be called in an asynchronous thread. Otherwise, the system breaks down.&gt;
> - **initializeWebEngine** takes effect globally and needs to be called only once in an application lifecycle.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

## injectOfflineResources

```TypeScript
injectOfflineResources(resourceMaps: Array<OfflineResourceMap>): void
```

Injects local offline resources to the memory cache to improve the initial page startup speed.Resources in the memory cache are automatically managed by the ArkWeb engine. When the injected resources are excessive and cause significant memory pressure, the engine will automatically release unused resources. It is advisable to avoid injecting a large number of resources into the memory cache.Under normal circumstances, the validity period of the resources is controlled by the provided Cache-Control or Expires response header, with a default validity period of 86,400 seconds, which is one day.The MIME type of the resources is configured through the provided Content-Type response header. The Content-Type must comply with standards; otherwise, the resources cannot be used correctly. For resources of type MODULE_JS, a valid MIME type must be provided. For other types, the MIME type is optional.Resources injected in this mode can be loaded only through HTML tags. If a **script** tag on the web page uses the **crossorigin** attribute, the **Cross-Origin** response header must be set in the **responseHeaders** parameter of the API. The value for this header should be **anonymous** or **use-credentials**.After **webview.WebviewController.SetRenderProcessMode(webview.RenderProcessMode.MULTIPLE)** is called, the application starts the multi-rendering process mode. This API does not take effect in this scenario.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resourceMaps | Array&lt;[OfflineResourceMap](arkts-arkweb-webview-offlineresourcemap-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |

## isActiveWebEngineEvergreen

```TypeScript
static isActiveWebEngineEvergreen(): boolean
```

Checks whether the system is using the evergreen kernel, that is, the latest kernel.

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isAdsBlockEnabled

```TypeScript
isAdsBlockEnabled(): boolean
```

Checks whether ad blocking is enabled.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## isAdsBlockEnabledForCurPage

```TypeScript
isAdsBlockEnabledForCurPage(): boolean
```

Checks whether ad blocking is enabled on this web page.After ads blocking is enabled for the **Web** component, this feature is enabled for all web pages by default. You can call [addAdsBlockDisallowedList](arkts-arkweb-webview-adsblockmanager-c.md#addadsblockdisallowedlist) to disable the feature for specific domains.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## isAutoPreconnectEnabled

```TypeScript
static isAutoPreconnectEnabled(): boolean
```

Queries the automatic preconnection status of the Web kernel.If the automatic preconnection status of the Web kernel is not set by using [setAutoPreconnect](#setautopreconnect), automatic preconnection is enabled by default, and **true** is returned.

**Since:** 21

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isIncognitoMode

```TypeScript
isIncognitoMode(): boolean
```

Checks whether this Webview is in incognito mode.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## isIntelligentTrackingPreventionEnabled

```TypeScript
isIntelligentTrackingPreventionEnabled(): boolean
```

Obtains whether the **Web** component has enabled intelligent tracking prevention.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## isPrivateNetworkAccessEnabled

```TypeScript
static isPrivateNetworkAccessEnabled(): boolean
```

Obtains whether the private network access check feature is enabled for the **Web** component.

> **NOTE：**&gt;
> The private network access check feature currently takes effect mainly for Web Worker scenarios.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isSafeBrowsingEnabled

```TypeScript
isSafeBrowsingEnabled(): boolean
```

Checks whether the safe browsing feature is enabled for this web page.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## loadData

```TypeScript
loadData(data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string): void
```

Loads specified data.When both **baseUrl** and **historyUrl** are empty:If **encoding** is not base64 (including null values), ASCII encoding is used for octets within the secure URL character range, and the standard %xx hexadecimal encoding of the URL is used for octets outside the secure URL character range.  
**data** must be encoded using Base64 or any hash (#) in the content must be encoded as %23. Otherwise, hash (#) is considered as the end of the content, and the remaining text is used as the document fragment identifier.

> **NOTE：**&gt;
> - To load a local image, you can assign a space to either **baseUrl** or **historyUrl**. For details, see the
> sample code.&gt;
> - In the scenario of loading a local image, **baseUrl** and **historyUrl** cannot be both empty. Otherwise, the
> image cannot be loaded.&gt;
> - If the rich text in HTML contains special characters such as hash (#), you are advised to set the values of
> **baseUrl** and **historyUrl** to spaces.&gt;
> - To load texts, you need to set
> `&lt;meta name="viewport" content="width=device-width, initial-scale=1.0" charset="utf-8"&gt;` to avoid inconsistent
> font sizes.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | string | Yes |
| mimeType | string | Yes |
| encoding | string | Yes |
| baseUrl | string | No |
| [historyUrl](arkts-arkweb-webview-historyitem-i.md) | string | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |

## loadUrl

```TypeScript
loadUrl(url: string | Resource, headers?: Array<WebHeader>): void
```

Loads a specified URL.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |
| headers | Array & lt;WebHeader & gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |
| [17100003](../errorcode-webview.md#17100003-incorrect-resource-path) |

## off('controllerAttachStateChange')

```TypeScript
off(type: 'controllerAttachStateChange', callback?: Callback<ControllerAttachState>): void
```

Deregisters the attach state event of **WebViewController**. After the deregistration, callback notifications will not be received.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'controllerAttachStateChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ControllerAttachState](arkts-arkweb-webview-controllerattachstate-e.md)&gt; | No |

## on('controllerAttachStateChange')

```TypeScript
on(type: 'controllerAttachStateChange', callback: Callback<ControllerAttachState>): void
```

Registers the attach state event of **WebViewController**, which obtains the attach state change notification through a callback.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'controllerAttachStateChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ControllerAttachState](arkts-arkweb-webview-controllerattachstate-e.md)&gt; | Yes |

## onActive

```TypeScript
onActive(): void
```

Called when the **Web** component enters the active state.The application can interact with the user while in the active foreground state, and it remains in this state until the focus is moved away from it due to some event (for example, an incoming call is received or the device screen is turned off).If the page was previously in the inactive state, the event listener registered through document.addEventListener ('visibilitychange',...) in the H5 page will be triggered, and document.visibilityState changes from "hidden" to"visible".

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## onCreateNativeMediaPlayer

```TypeScript
onCreateNativeMediaPlayer(callback: CreateNativeMediaPlayerCallback): void
```

Registers a callback function. After [enableNativeMediaPlayer](../arkts-components/arkts-arkweb-web-attribute.md#enablenativemediaplayer) is used to enable the app to take over web page media playback, the registered callback function is triggered when media is played on the web page.If the application does not take over media playback on the web page, this callback is not invoked.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [CreateNativeMediaPlayerCallback](arkts-arkweb-webview-createnativemediaplayercallback-t.md) | Yes |

## onInactive

```TypeScript
onInactive(): void
```

Called when the **Web** component enters the inactive state. You can implement the behavior to perform after the application loses focus.When this API is called, any content that can be safely paused, such as animations and geographical locations, is paused as much as possible. However, the JavaScript is not paused. To pause the JavaScript globally, use [pauseAllTimers](#pausealltimers). To reactivate the **Web** component, use [onActive](#onactive).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## pageDown

```TypeScript
pageDown(bottom: boolean): void
```

Scrolls the page down by half the viewport or jumps to the bottom of the page.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bottom | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## pageUp

```TypeScript
pageUp(top: boolean): void
```

Scrolls the page up by half the viewport or jumps to the top of the page.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| top | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## pauseAllMedia

```TypeScript
pauseAllMedia(): void
```

Pauses all audio and video on a web page.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## pauseAllTimers

```TypeScript
static pauseAllTimers(): void
```

Pauses all WebView timers. While the timers are paused, timer operations such as setInterval and setTimeout in the web page are suspended. It is recommended to pause timers when the app enters the background and resume them when the app returns to the foreground, so as to save resources. This API can be used in pair with [resumeAllTimers](#resumealltimers)() to avoid timer state confusion.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## pauseMicrophone

```TypeScript
pauseMicrophone(): void
```

Pauses microphone capture on the current web page.

> **NOTE：**&gt;
> Differences from resumeMicrophone and stopMicrophone:&gt;
> pauseMicrophone only pauses microphone capture and can be restored through resumeMicrophone; stopMicrophone
> stops capture and releases resources.

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## postMessage

```TypeScript
postMessage(name: string, ports: Array<WebMessagePort>, uri: string): void
```

Sends a web message to an HTML window.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| ports | Array&lt;[WebMessagePort](arkts-arkweb-webview-webmessageport-i.md)&gt; | Yes |
| uri | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## postUrl

```TypeScript
postUrl(url: string, postData: ArrayBuffer): void
```

Loads a URL with postData using the "POST" method. If the URL is not a network URL, the [loadUrl](#loadurl) method is used to load the URL, and the postData parameter is ignored.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| postData | ArrayBuffer | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |

## precompileJavaScript

```TypeScript
precompileJavaScript(url: string, script: string | Uint8Array, cacheOptions: CacheOptions): Promise<number>
```

Precompiles JavaScript to generate the bytecode cache or update the existing bytecode cache based on the provided parameters.The API determines whether to update the existing bytecode cache based on the provided file information, E-Tag response header, and Last-Modified response header.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| script | string \| Uint8Array | Yes |
| cacheOptions | [CacheOptions](arkts-arkweb-webview-cacheoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## prefetchPage

```TypeScript
prefetchPage(url: string, additionalHeaders?: Array<WebHeader>): void
```

Prefetches resources in the background for a page that is likely to be accessed in the near future, without executing the page JavaScript code or presenting the page. This can significantly reduce the load time for the prefetched page.

> **NOTE：**&gt;
> - The downloaded page resources are cached for about five minutes. After this period, the **Web** component
> automatically releases them.&gt;
> - **prefetchPage** can also normally prefetch 302 redirect pages.&gt;
> - When **prefetchPage** is executed first and then the page is loaded, the prefetched resources are loaded
> directly from the cache.&gt;
> - When multiple URLs are prefetched consecutively with **prefetchPage**, only the first one takes effect.&gt;
> - **prefetchPage** has a time limit. Multiple prefetches cannot be performed within 500 ms.&gt;
> - **prefetchPage** caches all resources except those with the Cache-Control: no-store header. If a Vary
> response header or Cache-Control: no-store header exists, or the downloaded page resources have been cached for
> more than five minutes, the resources are revalidated before use.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| additionalHeaders | Array & lt;WebHeader & gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |

## prefetchPage

```TypeScript
prefetchPage(url: string, additionalHeaders?: Array<WebHeader>, prefetchOptions?: PrefetchOptions): void
```

Prefetches resources in the background for a page that is likely to be accessed in the near future, without executing the page JavaScript code or presenting the page. This can significantly reduce the load time for the prefetched page.

> **NOTE：**&gt;
> - The downloaded page resources are cached for about five minutes. After this period, the **Web** component
> automatically releases them.&gt;
> - **prefetchPage** can also normally prefetch 302 redirect pages.&gt;
> - When **prefetchPage** is executed first and then the page is loaded, the prefetched resources are loaded
> directly from the cache.&gt;
> - **prefetchPage** caches all resources except those with the Cache-Control: no-store header. If a Vary
> response header or Cache-Control: no-store header exists, or the downloaded page resources have been cached for
> more than five minutes, the resources are revalidated before use.

**Since:** 21

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| additionalHeaders | Array & lt;WebHeader & gt; | No |
| prefetchOptions | [PrefetchOptions](arkts-arkweb-webview-prefetchoptions-c.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |

## prefetchResource

```TypeScript
static prefetchResource(request: RequestInfo, additionalHeaders?: Array<WebHeader>, cacheKey?: string,
                            cacheValidTime?: number): void
```

Prefetches resource requests based on specified request information and additional HTTP request headers, saves them to the memory cache, and specifies the cache key and validity period to accelerate loading. Currently, only POST requests with Content-Type of application/x-www-form-urlencoded are supported. A maximum of six POST requests can be prefetched. To prefetch a seventh one, use [clearPrefetchedResource](#clearprefetchedresource) to clear unnecessary POST request caches. Otherwise, the earliest prefetched POST cache is automatically cleared. To use the prefetched resource cache, developers need to add the key-value pair "ArkWebPostCacheKey" to the request header of the actual POST request, with the value being the cacheKey of the corresponding cache.Resources in the memory cache are automatically managed by the kernel. When too many resources are injected, causing excessive memory pressure, the kernel automatically releases unused resources. However, injecting a large number of resources into the memory cache should still be avoided.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [RequestInfo](../../apis-ability-kit/arkts-apis/arkts-ability-dialogrequest-requestinfo-i.md) | Yes |
| additionalHeaders | Array & lt;WebHeader & gt; | No |
| cacheKey | string | No |
| cacheValidTime | number | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |

## prepareForPageLoad

```TypeScript
static prepareForPageLoad(url: string, preconnectable: boolean, numSockets: number): void
```

Preconnects to a URL. Call this API before loading the URL. It only performs DNS resolution and socket connection for the URL, without fetching the main resource or sub-resources.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| preconnectable | boolean | Yes |
| numSockets | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |
| [17100013](../errorcode-webview.md#17100013-invalid-number-of-sockets-during-preconnection) |

## refresh

```TypeScript
refresh(): void
```

Called when the **Web** component refreshes the web page.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## refresh

```TypeScript
refresh(ignoreCache: boolean): void
```

Notifies the **Web** component to refresh the web page. You can choose whether to ignore the cache refresh.

**Since:** 24

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ignoreCache | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## registerJavaScriptProxy

```TypeScript
registerJavaScriptProxy(jsObject: object, name: string, methodList: Array<string>,
        asyncMethodList?: Array<string>, permission?: string): void
```

Registers a proxy for interaction between the application and web pages loaded by the **Web** component. Registers a JavaScript object with the window. APIs of this object can then be invoked in the window.For the example, see [Invoking Application Functions on the Frontend Page](../../../web/web-in-page-app-function-invoking.md).

> **NOTE：**&gt;
> - The **registerJavaScriptProxy** API must be used together with the **deleteJavaScriptRegister** API to
> prevent memory leak.&gt;
> - It is recommended that **registerJavaScriptProxy** be used only with trusted URLs and over secure HTTPS
> connections. Injecting JavaScript objects into untrusted web components can expose your application to
> malicious attacks.&gt;
> - After **registerJavaScriptProxy** is called, the application exposes the registered JavaScript object to all
> page frames.&gt;
> - If a **registerJavaScriptProxy** is both registered in the synchronous and asynchronous lists, it is called
> asynchronously by default.&gt;
> - You should register **registerJavaScriptProxy** either in synchronous list or in asynchronous list.
> Otherwise, this API fails to be registered.&gt;
> - After the HTML5 thread submits an asynchronous JavaScript task to the ETS main thread, the HTML5 thread can
> continue to execute subsequent tasks without waiting for the task execution to complete and return a result. In
> this way, scenarios where the HTML5 thread is blocked due to number-running JavaScript tasks or a congested ETS
> thread can be effectively reduced. However, an asynchronous JavaScript task cannot return a value, and a task
> execution sequence cannot be ensured. Therefore, you should determine whether to use a synchronous or
> asynchronous function based on a specific scenario.&gt;
> - The injected object does not appear in JavaScript until the page is reloaded.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| jsObject | object | Yes |
| name | string | Yes |
| [methodList](../arkts-components/arkts-arkweb-javascriptproxy-i.md) | Array & lt;string & gt; | Yes |
| [asyncMethodList](../arkts-components/arkts-arkweb-javascriptproxy-i.md) | Array & lt;string & gt; | No |
| permission | string | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## removeAllCache

```TypeScript
static removeAllCache(clearRom: boolean): void
```

Removes all resource caches generated by Webview (including private mode) in the app.

**Since:** 18

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| clearRom | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## removeCache

```TypeScript
removeCache(clearRom: boolean): void
```

Removes all resource caches generated by Webview in the app.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| clearRom | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## removeIntelligentTrackingPreventionBypassingList

```TypeScript
static removeIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void
```

Deletes the domain names from the list of domain names added through the **addIntelligentTrackingPreventionBypassingList** API.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hostList | Array & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## requestFocus

```TypeScript
requestFocus(): void
```

Requests focus for the specified component.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## restoreWebState

```TypeScript
restoreWebState(state: Uint8Array) : void
```

Restores the page status history from the serialized data of the current WebView.If the value of **state** is too large, exceptions may occur. It is recommended that the page status history be not restored when the **state** value is greater than 512 KB.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| state | Uint8Array | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## resumeAllMedia

```TypeScript
resumeAllMedia(): void
```

Resumes the playback of the audio and video that are paused by the pauseAllMedia interface.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## resumeAllTimers

```TypeScript
static resumeAllTimers(): void
```

Resumes all timers that are paused from the **pauseAllTimers()** API.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## resumeMicrophone

```TypeScript
resumeMicrophone(): void
```

Resumes microphone capture on the current web page. Before using the microphone , add the **ohos.permission.MICROPHONE** permission to **module.json5**. For details about how to add the permission, see [Declaring Permissions in the Configuration File](../../../security/AccessToken/declare-permissions.md).

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## runJavaScript

```TypeScript
runJavaScript(script: string): Promise<string>
```

Executes a JavaScript script asynchronously in the context of the current page. This API uses a promise to return the script execution result. This method and its callback must be used on the UI thread.

> **NOTE：**&gt;
> - The JavaScript status is no longer retained during navigation operations (such as **loadUrl**). For example,
> the global variables and functions defined before **loadUrl** is called do not exist in the loaded page.&gt;
> - It is recommended that the app use **registerJavaScriptProxy** to ensure that the JavaScript status can be
> retained across page navigation.&gt;
> - Currently, passing objects is not supported. Passing structs is supported.&gt;
> - Executing asynchronous methods cannot obtain return values. Determine whether to use synchronous or
> asynchronous methods based on the specific context.&gt;
> - The string data type passed from the frontend page to the app side is treated as JSON-formatted data and
> needs to be deserialized with JSON.parse.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| script | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |
| [17100003](../errorcode-webview.md#17100003-incorrect-resource-path) |

## runJavaScript

```TypeScript
runJavaScript(script: string, callback: AsyncCallback<string>): void
```

Executes a JavaScript script asynchronously in the context of the current page. This API uses an asynchronous callback to return the script execution result. This method and its callback must be used on the UI thread.

> **NOTE：**&gt;
> - The JavaScript status is no longer retained during navigation operations (such as **loadUrl**). For example,
> the global variables and functions defined before **loadUrl** is called do not exist in the loaded page.&gt;
> - It is recommended that the app use **registerJavaScriptProxy** to ensure that the JavaScript status can be
> retained across page navigation.&gt;
> - Currently, passing objects is not supported. Passing structs is supported.&gt;
> - Executing asynchronous methods cannot obtain return values. Determine whether to use synchronous or
> asynchronous methods based on the specific context.&gt;
> - The string data type passed from the frontend page to the app side is treated as JSON-formatted data and
> needs to be deserialized with JSON.parse.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| script | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |
| [17100003](../errorcode-webview.md#17100003-incorrect-resource-path) |

## runJavaScriptExt

```TypeScript
runJavaScriptExt(script: string | ArrayBuffer): Promise<JsMessageExt>
```

Executes a JavaScript script asynchronously and returns the script execution result through a promise. **runJavaScriptExt** can be invoked only after **loadUrl** is executed, for example, in onPageEnd.

> **NOTE：**&gt;
> - The string data type passed from the frontend page to the app side is treated as JSON-formatted data and
> needs to be deserialized with JSON.parse.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| script | string \| ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[JsMessageExt](arkts-arkweb-webview-jsmessageext-c.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## runJavaScriptExt

```TypeScript
runJavaScriptExt(script: string | ArrayBuffer, callback: AsyncCallback<JsMessageExt>): void
```

Executes a JavaScript script. This API uses an asynchronous callback to return the script execution result. **runJavaScriptExt** can be invoked only after **loadUrl** is executed. For example, it can be invoked in **onPageEnd**.

> **NOTE：**&gt;
> - The string data type passed from the frontend page to the app side is treated as JSON-formatted data and
> needs to be deserialized with JSON.parse.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| script | string \| ArrayBuffer | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[JsMessageExt](arkts-arkweb-webview-jsmessageext-c.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## scrollBy

```TypeScript
scrollBy(deltaX: number, deltaY: number, duration?: number): void
```

Scrolls the page by the specified amount within a specified period.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deltaX | number | Yes |
| deltaY | number | Yes |
| duration | number | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## scrollByWithResult

```TypeScript
scrollByWithResult(deltaX: number, deltaY: number): boolean
```

Scrolls the page by the specified amount and returns value to indicate whether the scrolling is successful.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deltaX | number | Yes |
| deltaY | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## scrollTo

```TypeScript
scrollTo(x: number, y: number, duration?: number): void
```

Scrolls the page to the specified absolute position within a specified period.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |
| duration | number | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## searchAllAsync

```TypeScript
searchAllAsync(searchString: string): void
```

Searches the web page for content that matches the keyword specified by **'searchString'** and highlights the matches on the page. This API returns the result asynchronously through [onSearchResultReceive](../arkts-components/arkts-arkweb-web-attribute.md#onsearchresultreceive).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| searchString | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## searchNext

```TypeScript
searchNext(forward: boolean): void
```

Searches for and highlights the next match.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [forward](#forward) | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## serializeWebState

```TypeScript
serializeWebState(): Uint8Array
```

Serializes the page status history of the current WebView.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## setActiveWebEngineVersion

```TypeScript
static setActiveWebEngineVersion(engineVersion: ArkWebEngineVersion): void
```

Sets the ArkWeb kernel version. If the system does not support the specified version, the setting does not take effect and the system default kernel is used (see [Constraints](../../../web/web-component-overview.md#constraints)). This API is a global static API and must be executed before **initializeWebEngine** is called. If any **Web** component has been loaded, the setting does not take effect. Typical use case: when features or compatibility requirements of a specific kernel version are needed, you can switch to the corresponding kernel version.

> **NOTE：**&gt;
> - **setActiveWebEngineVersion** cannot be called in an asynchronous thread.&gt;
> - **setActiveWebEngineVersion** takes effect globally and needs to be called only once in an application
> lifecycle.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| engineVersion | [ArkWebEngineVersion](arkts-arkweb-webview-arkwebengineversion-e.md) | Yes |

## setAppCustomUserAgent

```TypeScript
static setAppCustomUserAgent(userAgent: string) : void
```

Sets the application-level custom user agent, which will overwrite the system user agent and take effect for all **Web** components in the application.If you need to set the application-level custom user agent, you are advised to call the **setAppCustomUserAgent** method to set the **User-Agent** before creating the **Web** component, and then create the **Web** component with the specified src or load the page using [loadUrl](#loadurl).For details about the default **User-Agent** definition, application scenarios, and API priorities, see [Developing User-Agent](../../../web/web-default-userAgent.md).

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userAgent | string | Yes |

## setAudioMuted

```TypeScript
setAudioMuted(mute: boolean): void
```

Mutes the web page. Typical use cases include: the app needs to control the web page volume (such as providing a mute switch), or needs to mute during background playback.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mute | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## setAutoPreconnect

```TypeScript
static setAutoPreconnect(enabled: boolean): void
```

Sets the automatic preconnection status of the Web kernel. If this API is not set, automatic preconnection is enabled by default.This API must be called before [initializeWebEngine()](#initializewebengine) initializes the kernel or a **Web** component is created. If any **Web** component has been loaded, the setting does not take effect.

**Since:** 21

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

## setBackForwardCacheOptions

```TypeScript
setBackForwardCacheOptions(options: BackForwardCacheOptions): void
```

Sets the back-forward cache options of the **Web** component.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [BackForwardCacheOptions](arkts-arkweb-webview-backforwardcacheoptions-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## setBlanklessLoadingCacheCapacity

```TypeScript
static setBlanklessLoadingCacheCapacity(capacity: number) : number
```

Sets the persistent cache capacity of the blankless loading solution and returns the value that takes effect. If the API is not explicitly called, the default cache capacity is 30 MB. When this limit is exceeded, transition frames that are not frequently used are eliminated.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| capacity | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## setBlanklessLoadingWithKey

```TypeScript
setBlanklessLoadingWithKey(key: string, is_start: boolean) : WebBlanklessErrorCode
```

Sets whether to enable blankless loading. This API must be used together with [getBlanklessInfoWithKey](#getblanklessinfowithkey).

> **NOTE：**&gt;
> - This API must be called after the page loading API is triggered. Other restrictions are the same as those of
> [getBlanklessInfoWithKey](#getblanklessinfowithkey).&gt;
> - The page must be loaded in the component that calls this API.&gt;
> - When the similarity is low, the system will deem the scene change too abrupt and frame insertion will fail.&gt;
> - Add the **ohos.permission.INTERNET** and **ohos.permission.GET_NETWORK_INFO** permissions to **module.json5**
> . For details, see
> [Declaring Permissions in the Configuration File](../../../security/AccessToken/declare-permissions.md#declaring-permissions-in-the-configuration-file).

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| is_start | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WebBlanklessErrorCode](arkts-arkweb-webview-webblanklesserrorcode-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## setBlanklessLoadingWithParams

```TypeScript
setBlanklessLoadingWithParams(key: string,
      param: BlanklessLoadingParam) : WebBlanklessErrorCode
```

Sets the configuration parameters for frame interpolation during blankless loading. This API must be used with [getBlanklessInfoWithKey](#getblanklessinfowithkey). Compared with [setBlanklessLoadingWithKey](#setblanklessloadingwithkey), this API supports more parameter settings for frame interpolation during blankless loading, including the frame interpolation duration, cache data validity period, and custom callback after frame interpolation is complete.

> **NOTE：**&gt;
> - This API must be called after the page loading API is triggered. Other restrictions are the same as those of
> [getBlanklessInfoWithKey](#getblanklessinfowithkey).&gt;
> - The page must be loaded in the component that calls this API.&gt;
> - When the similarity is low, the system will deem the scene change too abrupt and frame insertion will fail.&gt;
> - Add the **ohos.permission.INTERNET** and **ohos.permission.GET_NETWORK_INFO** permissions to
> **module.json5**. For details, see
> [Declaring Permissions in the Configuration File](../../../security/AccessToken/declare-permissions.md#declaring-permissions-in-the-configuration-file).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| param | [BlanklessLoadingParam](arkts-arkweb-webview-blanklessloadingparam-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WebBlanklessErrorCode](arkts-arkweb-webview-webblanklesserrorcode-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## setConnectionTimeout

```TypeScript
static setConnectionTimeout(timeout: number): void
```

Sets the network connection timeout interval. You can use the **onErrorReceive** method in the **Web** component to obtain the timeout error code. If this API is not called, the default timeout interval is **30** seconds.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timeout | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setCustomUserAgent

```TypeScript
setCustomUserAgent(userAgent: string): void
```

Sets a custom user agent, which will overwrite the default user agent.

> **NOTE：**&gt;
> - When **src** of the **Web** component is set to a URL, it is recommended to set **User-Agent** in the
> onControllerAttached callback. Do not set it in the
> **onLoadIntercept** callback, as this may cause the setting to fail or lead to unexpected results.&gt;
> - If **User-Agent** is not set in the **onControllerAttached** callback, calling **setCustomUserAgent** later
> may cause an anomaly where the loaded page does not match the actually set **User-Agent**.&gt;
> - When **src** of the **Web** component is not set to a URL, it is recommended to call **setCustomUserAgent**
> to set **User-Agent** first, and then use **loadUrl** to load a specific page.&gt;
> - For the definition and usage scenarios of the default **User-Agent**, see
> User-Agent Development Guide.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userAgent | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## setDownloadDelegate

```TypeScript
setDownloadDelegate(delegate: WebDownloadDelegate): void
```

Sets a **WebDownloadDelegate** for the current **Web** component. The delegate is used to receive the download progress triggered within the page.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| delegate | [WebDownloadDelegate](arkts-arkweb-webview-webdownloaddelegate-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## setErrorPageEnabled

```TypeScript
setErrorPageEnabled(enable: boolean): void
```

Sets whether to enable the default error page.When this API is set to true, if an error occurs during page loading, the [onOverrideErrorPage](../arkts-components/arkts-arkweb-web-attribute.md#onoverrideerrorpage) callback is triggered. You can customize the error display page in the callback.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## setErrorPageEnabled

```TypeScript
setErrorPageEnabled(enable: boolean, includeSubframe: boolean): void
```

Sets whether to enable the mainframe error page feature, and controls whether to also enable the subframe error page feature.When **enable** is set to **true**, an error page is displayed when a mainframe loading error occurs: if the [onOverrideErrorPage](../arkts-components/arkts-arkweb-web-attribute.md#onoverrideerrorpage) callback is set, the user-defined error page is displayed; if not, the default error page provided by ArkWeb is displayed. When both **enable** and **includeSubframe** are set to **true**, an error page is also displayed when a subframe loading error occurs, and the **onOverrideErrorPage** callback also takes effect for subframes.

> **NOTE：**&gt;
> - When **enable** is set to **false**, the error page feature for both mainframe and subframe is disabled
> regardless of the value of **includeSubframe**.&gt;
> - When **includeSubframe** is set to **false**, the behavior of this API is the same as that of
> [setErrorPageEnabled](#seterrorpageenabled)&lt;sup&gt;20+&lt;/sup&gt;, that
> is, only the mainframe error page feature is enabled, and the subframe error page feature is not enabled.&gt;
> - You can use errorPageEvent.request.isMainFrame() to determine whether
> the error source is a mainframe or a subframe, so as to set the corresponding custom error page in the
> **onOverrideErrorPage** callback.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |
| includeSubframe | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## setHostIP

```TypeScript
static setHostIP(hostName: string, address: string, aliveTime: number): void
```

Sets the IP address of the host after domain name resolution.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hostName | string | Yes |
| address | string | Yes |
| aliveTime | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setHttpDns

```TypeScript
static setHttpDns(secureDnsMode: SecureDnsMode, secureDnsConfig: string): void
```

Sets how the **Web** component uses HTTPDNS for DNS resolution.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| secureDnsMode | [SecureDnsMode](arkts-arkweb-webview-securednsmode-e.md) | Yes |
| secureDnsConfig | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setNetworkAvailable

```TypeScript
setNetworkAvailable(enable: boolean): void
```

Sets the **window.navigator.onLine** attribute in JavaScript.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## setPathAllowingUniversalAccess

```TypeScript
setPathAllowingUniversalAccess(pathList: Array<string>): void
```

Sets a path list. When the file protocol accesses resources in the path list, cross-origin access to local files and other online resources is allowed. In addition, when a path list is set, the file protocol only allows access to resources in the path list. Typical use case: used when the **Web** component needs to be allowed to access local resource files across origins while restricting the access scope to ensure security. (The behavior of fileAccess will be overridden by the behavior of this API.)Using setPathAllowingUniversalAccess to relax cross-origin access restrictions on directories is a high-risk operation. Based on the principle of least privilege, the paths for el1 and el2 are fixed. The paths in the path list must conform to one of the following path formats:
1. A subdirectory of the app file directory. (The app file directory is obtained through [Context.filesDir]
(../../../reference/apis-ability-kit/js-apis-inner-application-context.md#properties) in Ability Kit.) For example:  
* /data/storage/el2/base/files/example  
* /data/storage/el2/base/haps/entry/files/example
2. The app resource directory or its subdirectory.
(The app resource directory is obtained through [Context.resourceDir] (../../../reference/apis-ability-kit/js-apis-inner-application-context.md#properties) in Ability Kit.) For example:  
* /data/storage/el1/bundle/entry/resource/resfile  
* /data/storage/el1/bundle/entry/resource/resfile/example
3. Since API version 21, the app cache directory and its subdirectory are also included.
(The app cache directory is obtained through [Context.cacheDir] (../../../reference/apis-ability-kit/js-apis-inner-application-context.md#properties) in Ability Kit.) For example:  
* /data/storage/el2/base/cache  
* /data/storage/el2/base/haps/entry/cache/example  
* The **cache/web** directory is not allowed. If it is included, an exception with the code **401** will be thrown. If the **cache** directory is set, **cache/web** cannot be accessed.
4. Since API version 21, the app temporary directory and its subdirectory are also included.
(The app temporary directory is obtained through [Context.tempDir] (../../../reference/apis-ability-kit/js-apis-inner-application-context.md#properties) in Ability Kit.) For example:  
* /data/storage/el2/base/temp  
* /data/storage/el2/base/haps/entry/temp/example If a path in the list is not of the preceding paths, error code 401 is reported and the path list fails to be set. When the path list is set to empty, the accessible files for the file protocol are subject to the behavior of the fileAccess.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pathList | Array & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## setPrintBackground

```TypeScript
setPrintBackground(enable: boolean): void
```

Sets whether to print the background of a web page. If the setting of this API is inconsistent with that of [PrintAttributes](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-print-printattributes-i.md), the setting of this API takes precedence.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## setRenderProcessMode

```TypeScript
static setRenderProcessMode(mode: RenderProcessMode): void
```

Sets the ArkWeb rendering subprocess mode. You can select the appropriate mode based on the app's requirements for memory usage and rendering process isolation.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [RenderProcessMode](arkts-arkweb-webview-renderprocessmode-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setScrollable

```TypeScript
setScrollable(enable: boolean, type?: ScrollType): void
```

Sets whether this web page is scrollable.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |
| type | [ScrollType](arkts-arkweb-webview-scrolltype-e.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## setScrollbarMode

```TypeScript
static setScrollbarMode(scrollbarMode: ScrollbarMode): void
```

Sets the global scrollbar mode in the web page. When this API is not explicitly called, [ScrollbarMode.OVERLAY_LAYOUT_SCROLLBAR](arkts-arkweb-webview-scrollbarmode-e.md) is used by default, indicating that the scroll bar is not always displayed.

> **NOTE：**&gt;
> - You can set whether to always display the web scrollbar of the current application based on the scrollbar
> mode.&gt;
> - If the [forceDisplayScrollBar](../arkts-components/arkts-arkweb-web-attribute.md#forcedisplayscrollbar) API is set at the same time as this
> API, the setting of **forceDisplayScrollBar** does not take effect.&gt;
> - This API must be called before WebViewController is bound to a **Web** component.

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scrollbarMode | [ScrollbarMode](arkts-arkweb-webview-scrollbarmode-e.md) | Yes |

## setServiceWorkerWebSchemeHandler

```TypeScript
static setServiceWorkerWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void
```

Sets a WebSchemeHandler for all **Web** components of the current app, used to intercept requests of a specified scheme in ServiceWorker.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scheme | string | Yes |
| handler | [WebSchemeHandler](arkts-arkweb-webview-webschemehandler-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setSiteIsolationMode

```TypeScript
static setSiteIsolationMode(mode: SiteIsolationMode): void
```

Sets the site isolation mode. The site isolation mechanism isolates websites from different origins in different rendering processes to reduce the cross-domain attack surface. For example, on devices such as PCs, when site isolation mode is not enabled, the original process model assigns one rendering process per tab. After site isolation is enabled, iframes from different origins within a tab can run in independent rendering processes.For third-party applications that load only trusted web pages, you can disable this functionality to improve performance, reduce memory usage, and reduce interception of cross-domain access. The default value varies according to the device. [SiteIsolationMode.STRICT](arkts-arkweb-webview-siteisolationmode-e.md) is used for PCs and tablets, and [SiteIsolationMode.PARTIAL](arkts-arkweb-webview-siteisolationmode-e.md) is used for phones. In [Secure Shield mode](../../../web/web-secure-shield-mode.md), strict site isolation is used.

> **NOTE：**&gt;
> Strict site isolation cannot be set in single-process mode.&gt;
> This API can be called only once during initialization. The site isolation mode cannot be repeatedly changed.

**Since:** 21

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [SiteIsolationMode](arkts-arkweb-webview-siteisolationmode-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## setSocketIdleTimeout

```TypeScript
static setSocketIdleTimeout(timeout: number): void
```

Sets the timeout interval for used sockets to stay idle in the **Web** component. If the value is different from the timeout interval of existing idle sockets, the existing idle sockets are cleared according to the new value.If this API is not used to set the timeout interval for idle sockets, the default value **300s** is used for the **Web** component.

**Since:** 21

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timeout | number | Yes |

## setSoftKeyboardBehaviorMode

```TypeScript
setSoftKeyboardBehaviorMode(mode: WebSoftKeyboardBehaviorMode): void
```

Sets the automatic control mode of the soft keyboard. When this API is not explicitly called, the system attempts to automatically hide or show the soft keyboard when the **Web** component loses or gains focus, or when its state switches to inactive or active. Typical use case: when you do not want the **Web** component to automatically hide or re-show the soft keyboard during inactive or active state switching, use DISABLE_AUTO_KEYBOARD_ON_ACTIVE; when you need to retain the default automatic management behavior, use DEFAULT.

**Since:** 22

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [WebSoftKeyboardBehaviorMode](arkts-arkweb-webview-websoftkeyboardbehaviormode-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## setUrlTrustList

```TypeScript
setUrlTrustList(urlTrustList: string): void
```

Sets a URL trust list for the Web. Only URLs in the trust list are allowed to be loaded or navigated to. Otherwise, they are intercepted and an alert page is displayed.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| urlTrustList | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## setUrlTrustList

```TypeScript
setUrlTrustList(urlTrustList: string, allowOpaqueOrigin: boolean, supportWildcard: boolean): void
```

Sets a URL trust list for the Web. Only URLs in the trust list are allowed to be loaded or navigated to. Otherwise, they are intercepted and an alert page is displayed. This API extends the control over opaque origin URLs and wildcard rules.

**Since:** 24

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| urlTrustList | string | Yes |
| allowOpaqueOrigin | boolean | Yes |
| supportWildcard | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setUserAgentClientHintsEnabled

```TypeScript
static setUserAgentClientHintsEnabled(enabled: boolean): void
```

Sets whether to enable the User-Agent Client Hints feature.

> **NOTE：**&gt;
> User-Agent Client Hints (UA-CH) is a privacy protection mechanism that replaces the traditional **User-Agent**
> string. It transfers client information through on-demand requests and structured data, reducing the risk of
> excessive tracking.&gt;
> If this method is not used, the User-Agent Client Hints feature is disabled by default.

**Since:** 24

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

## setUserAgentForHosts

```TypeScript
static setUserAgentForHosts(userAgent: string, hosts : Array<string>) : void
```

Sets a custom user agent for a specific website, which overwrites the system user agent and takes effect for all **Web** components in the application.To set a custom user agent for a specific website, you are advised to call the **setUserAgentForHosts** method to set **User-Agent** before creating a **Web** component, and then create a **Web** component with a specified src or use [loadUrl](#loadurl) to load a specific page.For details about the default **User-Agent** definition, application scenarios, and API priorities, see [Developing User-Agent](../../../web/web-default-userAgent.md).

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userAgent | string | Yes |
| hosts | Array & lt;string & gt; | Yes |

## setUserAgentMetadata

```TypeScript
setUserAgentMetadata(userAgent: string, metaData: UserAgentMetadata): void
```

Sets the **UserAgentMetadata** corresponding to the **User-Agent**.

> **NOTE：**&gt;
> User-Agent Metadata is used to populate user agent client hints. It can provide the brand and version
> information of the client, the brand and major version of the underlying operating system, and detailed
> information about the underlying device.&gt;
> The user agent can be set through setCustomUserAgent, setAppCustomUserAgent, or setUserAgentForHosts.&gt;
> If no UserAgentMetadata is found based on the overridden User-Agent, and the overridden User-Agent contains the
> system default User-Agent, the system default value is used.&gt;
> If no UserAgentMetadata is found based on the overridden User-Agent, but the overridden User-Agent does not
> contain the system default user agent, only low-level user agent client hints are generated.

**Since:** 24

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userAgent | string | Yes |
| metaData | [UserAgentMetadata](arkts-arkweb-webview-useragentmetadata-c.md) | Yes |

## setWebDebuggingAccess

```TypeScript
static setWebDebuggingAccess(webDebuggingAccess: boolean): void
```

Sets whether to enable web debugging. For details, see [Debugging Frontend Pages by Using DevTools](../../../web/web-debugging-with-devtools.md).NOTE: Enabling web debugging allows users to check and modify the internal status of the web page, which poses security risks. Therefore, you are advised not to enable this feature in the officially released version of the application.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| webDebuggingAccess | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setWebDebuggingAccess

```TypeScript
static setWebDebuggingAccess(webDebuggingAccess: boolean, port: number): void
```

Sets whether to enable wireless web debugging. By default, wireless web debugging is disabled.  
* If no port is specified, this API is equivalent to the  
[setWebDebuggingAccess](#setwebdebuggingaccess) API. In this case, ArkWeb starts a local domain socket listener.  
* When a port is specified, ArkWeb starts a TCP socket listener. In this case, you can debug the web page wirelessly. For details, see [Wireless Debugging](../../../web/web-debugging-with-devtools.md#wireless-debugging).A port number smaller than 1024 is a well-known or system port and can be enabled only with privileges in the operating system. Therefore, the value of port must be greater than 1024. Otherwise, the API throws an exception.NOTE: Enabling web debugging allows users to check and modify the internal status of the web page, which poses security risks. Therefore, you are advised not to enable this feature in the officially released version of the application.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| webDebuggingAccess | boolean | Yes |
| port | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17100023](../errorcode-webview.md#17100023-port-number-not-allowed) |

## setWebDestroyMode

```TypeScript
static setWebDestroyMode(mode: WebDestroyMode): void
```

Sets the destroy mode of the **Web** component. The destroy mode of the **Web** component affects the time when web kernel resources, such as the JavaScript running context and rendering context, are released. The default value is [WebDestroyMode.NORMAL_MODE](arkts-arkweb-webview-webdestroymode-e.md) (normal mode), indicating that the system determines the destroy time. You can set [WebDestroyMode.FAST_MODE](arkts-arkweb-webview-webdestroymode-e.md) (fast mode) to destroy resources immediately, improving performance in specific scenarios.

> **NOTE：**&gt;
> [WebDestroyMode.FAST_MODE](arkts-arkweb-webview-webdestroymode-e.md) changes the time when the **Web** component is
> destroyed. When it is used, pay attention to the incorrect implementation that depends on the destroy time of
> the **Web** component. For example, when a **WebViewController** is called in fast mode rather than using
> [WebDestroyMode.NORMAL_MODE](arkts-arkweb-webview-webdestroymode-e.md), the unbinding exception (**17100001**) is more
> likely to be triggered. In this case, the application needs to capture the exception, or use
> [getAttachState](#getattachstate) to obtain the attach state to avoid stability
> problems.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [WebDestroyMode](arkts-arkweb-webview-webdestroymode-e.md) | Yes |

## setWebSchemeHandler

```TypeScript
setWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void
```

Sets a [WebSchemeHandler](arkts-arkweb-webview-webschemehandler-c.md) for the **Web** component. The [WebSchemeHandler](arkts-arkweb-webview-webschemehandler-c.md) class is used to intercept requests of a specified scheme.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scheme | string | Yes |
| handler | [WebSchemeHandler](arkts-arkweb-webview-webschemehandler-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## slideScroll

```TypeScript
slideScroll(vx: number, vy: number): void
```

Simulates a slide-to-scroll action on the page at the specified velocity.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| vx | number | Yes |
| vy | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## startCamera

```TypeScript
startCamera(): void
```

Enables the camera capture of the current web page. Before using the camera, add the **ohos.permission.CAMERA** permission to **module.json5**. For details about how to add the permission, see [Declaring Permissions in the Configuration File](../../../security/AccessToken/declare-permissions.md).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## startDownload

```TypeScript
startDownload(url: string): void
```

Uses the download capability of the **Web** component to download a specified URL, for example, downloading a specified image from a web page.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |

## stop

```TypeScript
stop(): void
```

Stops page loading.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## stopAllMedia

```TypeScript
stopAllMedia(): void
```

Stops all audio and video on a web page.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## stopCamera

```TypeScript
stopCamera(): void
```

Stops the camera capture of the current web page.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## stopMicrophone

```TypeScript
stopMicrophone(): void
```

Stops microphone capture on the current web page.

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## storeWebArchive

```TypeScript
storeWebArchive(baseName: string, autoName: boolean): Promise<string>
```

Stores this web page. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| baseName | string | Yes |
| autoName | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |
| [17100003](../errorcode-webview.md#17100003-incorrect-resource-path) |

## storeWebArchive

```TypeScript
storeWebArchive(baseName: string, autoName: boolean, callback: AsyncCallback<string>): void
```

Stores this web page. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| baseName | string | Yes |
| autoName | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |
| [17100003](../errorcode-webview.md#17100003-incorrect-resource-path) |

## terminateRenderProcess

```TypeScript
terminateRenderProcess(): boolean
```

Terminates this render process.Calling this API will destroy the associated render process. If the render process has not been started or has been destroyed, there is no impact. In addition, destroying the render process affects all other instances associated with the render process.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |

## trimMemoryByPressureLevel

```TypeScript
static trimMemoryByPressureLevel(level: PressureLevel): void
```

Clears the cache occupied by **Web** component based on the specified memory pressure level.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| level | [PressureLevel](arkts-arkweb-webview-pressurelevel-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## waitForAttached

```TypeScript
waitForAttached(timeout: number): Promise<ControllerAttachState>
```

Asynchronously waits for the **WebViewController** to be attached to the **Web** component. If the attachment is complete or times out, a callback is triggered to return the current [ControllerAttachState](arkts-arkweb-webview-controllerattachstate-e.md) through a promise.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timeout | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ControllerAttachState](arkts-arkweb-webview-controllerattachstate-e.md)&gt; |

## warmupServiceWorker

```TypeScript
static warmupServiceWorker(url: string): void
```

Warms up ServiceWorker to improve the loading speed of the first screen page (only for pages that use ServiceWorker). Call this API before loading the URL.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |

## webPageSnapshot

```TypeScript
webPageSnapshot(info: SnapshotInfo, callback: AsyncCallback<SnapshotResult>): void
```

Obtains the full drawing result of the web page.

> **NOTE：**&gt;
> - This API does not support concurrent calls.&gt;
> - Only supports taking snapshots of resources on the rendering process: static images and text.&gt;
> - If the page contains a video, a placeholder image of the video is displayed in the snapshot. If there is no
> placeholder image, a blank area is displayed.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [SnapshotInfo](arkts-arkweb-webview-snapshotinfo-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SnapshotResult](arkts-arkweb-webview-snapshotresult-i.md)&gt; | Yes |

## zoom

```TypeScript
zoom(factor: number): void
```

Zooms in or out of this web page. This API is effective only when [zoomAccess](../arkts-components/arkts-arkweb-web-attribute.md#zoomaccess) is **true**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [factor](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-materialproperty-i.md) | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |
| [17100004](../errorcode-webview.md#17100004-function-not-enabled) |

## zoomIn

```TypeScript
zoomIn(): void
```

Zooms in on this web page by 25%.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |
| [17100004](../errorcode-webview.md#17100004-function-not-enabled) |

## zoomOut

```TypeScript
zoomOut(): void
```

Zooms out of this web page by 20%.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) |
| [17100004](../errorcode-webview.md#17100004-function-not-enabled) |
