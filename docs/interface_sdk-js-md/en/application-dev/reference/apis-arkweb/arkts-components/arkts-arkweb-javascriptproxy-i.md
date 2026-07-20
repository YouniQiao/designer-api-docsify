# JavaScriptProxy

Defines the JavaScript object to be injected.

**Since:** 12

<!--Device-unnamed-declare interface JavaScriptProxy--><!--Device-unnamed-declare interface JavaScriptProxy-End-->

**System capability:** SystemCapability.Web.Webview.Core

## asyncMethodList

```TypeScript
asyncMethodList?: Array<string>
```

The async method of the application side JavaScript object participating in the registration.

**Type:** Array&lt;string&gt;

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-JavaScriptProxy-asyncMethodList?: Array<string>--><!--Device-JavaScriptProxy-asyncMethodList?: Array<string>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## controller

```TypeScript
controller: WebController | WebviewController
```

Controller.

**Type:** WebController \| WebviewController

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-JavaScriptProxy-controller: WebController | WebviewController--><!--Device-JavaScriptProxy-controller: WebController | WebviewController-End-->

**System capability:** SystemCapability.Web.Webview.Core

## methodList

```TypeScript
methodList: Array<string>
```

The method of the application side JavaScript object participating in the registration.

**Type:** Array&lt;string&gt;

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-JavaScriptProxy-methodList: Array<string>--><!--Device-JavaScriptProxy-methodList: Array<string>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## name

```TypeScript
name: string
```

The name of the registered object, which is consistent with the object name called in the window.

**Type:** string

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-JavaScriptProxy-name: string--><!--Device-JavaScriptProxy-name: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## object

```TypeScript
object: object
```

Objects participating in registration.

**Type:** object

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-JavaScriptProxy-object: object--><!--Device-JavaScriptProxy-object: object-End-->

**System capability:** SystemCapability.Web.Webview.Core

## permission

```TypeScript
permission?: string
```

permission configuration defining web page URLs that can access JavaScriptProxy methods.The configuration can be defined at two levels, object level and method level.

**Type:** string

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-JavaScriptProxy-permission?: string--><!--Device-JavaScriptProxy-permission?: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

