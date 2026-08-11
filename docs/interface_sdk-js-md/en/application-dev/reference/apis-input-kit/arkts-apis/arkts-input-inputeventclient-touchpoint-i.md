# TouchPoint

Represents information about a single touch point on the display.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-inputEventClient-interface TouchPoint--><!--Device-inputEventClient-interface TouchPoint-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

## Modules to Import

```TypeScript
import { inputEventClient } from 'kits/@kit.InputKit';
```

## displayId

```TypeScript
displayId: int
```

Unique ID of the display where the touch point is located. The value must be an integer.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchPoint-displayId: int--><!--Device-TouchPoint-displayId: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

## displayX

```TypeScript
displayX: int
```

X coordinate of the touch point relative to the left edge of the display, in pixels. The value must be an integer.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchPoint-displayX: int--><!--Device-TouchPoint-displayX: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

## displayY

```TypeScript
displayY: int
```

Y coordinate of the touch point relative to the top edge of the display, in pixels. The value must be an integer.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchPoint-displayY: int--><!--Device-TouchPoint-displayY: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

## id

```TypeScript
id: int
```

Unique ID of a touch point. The value must be an integer in the range of [0, 9].

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchPoint-id: int--><!--Device-TouchPoint-id: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

