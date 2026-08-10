# Key

按键。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface Key--><!--Device-unnamed-export declare interface Key-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## Modules to Import

```TypeScript
import { KeyEvent, Action, Key } from 'kits/@kit.InputKit';
```

## code

```TypeScript
code: KeyCode
```

键值。

**Type:** [KeyCode](arkts-input-multimodalinput-keycode-keycode-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Key-code: KeyCode--><!--Device-Key-code: KeyCode-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## deviceId

```TypeScript
deviceId: int
```

输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Key-deviceId: int--><!--Device-Key-deviceId: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## pressedTime

```TypeScript
pressedTime: long
```

按键按下时间，表示系统启动运行至今逝去的微秒数，单位为微秒（μs）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Key-pressedTime: long--><!--Device-Key-pressedTime: long-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

