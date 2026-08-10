# SubscribeBLEFoundOptions

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

<!--Device-unnamed-export interface SubscribeBLEFoundOptions--><!--Device-unnamed-export interface SubscribeBLEFoundOptions-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Lite

## 导入模块

```TypeScript
import { BluetoothDevice, BLEFoundResponse, StopBLEScanOptions, SubscribeBLEFoundOptions, StartBLEScanOptions } from 'kits/@kit.ConnectivityKit';
```

## fail

```TypeScript
fail: (data: string, code: number) => void
```

SubscribeBLEFoundOptions failed

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-SubscribeBLEFoundOptions-fail: (data: string, code: number) => void--><!--Device-SubscribeBLEFoundOptions-fail: (data: string, code: number) => void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | 是 |  |
| code | number | 是 |  |

## success

```TypeScript
success: (data: BLEFoundResponse) => void
```

SubscribeBLEFoundOptions success

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-SubscribeBLEFoundOptions-success: (data: BLEFoundResponse) => void--><!--Device-SubscribeBLEFoundOptions-success: (data: BLEFoundResponse) => void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [BLEFoundResponse](arkts-connectivity-system-bluetooth-blefoundresponse-i.md) | 是 |  |

