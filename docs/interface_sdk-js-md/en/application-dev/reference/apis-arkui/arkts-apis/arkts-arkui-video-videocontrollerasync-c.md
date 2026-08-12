# VideoControllerAsync

Video playback controller class for asynchronous operations.Provides methods to control video playback, timing, and display mode.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare class VideoControllerAsync--><!--Device-unnamed-export declare class VideoControllerAsync-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

Creates a VideoControllerAsync instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoControllerAsync-constructor()--><!--Device-VideoControllerAsync-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## exitFullscreen

```TypeScript
exitFullscreen(): void
```

Exits fullscreen display mode.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoControllerAsync-exitFullscreen(): void--><!--Device-VideoControllerAsync-exitFullscreen(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pause

```TypeScript
pause(): Promise<void>
```

Pauses video playback asynchronously.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoControllerAsync-pause(): Promise<void>--><!--Device-VideoControllerAsync-pause(): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

## requestFullscreen

```TypeScript
requestFullscreen(value: boolean): void
```

Requests fullscreen display for the video.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoControllerAsync-requestFullscreen(value: boolean): void--><!--Device-VideoControllerAsync-requestFullscreen(value: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes |  |

## reset

```TypeScript
reset(): Promise<void>
```

Resets the video controller asynchronously.Restores the controller to its initial state.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoControllerAsync-reset(): Promise<void>--><!--Device-VideoControllerAsync-reset(): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

## setCurrentTime

```TypeScript
setCurrentTime(value: double, seekMode?: SeekMode): void
```

Sets the current playback time with specified seek mode.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoControllerAsync-setCurrentTime(value: double, seekMode?: SeekMode): void--><!--Device-VideoControllerAsync-setCurrentTime(value: double, seekMode?: SeekMode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | &lt;br&gt;Unit: Seconds, The value must be greater than or equal to 0, The value must be greater than or equal to 0, The maximum value is the total duration of the video. If the duration exceeds the maximum value, the system jumps to the end of the video. |
| seekMode | [SeekMode](arkts-arkui-video-seekmode-e.md) | No |  |

## start

```TypeScript
start(): Promise<void>
```

Starts video playback asynchronously.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoControllerAsync-start(): Promise<void>--><!--Device-VideoControllerAsync-start(): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

## stop

```TypeScript
stop(): Promise<void>
```

Stops video playback asynchronously.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoControllerAsync-stop(): Promise<void>--><!--Device-VideoControllerAsync-stop(): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

