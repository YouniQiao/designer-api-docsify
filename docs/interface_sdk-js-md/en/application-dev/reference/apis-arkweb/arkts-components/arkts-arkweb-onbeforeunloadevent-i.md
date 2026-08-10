# OnBeforeUnloadEvent

Defines the triggered function when the web page wants to confirm navigation from JavaScript onbeforeunload.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface OnBeforeUnloadEvent--><!--Device-unnamed-declare interface OnBeforeUnloadEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isReload

```TypeScript
isReload?: boolean
```

页面是否刷新。&lt;br&gt;当页面因刷新即将离开时，isReload参数被设置为true；当页面因关闭即将离开时，isReload参数被设置为false。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-OnBeforeUnloadEvent-isReload?: boolean--><!--Device-OnBeforeUnloadEvent-isReload?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## message

```TypeScript
message: string
```

弹窗中显示的信息。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnBeforeUnloadEvent-message: string--><!--Device-OnBeforeUnloadEvent-message: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## result

```TypeScript
result: JsResult
```

通知Web组件用户操作行为。

**Type:** [JsResult](../arkts-apis/arkts-arkweb-web-jsresult-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnBeforeUnloadEvent-result: JsResult--><!--Device-OnBeforeUnloadEvent-result: JsResult-End-->

**System capability:** SystemCapability.Web.Webview.Core

## url

```TypeScript
url: string
```

当前显示弹窗所在网页的URL。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnBeforeUnloadEvent-url: string--><!--Device-OnBeforeUnloadEvent-url: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

