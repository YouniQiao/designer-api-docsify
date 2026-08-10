# VideoController

一个VideoController对象可以控制一个或多个Video。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class VideoController--><!--Device-unnamed-export declare class VideoController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

VideoController的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoController-constructor()--><!--Device-VideoController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## exitFullscreen

```TypeScript
exitFullscreen(): void
```

退出全屏播放。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoController-exitFullscreen(): void--><!--Device-VideoController-exitFullscreen(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pause

```TypeScript
pause(): void
```

暂停播放，显示当前帧，再次播放时从当前位置继续播放。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoController-pause(): void--><!--Device-VideoController-pause(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## requestFullscreen

```TypeScript
requestFullscreen(value: boolean): void
```

请求全屏播放。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoController-requestFullscreen(value: boolean): void--><!--Device-VideoController-requestFullscreen(value: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | 是否全屏（填充满应用窗口）播放。 true：请求全屏播放；false：不请求全屏播放。 默认值：false |

## reset

```TypeScript
reset(): void
```

Video组件重置AVPlayer。显示当前帧，再次播放时从头开始播放。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoController-reset(): void--><!--Device-VideoController-reset(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setCurrentTime

```TypeScript
setCurrentTime(value: double, seekMode?: SeekMode): void
```

指定视频播放的进度位置，并指定跳转模式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoController-setCurrentTime(value: double, seekMode?: SeekMode): void--><!--Device-VideoController-setCurrentTime(value: double, seekMode?: SeekMode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | 视频播放进度位置，单位：秒。 |
| seekMode | [SeekMode](../arkts-components/arkts-arkui-seekmode-e.md) | No | 跳转模式。 |

## start

```TypeScript
start(): void
```

开始播放。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoController-start(): void--><!--Device-VideoController-start(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stop

```TypeScript
stop(): void
```

停止播放，显示当前帧，再次播放时从头开始播放。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoController-stop(): void--><!--Device-VideoController-stop(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

