# @ohos.bluetooth.connection

Provides methods to operate or manage Bluetooth.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace connection--><!--Device-unnamed-declare namespace connection-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [connectAllowedProfiles](arkts-connectivity-connection-connectallowedprofiles-f.md#connectallowedprofiles) |
| [connectAllowedProfiles](arkts-connectivity-connection-connectallowedprofiles-f.md#connectallowedprofiles-1) |
| [disconnectAllowedProfiles](arkts-connectivity-connection-disconnectallowedprofiles-f.md#disconnectallowedprofiles-1) |
| [getBluetoothScanMode](arkts-connectivity-connection-getbluetoothscanmode-f.md#getbluetoothscanmode) |
| [getLastConnectionTime](arkts-connectivity-connection-getlastconnectiontime-f.md#getlastconnectiontime) |
| [getLocalName](arkts-connectivity-connection-getlocalname-f.md#getlocalname) |
| [getPairState](arkts-connectivity-connection-getpairstate-f.md#getpairstate) |
| [getPairedDevices](arkts-connectivity-connection-getpaireddevices-f.md#getpaireddevices) |
| [getProfileConnectionState](arkts-connectivity-connection-getprofileconnectionstate-f.md#getprofileconnectionstate) |
| [getRemoteDeviceBatteryInfo](arkts-connectivity-connection-getremotedevicebatteryinfo-f.md#getremotedevicebatteryinfo) |
| [getRemoteDeviceClass](arkts-connectivity-connection-getremotedeviceclass-f.md#getremotedeviceclass) |
| [getRemoteDeviceName](arkts-connectivity-connection-getremotedevicename-f.md#getremotedevicename) |
| [getRemoteDeviceName](arkts-connectivity-connection-getremotedevicename-f.md#getremotedevicename-1) |
| [getRemoteDeviceTransport](arkts-connectivity-connection-getremotedevicetransport-f.md#getremotedevicetransport) |
| [getRemoteProfileUuids](arkts-connectivity-connection-getremoteprofileuuids-f.md#getremoteprofileuuids) |
| [getRemoteProfileUuids](arkts-connectivity-connection-getremoteprofileuuids-f.md#getremoteprofileuuids-1) |
| [getVirtualAddressByHash](arkts-connectivity-connection-getvirtualaddressbyhash-f.md#getvirtualaddressbyhash) |
| [isBluetoothDiscovering](arkts-connectivity-connection-isbluetoothdiscovering-f.md#isbluetoothdiscovering) |
| [off](arkts-connectivity-connection-off-f.md#off) |
| [off](arkts-connectivity-connection-off-f.md#off-1) |
| [off](arkts-connectivity-connection-off-f.md#off-2) |
| [off](arkts-connectivity-connection-off-f.md#off-3) |
| [off](arkts-connectivity-connection-off-f.md#off-4) |
| [offAclStateChange](arkts-connectivity-connection-offaclstatechange-f.md#offaclstatechange) |
| [offScanModeChange](arkts-connectivity-connection-offscanmodechange-f.md#offscanmodechange) |
| [on](arkts-connectivity-connection-on-f.md#on) |
| [on](arkts-connectivity-connection-on-f.md#on-1) |
| [on](arkts-connectivity-connection-on-f.md#on-2) |
| [on](arkts-connectivity-connection-on-f.md#on-3) |
| [on](arkts-connectivity-connection-on-f.md#on-4) |
| [onAclStateChange](arkts-connectivity-connection-onaclstatechange-f.md#onaclstatechange) |
| [onScanModeChange](arkts-connectivity-connection-onscanmodechange-f.md#onscanmodechange) |
| [pairDevice](arkts-connectivity-connection-pairdevice-f.md#pairdevice) |
| [pairDevice](arkts-connectivity-connection-pairdevice-f.md#pairdevice-1) |
| [pairDevice](arkts-connectivity-connection-pairdevice-f.md#pairdevice-2) |
| [setBluetoothScanMode](arkts-connectivity-connection-setbluetoothscanmode-f.md#setbluetoothscanmode) |
| [setDevicePairingConfirmation](arkts-connectivity-connection-setdevicepairingconfirmation-f.md#setdevicepairingconfirmation) |
| [setDevicePinCode](arkts-connectivity-connection-setdevicepincode-f.md#setdevicepincode) |
| [setDevicePinCode](arkts-connectivity-connection-setdevicepincode-f.md#setdevicepincode-1) |
| [setLocalName](arkts-connectivity-connection-setlocalname-f.md#setlocalname) |
| [setRemoteDeviceName](arkts-connectivity-connection-setremotedevicename-f.md#setremotedevicename) |
| [startBluetoothDiscovery](arkts-connectivity-connection-startbluetoothdiscovery-f.md#startbluetoothdiscovery) |
| [stopBluetoothDiscovery](arkts-connectivity-connection-stopbluetoothdiscovery-f.md#stopbluetoothdiscovery) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cancelPairedDevice](arkts-connectivity-connection-cancelpaireddevice-f-sys.md#cancelpaireddevice) |
| [cancelPairedDevice](arkts-connectivity-connection-cancelpaireddevice-f-sys.md#cancelpaireddevice-1) |
| [cancelPairingDevice](arkts-connectivity-connection-cancelpairingdevice-f-sys.md#cancelpairingdevice) |
| [cancelPairingDevice](arkts-connectivity-connection-cancelpairingdevice-f-sys.md#cancelpairingdevice-1) |
| [controlDeviceAction](arkts-connectivity-connection-controldeviceaction-f-sys.md#controldeviceaction) |
| [disconnectAllowedProfiles](arkts-connectivity-connection-disconnectallowedprofiles-f-sys.md#disconnectallowedprofiles) |
| [generateLocalOobData](arkts-connectivity-connection-generatelocaloobdata-f-sys.md#generatelocaloobdata) |
| [getCarKeyDfxData](arkts-connectivity-connection-getcarkeydfxdata-f-sys.md#getcarkeydfxdata) |
| [getLocalProfileUuids](arkts-connectivity-connection-getlocalprofileuuids-f-sys.md#getlocalprofileuuids) |
| [getLocalProfileUuids](arkts-connectivity-connection-getlocalprofileuuids-f-sys.md#getlocalprofileuuids-1) |
| [getRemoteDeviceType](arkts-connectivity-connection-getremotedevicetype-f-sys.md#getremotedevicetype) |
| [getRemoteProductId](arkts-connectivity-connection-getremoteproductid-f-sys.md#getremoteproductid) |
| [pairCredibleDevice](arkts-connectivity-connection-paircredibledevice-f-sys.md#paircredibledevice) |
| [pairCredibleDevice](arkts-connectivity-connection-paircredibledevice-f-sys.md#paircredibledevice-1) |
| [pairDeviceOutOfBand](arkts-connectivity-connection-pairdeviceoutofband-f-sys.md#pairdeviceoutofband) |
| [setCarKeyDfxData](arkts-connectivity-connection-setcarkeydfxdata-f-sys.md#setcarkeydfxdata) |
| [setRemoteDeviceType](arkts-connectivity-connection-setremotedevicetype-f-sys.md#setremotedevicetype) |
| [startPairOutOfBand](arkts-connectivity-connection-startpairoutofband-f-sys.md#startpairoutofband) |
| [updateCloudBluetoothDevice](arkts-connectivity-connection-updatecloudbluetoothdevice-f-sys.md#updatecloudbluetoothdevice) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AclStateResult](arkts-connectivity-connection-aclstateresult-i.md) |
| [BatteryInfo](arkts-connectivity-connection-batteryinfo-i.md) |
| [BondStateParam](arkts-connectivity-connection-bondstateparam-i.md) |
| [DeviceClass](arkts-connectivity-connection-deviceclass-i.md) |
| [DiscoveryResult](arkts-connectivity-connection-discoveryresult-i.md) |
| [PinRequiredParam](arkts-connectivity-connection-pinrequiredparam-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BatteryInfo](arkts-connectivity-connection-batteryinfo-i-sys.md) |
| [ControlDeviceActionParams](arkts-connectivity-connection-controldeviceactionparams-i-sys.md) |
| [OobData](arkts-connectivity-connection-oobdata-i-sys.md) |
| [PinRequiredParam](arkts-connectivity-connection-pinrequiredparam-i-sys.md) |
| [TrustedPairedDevice](arkts-connectivity-connection-trustedpaireddevice-i-sys.md) |
| [TrustedPairedDevices](arkts-connectivity-connection-trustedpaireddevices-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AclState](arkts-connectivity-connection-aclstate-e.md) |
| [BluetoothTransport](arkts-connectivity-connection-bluetoothtransport-e.md) |
| [BondState](arkts-connectivity-connection-bondstate-e.md) |
| [DeviceChargeState](arkts-connectivity-connection-devicechargestate-e.md) |
| [HashAlgorithmType](arkts-connectivity-connection-hashalgorithmtype-e.md) |
| [ScanMode](arkts-connectivity-connection-scanmode-e.md) |
| [UnbondCause](arkts-connectivity-connection-unbondcause-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CarKeyActionType](arkts-connectivity-connection-carkeyactiontype-e-sys.md) |
| [ControlObject](arkts-connectivity-connection-controlobject-e-sys.md) |
| [ControlType](arkts-connectivity-connection-controltype-e-sys.md) |
| [ControlTypeValue](arkts-connectivity-connection-controltypevalue-e-sys.md) |
| [DeviceRole](arkts-connectivity-connection-devicerole-e-sys.md) |
| [DeviceType](arkts-connectivity-connection-devicetype-e-sys.md) |
| [PinType](arkts-connectivity-connection-pintype-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BluetoothAddress](arkts-connectivity-connection-bluetoothaddress-t.md) |
| [MajorClass](arkts-connectivity-connection-majorclass-t.md) |
| [MajorMinorClass](arkts-connectivity-connection-majorminorclass-t.md) |
| [ProfileConnectionState](arkts-connectivity-connection-profileconnectionstate-t.md) |
| [ProfileId](arkts-connectivity-connection-profileid-t.md) |
| [ProfileUuids](arkts-connectivity-connection-profileuuids-t.md) |
