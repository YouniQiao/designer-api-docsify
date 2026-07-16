# OnWindowNewExtEvent

Callback invoked when the web page requests the user to create a window.

**Since:** 23

<!--Device-unnamed-declare interface OnWindowNewExtEvent--><!--Device-unnamed-declare interface OnWindowNewExtEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## handler

```TypeScript
handler: ControllerHandler
```

**WebviewController** instance for setting the new window.

**Type:** ControllerHandler

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-OnWindowNewExtEvent-handler: ControllerHandler--><!--Device-OnWindowNewExtEvent-handler: ControllerHandler-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isAlert

```TypeScript
isAlert: boolean
```

The value **true** indicates that a dialog box is requested to be created, and the value **false** indicates that a new tab page is requested to be created.

**Type:** boolean

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-OnWindowNewExtEvent-isAlert: boolean--><!--Device-OnWindowNewExtEvent-isAlert: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isUserTrigger

```TypeScript
isUserTrigger: boolean
```

Whether the creation is triggered by the user. The value **true** means that the creation is triggered by the user,and **false** means the opposite.

**Type:** boolean

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-OnWindowNewExtEvent-isUserTrigger: boolean--><!--Device-OnWindowNewExtEvent-isUserTrigger: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## navigationPolicy

```TypeScript
navigationPolicy: NavigationPolicy
```

Window opening mode when the web page requests a user to create a new window.

**Type:** NavigationPolicy

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-OnWindowNewExtEvent-navigationPolicy: NavigationPolicy--><!--Device-OnWindowNewExtEvent-navigationPolicy: NavigationPolicy-End-->

**System capability:** SystemCapability.Web.Webview.Core

## targetUrl

```TypeScript
targetUrl: string
```

URL to be opened in the new window.

**Type:** string

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-OnWindowNewExtEvent-targetUrl: string--><!--Device-OnWindowNewExtEvent-targetUrl: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## windowFeatures

```TypeScript
windowFeatures: WindowFeatures
```

Feature information of the new window requested to be created by the web page.

**Type:** WindowFeatures

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-OnWindowNewExtEvent-windowFeatures: WindowFeatures--><!--Device-OnWindowNewExtEvent-windowFeatures: WindowFeatures-End-->

**System capability:** SystemCapability.Web.Webview.Core

