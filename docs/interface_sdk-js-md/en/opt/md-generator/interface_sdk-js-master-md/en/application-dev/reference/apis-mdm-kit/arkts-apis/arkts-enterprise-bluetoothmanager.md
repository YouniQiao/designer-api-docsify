# @ohos.enterprise.bluetoothManager

This module provides device Bluetooth management capabilities, including setting Bluetooth switch states, querying Bluetooth information, and managing the Bluetooth device trustlist, Bluetooth device blocklist, and Bluetooth protocol blocklist. Through this module, enterprises can centrally manage Bluetooth functions on devices, enabling fine-grained control over Bluetooth device connections and enhancing enterprise information security. This is suitable for scenarios where enterprises need to regulate Bluetooth usage on employee devices. > **NOTE：**> > The APIs of this module can be called only by a device administrator application that is enabled. For details, see > [MDM Kit Development](../../../mdm/mdm-kit-guide.md). > > The global restriction policies are provided by **restrictions**. To disable Bluetooth globally, see > [@ohos.enterprise.restrictions](arkts-enterprise-restrictions.md#@ohos.enterprise.restrictions).

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace bluetoothManager--><!--Device-unnamed-declare namespace bluetoothManager-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { bluetoothManager } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addAllowedBluetoothDevices](arkts-mdm-bluetoothmanager-addallowedbluetoothdevices-f.md#addAllowedBluetoothDevices) |
| [addDisallowedBluetoothDevices](arkts-mdm-bluetoothmanager-adddisallowedbluetoothdevices-f.md#addDisallowedBluetoothDevices) |
| [addDisallowedBluetoothProtocols](arkts-mdm-bluetoothmanager-adddisallowedbluetoothprotocols-f.md#addDisallowedBluetoothProtocols) |
| [addDisallowedBluetoothProtocols](arkts-mdm-bluetoothmanager-adddisallowedbluetoothprotocols-f.md#addDisallowedBluetoothProtocols) |
| [getAllowedBluetoothDevices](arkts-mdm-bluetoothmanager-getallowedbluetoothdevices-f.md#getAllowedBluetoothDevices) |
| [getAllowedBluetoothDevices](arkts-mdm-bluetoothmanager-getallowedbluetoothdevices-f.md#getAllowedBluetoothDevices) |
| [getBluetoothInfo](arkts-mdm-bluetoothmanager-getbluetoothinfo-f.md#getBluetoothInfo) |
| [getDisallowedBluetoothDevices](arkts-mdm-bluetoothmanager-getdisallowedbluetoothdevices-f.md#getDisallowedBluetoothDevices) |
| [getDisallowedBluetoothDevices](arkts-mdm-bluetoothmanager-getdisallowedbluetoothdevices-f.md#getDisallowedBluetoothDevices) |
| [getDisallowedBluetoothProtocols](arkts-mdm-bluetoothmanager-getdisallowedbluetoothprotocols-f.md#getDisallowedBluetoothProtocols) |
| [getDisallowedBluetoothProtocols](arkts-mdm-bluetoothmanager-getdisallowedbluetoothprotocols-f.md#getDisallowedBluetoothProtocols) |
| [removeAllowedBluetoothDevices](arkts-mdm-bluetoothmanager-removeallowedbluetoothdevices-f.md#removeAllowedBluetoothDevices) |
| [removeDisallowedBluetoothDevices](arkts-mdm-bluetoothmanager-removedisallowedbluetoothdevices-f.md#removeDisallowedBluetoothDevices) |
| [removeDisallowedBluetoothProtocols](arkts-mdm-bluetoothmanager-removedisallowedbluetoothprotocols-f.md#removeDisallowedBluetoothProtocols) |
| [removeDisallowedBluetoothProtocols](arkts-mdm-bluetoothmanager-removedisallowedbluetoothprotocols-f.md#removeDisallowedBluetoothProtocols) |
| [turnOffBluetooth](arkts-mdm-bluetoothmanager-turnoffbluetooth-f.md#turnOffBluetooth) |
| [turnOnBluetooth](arkts-mdm-bluetoothmanager-turnonbluetooth-f.md#turnOnBluetooth) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [isBluetoothDisabled](arkts-mdm-bluetoothmanager-isbluetoothdisabled-f-sys.md#isBluetoothDisabled-(System-API)) |
| [setBluetoothDisabled](arkts-mdm-bluetoothmanager-setbluetoothdisabled-f-sys.md#setBluetoothDisabled-(System-API)) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BluetoothInfo](arkts-mdm-bluetoothmanager-bluetoothinfo-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Protocol](arkts-mdm-bluetoothmanager-protocol-e.md) |
| [TransferPolicy](arkts-mdm-bluetoothmanager-transferpolicy-e.md) |
