# RenderMode

Enumerates the rendering modes of the **Web** component. By default, the asynchronous rendering mode is used.

**Since:** 12

<!--Device-unnamed-declare enum RenderMode--><!--Device-unnamed-declare enum RenderMode-End-->

**System capability:** SystemCapability.Web.Webview.Core

## ASYNC_RENDER

```TypeScript
ASYNC_RENDER = 0
```

The **Web** component as a graphic surface node is rendered asynchronously and displayed independently. The maximum width of the **Web** component is 7,680 px (physical pixel)

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderMode-ASYNC_RENDER = 0--><!--Device-RenderMode-ASYNC_RENDER = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## SYNC_RENDER

```TypeScript
SYNC_RENDER = 1
```

The **Web** component as a graphic canvas node is rendered synchronously and displayed together with the system component. The maximum width of the **Web** component is 500,000 px (physical pixel).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderMode-SYNC_RENDER = 1--><!--Device-RenderMode-SYNC_RENDER = 1-End-->

**System capability:** SystemCapability.Web.Webview.Core

