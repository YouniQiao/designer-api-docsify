# VideoControllerAsync

Video playback controller class for asynchronous operations. Provides methods to control video playback, timing, and display mode.

**Since:** 26.0.0

**Deprecated since:** -1

<!--Device-unnamed-declare class VideoControllerAsync--><!--Device-unnamed-declare class VideoControllerAsync-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

Creates a VideoControllerAsync instance.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-VideoControllerAsync-constructor()--><!--Device-VideoControllerAsync-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## exitFullscreen

```TypeScript
exitFullscreen()
```

Exits fullscreen display mode.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-VideoControllerAsync-exitFullscreen()--><!--Device-VideoControllerAsync-exitFullscreen()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pause

```TypeScript
pause(): Promise<void>
```

Pauses video playback asynchronously.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-VideoControllerAsync-pause(): Promise<void>--><!--Device-VideoControllerAsync-pause(): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## requestFullscreen

```TypeScript
requestFullscreen(value: boolean)
```

Requests fullscreen display for the video.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-VideoControllerAsync-requestFullscreen(value: boolean)--><!--Device-VideoControllerAsync-requestFullscreen(value: boolean)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## reset

```TypeScript
reset(): Promise<void>
```

Resets the video controller asynchronously. Restores the controller to its initial state.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-VideoControllerAsync-reset(): Promise<void>--><!--Device-VideoControllerAsync-reset(): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setCurrentTime

```TypeScript
setCurrentTime(value: number, seekMode?: SeekMode)
```

Sets the current playback time with specified seek mode.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-VideoControllerAsync-setCurrentTime(value: double, seekMode?: SeekMode)--><!--Device-VideoControllerAsync-setCurrentTime(value: double, seekMode?: SeekMode)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| seekMode | [SeekMode](arkts-arkui-seekmode-e.md) | No |

## start

```TypeScript
start(): Promise<void>
```

Starts video playback asynchronously.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-VideoControllerAsync-start(): Promise<void>--><!--Device-VideoControllerAsync-start(): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## stop

```TypeScript
stop(): Promise<void>
```

Stops video playback asynchronously.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-VideoControllerAsync-stop(): Promise<void>--><!--Device-VideoControllerAsync-stop(): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
