# WebOptions

Defines the Web options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface WebOptions--><!--Device-unnamed-export declare interface WebOptions-End-->

**System capability:** SystemCapability.Web.Webview.Core

## controller

```TypeScript
controller: WebviewController
```

Sets the controller of the Web.

**Type:** [WebviewController](arkts-arkweb-webviewcontroller-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebOptions-controller: WebviewController--><!--Device-WebOptions-controller: WebviewController-End-->

**System capability:** SystemCapability.Web.Webview.Core

## emulateTouchFromMouseEvent

```TypeScript
emulateTouchFromMouseEvent?: boolean
```

Sets whether mouse event will be transferred to touch event.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebOptions-emulateTouchFromMouseEvent?: boolean--><!--Device-WebOptions-emulateTouchFromMouseEvent?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## incognitoMode

```TypeScript
incognitoMode?: boolean
```

Sets the incognito mode of the Web, the parameter is optional and default value is false.When the Web is in incognito mode, cookies, records of websites, geolocation permissions will not save in persistent files.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebOptions-incognitoMode?: boolean--><!--Device-WebOptions-incognitoMode?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## renderMode

```TypeScript
renderMode?: RenderMode
```

Rendering mode.RenderMode.ASYNC_RENDER (default, cannot be dynamically adjusted): The Web component is rendered asynchronously.RenderMode.SYNC_RENDER: The Web component is rendered synchronously within the current execution context.

**Type:** [RenderMode](arkts-arkweb-web-rendermode-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebOptions-renderMode?: RenderMode--><!--Device-WebOptions-renderMode?: RenderMode-End-->

**System capability:** SystemCapability.Web.Webview.Core

## sharedRenderProcessToken

```TypeScript
sharedRenderProcessToken?: string
```

A token indicating that the current Web component specifies a shared rendering process.In the multi-rendering process mode, Web components with the same token will preferentially try to reuse the rendering process bound to the token.The binding of token to the rendering process occurs in the initialization stage of the rendering process.When the rendering process has no associated Web component, its binding relationship with token will be removed.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebOptions-sharedRenderProcessToken?: string--><!--Device-WebOptions-sharedRenderProcessToken?: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## src

```TypeScript
src: string | Resource
```

Web resource address. If accessing local resource files, please use \$rawfile or resource protocol.If you load a local resource file that applies the sandbox path outside the package (files support html and txt types),please use the file:// sandbox file path.Src cannot dynamically change the address through state variables (for example: @State).If you need to change it, please reload it through [loadUrl](loadUrl).

**Type:** string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebOptions-src: string | Resource--><!--Device-WebOptions-src: string | Resource-End-->

**System capability:** SystemCapability.Web.Webview.Core

