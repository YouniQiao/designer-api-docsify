# KeyEvent

Defines the key event to inject.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-inputEventClient-interface KeyEvent--><!--Device-inputEventClient-interface KeyEvent-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

## Modules to Import

```TypeScript
import { inputEventClient } from 'kits/@kit.InputKit';
```

## isIntercepted

```TypeScript
isIntercepted: boolean
```

Whether the key event can be intercepted.

The value **true** indicates that the key event can be intercepted, and the value **false** indicates the opposite.

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-KeyEvent-isIntercepted: boolean--><!--Device-KeyEvent-isIntercepted: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

## isPressed

```TypeScript
isPressed: boolean
```

Whether the key is pressed.

The value **true** indicates that the key is pressed, and the value **false** indicates that the key is released.

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-KeyEvent-isPressed: boolean--><!--Device-KeyEvent-isPressed: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

## keyCode

```TypeScript
keyCode: int
```

Key code. Currently, only the **KEYCODE_BACK** key is supported.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-KeyEvent-keyCode: int--><!--Device-KeyEvent-keyCode: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

## keyDownDuration

```TypeScript
keyDownDuration: int
```

Duration of key press, in microseconds (μs).

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-KeyEvent-keyDownDuration: int--><!--Device-KeyEvent-keyDownDuration: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

