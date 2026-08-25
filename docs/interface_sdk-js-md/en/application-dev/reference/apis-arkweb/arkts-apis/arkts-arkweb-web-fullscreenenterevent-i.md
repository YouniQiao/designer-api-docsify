# FullScreenEnterEvent

Provides details about the event that the **Web** component to enter the full-screen mode.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## handler

```TypeScript
handler: FullScreenExitHandler
```

Function handle for exiting full screen mode.

**Type:** [FullScreenExitHandler](arkts-arkweb-web-fullscreenexithandler-c.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## videoHeight

```TypeScript
videoHeight?: int
```

Video height, in px. If the element that enters fulls screen mode is a **&lt;video&gt;** element, the value represents its height; if the element that enters fulls screen mode contains a **&lt;video&gt;** element, the value represents the height of the first sub-video element; in other cases, the value is **0**.

**Type:** int

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## videoWidth

```TypeScript
videoWidth?: int
```

Video width, in px. If the element that enters fulls screen mode is a **&lt;video&gt;** element, the value represents its width; if the element that enters fulls screen mode contains a **&lt;video&gt;** element, the value represents the width of the first sub-video element; in other cases, the value is **0**.

**Type:** int

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core
