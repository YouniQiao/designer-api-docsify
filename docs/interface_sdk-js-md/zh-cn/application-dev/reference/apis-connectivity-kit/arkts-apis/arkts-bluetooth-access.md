# @ohos.bluetooth.access

Provides methods for enabling/disabling bluetooth or monitoring bluetooth state.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-unnamed-declare namespace access--><!--Device-unnamed-declare namespace access-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { access } from 'kits/@kit.ConnectivityKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [addPersistentDeviceId](arkts-connectivity-access-addpersistentdeviceid-f.md#addpersistentdeviceid) | Add a persistent random device address. Once the randomized address is successfully added,the application can save it for an extended period of time. |
| [convertUuid](arkts-connectivity-access-convertuuid-f.md#convertuuid) | Convert 2-byte and 4-byte UUID strings to the 16-byte UUID string standard used in Bluetooth. |
| [deletePersistentDeviceId](arkts-connectivity-access-deletepersistentdeviceid-f.md#deletepersistentdeviceid) | Delete a persistent random device address. |
| [disableBluetooth](arkts-connectivity-access-disablebluetooth-f.md#disablebluetooth) | Disables Bluetooth on a device. |
| [disableBluetoothAsync](arkts-connectivity-access-disablebluetoothasync-f.md#disablebluetoothasync) | Asynchronous interface for disables Bluetooth on a device. |
| [enableBluetooth](arkts-connectivity-access-enablebluetooth-f.md#enablebluetooth) | Enables Bluetooth on a device. |
| [enableBluetoothAsync](arkts-connectivity-access-enablebluetoothasync-f.md#enablebluetoothasync) | Asynchronous interface for enables Bluetooth on a device. |
| [getPersistentDeviceIds](arkts-connectivity-access-getpersistentdeviceids-f.md#getpersistentdeviceids) | Obtains the persistent randomized device address of the application. |
| [getState](arkts-connectivity-access-getstate-f.md#getstate) | Obtains the Bluetooth status of a device. |
| [isBluetoothSupported](arkts-connectivity-access-isbluetoothsupported-f.md#isbluetoothsupported) | Check whether Bluetooth is available. |
| [isValidRandomDeviceId](arkts-connectivity-access-isvalidrandomdeviceid-f.md#isvalidrandomdeviceid) | Determine whether the randomized device address application can still be used. |
| [off](arkts-connectivity-access-off-f.md#off) | Unsubscribe the event reported when the Bluetooth state changes. |
| [offStateChange](arkts-connectivity-access-offstatechange-f.md#offstatechange) | Unsubscribe the event reported when the Bluetooth state changes. |
| [on](arkts-connectivity-access-on-f.md#on) | Subscribe the event reported when the Bluetooth state changes. |
| [onStateChange](arkts-connectivity-access-onstatechange-f.md#onstatechange) | Subscribe the event reported when the Bluetooth state changes. |

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [factoryReset](arkts-connectivity-access-factoryreset-f-sys.md#factoryreset) | Restoring bluetooth settings. |
| [factoryReset](arkts-connectivity-access-factoryreset-f-sys.md#factoryreset-1) | Restoring bluetooth settings. |
| [getLocalAddress](arkts-connectivity-access-getlocaladdress-f-sys.md#getlocaladdress) | Obtaining the MAC address of the local device. |
| [notifyDialogResult](arkts-connectivity-access-notifydialogresult-f-sys.md#notifydialogresult) | Notify bluetooth the result of bluetooth dialog. |
| [restrictBluetooth](arkts-connectivity-access-restrictbluetooth-f-sys.md#restrictbluetooth) | Restrict Bluetooth BR/EDR ability on a device. |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [NotifyDialogResultParams](arkts-connectivity-access-notifydialogresultparams-i-sys.md) | Describes the result of bluetooth dialog. |
<!--DelEnd-->

### 枚举

| 名称 | 说明 |
| --- | --- |
| [BluetoothState](arkts-connectivity-access-bluetoothstate-e.md) | The enum of bluetooth state. |

<!--Del-->
### 枚举（系统接口）

| 名称 | 说明 |
| --- | --- |
| [DialogType](arkts-connectivity-access-dialogtype-e-sys.md) | The enum of bluetooth dialog type. |
<!--DelEnd-->

