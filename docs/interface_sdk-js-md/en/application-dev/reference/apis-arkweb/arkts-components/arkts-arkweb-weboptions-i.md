# WebOptions

Defines the Web options.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface WebOptions--><!--Device-unnamed-declare interface WebOptions-End-->

**System capability:** SystemCapability.Web.Webview.Core

## controller

```TypeScript
controller: WebController | WebviewController
```

Sets the controller of the Web.

**Type:** [WebController](arkts-arkweb-webcontroller-c.md) \| WebviewController

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebOptions-controller: WebController | WebviewController--><!--Device-WebOptions-controller: WebController | WebviewController-End-->

**System capability:** SystemCapability.Web.Webview.Core

## emulateTouchFromMouseEvent

```TypeScript
emulateTouchFromMouseEvent? : boolean
```

设定鼠标事件是否被转换成触摸事件。

默认值：false。

**Type:** boolean

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

<!--Device-WebOptions-emulateTouchFromMouseEvent? : boolean--><!--Device-WebOptions-emulateTouchFromMouseEvent? : boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## incognitoMode

```TypeScript
incognitoMode? : boolean
```

Sets the incognito mode of the Web, the parameter is optional and default value is false.When the Web is in incognito mode, cookies, records of websites, geolocation permissions will not save in persistent files.

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-WebOptions-incognitoMode? : boolean--><!--Device-WebOptions-incognitoMode? : boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## renderMode

```TypeScript
renderMode? : RenderMode
```

Sets the render mode of the web.

**Type:** [RenderMode](../arkts-apis/arkts-arkweb-web-rendermode-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebOptions-renderMode? : RenderMode--><!--Device-WebOptions-renderMode? : RenderMode-End-->

**System capability:** SystemCapability.Web.Webview.Core

## sharedRenderProcessToken

```TypeScript
sharedRenderProcessToken? : string
```

Sets the shared render process token of the web.When the web is in multiprocess mode, web with the same sharedRenderProcessToken will attempt to reuse the same render process.The shared render process will remain active until all associated web are destroyed.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-WebOptions-sharedRenderProcessToken? : string--><!--Device-WebOptions-sharedRenderProcessToken? : string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## src

```TypeScript
src: string | Resource
```

Sets the address of the web page to be displayed.

**Type:** string \| Resource

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebOptions-src: string | Resource--><!--Device-WebOptions-src: string | Resource-End-->

**System capability:** SystemCapability.Web.Webview.Core

