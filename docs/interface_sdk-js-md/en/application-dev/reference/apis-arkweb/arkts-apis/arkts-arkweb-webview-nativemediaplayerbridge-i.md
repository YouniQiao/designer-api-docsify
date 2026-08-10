# NativeMediaPlayerBridge

[CreateNativeMediaPlayerCallback](../../../reference/apis-arkweb/arkts-apis-webview-t.md#createnativemediaplayercallback12)回调函数的返回值类型。接管网页媒体的播放器和ArkWeb内核之间的一个接口类。

ArkWeb内核通过该接口类的实例对象来控制应用创建的用来接管网页媒体的播放器。

> **说明：**
> 
> - 本模块同时支持ArkTS-Dyn、ArkTS-Sta。
> 
> - 本Interface首批接口从API version 12开始支持。
> 
> - 示例效果请以真机运行为准。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-webview-interface NativeMediaPlayerBridge--><!--Device-webview-interface NativeMediaPlayerBridge-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from 'kits/@kit.ArkWeb';
```

## enterFullscreen

```TypeScript
enterFullscreen: ZeroParamFn<>
```

播放器进入全屏。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerBridge-enterFullscreen: ZeroParamFn<>--><!--Device-NativeMediaPlayerBridge-enterFullscreen: ZeroParamFn<>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## exitFullscreen

```TypeScript
exitFullscreen: ZeroParamFn<>
```

播放器退出全屏。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerBridge-exitFullscreen: ZeroParamFn<>--><!--Device-NativeMediaPlayerBridge-exitFullscreen: ZeroParamFn<>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## pause

```TypeScript
pause: ZeroParamFn<>
```

暂停播放。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerBridge-pause: ZeroParamFn<>--><!--Device-NativeMediaPlayerBridge-pause: ZeroParamFn<>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## play

```TypeScript
play: ZeroParamFn<>
```

播放视频。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerBridge-play: ZeroParamFn<>--><!--Device-NativeMediaPlayerBridge-play: ZeroParamFn<>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## release

```TypeScript
release: ZeroParamFn<>
```

销毁播放器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerBridge-release: ZeroParamFn<>--><!--Device-NativeMediaPlayerBridge-release: ZeroParamFn<>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## resumePlayer

```TypeScript
resumePlayer?: ResumePlayerFn
```

通知应用销毁应用内播放器，并保存应用内播放器的状态信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerBridge-resumePlayer?: ResumePlayerFn--><!--Device-NativeMediaPlayerBridge-resumePlayer?: ResumePlayerFn-End-->

**System capability:** SystemCapability.Web.Webview.Core

## seek

```TypeScript
seek: OneParamFn<double>
```

播放跳转到某个时间点。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerBridge-seek: OneParamFn<double>--><!--Device-NativeMediaPlayerBridge-seek: OneParamFn<double>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## setMuted

```TypeScript
setMuted: OneParamFn<boolean>
```

设置静音状态。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerBridge-setMuted: OneParamFn<boolean>--><!--Device-NativeMediaPlayerBridge-setMuted: OneParamFn<boolean>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## setPlaybackRate

```TypeScript
setPlaybackRate: OneParamFn<double>
```

设置播放速度。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerBridge-setPlaybackRate: OneParamFn<double>--><!--Device-NativeMediaPlayerBridge-setPlaybackRate: OneParamFn<double>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## setVolume

```TypeScript
setVolume: OneParamFn<double>
```

设置播放器音量值。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerBridge-setVolume: OneParamFn<double>--><!--Device-NativeMediaPlayerBridge-setVolume: OneParamFn<double>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## suspendPlayer

```TypeScript
suspendPlayer?: SuspendPlayerFn
```

通知应用销毁应用内播放器，并保存应用内播放器的状态信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerBridge-suspendPlayer?: SuspendPlayerFn--><!--Device-NativeMediaPlayerBridge-suspendPlayer?: SuspendPlayerFn-End-->

**System capability:** SystemCapability.Web.Webview.Core

## updateRect

```TypeScript
updateRect: UpdateRectFn
```

更新surface位置信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerBridge-updateRect: UpdateRectFn--><!--Device-NativeMediaPlayerBridge-updateRect: UpdateRectFn-End-->

**System capability:** SystemCapability.Web.Webview.Core

