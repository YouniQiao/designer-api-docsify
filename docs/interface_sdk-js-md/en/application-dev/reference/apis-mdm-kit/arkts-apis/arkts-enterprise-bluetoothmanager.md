# @ohos.enterprise.bluetoothManager(Bluetooth Management)

This module provides device Bluetooth management capabilities, including setting Bluetooth switch states, querying Bluetooth information, and managing the Bluetooth device trustlist, Bluetooth device blocklist, and Bluetooth protocol blocklist. Through this module, enterprises can centrally manage Bluetooth functions on devices, enabling fine-grained control over Bluetooth device connections and enhancing enterprise information security. This is suitable for scenarios where enterprises need to regulate Bluetooth usage on employee devices.

> **NOTE：**&gt;
> The APIs of this module can be called only by a device administrator application that is enabled. For details, see
> [MDM Kit Development](../../../mdm/mdm-kit-guide.md).&gt;
> The global restriction policies are provided by **restrictions**. To disable Bluetooth globally, see
> [@ohos.enterprise.restrictions](arkts-enterprise-restrictions.md).

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { bluetoothManager } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addAllowedBluetoothDevices(Bluetooth Management)](arkts-mdm-bluetoothmanager-addallowedbluetoothdevices-f.md) |
| [addDisallowedBluetoothDevices(Bluetooth Management)](arkts-mdm-bluetoothmanager-adddisallowedbluetoothdevices-f.md) |
| [addDisallowedBluetoothProtocols(Bluetooth Management)](arkts-mdm-bluetoothmanager-adddisallowedbluetoothprotocols-f.md) |
| [addDisallowedBluetoothProtocols(Bluetooth Management)](arkts-mdm-bluetoothmanager-adddisallowedbluetoothprotocols-f.md) |
| [getAllowedBluetoothDevices(Bluetooth Management)](arkts-mdm-bluetoothmanager-getallowedbluetoothdevices-f.md) |
| [getAllowedBluetoothDevices(Bluetooth Management)](arkts-mdm-bluetoothmanager-getallowedbluetoothdevices-f.md) |
| [getBluetoothInfo(Bluetooth Management)](arkts-mdm-bluetoothmanager-getbluetoothinfo-f.md) |
| [getDisallowedBluetoothDevices(Bluetooth Management)](arkts-mdm-bluetoothmanager-getdisallowedbluetoothdevices-f.md) |
| [getDisallowedBluetoothDevices(Bluetooth Management)](arkts-mdm-bluetoothmanager-getdisallowedbluetoothdevices-f.md) |
| [getDisallowedBluetoothProtocols(Bluetooth Management)](arkts-mdm-bluetoothmanager-getdisallowedbluetoothprotocols-f.md) |
| [getDisallowedBluetoothProtocols(Bluetooth Management)](arkts-mdm-bluetoothmanager-getdisallowedbluetoothprotocols-f.md) |
| [removeAllowedBluetoothDevices(Bluetooth Management)](arkts-mdm-bluetoothmanager-removeallowedbluetoothdevices-f.md) |
| [removeDisallowedBluetoothDevices(Bluetooth Management)](arkts-mdm-bluetoothmanager-removedisallowedbluetoothdevices-f.md) |
| [removeDisallowedBluetoothProtocols(Bluetooth Management)](arkts-mdm-bluetoothmanager-removedisallowedbluetoothprotocols-f.md) |
| [removeDisallowedBluetoothProtocols(Bluetooth Management)](arkts-mdm-bluetoothmanager-removedisallowedbluetoothprotocols-f.md) |
| [turnOffBluetooth(Bluetooth Management)](arkts-mdm-bluetoothmanager-turnoffbluetooth-f.md) |
| [turnOnBluetooth(Bluetooth Management)](arkts-mdm-bluetoothmanager-turnonbluetooth-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [isBluetoothDisabled(Bluetooth Management)](arkts-mdm-bluetoothmanager-isbluetoothdisabled-f-sys.md) |
| [setBluetoothDisabled(Bluetooth Management)](arkts-mdm-bluetoothmanager-setbluetoothdisabled-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BluetoothInfo(Bluetooth Management)](arkts-mdm-bluetoothmanager-bluetoothinfo-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Protocol(Bluetooth Management)](arkts-mdm-bluetoothmanager-protocol-e.md) |
| [TransferPolicy(Bluetooth Management)](arkts-mdm-bluetoothmanager-transferpolicy-e.md) |
