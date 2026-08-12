# VideoController

Defines the video controller.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class VideoController--><!--Device-unnamed-export declare class VideoController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoController-constructor()--><!--Device-VideoController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## exitFullscreen

```TypeScript
exitFullscreen(): void
```

Provides a method to exit full screen playback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoController-exitFullscreen(): void--><!--Device-VideoController-exitFullscreen(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pause

```TypeScript
pause(): void
```

Provides a pause event for playback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoController-pause(): void--><!--Device-VideoController-pause(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## requestFullscreen

```TypeScript
requestFullscreen(value: boolean): void
```

Provides a full screen playback method.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoController-requestFullscreen(value: boolean): void--><!--Device-VideoController-requestFullscreen(value: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes |  |

## reset

```TypeScript
reset(): void
```

Provide the reset method of video playback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoController-reset(): void--><!--Device-VideoController-reset(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setCurrentTime

```TypeScript
setCurrentTime(value: double, seekMode?: SeekMode): void
```

Provide the progress method of video playback with SeekMode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoController-setCurrentTime(value: double, seekMode?: SeekMode): void--><!--Device-VideoController-setCurrentTime(value: double, seekMode?: SeekMode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes |  |
| seekMode | [SeekMode](arkts-arkui-video-seekmode-e.md) | No |  |

## start

```TypeScript
start(): void
```

Provides events to play.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoController-start(): void--><!--Device-VideoController-start(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stop

```TypeScript
stop(): void
```

Provides an event to stop playback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoController-stop(): void--><!--Device-VideoController-stop(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

