# RenderMode

Enumerates the rendering mode of Web components. By default, the asynchronous rendering mode is used. The asynchronous rendering mode is recommended because it has better performance and lower power consumption.@enum { number }

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## ASYNC_RENDER

```TypeScript
ASYNC_RENDER = 0
```

The Web component is rendered asynchronously. The ArkWeb component as a graphic surface node is displayed independently. The maximum width of the Web component is 7,680 px (physical pixel).

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## SYNC_RENDER

```TypeScript
SYNC_RENDER = 1
```

The Web component is rendered synchronously. The ArkWeb component as a graphic canvas node is displayed together with the system component. The maximum width of the Web component is 500,000 px (physical pixel).

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core
