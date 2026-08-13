# @ohos.bluetooth.connection

Provides methods to operate or manage Bluetooth.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace connection--><!--Device-unnamed-declare namespace connection-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getBluetoothScanMode](arkts-connectivity-connection-getbluetoothscanmode-f.md#getBluetoothScanMode) | Obtains the Bluetooth scanning mode of a device. |
| [getLastConnectionTime](arkts-connectivity-connection-getlastconnectiontime-f.md#getLastConnectionTime) | Get latest connection time of device. |
| [getLocalName](arkts-connectivity-connection-getlocalname-f.md#getLocalName) | Obtains the Bluetooth local name of a device. |
| [getPairState](arkts-connectivity-connection-getpairstate-f.md#getPairState) | Obtains the pair state of a specified device. |
| [getPairedDevices](arkts-connectivity-connection-getpaireddevices-f.md#getPairedDevices) | Obtains the list of Bluetooth devices that have been paired with the current device. On API 26.0.0 and above, if the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC, the type of the peer device address is real. Otherwise, the type of the peer device address is virtual. |
| [getProfileConnectionState](arkts-connectivity-connection-getprofileconnectionstate-f.md#getProfileConnectionState) | Get the profile connection state of the current device. |
| [getRemoteDeviceBatteryInfo](arkts-connectivity-connection-getremotedevicebatteryinfo-f.md#getRemoteDeviceBatteryInfo) | Get remote device battery information. |
| [getRemoteDeviceClass](arkts-connectivity-connection-getremotedeviceclass-f.md#getRemoteDeviceClass) | Obtains the class of a peer Bluetooth device. |
| [getRemoteDeviceName](arkts-connectivity-connection-getremotedevicename-f.md#getRemoteDeviceName) | Obtains the name of a peer Bluetooth device. |
| [getRemoteDeviceName](arkts-connectivity-connection-getremotedevicename-f.md#getRemoteDeviceName) | Obtains the name or alias of the Bluetooth peer device. |
| [getRemoteDeviceTransport](arkts-connectivity-connection-getremotedevicetransport-f.md#getRemoteDeviceTransport) | Get the transport of the bluetooth device. |
| [getVirtualAddressByHash](arkts-connectivity-connection-getvirtualaddressbyhash-f.md#getVirtualAddressByHash) | Obtain the virtual address of the corresponding device based on the hash value of the real address. |
| [isBluetoothDiscovering](arkts-connectivity-connection-isbluetoothdiscovering-f.md#isBluetoothDiscovering) | Check if bluetooth is discovering. |
| [offAclStateChange](arkts-connectivity-connection-offaclstatechange-f.md#offAclStateChange) | Unsubscribe the event of acl state changed from a remote device. If the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC, the type of the peer device address is real. Otherwise, the type of the peer device address is virtual. |
| [offBatteryChange](arkts-connectivity-connection-offbatterychange-f.md#offBatteryChange) | Unsubscribe the event of battery state changed from a remote device. |
| [offBluetoothDeviceFind](arkts-connectivity-connection-offbluetoothdevicefind-f.md#offBluetoothDeviceFind) | Unsubscribe the event reported when a remote Bluetooth device is discovered. |
| [offBondStateChange](arkts-connectivity-connection-offbondstatechange-f.md#offBondStateChange) | Unsubscribe the event reported when a remote Bluetooth device is bonded. |
| [offDiscoveryResult](arkts-connectivity-connection-offdiscoveryresult-f.md#offDiscoveryResult) | Unsubscribe the event reported when a remote Bluetooth device is discovered. |
| [offPinRequired](arkts-connectivity-connection-offpinrequired-f.md#offPinRequired) | Unsubscribe the event of a pairing request from a remote Bluetooth device. |
| [offScanModeChange](arkts-connectivity-connection-offscanmodechange-f.md#offScanModeChange) | Unsubscribe to an event indicating that the scanning mode of the local device has changed. |
| off_batteryChange | Unsubscribe the event of battery state changed from a remote device. |
| off_bluetoothDeviceFind | Unsubscribe the event reported when a remote Bluetooth device is discovered. |
| off_bondStateChange | Unsubscribe the event reported when a remote Bluetooth device is bonded. |
| off_pinRequired | Unsubscribe the event of a pairing request from a remote Bluetooth device. |
| [onAclStateChange](arkts-connectivity-connection-onaclstatechange-f.md#onAclStateChange) | Subscribe the event of acl state changed from a remote device. If the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC, the type of the peer device address is real. Otherwise, the type of the peer device address is virtual. |
| [onBatteryChange](arkts-connectivity-connection-onbatterychange-f.md#onBatteryChange) | Subscribe the event of battery state changed from a remote device. |
| [onBluetoothDeviceFind](arkts-connectivity-connection-onbluetoothdevicefind-f.md#onBluetoothDeviceFind) | Subscribe the event reported when a remote Bluetooth device is discovered. On API 26.0.0 and above, if the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC, the type of the peer device address is real. Otherwise, the type of the peer device address is virtual. |
| [onBondStateChange](arkts-connectivity-connection-onbondstatechange-f.md#onBondStateChange) | Subscribe the event reported when a remote Bluetooth device is bonded. On API 26.0.0 and above, if the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC, the type of the peer device address is real. Otherwise, the type of the peer device address is virtual. |
| [onDiscoveryResult](arkts-connectivity-connection-ondiscoveryresult-f.md#onDiscoveryResult) | Subscribe the event reported when a remote Bluetooth device is discovered. On API 26.0.0 and above, if the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC, the type of the peer device address is real. Otherwise, the type of the peer device address is virtual. |
| [onPinRequired](arkts-connectivity-connection-onpinrequired-f.md#onPinRequired) | Subscribe the event of a pairing request from a remote Bluetooth device. On API 26.0.0 and above, if the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC, the type of the peer device address is real. Otherwise, the type of the peer device address is virtual. |
| [onScanModeChange](arkts-connectivity-connection-onscanmodechange-f.md#onScanModeChange) | Subscribe to an event indicating that the scanning mode of the local device has changed. |
| on_batteryChange | Subscribe the event of battery state changed from a remote device. |
| on_bluetoothDeviceFind | Subscribe the event reported when a remote Bluetooth device is discovered. On API 26.0.0 and above, if the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC, the type of the peer device address is real. Otherwise, the type of the peer device address is virtual. |
| on_bondStateChange | Subscribe the event reported when a remote Bluetooth device is bonded. On API 26.0.0 and above, if the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC, the type of the peer device address is real. Otherwise, the type of the peer device address is virtual. |
| on_pinRequired | Subscribe the event of a pairing request from a remote Bluetooth device. On API 26.0.0 and above, if the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC, the type of the peer device address is real. Otherwise, the type of the peer device address is virtual. |
| [pairDevice](arkts-connectivity-connection-pairdevice-f.md#pairDevice) | Starts pairing with a remote Bluetooth device. |
| [pairDevice](arkts-connectivity-connection-pairdevice-f.md#pairDevice) | Starts pairing with a remote Bluetooth device. |
| [pairDevice](arkts-connectivity-connection-pairdevice-f.md#pairDevice) | Starts pairing with a remote Bluetooth device. |
| [setBluetoothScanMode](arkts-connectivity-connection-setbluetoothscanmode-f.md#setBluetoothScanMode) | Sets the Bluetooth scan mode for a device. |
| [setDevicePairingConfirmation](arkts-connectivity-connection-setdevicepairingconfirmation-f.md#setDevicePairingConfirmation) | Sets the confirmation of pairing with a certain device. |
| [setDevicePinCode](arkts-connectivity-connection-setdevicepincode-f.md#setDevicePinCode) | Set the pin during pairing when the pin type is PIN_TYPE_ENTER_PIN_CODE. |
| [setDevicePinCode](arkts-connectivity-connection-setdevicepincode-f.md#setDevicePinCode) | Set the pin during pairing when the pin type is PIN_TYPE_ENTER_PIN_CODE. |
| [setLocalName](arkts-connectivity-connection-setlocalname-f.md#setLocalName) | Sets the Bluetooth friendly name of a device. It is used only by system applications for security. If a non-system application invokes the interface, exception 801 is thrown. |
| [setRemoteDeviceName](arkts-connectivity-connection-setremotedevicename-f.md#setRemoteDeviceName) | Modify remote device name. |
| [startBluetoothDiscovery](arkts-connectivity-connection-startbluetoothdiscovery-f.md#startBluetoothDiscovery) | Starts scanning Bluetooth devices. |
| [stopBluetoothDiscovery](arkts-connectivity-connection-stopbluetoothdiscovery-f.md#stopBluetoothDiscovery) | Stops Bluetooth device scanning. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [cancelPairedDevice](arkts-connectivity-connection-cancelpaireddevice-f-sys.md#cancelPairedDevice) | Remove a paired remote device. |
| [cancelPairedDevice](arkts-connectivity-connection-cancelpaireddevice-f-sys.md#cancelPairedDevice-(System-API)) | Remove a paired remote device. |
| [cancelPairingDevice](arkts-connectivity-connection-cancelpairingdevice-f-sys.md#cancelPairingDevice) | Remove a pairing remote device. |
| [cancelPairingDevice](arkts-connectivity-connection-cancelpairingdevice-f-sys.md#cancelPairingDevice-(System-API)) | Remove a pairing remote device. |
| [connectAllowedProfiles](arkts-connectivity-connection-connectallowedprofiles-f-sys.md#connectAllowedProfiles) | Connects all allowed bluetooth profiles between the local and remote device. |
| [connectAllowedProfiles](arkts-connectivity-connection-connectallowedprofiles-f-sys.md#connectAllowedProfiles-(System-API)) | Connects all allowed bluetooth profiles between the local and remote device. |
| [controlDeviceAction](arkts-connectivity-connection-controldeviceaction-f-sys.md#controlDeviceAction) | Controls the actions of Bluetooth peripherals. |
| [disconnectAllowedProfiles](arkts-connectivity-connection-disconnectallowedprofiles-f-sys.md#disconnectAllowedProfiles) | Disconnects all allowed bluetooth profiles between the local and remote device. |
| [disconnectAllowedProfiles](arkts-connectivity-connection-disconnectallowedprofiles-f-sys.md#disconnectAllowedProfiles-(System-API)) | Disconnects all allowed bluetooth profiles between the local and remote device. |
| [generateLocalOobData](arkts-connectivity-connection-generatelocaloobdata-f-sys.md#generateLocalOobData) | Generate out-of-band data of the local device. |
| [getCarKeyDfxData](arkts-connectivity-connection-getcarkeydfxdata-f-sys.md#getCarKeyDfxData) | Get the dfx data of car key. |
| [getLocalProfileUuids](arkts-connectivity-connection-getlocalprofileuuids-f-sys.md#getLocalProfileUuids) | Obtains the profile UUIDs supported by the local device. |
| [getLocalProfileUuids](arkts-connectivity-connection-getlocalprofileuuids-f-sys.md#getLocalProfileUuids-(System-API)) | Obtains the profile UUIDs supported by the local device. |
| [getRemoteDeviceType](arkts-connectivity-connection-getremotedevicetype-f-sys.md#getRemoteDeviceType) | Get remote device custom type. |
| [getRemoteProductId](arkts-connectivity-connection-getremoteproductid-f-sys.md#getRemoteProductId) | Obtains the product ID of a remote device. |
| [getRemoteProfileUuids](arkts-connectivity-connection-getremoteprofileuuids-f-sys.md#getRemoteProfileUuids) | Obtains the profile UUIDs supported by the remote device. |
| [getRemoteProfileUuids](arkts-connectivity-connection-getremoteprofileuuids-f-sys.md#getRemoteProfileUuids-(System-API)) | Obtains the profile UUIDs supported by the remote device. |
| [off_discoveryResult](arkts-connectivity-connection-offdiscoveryresult-f-sys.md#off_discoveryResult) | Unsubscribe the event reported when a remote Bluetooth device is discovered. |
| [on_discoveryResult](arkts-connectivity-connection-ondiscoveryresult-f-sys.md#on_discoveryResult) | Subscribe the event reported when a remote Bluetooth device is discovered. On API 26.0.0 and above, if the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC, the type of the peer device address is real. Otherwise, the type of the peer device address is virtual. |
| [pairCredibleDevice](arkts-connectivity-connection-paircredibledevice-f-sys.md#pairCredibleDevice) | Starts pairing with a credible remote Bluetooth device with transport. This interface does not trigger a dialog box and does not require user authorization. Only specific system application can use this function. |
| [pairCredibleDevice](arkts-connectivity-connection-paircredibledevice-f-sys.md#pairCredibleDevice-(System-API)) | Starts pairing with a credible remote Bluetooth device with transport. This interface does not trigger a dialog box and does not require user authorization. Only specific system application can use this function. |
| [pairDeviceOutOfBand](arkts-connectivity-connection-pairdeviceoutofband-f-sys.md#pairDeviceOutOfBand) | Starts pairing with a remote Bluetooth device using the Out Of Band mechanism. This function is asynchronous, and the pairing status is obtained by listening to the bondStateChange event. If both p192Data and p256Data are null, the function call will fail. If both p192Data and p256Data are used simultaneously, p256Data takes effect. |
| [setCarKeyDfxData](arkts-connectivity-connection-setcarkeydfxdata-f-sys.md#setCarKeyDfxData) | Set the dfx data of car key. |
| [setRemoteDeviceType](arkts-connectivity-connection-setremotedevicetype-f-sys.md#setRemoteDeviceType) | Set remote device custom type. |
| [startPairOutOfBand](arkts-connectivity-connection-startpairoutofband-f-sys.md#startPairOutOfBand) | Starts pairing with the specific remote Bluetooth device using the Out Of Band mechanism. This function is asynchronous, and the pairing status is obtained by listening to the bondStateChange event. If both p192Data and p256Data are not used, the function call will fail. If both p192Data and p256Data are used simultaneously, p256Data takes effect. |
| [updateCloudBluetoothDevice](arkts-connectivity-connection-updatecloudbluetoothdevice-f-sys.md#updateCloudBluetoothDevice) | update cloud devices. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [AclStateResult](arkts-connectivity-connection-aclstateresult-i.md) | Acl state change result. |
| [BatteryInfo](arkts-connectivity-connection-batteryinfo-i.md) | Describes the contents of the battery information. |
| [BondStateParam](arkts-connectivity-connection-bondstateparam-i.md) | Describes the class of a bluetooth device. |
| [DeviceClass](arkts-connectivity-connection-deviceclass-i.md) | Describes the class of a bluetooth device. |
| [PinRequiredParam](arkts-connectivity-connection-pinrequiredparam-i.md) | Describes the bond key param. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [BatteryInfo](arkts-connectivity-connection-batteryinfo-i-sys.md) | Describes the contents of the battery information. |
| [ControlDeviceActionParams](arkts-connectivity-connection-controldeviceactionparams-i-sys.md) | Describes information about controlling the Bluetooth peripheral. |
| [DiscoveryResult](arkts-connectivity-connection-discoveryresult-i-sys.md) | Describes the contents of the discovery results |
| [OobData](arkts-connectivity-connection-oobdata-i-sys.md) | Out Of Band data used in Bluetooth device pairing. |
| [PinRequiredParam](arkts-connectivity-connection-pinrequiredparam-i-sys.md) | Describes the bond key param. |
| [TrustedPairedDevice](arkts-connectivity-connection-trustedpaireddevice-i-sys.md) | Describes device of cloud pair. |
| [TrustedPairedDevices](arkts-connectivity-connection-trustedpaireddevices-i-sys.md) | Describes the cloud pair device. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [AclState](arkts-connectivity-connection-aclstate-e.md) | The enum of acl state. |
| [BluetoothTransport](arkts-connectivity-connection-bluetoothtransport-e.md) | Enum for the transport of a remote device |
| [BondState](arkts-connectivity-connection-bondstate-e.md) | The enum of bond state. |
| [DeviceChargeState](arkts-connectivity-connection-devicechargestate-e.md) | Enum for the charge state. |
| [HashAlgorithmType](arkts-connectivity-connection-hashalgorithmtype-e.md) | Enum for the hash algorithm type. |
| [ScanMode](arkts-connectivity-connection-scanmode-e.md) | The enum of BR scan mode. |
| [UnbondCause](arkts-connectivity-connection-unbondcause-e.md) | Enum for cause of unbond. |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [CarKeyActionType](arkts-connectivity-connection-carkeyactiontype-e-sys.md) | Enum for the action of car key. |
| [ControlObject](arkts-connectivity-connection-controlobject-e-sys.md) | Describes the control object. |
| [ControlType](arkts-connectivity-connection-controltype-e-sys.md) | Describes the control type. |
| [ControlTypeValue](arkts-connectivity-connection-controltypevalue-e-sys.md) | Describes the control type value. |
| [DeviceRole](arkts-connectivity-connection-devicerole-e-sys.md) | Enum for the role of device. |
| [DeviceType](arkts-connectivity-connection-devicetype-e-sys.md) | Enum for the custom type of remote device. |
| [PinType](arkts-connectivity-connection-pintype-e-sys.md) | Enum for the type of pairing to a remote device |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [BluetoothAddress](arkts-connectivity-connection-bluetoothaddress-t.md) | Bluetooth device address. |
| [MajorClass](arkts-connectivity-connection-majorclass-t.md) | Indicate the major class of a bluetooth device. |
| [MajorMinorClass](arkts-connectivity-connection-majorminorclass-t.md) | Indicate the major minor class of a bluetooth device. |
| [ProfileConnectionState](arkts-connectivity-connection-profileconnectionstate-t.md) | Indicate the profile connection state. |
| [ProfileId](arkts-connectivity-connection-profileid-t.md) | Indicate the profile id. |

<!--Del-->
### Types（系统接口）

| Name | Description |
| --- | --- |
| [ProfileUuids](arkts-connectivity-connection-profileuuids-t-sys.md) | Indicate the profile uuid. |
<!--DelEnd-->

