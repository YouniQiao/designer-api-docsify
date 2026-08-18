# NativeMediaPlayerSurfaceInfo

Implements a **NativeMediaPlayerSurfaceInfo** object to provide the surface information used for same-layer rendering [when the application takes over the media playback of the web page] (../../../reference/apis-arkweb/arkts-basic-components-web-attributes.md#enablenativemediaplayer12). > **NOTE：**> > - The sample effect is subject to the actual device.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-webview-class NativeMediaPlayerSurfaceInfo--><!--Device-webview-class NativeMediaPlayerSurfaceInfo-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## id

```TypeScript
id: string
```

Surface ID, which is the **psurfaceid** of the native image used for rendering at the same layer.<br>For details, see [NativeEmbedDataInfo](../../apis-arkweb/arkts-components/arkts-arkweb-nativeembeddatainfo-i.md).

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-NativeMediaPlayerSurfaceInfo-id: string--><!--Device-NativeMediaPlayerSurfaceInfo-id: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## rect

```TypeScript
rect: RectEvent
```

Position of the surface.

**Type:** [RectEvent](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-rectevent-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-NativeMediaPlayerSurfaceInfo-rect: RectEvent--><!--Device-NativeMediaPlayerSurfaceInfo-rect: RectEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

