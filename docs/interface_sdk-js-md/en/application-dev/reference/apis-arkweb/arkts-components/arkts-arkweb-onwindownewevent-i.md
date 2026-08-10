# OnWindowNewEvent

定义网页要求用户创建窗口时触发的回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface OnWindowNewEvent--><!--Device-unnamed-declare interface OnWindowNewEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## handler

```TypeScript
handler: ControllerHandler
```

Lets you set the WebviewController instance for creating a new window.

**Type:** [ControllerHandler](arkts-arkweb-controllerhandler-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnWindowNewEvent-handler: ControllerHandler--><!--Device-OnWindowNewEvent-handler: ControllerHandler-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isAlert

```TypeScript
isAlert: boolean
```

true indicates the request to create a dialog and false indicates a new tab.

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnWindowNewEvent-isAlert: boolean--><!--Device-OnWindowNewEvent-isAlert: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isUserTrigger

```TypeScript
isUserTrigger: boolean
```

true indicates that it is triggered by the user, and false indicates that it is triggered by a non-user.

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnWindowNewEvent-isUserTrigger: boolean--><!--Device-OnWindowNewEvent-isUserTrigger: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## targetUrl

```TypeScript
targetUrl: string
```

Destination URL.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnWindowNewEvent-targetUrl: string--><!--Device-OnWindowNewEvent-targetUrl: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

