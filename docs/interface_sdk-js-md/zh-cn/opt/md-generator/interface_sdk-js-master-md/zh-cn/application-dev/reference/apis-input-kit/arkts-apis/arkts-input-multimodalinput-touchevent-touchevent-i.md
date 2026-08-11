# TouchEvent

触屏输入事件。

**继承/实现关系：** TouchEvent extends [InputEvent](arkts-input-multimodalinput-inputevent-inputevent-i.md)

**起始版本：** 9

<!--Device-unnamed-export declare interface TouchEvent extends InputEvent--><!--Device-unnamed-export declare interface TouchEvent extends InputEvent-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Core

## action

```TypeScript
action: Action
```

触屏输入事件类型。

**类型：** [Action](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-action-e.md)

**起始版本：** 9

<!--Device-TouchEvent-action: Action--><!--Device-TouchEvent-action: Action-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Core

## sourceType

```TypeScript
sourceType: SourceType
```

触屏来源的设备类型。

**类型：** [SourceType](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-sourcetype-e.md)

**起始版本：** 9

<!--Device-TouchEvent-sourceType: SourceType--><!--Device-TouchEvent-sourceType: SourceType-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Core

## touch

```TypeScript
touch: Touch
```

当前触屏点信息。

**类型：** [Touch](arkts-input-multimodalinput-touchevent-touch-i.md)

**起始版本：** 9

<!--Device-TouchEvent-touch: Touch--><!--Device-TouchEvent-touch: Touch-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Core

## touches

```TypeScript
touches: Touch[]
```

所有触屏点。

**类型：** [Touch](arkts-input-multimodalinput-touchevent-touch-i.md)[]

**起始版本：** 9

<!--Device-TouchEvent-touches: Touch[]--><!--Device-TouchEvent-touches: Touch[]-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Core
