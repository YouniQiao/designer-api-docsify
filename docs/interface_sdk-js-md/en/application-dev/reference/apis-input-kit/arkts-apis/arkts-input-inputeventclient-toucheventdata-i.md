# TouchEventData

Defines the touch event data.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-inputEventClient-interface TouchEventData--><!--Device-inputEventClient-interface TouchEventData-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

## Modules to Import

```TypeScript
import { inputEventClient } from '@kit.InputKit';
```

## touchEvent

```TypeScript
touchEvent: TouchEvent
```

Touch event.

**Type:** [TouchEvent](arkts-input-multimodalinput-touchevent-touchevent-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-TouchEventData-touchEvent: TouchEvent--><!--Device-TouchEventData-touchEvent: TouchEvent-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

## useGlobalCoordinate

```TypeScript
useGlobalCoordinate?: boolean
```

Whether to use global coordinates to calculate the injected touch event. The default value is **false**. If this parameter is set to **false**, the coordinates of the relative coordinate system with the upper left corner of the specified screen as the origin are used to calculate the injected touch event. If this parameter is set to  
**true**, the coordinates of the global coordinate system with the upper left corner of the primary screen as the origin are used to calculate the injected touch event.

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-TouchEventData-useGlobalCoordinate?: boolean--><!--Device-TouchEventData-useGlobalCoordinate?: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

