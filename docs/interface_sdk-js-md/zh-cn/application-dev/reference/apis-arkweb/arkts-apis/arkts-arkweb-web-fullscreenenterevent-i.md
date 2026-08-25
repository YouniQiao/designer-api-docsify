# FullScreenEnterEvent

Web组件进入全屏回调事件的详情。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## handler

```TypeScript
handler: FullScreenExitHandler
```

用于退出全屏模式的函数句柄。

**类型：** [FullScreenExitHandler](arkts-arkweb-web-fullscreenexithandler-c.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## videoHeight

```TypeScript
videoHeight?: int
```

视频的高度，单位：px。如果进入全屏的是 `&lt;video&gt;` 元素，表示其高度；如果进入全屏的子元素中包含 `&lt;video&gt;` 元素，表示第一个子视频元素的高度；其他情况下，为0。23

**类型：** int

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## videoWidth

```TypeScript
videoWidth?: int
```

视频的宽度，单位：px。如果进入全屏的是 `&lt;video&gt;` 元素，表示其宽度；如果进入全屏的子元素中包含 `&lt;video&gt;` 元素，表示第一个子视频元素的宽度；其他情况下，为0。23

**类型：** int

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core
