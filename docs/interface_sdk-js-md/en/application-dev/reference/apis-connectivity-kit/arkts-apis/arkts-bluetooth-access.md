# @ohos.bluetooth.access

Provides methods for enabling/disabling bluetooth or monitoring bluetooth state.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace access--><!--Device-unnamed-declare namespace access-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { access } from 'access';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [addPersistentDeviceId](arkts-connectivity-access-addpersistentdeviceid-f.md#addPersistentDeviceId) | Add a persistent random device address. Once the randomized address is successfully added, the application can save it for an extended period of time. |
| [convertUuid](arkts-connectivity-access-convertuuid-f.md#convertUuid) | Convert 2-byte and 4-byte UUID strings to the 16-byte UUID string standard used in Bluetooth. |
| [deletePersistentDeviceId](arkts-connectivity-access-deletepersistentdeviceid-f.md#deletePersistentDeviceId) | Delete a persistent random device address. |
| [disableBluetooth](arkts-connectivity-access-disablebluetooth-f.md#disableBluetooth) | Disables Bluetooth on a device. |
| [disableBluetoothAsync](arkts-connectivity-access-disablebluetoothasync-f.md#disableBluetoothAsync) | Asynchronous interface for disables Bluetooth on a device. |
| [enableBluetooth](arkts-connectivity-access-enablebluetooth-f.md#enableBluetooth) | Enables Bluetooth on a device. |
| [enableBluetoothAsync](arkts-connectivity-access-enablebluetoothasync-f.md#enableBluetoothAsync) | Asynchronous interface for enables Bluetooth on a device. |
| [getPersistentDeviceIds](arkts-connectivity-access-getpersistentdeviceids-f.md#getPersistentDeviceIds) | Obtains the persistent randomized device address of the application. |
| [getState](arkts-connectivity-access-getstate-f.md#getState) | Obtains the Bluetooth status of a device. |
| [isBluetoothSupported](arkts-connectivity-access-isbluetoothsupported-f.md#isBluetoothSupported) | Check whether Bluetooth is available. |
| [isValidRandomDeviceId](arkts-connectivity-access-isvalidrandomdeviceid-f.md#isValidRandomDeviceId) | Determine whether the randomized device address application can still be used. |
| [offStateChange](arkts-connectivity-access-offstatechange-f.md#offStateChange) | Unsubscribe the event reported when the Bluetooth state changes. |
| off_stateChange | Unsubscribe the event reported when the Bluetooth state changes. |
| [onStateChange](arkts-connectivity-access-onstatechange-f.md#onStateChange) | Subscribe the event reported when the Bluetooth state changes. |
| on_stateChange | Subscribe the event reported when the Bluetooth state changes. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [factoryReset](arkts-connectivity-access-factoryreset-f-sys.md#factoryReset) | Restoring bluetooth settings. |
| [factoryReset](arkts-connectivity-access-factoryreset-f-sys.md#factoryReset-(System-API)) | Restoring bluetooth settings. |
| [getLocalAddress](arkts-connectivity-access-getlocaladdress-f-sys.md#getLocalAddress) | Obtaining the MAC address of the local device. |
| [notifyDialogResult](arkts-connectivity-access-notifydialogresult-f-sys.md#notifyDialogResult) | Notify bluetooth the result of bluetooth dialog. |
| [restrictBluetooth](arkts-connectivity-access-restrictbluetooth-f-sys.md#restrictBluetooth) | Restrict Bluetooth BR/EDR ability on a device. |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [NotifyDialogResultParams](arkts-connectivity-access-notifydialogresultparams-i-sys.md) | Describes the result of bluetooth dialog. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [BluetoothState](arkts-connectivity-access-bluetoothstate-e.md) | The enum of bluetooth state. |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [DialogType](arkts-connectivity-access-dialogtype-e-sys.md) | The enum of bluetooth dialog type. |
<!--DelEnd-->

