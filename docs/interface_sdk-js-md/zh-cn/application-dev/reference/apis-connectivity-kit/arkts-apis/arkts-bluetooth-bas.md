# @ohos.bluetooth.bas

Provide methods to access BAS(Battery Service)-related capabilities.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace bas--><!--Device-unnamed-declare namespace bas-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { bas } from 'kits/@kit.ConnectivityKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [getRemoteDeviceBatteryInfo](arkts-connectivity-bas-getremotedevicebatteryinfo-f-sys.md#getremotedevicebatteryinfo) | Get remote device battery information. |
| [isBasSupported](arkts-connectivity-bas-isbassupported-f-sys.md#isbassupported) | Determine whether the local device can obtain the battery level of the remote device. |
| [offBatteryChange](arkts-connectivity-bas-offbatterychange-f-sys.md#offbatterychange) | Unsubscribe the event of battery state changes from a remote device. |
| [onBatteryChange](arkts-connectivity-bas-onbatterychange-f-sys.md#onbatterychange) | Subscribe the event of battery state changed from a remote device. |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [BatteryInfo](arkts-connectivity-bas-batteryinfo-i-sys.md) | Describe the contents of the battery information. |
<!--DelEnd-->

<!--Del-->
### 类型（系统接口）

| 名称 | 说明 |
| --- | --- |
| [BluetoothAddress](arkts-connectivity-bas-bluetoothaddress-t-sys.md) | Bluetooth device address. |
<!--DelEnd-->

