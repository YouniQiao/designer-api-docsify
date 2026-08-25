# @ohos.bluetooth.connection

Provides methods to operate or manage Bluetooth.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [connectAllowedProfiles](arkts-connectivity-connection-connectallowedprofiles-f.md) |
| [connectAllowedProfiles](arkts-connectivity-connection-connectallowedprofiles-f.md) |
| [disconnectAllowedProfiles](arkts-connectivity-connection-disconnectallowedprofiles-f.md) |
| [getBluetoothScanMode](arkts-connectivity-connection-getbluetoothscanmode-f.md) |
| [getLastConnectionTime](arkts-connectivity-connection-getlastconnectiontime-f.md) |
| [getLocalName](arkts-connectivity-connection-getlocalname-f.md) |
| [getPairedDevices](arkts-connectivity-connection-getpaireddevices-f.md) |
| [getPairState](arkts-connectivity-connection-getpairstate-f.md) |
| [getProfileConnectionState](arkts-connectivity-connection-getprofileconnectionstate-f.md) |
| [getRemoteDeviceBatteryInfo](arkts-connectivity-connection-getremotedevicebatteryinfo-f.md) |
| [getRemoteDeviceClass](arkts-connectivity-connection-getremotedeviceclass-f.md) |
| [getRemoteDeviceName](arkts-connectivity-connection-getremotedevicename-f.md) |
| [getRemoteDeviceName](arkts-connectivity-connection-getremotedevicename-f.md) |
| [getRemoteDeviceTransport](arkts-connectivity-connection-getremotedevicetransport-f.md) |
| [getRemoteProfileUuids](arkts-connectivity-connection-getremoteprofileuuids-f.md) |
| [getRemoteProfileUuids](arkts-connectivity-connection-getremoteprofileuuids-f.md) |
| [getVirtualAddressByHash](arkts-connectivity-connection-getvirtualaddressbyhash-f.md) |
| [isBluetoothDiscovering](arkts-connectivity-connection-isbluetoothdiscovering-f.md) |
| [off](arkts-connectivity-connection-off-f.md#offbluetoothdevicefind) |
| [off](arkts-connectivity-connection-off-f.md#offdiscoveryresult) |
| [off](arkts-connectivity-connection-off-f.md#offbondstatechange) |
| [off](arkts-connectivity-connection-off-f.md#offpinrequired) |
| [off](arkts-connectivity-connection-off-f.md#offbatterychange) |
| [offAclStateChange](arkts-connectivity-connection-offaclstatechange-f.md) |
| [offBatteryChange](arkts-connectivity-connection-offbatterychange-f.md) |
| [offBluetoothDeviceFind](arkts-connectivity-connection-offbluetoothdevicefind-f.md) |
| [offBondStateChange](arkts-connectivity-connection-offbondstatechange-f.md) |
| [offDiscoveryResult](arkts-connectivity-connection-offdiscoveryresult-f.md) |
| [offPinRequired](arkts-connectivity-connection-offpinrequired-f.md) |
| [offScanModeChange](arkts-connectivity-connection-offscanmodechange-f.md) |
| [on](arkts-connectivity-connection-on-f.md#onbluetoothdevicefind) |
| [on](arkts-connectivity-connection-on-f.md#ondiscoveryresult) |
| [on](arkts-connectivity-connection-on-f.md#onbondstatechange) |
| [on](arkts-connectivity-connection-on-f.md#onpinrequired) |
| [on](arkts-connectivity-connection-on-f.md#onbatterychange) |
| [onAclStateChange](arkts-connectivity-connection-onaclstatechange-f.md) |
| [onBatteryChange](arkts-connectivity-connection-onbatterychange-f.md) |
| [onBluetoothDeviceFind](arkts-connectivity-connection-onbluetoothdevicefind-f.md) |
| [onBondStateChange](arkts-connectivity-connection-onbondstatechange-f.md) |
| [onDiscoveryResult](arkts-connectivity-connection-ondiscoveryresult-f.md) |
| [onPinRequired](arkts-connectivity-connection-onpinrequired-f.md) |
| [onScanModeChange](arkts-connectivity-connection-onscanmodechange-f.md) |
| [pairDevice](arkts-connectivity-connection-pairdevice-f.md) |
| [pairDevice](arkts-connectivity-connection-pairdevice-f.md) |
| [pairDevice](arkts-connectivity-connection-pairdevice-f.md) |
| [setBluetoothScanMode](arkts-connectivity-connection-setbluetoothscanmode-f.md) |
| [setDevicePairingConfirmation](arkts-connectivity-connection-setdevicepairingconfirmation-f.md) |
| [setDevicePinCode](arkts-connectivity-connection-setdevicepincode-f.md) |
| [setDevicePinCode](arkts-connectivity-connection-setdevicepincode-f.md) |
| [setLocalName](arkts-connectivity-connection-setlocalname-f.md) |
| [setRemoteDeviceName](arkts-connectivity-connection-setremotedevicename-f.md) |
| [startBluetoothDiscovery](arkts-connectivity-connection-startbluetoothdiscovery-f.md) |
| [stopBluetoothDiscovery](arkts-connectivity-connection-stopbluetoothdiscovery-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cancelPairedDevice](arkts-connectivity-connection-cancelpaireddevice-f-sys.md) |
| [cancelPairedDevice](arkts-connectivity-connection-cancelpaireddevice-f-sys.md) |
| [cancelPairingDevice](arkts-connectivity-connection-cancelpairingdevice-f-sys.md) |
| [cancelPairingDevice](arkts-connectivity-connection-cancelpairingdevice-f-sys.md) |
| [controlDeviceAction](arkts-connectivity-connection-controldeviceaction-f-sys.md) |
| [disconnectAllowedProfiles](arkts-connectivity-connection-disconnectallowedprofiles-f-sys.md) |
| [generateLocalOobData](arkts-connectivity-connection-generatelocaloobdata-f-sys.md) |
| [getCarKeyDfxData](arkts-connectivity-connection-getcarkeydfxdata-f-sys.md) |
| [getLocalProfileUuids](arkts-connectivity-connection-getlocalprofileuuids-f-sys.md) |
| [getLocalProfileUuids](arkts-connectivity-connection-getlocalprofileuuids-f-sys.md) |
| [getRemoteDeviceType](arkts-connectivity-connection-getremotedevicetype-f-sys.md) |
| [getRemoteProductId](arkts-connectivity-connection-getremoteproductid-f-sys.md) |
| [pairCredibleDevice](arkts-connectivity-connection-paircredibledevice-f-sys.md) |
| [pairCredibleDevice](arkts-connectivity-connection-paircredibledevice-f-sys.md) |
| [pairDeviceOutOfBand](arkts-connectivity-connection-pairdeviceoutofband-f-sys.md) |
| [setCarKeyDfxData](arkts-connectivity-connection-setcarkeydfxdata-f-sys.md) |
| [setRemoteDeviceType](arkts-connectivity-connection-setremotedevicetype-f-sys.md) |
| [startPairOutOfBand](arkts-connectivity-connection-startpairoutofband-f-sys.md) |
| [updateCloudBluetoothDevice](arkts-connectivity-connection-updatecloudbluetoothdevice-f-sys.md) |
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
### Interfaces(System API)

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
### Enums(System API)

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
