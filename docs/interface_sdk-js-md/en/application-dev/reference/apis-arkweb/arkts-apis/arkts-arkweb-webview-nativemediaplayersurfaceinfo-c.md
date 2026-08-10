# NativeMediaPlayerSurfaceInfo

[应用接管网页媒体播放功能](../../../reference/apis-arkweb/arkts-basic-components-web-attributes.md#enablenativemediaplayer12)中用于同层渲染的 surface 信息。

> **说明：**
> 
> - 本模块同时支持ArkTS-Dyn、ArkTS-Sta。
> 
> - 本Class首批接口从API version 12开始支持。
> 
> - 示例效果请以真机运行为准。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-webview-class NativeMediaPlayerSurfaceInfo--><!--Device-webview-class NativeMediaPlayerSurfaceInfo-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from 'kits/@kit.ArkWeb';
```

## id

```TypeScript
id: string
```

surface的id，用于同层渲染的NativeImage的surfaceId。

详见[NativeEmbedDataInfo](arkts-arkweb-web-nativeembeddatainfo-i.md)。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerSurfaceInfo-id: string--><!--Device-NativeMediaPlayerSurfaceInfo-id: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## rect

```TypeScript
rect: RectEvent
```

surface的位置信息。

**Type:** [RectEvent](arkts-arkweb-webview-rectevent-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerSurfaceInfo-rect: RectEvent--><!--Device-NativeMediaPlayerSurfaceInfo-rect: RectEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

