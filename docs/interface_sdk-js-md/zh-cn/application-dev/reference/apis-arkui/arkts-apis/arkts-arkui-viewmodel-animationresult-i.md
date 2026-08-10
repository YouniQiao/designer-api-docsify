# AnimationResult

AnimationResult

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

<!--Device-unnamed-export interface AnimationResult--><!--Device-unnamed-export interface AnimationResult-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## cancel

```TypeScript
cancel(): void
```

Cancels the animation.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-AnimationResult-cancel(): void--><!--Device-AnimationResult-cancel(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## finish

```TypeScript
finish(): void
```

Ends the animation.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-AnimationResult-finish(): void--><!--Device-AnimationResult-finish(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## oncancel

```TypeScript
oncancel: () => void
```

The animation is canceled.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-AnimationResult-oncancel: () => void--><!--Device-AnimationResult-oncancel: () => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onfinish

```TypeScript
onfinish: () => void
```

The animation is finished.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-AnimationResult-onfinish: () => void--><!--Device-AnimationResult-onfinish: () => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onrepeat

```TypeScript
onrepeat: () => void
```

The animation is repeated.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-AnimationResult-onrepeat: () => void--><!--Device-AnimationResult-onrepeat: () => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onstart

```TypeScript
onstart: () => void
```

The animation is started.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-AnimationResult-onstart: () => void--><!--Device-AnimationResult-onstart: () => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## pause

```TypeScript
pause(): void
```

Pauses the animation.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-AnimationResult-pause(): void--><!--Device-AnimationResult-pause(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## play

```TypeScript
play(): void
```

Starts the animation.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-AnimationResult-play(): void--><!--Device-AnimationResult-play(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## reverse

```TypeScript
reverse(): void
```

Plays the animation in reverse direction.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-AnimationResult-reverse(): void--><!--Device-AnimationResult-reverse(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## finished

```TypeScript
finished: boolean
```

Read-only attribute, which indicates whether the animation playback is complete.

**类型：** boolean

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-AnimationResult-finished: boolean--><!--Device-AnimationResult-finished: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## pending

```TypeScript
pending: boolean
```

Read-only attribute, which indicates whether an animation is waiting for the completion of other asynchronous operations(for example, start an animation with a delay).

**类型：** boolean

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-AnimationResult-pending: boolean--><!--Device-AnimationResult-pending: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## playstate

```TypeScript
playstate: string
```

Animation running state:idle: The animation is not running (playback ended or not started).running: The animation is running.paused: The animation is paused.finished: Animation playback ends.

**类型：** string

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-AnimationResult-playstate: string--><!--Device-AnimationResult-playstate: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## startTime

```TypeScript
startTime: number
```

Animation start time. This attribute is similar to that of delay in the options parameters.

**类型：** number

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-AnimationResult-startTime: number--><!--Device-AnimationResult-startTime: number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

