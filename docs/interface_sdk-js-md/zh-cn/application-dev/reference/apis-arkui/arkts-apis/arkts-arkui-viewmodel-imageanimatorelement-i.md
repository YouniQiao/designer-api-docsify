# ImageAnimatorElement

Image animator element

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

<!--Device-unnamed-export interface ImageAnimatorElement--><!--Device-unnamed-export interface ImageAnimatorElement-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## getState

```TypeScript
getState(): "Playing" | "Paused" | "Stopped"
```

Obtains the playback state. Available values are as follows:Playing Paused Stopped

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-ImageAnimatorElement-getState(): "Playing" | "Paused" | "Stopped"--><!--Device-ImageAnimatorElement-getState(): "Playing" | "Paused" | "Stopped"-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**返回值：**

| 类型 | 说明 |
| --- | --- |
| "Playing" |  |

## pause

```TypeScript
pause(): void
```

Pauses the frame animation playback of an image.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-ImageAnimatorElement-pause(): void--><!--Device-ImageAnimatorElement-pause(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## resume

```TypeScript
resume(): void
```

Resumes the frame animation playback of an image.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-ImageAnimatorElement-resume(): void--><!--Device-ImageAnimatorElement-resume(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## start

```TypeScript
start(): void
```

Starts to play the frame animation of an image. If this method is called again, the playback starts from the first frame.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-ImageAnimatorElement-start(): void--><!--Device-ImageAnimatorElement-start(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## stop

```TypeScript
stop(): void
```

Stops the frame animation playback of an image.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-ImageAnimatorElement-stop(): void--><!--Device-ImageAnimatorElement-stop(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

