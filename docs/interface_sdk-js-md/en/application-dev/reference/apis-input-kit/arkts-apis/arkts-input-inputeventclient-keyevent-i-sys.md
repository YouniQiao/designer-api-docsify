# KeyEvent (System API)

Defines the key event to inject.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { inputEventClient } from '@kit.InputKit';
```

## isIntercepted

```TypeScript
isIntercepted: boolean
```

Whether the key event can be intercepted.The value **true** indicates that the key event can be intercepted, and the value **false** indicates the opposite.

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**System API:** This is a system API.

## isPressed

```TypeScript
isPressed: boolean
```

Whether the key is pressed.The value **true** indicates that the key is pressed, and the value **false** indicates that the key is released.

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**System API:** This is a system API.

## keyCode

```TypeScript
keyCode: int
```

Key code. Currently, only the **KEYCODE_BACK** key is supported.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**System API:** This is a system API.

## keyDownDuration

```TypeScript
keyDownDuration: int
```

Duration of key press, in microseconds (μs).

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**System API:** This is a system API.
