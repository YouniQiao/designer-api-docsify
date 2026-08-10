# KeyEvent

按键注入描述信息。

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

按键是否可以被拦截。

true表示可以被拦截，false表示不可被拦截。

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-KeyEvent-isIntercepted: boolean--><!--Device-KeyEvent-isIntercepted: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

## isPressed

```TypeScript
isPressed: boolean
```

按键是否按下。

true表示按键按下，false表示按键抬起。

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-KeyEvent-isPressed: boolean--><!--Device-KeyEvent-isPressed: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

## keyCode

```TypeScript
keyCode: int
```

按键键值。当前仅支持返回键/KEYCODE_BACK键。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-KeyEvent-keyCode: int--><!--Device-KeyEvent-keyCode: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

## keyDownDuration

```TypeScript
keyDownDuration: int
```

按键按下持续时间，单位为微秒（μs）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-KeyEvent-keyDownDuration: int--><!--Device-KeyEvent-keyDownDuration: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

