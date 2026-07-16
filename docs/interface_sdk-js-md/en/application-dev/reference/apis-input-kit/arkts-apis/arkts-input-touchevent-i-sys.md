# TouchEvent

Defines a touch event.

**Inheritance/Implementation:** TouchEvent extends [InputEvent](arkts-input-inputevent-i.md)

**Since:** 9

<!--Device-unnamed-export declare interface TouchEvent extends InputEvent--><!--Device-unnamed-export declare interface TouchEvent extends InputEvent-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## Modules to Import

```TypeScript
import { SourceType, ToolType, TouchEvent, FixedMode, KeyAction, Touch } from '@kit.InputKit';
```

## fixedMode

```TypeScript
fixedMode?: FixedMode
```

Coordinate correction mode.

**Type:** FixedMode

**Since:** 19

<!--Device-TouchEvent-fixedMode?: FixedMode--><!--Device-TouchEvent-fixedMode?: FixedMode-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

## isInject

```TypeScript
isInject?: boolean
```

Whether the touch event is an injection event. For details about injection events, see [@ohos.multimodalInput.inputEventClient](arkts-multimodalinput-inputeventclient.md).

**Type:** boolean

**Since:** 20

<!--Device-TouchEvent-isInject?: boolean--><!--Device-TouchEvent-isInject?: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

