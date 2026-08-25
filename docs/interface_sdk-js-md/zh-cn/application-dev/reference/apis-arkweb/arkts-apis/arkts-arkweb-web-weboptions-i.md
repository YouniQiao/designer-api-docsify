# WebOptions

Defines the Web options.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## controller

```TypeScript
controller: WebviewController
```

Sets the controller of the Web.

**类型：** [WebviewController](arkts-arkweb-webviewcontroller-t.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## emulateTouchFromMouseEvent

```TypeScript
emulateTouchFromMouseEvent?: boolean
```

Sets whether mouse event will be transferred to touch event.

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## incognitoMode

```TypeScript
incognitoMode?: boolean
```

Sets the incognito mode of the Web, the parameter is optional and default value is false. When the Web is in incognito mode, cookies, records of websites, geolocation permissions will not save in persistent files.

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## renderMode

```TypeScript
renderMode?: RenderMode
```

Rendering mode. RenderMode.ASYNC_RENDER (default, cannot be dynamically adjusted): The Web component is rendered asynchronously. RenderMode.SYNC_RENDER: The Web component is rendered synchronously within the current execution context.

**类型：** [RenderMode](arkts-arkweb-web-rendermode-e.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## sharedRenderProcessToken

```TypeScript
sharedRenderProcessToken?: string
```

A token indicating that the current Web component specifies a shared rendering process. In the multi-rendering process mode, Web components with the same token will preferentially try to reuse the rendering process bound to the token. The binding of token to the rendering process occurs in the initialization stage of the rendering process. When the rendering process has no associated Web component, its binding relationship with token will be removed.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## src

```TypeScript
src: string | Resource
```

Web resource address. If accessing local resource files, please use \$rawfile or resource protocol. If you load a local resource file that applies the sandbox path outside the package (files support html and txt types), please use the file:// sandbox file path. Src cannot dynamically change the address through state variables (for example: @State). If you need to change it, please reload it through loadUrl.

**类型：** string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core
