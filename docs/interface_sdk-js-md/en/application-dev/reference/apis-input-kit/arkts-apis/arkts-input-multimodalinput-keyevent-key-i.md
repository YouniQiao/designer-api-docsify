# Key

Defines a key.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface Key--><!--Device-unnamed-export declare interface Key-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## Modules to Import

```TypeScript
import { KeyEvent, Action, Key } from '@kit.InputKit';
```

## code

```TypeScript
code: KeyCode
```

Key code.

**Type:** [KeyCode](arkts-input-multimodalinput-keycode-keycode-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Key-code: KeyCode--><!--Device-Key-code: KeyCode-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## deviceId

```TypeScript
deviceId: int
```

Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Key-deviceId: int--><!--Device-Key-deviceId: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## pressedTime

```TypeScript
pressedTime: long
```

Time when the key is pressed, in microseconds (μs) since the system starts.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Key-pressedTime: long--><!--Device-Key-pressedTime: long-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

