# KeyEvent (System API)

Defines the key event to inject.

**Since:** 23

<!--Device-inputEventClient-interface KeyEvent--><!--Device-inputEventClient-interface KeyEvent-End-->

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

Whether the key event can be intercepted.

The value **true** indicates that the key event can be intercepted, and the value **false** indicates the opposite.

**Type:** boolean

**Since:** 23

<!--Device-KeyEvent-isIntercepted: boolean--><!--Device-KeyEvent-isIntercepted: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**System API:** This is a system API.

## isPressed

```TypeScript
isPressed: boolean
```

Whether the key is pressed.

The value **true** indicates that the key is pressed, and the value **false** indicates that the key is released.

**Type:** boolean

**Since:** 23

<!--Device-KeyEvent-isPressed: boolean--><!--Device-KeyEvent-isPressed: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**System API:** This is a system API.

## keyCode

```TypeScript
keyCode: int
```

Key code. Currently, only the **KEYCODE_BACK** key is supported.

**Type:** int

**Since:** 23

<!--Device-KeyEvent-keyCode: int--><!--Device-KeyEvent-keyCode: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**System API:** This is a system API.

## keyDownDuration

```TypeScript
keyDownDuration: int
```

Duration of key press, in microseconds (μs).

**Type:** int

**Since:** 23

<!--Device-KeyEvent-keyDownDuration: int--><!--Device-KeyEvent-keyDownDuration: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**System API:** This is a system API.

