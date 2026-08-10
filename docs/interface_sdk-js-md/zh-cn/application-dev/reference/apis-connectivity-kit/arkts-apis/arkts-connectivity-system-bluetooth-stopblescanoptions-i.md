# StopBLEScanOptions

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

<!--Device-unnamed-export interface StopBLEScanOptions--><!--Device-unnamed-export interface StopBLEScanOptions-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Lite

## 导入模块

```TypeScript
import { BluetoothDevice, BLEFoundResponse, StopBLEScanOptions, SubscribeBLEFoundOptions, StartBLEScanOptions } from 'kits/@kit.ConnectivityKit';
```

## complete

```TypeScript
complete: () => void
```

StopBLEScanOptions completed

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-StopBLEScanOptions-complete: () => void--><!--Device-StopBLEScanOptions-complete: () => void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Lite

## fail

```TypeScript
fail: (data: string, code: number) => void
```

StopBLEScanOptions failed

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-StopBLEScanOptions-fail: (data: string, code: number) => void--><!--Device-StopBLEScanOptions-fail: (data: string, code: number) => void-End-->

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

StopBLEScanOptions success

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-StopBLEScanOptions-success: () => void--><!--Device-StopBLEScanOptions-success: () => void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Lite

