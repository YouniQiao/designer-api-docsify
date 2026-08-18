# @ohos.enterprise.bluetoothManager

This module provides device Bluetooth management capabilities, including setting Bluetooth switch states, querying Bluetooth information, and managing the Bluetooth device trustlist, Bluetooth device blocklist, and Bluetooth protocol blocklist. Through this module, enterprises can centrally manage Bluetooth functions on devices, enabling fine-grained control over Bluetooth device connections and enhancing enterprise information security. This is suitable for scenarios where enterprises need to regulate Bluetooth usage on employee devices. > **NOTE：**> > The APIs of this module can be called only by a device administrator application that is enabled. For details, see > [MDM Kit Development](../../../mdm/mdm-kit-guide.md). > > The global restriction policies are provided by **restrictions**. To disable Bluetooth globally, see > [@ohos.enterprise.restrictions](arkts-enterprise-restrictions.md).

**Since:** 11

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

| Name | Description |
| --- | --- |
| [addAllowedBluetoothDevices](arkts-mdm-bluetoothmanager-addallowedbluetoothdevices-f.md) | Adds Bluetooth devices to the trustlist. After adding devices to this list, the current device will only be allowed to connect to Bluetooth devices in the list. Since API version 22, the MAC addresses in the array must comply with the Bluetooth MAC address specifications (for example, 00:1A:2B:3C:4D:5E). Invalid MAC addresses will be removed and only valid MAC addresses will be added. A policy conflict is reported when this API is called in the following scenarios: 1. Bluetooth has been disabled via [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md). In this case, you can call [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md) enable Bluetooth to solve the conflict. 2. Disallowed Bluetooth devices have been added by calling [addDisallowedBluetoothDevices](arkts-mdm-bluetoothmanager-adddisallowedbluetoothdevices-f.md). You can resolve the conflict by removing disallowed Bluetooth devices through [removeDisallowedBluetoothDevices](arkts-mdm-bluetoothmanager-removedisallowedbluetoothdevices-f.md). |
| [addDisallowedBluetoothDevices](arkts-mdm-bluetoothmanager-adddisallowedbluetoothdevices-f.md) | Adds Bluetooth devices to the blocklist. The current device cannot connect to the disallowed Bluetooth devices. Since API version 22, the MAC addresses in the array must comply with the Bluetooth MAC address specifications (for example, 00:1A:2B:3C:4D:5E). Invalid MAC addresses will be removed and only valid MAC addresses will be added. A policy conflict is reported when this API is called in the following scenarios: 1. Bluetooth has been disabled via [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md). In this case, you can call [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md) enable Bluetooth to solve the conflict. 2. Allowed Bluetooth devices have been added by calling [addAllowedBluetoothDevices](arkts-mdm-bluetoothmanager-addallowedbluetoothdevices-f.md). You can resolve the conflict by removing allowed Bluetooth devices through [removeAllowedBluetoothDevices](arkts-mdm-bluetoothmanager-removeallowedbluetoothdevices-f.md). |
| [addDisallowedBluetoothProtocols](arkts-mdm-bluetoothmanager-adddisallowedbluetoothprotocols-f.md) | Adds disallowed Bluetooth protocols. Specified users cannot use the disallowed Bluetooth protocols to send files to other devices. This API is used to disable the GATT or SPP protocol, which does not take effect for system services and system applications. When the SPP protocol is passed, both the receiving and sending functions are disabled. |
| [addDisallowedBluetoothProtocols](arkts-mdm-bluetoothmanager-adddisallowedbluetoothprotocols-f.md) | Adds disallowed Bluetooth protocols. After the setting, specified users cannot use the disallowed Bluetooth protocols based on the specified transfer policy. > **NOTE：**> > 1. This API is used to disable the GATT or SPP protocol, which does not take effect for system services and > system applications. > > 2. When the SPP protocol is passed, the value of the **policy** parameter can only be > **TransferPolicy.RECEIVE_SEND**. Otherwise, error code 9200012 will be returned. > > 3. This API and > [addDisallowedBluetoothProtocols&lt;sup&gt;20+&lt;/sup&gt;](arkts-mdm-bluetoothmanager-adddisallowedbluetoothprotocols-f.md) are > overloaded APIs. This API adds the **policy** parameter to specify the transfer policy, enabling more fine- > grained control over Bluetooth protocol disabling behavior (for example, blocking only sending, only receiving, > or both sending and receiving). If both APIs are used to configure disabling policies, the policies will be > combined and take effect. |
| [getAllowedBluetoothDevices](arkts-mdm-bluetoothmanager-getallowedbluetoothdevices-f.md) | Obtains allowed Bluetooth devices. |
| [getAllowedBluetoothDevices](arkts-mdm-bluetoothmanager-getallowedbluetoothdevices-f.md) | Obtains allowed Bluetooth devices. |
| [getBluetoothInfo](arkts-mdm-bluetoothmanager-getbluetoothinfo-f.md) | Obtains device Bluetooth information. |
| [getDisallowedBluetoothDevices](arkts-mdm-bluetoothmanager-getdisallowedbluetoothdevices-f.md) | Obtains disallowed Bluetooth devices. |
| [getDisallowedBluetoothDevices](arkts-mdm-bluetoothmanager-getdisallowedbluetoothdevices-f.md) | Obtains disallowed Bluetooth devices. |
| [getDisallowedBluetoothProtocols](arkts-mdm-bluetoothmanager-getdisallowedbluetoothprotocols-f.md) | Obtains the disallowed Bluetooth protocols of a specified user. |
| [getDisallowedBluetoothProtocols](arkts-mdm-bluetoothmanager-getdisallowedbluetoothprotocols-f.md) | Obtains the list of disallowed Bluetooth protocols for a specified user under a specified transfer policy. > **NOTE：**> > 1. This API and > [getDisallowedBluetoothProtocols&lt;sup&gt;20+&lt;/sup&gt;](arkts-mdm-bluetoothmanager-getdisallowedbluetoothprotocols-f.md) are > overloaded APIs. This API adds the **policy** parameter to query the disallowing configuration based on the > transfer policy. |
| [removeAllowedBluetoothDevices](arkts-mdm-bluetoothmanager-removeallowedbluetoothdevices-f.md) | Removes allowed Bluetooth devices. |
| [removeDisallowedBluetoothDevices](arkts-mdm-bluetoothmanager-removedisallowedbluetoothdevices-f.md) | Removes disallowed Bluetooth devices. If some Bluetooth devices are removed from the disallowed list, the current device cannot connect to the remaining ones; if all Bluetooth devices are removed, the current device can connect to any Bluetooth device. |
| [removeDisallowedBluetoothProtocols](arkts-mdm-bluetoothmanager-removedisallowedbluetoothprotocols-f.md) | Removes disallowed Bluetooth protocols. After removing some protocols, the user is still restricted by the remaining disallowed protocols; after removing all protocols, the user can use any protocol; removing non-existent protocols results in a successful API call but no actual change. |
| [removeDisallowedBluetoothProtocols](arkts-mdm-bluetoothmanager-removedisallowedbluetoothprotocols-f.md) | Removes Bluetooth protocols from the blocklist. After the setting, specified users are no longer restricted by the transfer policy and can properly use these Bluetooth protocols. > **NOTE：**> > 1. When the SPP protocol is passed, the value of the **policy** parameter can only be > **TransferPolicy.RECEIVE_SEND**. Otherwise, error code 9200012 will be returned. > > 2. This API and > [removeDisallowedBluetoothProtocols&lt;sup&gt;20+&lt;/sup&gt;](arkts-mdm-bluetoothmanager-removedisallowedbluetoothprotocols-f.md) are > overloaded APIs. This API adds the **policy** parameter to remove the disallowing configuration based on the > transfer policy. If the same protocol has been blocked under different policies via the two APIs, calling this > API removes only the blocking configuration for the corresponding policy, while blocking configurations of other > policies remain effective. |
| [turnOffBluetooth](arkts-mdm-bluetoothmanager-turnoffbluetooth-f.md) | Disables Bluetooth. After Bluetooth is disabled, the user can manually enable it. |
| [turnOnBluetooth](arkts-mdm-bluetoothmanager-turnonbluetooth-f.md) | Enables Bluetooth. After Bluetooth is enabled, the user can manually disable it. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [isBluetoothDisabled](arkts-mdm-bluetoothmanager-isbluetoothdisabled-f-sys.md) | Queries whether Bluetooth is disabled. |
| [setBluetoothDisabled](arkts-mdm-bluetoothmanager-setbluetoothdisabled-f-sys.md) | Sets the policy for disabling Bluetooth. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [BluetoothInfo](arkts-mdm-bluetoothmanager-bluetoothinfo-i.md) | Represents the device Bluetooth information. |

### Enums

| Name | Description |
| --- | --- |
| [Protocol](arkts-mdm-bluetoothmanager-protocol-e.md) | Represents the Bluetooth protocol type. |
| [TransferPolicy](arkts-mdm-bluetoothmanager-transferpolicy-e.md) | Transfer policy. |

