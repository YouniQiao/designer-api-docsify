# FullScreenEnterEvent

Web组件进入全屏回调事件的详情。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface FullScreenEnterEvent--><!--Device-unnamed-declare interface FullScreenEnterEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## handler

```TypeScript
handler: FullScreenExitHandler
```

用于退出全屏模式的函数句柄。

**Type:** [FullScreenExitHandler](arkts-arkweb-fullscreenexithandler-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FullScreenEnterEvent-handler: FullScreenExitHandler--><!--Device-FullScreenEnterEvent-handler: FullScreenExitHandler-End-->

**System capability:** SystemCapability.Web.Webview.Core

## videoHeight

```TypeScript
videoHeight?: number
```

视频的高度，单位：px。如果进入全屏的是 `&lt;video&gt;` 元素，表示其高度；如果进入全屏的子元素中包含 `&lt;video&gt;` 元素，表示第一个子视频元素的高度；其他情况下，为0。

**Type:** number

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-FullScreenEnterEvent-videoHeight?: number--><!--Device-FullScreenEnterEvent-videoHeight?: number-End-->

**System capability:** SystemCapability.Web.Webview.Core

## videoWidth

```TypeScript
videoWidth?: number
```

视频的宽度，单位：px。如果进入全屏的是 `&lt;video&gt;` 元素，表示其宽度；如果进入全屏的子元素中包含 `&lt;video&gt;` 元素，表示第一个子视频元素的宽度；其他情况下，为0。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FullScreenEnterEvent-videoWidth?: number--><!--Device-FullScreenEnterEvent-videoWidth?: number-End-->

**System capability:** SystemCapability.Web.Webview.Core

