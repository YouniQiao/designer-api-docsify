# StartBLEScanOptions

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

<!--Device-unnamed-export interface StartBLEScanOptions--><!--Device-unnamed-export interface StartBLEScanOptions-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Lite

## 导入模块

```TypeScript
import { BluetoothDevice, BLEFoundResponse, StopBLEScanOptions, SubscribeBLEFoundOptions, StartBLEScanOptions } from 'kits/@kit.ConnectivityKit';
```

## complete

```TypeScript
complete: () => void
```

StartBLEScanOptions completed

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-StartBLEScanOptions-complete: () => void--><!--Device-StartBLEScanOptions-complete: () => void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Lite

## fail

```TypeScript
fail: (data: string, code: number) => void
```

StartBLEScanOptions failed

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-StartBLEScanOptions-fail: (data: string, code: number) => void--><!--Device-StartBLEScanOptions-fail: (data: string, code: number) => void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | 是 |  |
| code | number | 是 |  |

## success

```TypeScript
success: () => void
```

StartBLEScanOptions success

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-StartBLEScanOptions-success: () => void--><!--Device-StartBLEScanOptions-success: () => void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Lite

## interval

```TypeScript
interval: number
```

Time of delay for reporting the scan result

**类型：** number

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-StartBLEScanOptions-interval: number--><!--Device-StartBLEScanOptions-interval: number-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Lite

