# TouchEvent

Defines a touch event.

**Inheritance/Implementation:** TouchEvent extends [InputEvent](arkts-input-multimodalinput-inputevent-inputevent-i.md)

**Since:** 9

<!--Device-unnamed-export declare interface TouchEvent extends InputEvent--><!--Device-unnamed-export declare interface TouchEvent extends InputEvent-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## Modules to Import

```TypeScript
import { SourceType, ToolType, TouchEvent, FixedMode, KeyAction, Touch } from '@kit.InputKit';
```

## action

```TypeScript
action: Action
```

Event type.

**Type:** Action

**Since:** 9

<!--Device-TouchEvent-action: Action--><!--Device-TouchEvent-action: Action-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## sourceType

```TypeScript
sourceType: SourceType
```

Device type of the touch source.

**Type:** SourceType

**Since:** 9

<!--Device-TouchEvent-sourceType: SourceType--><!--Device-TouchEvent-sourceType: SourceType-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## touch

```TypeScript
touch: Touch
```

Current touch point.

**Type:** Touch

**Since:** 9

<!--Device-TouchEvent-touch: Touch--><!--Device-TouchEvent-touch: Touch-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## touches

```TypeScript
touches: Touch[]
```

All touch points.

**Type:** Touch[]

**Since:** 9

<!--Device-TouchEvent-touches: Touch[]--><!--Device-TouchEvent-touches: Touch[]-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

