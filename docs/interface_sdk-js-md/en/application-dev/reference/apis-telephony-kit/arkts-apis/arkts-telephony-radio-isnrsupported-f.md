# isNRSupported

## Modules to Import

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## isNRSupported

```TypeScript
function isNRSupported(): boolean
```

Checks whether the device supports 5G New Radio (NR).

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-radio-function isNRSupported(): boolean--><!--Device-radio-function isNRSupported(): boolean-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

## Examples

```TypeScript
let result: boolean = radio.isNRSupported();
console.info("Result: "+ result);
```


## isNRSupported

```TypeScript
function isNRSupported(slotId: int): boolean
```

Checks whether the device supports 5G New Radio (NR) by according card slot.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-radio-function isNRSupported(slotId: int): boolean--><!--Device-radio-function isNRSupported(slotId: int): boolean-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the card slot index int, ranging from 0 to the maximum card slot index number supported by the device. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

## Examples

```TypeScript
let slotId: number = 0;
let result: boolean = radio.isNRSupported(slotId);
console.info("Result: "+ result);
```

