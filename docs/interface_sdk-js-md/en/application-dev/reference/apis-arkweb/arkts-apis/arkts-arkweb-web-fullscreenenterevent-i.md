# FullScreenEnterEvent

Web组件进入全屏回调事件的详情。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface FullScreenEnterEvent--><!--Device-unnamed-export declare interface FullScreenEnterEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## handler

```TypeScript
handler: FullScreenExitHandler
```

用于退出全屏模式的函数句柄。

**Type:** [FullScreenExitHandler](../arkts-components/arkts-arkweb-fullscreenexithandler-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-FullScreenEnterEvent-handler: FullScreenExitHandler--><!--Device-FullScreenEnterEvent-handler: FullScreenExitHandler-End-->

**System capability:** SystemCapability.Web.Webview.Core

## videoHeight

```TypeScript
videoHeight?: int
```

视频的高度，单位：px。如果进入全屏的是 `&lt;video&gt;` 元素，表示其高度；如果进入全屏的子元素中包含 `&lt;video&gt;` 元素，表示第一个子视频元素的高度；其他情况下，为0。

23

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-FullScreenEnterEvent-videoHeight?: int--><!--Device-FullScreenEnterEvent-videoHeight?: int-End-->

**System capability:** SystemCapability.Web.Webview.Core

## videoWidth

```TypeScript
videoWidth?: int
```

视频的宽度，单位：px。如果进入全屏的是 `&lt;video&gt;` 元素，表示其宽度；如果进入全屏的子元素中包含 `&lt;video&gt;` 元素，表示第一个子视频元素的宽度；其他情况下，为0。

23

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-FullScreenEnterEvent-videoWidth?: int--><!--Device-FullScreenEnterEvent-videoWidth?: int-End-->

**System capability:** SystemCapability.Web.Webview.Core

