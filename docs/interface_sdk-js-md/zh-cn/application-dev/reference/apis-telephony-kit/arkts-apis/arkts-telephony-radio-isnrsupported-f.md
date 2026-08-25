# isNRSupported

## 导入模块

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## isNRSupported

```TypeScript
function isNRSupported(): boolean
```

判断当前设备是否支持NR(New Radio)。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Telephony.CoreService

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
let result: boolean = radio.isNRSupported();
console.info("Result: "+ result);
```

ArkTS-Dyn示例：

```TypeScript
let slotId: number = 0;
let result: boolean = radio.isNRSupported(slotId);
console.info("Result: "+ result);
```

ArkTS-Sta示例：

```TypeScript
let slotId: int = 0;
let result: boolean = radio.isNRSupported(slotId);
console.info("Result: "+ result);
```


## isNRSupported

```TypeScript
function isNRSupported(slotId: int): boolean
```

判断当前设备是否支持NR(New Radio)。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

参见 [isNRSupported](#isnrsupported)
