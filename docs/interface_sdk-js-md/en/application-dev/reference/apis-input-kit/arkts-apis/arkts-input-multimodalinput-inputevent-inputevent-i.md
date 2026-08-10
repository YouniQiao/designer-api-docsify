# InputEvent

设备上报的基本事件。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface InputEvent--><!--Device-unnamed-export declare interface InputEvent-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## Modules to Import

```TypeScript
import { InputEvent } from 'kits/@kit.InputKit';
```

## actionTime

```TypeScript
actionTime: long
```

上报输入事件的时间，表示系统启动运行至今逝去的微秒数，单位为微秒（μs）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-InputEvent-actionTime: long--><!--Device-InputEvent-actionTime: long-End-->

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

<!--Device-InputEvent-deviceId: int--><!--Device-InputEvent-deviceId: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## id

```TypeScript
id: int
```

事件ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-InputEvent-id: int--><!--Device-InputEvent-id: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## screenId

```TypeScript
screenId: int
```

目标屏幕ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-InputEvent-screenId: int--><!--Device-InputEvent-screenId: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## windowId

```TypeScript
windowId: int
```

目标窗口ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-InputEvent-windowId: int--><!--Device-InputEvent-windowId: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

