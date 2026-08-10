# @ohos.bluetooth.common

Provide common Bluetooth interfaces and types.

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为26.0.0。

<!--Device-unnamed-declare namespace common--><!--Device-unnamed-declare namespace common-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { common } from 'kits/@kit.ConnectivityKit';
```

## 汇总

### 接口

| 名称 | 说明 |
| --- | --- |
| [BluetoothAddress](arkts-connectivity-common-bluetoothaddress-i.md) | Describe the type of Bluetooth address. |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [BluetoothAddressType](arkts-connectivity-common-bluetoothaddresstype-e.md) | Enum for the type of Bluetooth address. |
| [BluetoothRawAddressType](arkts-connectivity-common-bluetoothrawaddresstype-e.md) | Enum for the type of Bluetooth raw address.The enum is used only when the {@link BluetoothAddress#addressType} is {@link BluetoothAddressType#REAL}. |

