# VideoElement

The &lt;video&gt; component provides a video player.

**继承/实现关系：** VideoElement extends [Element](arkts-arkui-viewmodel-element-i.md)

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

<!--Device-unnamed-export interface VideoElement extends Element--><!--Device-unnamed-export interface VideoElement extends Element-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## exitFullscreen

```TypeScript
exitFullscreen(): void
```

Requests to exit the full screen mode.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-VideoElement-exitFullscreen(): void--><!--Device-VideoElement-exitFullscreen(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## pause

```TypeScript
pause(): void
```

Requests to pause a video.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-VideoElement-pause(): void--><!--Device-VideoElement-pause(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## requestFullscreen

```TypeScript
requestFullscreen(param: { screenOrientation: "default" }): void
```

Requests to enter the full screen mode.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-VideoElement-requestFullscreen(param: { screenOrientation: "default" }): void--><!--Device-VideoElement-requestFullscreen(param: { screenOrientation: "default" }): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | { screenOrientation: "default" } | 是 |  |

## setCurrentTime

```TypeScript
setCurrentTime(param: { currenttime: number }): void
```

Specifies the video playing position.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-VideoElement-setCurrentTime(param: { currenttime: number }): void--><!--Device-VideoElement-setCurrentTime(param: { currenttime: number }): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | { currenttime: number } | 是 |  |

## start

```TypeScript
start(): void
```

Requests to start playing a video.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-VideoElement-start(): void--><!--Device-VideoElement-start(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## stop

```TypeScript
stop(): void
```

Requests to stop playing a video.

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-VideoElement-stop(): void--><!--Device-VideoElement-stop(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

