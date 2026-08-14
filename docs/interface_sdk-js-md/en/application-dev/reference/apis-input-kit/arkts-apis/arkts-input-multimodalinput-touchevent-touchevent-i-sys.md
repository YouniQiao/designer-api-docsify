# TouchEvent

Defines a touch event.

**Inheritance/Implementation:** TouchEvent extends [InputEvent](arkts-input-multimodalinput-inputevent-inputevent-i.md#InputEvent)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface TouchEvent--><!--Device-unnamed-export declare interface TouchEvent-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## Modules to Import

```TypeScript
import { KeyAction } from 'Action';
import { SourceType } from 'SourceType';
import { ToolType } from 'ToolType';
import { Touch } from 'Touch';
import { TouchEvent } from 'TouchEvent';
import { FixedMode } from 'FixedMode';
```

## fixedMode

```TypeScript
fixedMode?: FixedMode
```

Coordinate correction mode.

**Type:** [FixedMode](arkts-input-multimodalinput-touchevent-fixedmode-e-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-TouchEvent-fixedMode?: FixedMode--><!--Device-TouchEvent-fixedMode?: FixedMode-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

## isInject

```TypeScript
isInject?: boolean
```

Whether the touch event is an injection event. For details about injection events, see [@ohos.multimodalInput.inputEventClient](arkts-multimodalinput-inputeventclient.md#@ohos.multimodalInput.inputEventClient).

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-TouchEvent-isInject?: boolean--><!--Device-TouchEvent-isInject?: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

