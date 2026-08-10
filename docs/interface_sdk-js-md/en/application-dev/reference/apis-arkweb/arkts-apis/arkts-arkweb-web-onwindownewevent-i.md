# OnWindowNewEvent

Defines the triggered callback when web page requires the user to create a window.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface OnWindowNewEvent--><!--Device-unnamed-export declare interface OnWindowNewEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## handler

```TypeScript
handler: ControllerHandler
```

Lets you set the WebviewController instance for creating a new window.

**Type:** [ControllerHandler](../arkts-components/arkts-arkweb-controllerhandler-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-OnWindowNewEvent-handler: ControllerHandler--><!--Device-OnWindowNewEvent-handler: ControllerHandler-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isAlert

```TypeScript
isAlert: boolean
```

true indicates the request to create a dialog and false indicates a new tab.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-OnWindowNewEvent-isAlert: boolean--><!--Device-OnWindowNewEvent-isAlert: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isUserTrigger

```TypeScript
isUserTrigger: boolean
```

true indicates that it is triggered by the user, and false indicates that it is triggered by a non-user.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-OnWindowNewEvent-isUserTrigger: boolean--><!--Device-OnWindowNewEvent-isUserTrigger: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## targetUrl

```TypeScript
targetUrl: string
```

Destination URL.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-OnWindowNewEvent-targetUrl: string--><!--Device-OnWindowNewEvent-targetUrl: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

