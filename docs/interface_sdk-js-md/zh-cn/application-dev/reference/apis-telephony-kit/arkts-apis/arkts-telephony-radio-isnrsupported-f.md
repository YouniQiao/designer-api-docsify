# isNRSupported

## 导入模块

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## isNRSupported

```TypeScript
function isNRSupported(): boolean
```

Checks whether the device supports 5G New Radio (NR).

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-radio-function isNRSupported(): boolean--><!--Device-radio-function isNRSupported(): boolean-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns { |

## 示例

```TypeScript
let result: boolean = radio.isNRSupported();
console.info("Result: "+ result);
```


## isNRSupported

```TypeScript
function isNRSupported(slotId: int): boolean
```

Checks whether the device supports 5G New Radio (NR) by according card slot.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-radio-function isNRSupported(slotId: int): boolean--><!--Device-radio-function isNRSupported(slotId: int): boolean-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the card slot index int, ranging from 0 to the maximum card slot index number supported by the device. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns { |

## 示例

```TypeScript
let slotId: number = 0;
let result: boolean = radio.isNRSupported(slotId);
console.info("Result: "+ result);
```

