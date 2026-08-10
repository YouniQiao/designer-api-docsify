# OnWindowNewExtEvent

Defines the triggered callback when web page requires the user to create a window.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-unnamed-declare interface OnWindowNewExtEvent--><!--Device-unnamed-declare interface OnWindowNewExtEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## handler

```TypeScript
handler: ControllerHandler
```

Lets you set the WebviewController instance for creating a new window.

**Type:** [ControllerHandler](arkts-arkweb-controllerhandler-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-OnWindowNewExtEvent-handler: ControllerHandler--><!--Device-OnWindowNewExtEvent-handler: ControllerHandler-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isAlert

```TypeScript
isAlert: boolean
```

true indicates the request to create a dialog and false indicates a new tab.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-OnWindowNewExtEvent-isAlert: boolean--><!--Device-OnWindowNewExtEvent-isAlert: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isUserTrigger

```TypeScript
isUserTrigger: boolean
```

true indicates that it is triggered by the user, and false indicates that it is triggered by a non-user.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-OnWindowNewExtEvent-isUserTrigger: boolean--><!--Device-OnWindowNewExtEvent-isUserTrigger: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## navigationPolicy

```TypeScript
navigationPolicy: NavigationPolicy
```

The navigation policy causing the new web view to be created.

**Type:** [NavigationPolicy](arkts-arkweb-navigationpolicy-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-OnWindowNewExtEvent-navigationPolicy: NavigationPolicy--><!--Device-OnWindowNewExtEvent-navigationPolicy: NavigationPolicy-End-->

**System capability:** SystemCapability.Web.Webview.Core

## targetUrl

```TypeScript
targetUrl: string
```

Destination URL.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-OnWindowNewExtEvent-targetUrl: string--><!--Device-OnWindowNewExtEvent-targetUrl: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## windowFeatures

```TypeScript
windowFeatures: WindowFeatures
```

Contains the attributes that a webpage requests from its containing web view, the parameters of window.open.

**Type:** [WindowFeatures](arkts-arkweb-windowfeatures-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-OnWindowNewExtEvent-windowFeatures: WindowFeatures--><!--Device-OnWindowNewExtEvent-windowFeatures: WindowFeatures-End-->

**System capability:** SystemCapability.Web.Webview.Core

