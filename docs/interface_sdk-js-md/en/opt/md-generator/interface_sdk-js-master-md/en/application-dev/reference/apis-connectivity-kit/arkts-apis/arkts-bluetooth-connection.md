# @ohos.bluetooth.connection

Provides methods to operate or manage Bluetooth.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace connection--><!--Device-unnamed-declare namespace connection-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getBluetoothScanMode](arkts-connectivity-connection-getbluetoothscanmode-f.md#getbluetoothscanmode) |
| [getLastConnectionTime](arkts-connectivity-connection-getlastconnectiontime-f.md#getlastconnectiontime) |
| [getLocalName](arkts-connectivity-connection-getlocalname-f.md#getlocalname) |
| [getPairState](arkts-connectivity-connection-getpairstate-f.md#getpairstate) |
| [getPairedDevices](arkts-connectivity-connection-getpaireddevices-f.md#getpaireddevices) |
| [getProfileConnectionState](arkts-connectivity-connection-getprofileconnectionstate-f.md#getprofileconnectionstate) |
| [getRemoteDeviceBatteryInfo](arkts-connectivity-connection-getremotedevicebatteryinfo-f.md#getremotedevicebatteryinfo) |
| [getRemoteDeviceClass](arkts-connectivity-connection-getremotedeviceclass-f.md#getremotedeviceclass) |
| [getRemoteDeviceName](arkts-connectivity-connection-getremotedevicename-f.md#getremotedevicename) |
| [getRemoteDeviceName](arkts-connectivity-connection-getremotedevicename-f.md#getremotedevicename) |
| [getRemoteDeviceTransport](arkts-connectivity-connection-getremotedevicetransport-f.md#getremotedevicetransport) |
| [getVirtualAddressByHash](arkts-connectivity-connection-getvirtualaddressbyhash-f.md#getvirtualaddressbyhash) |
| [isBluetoothDiscovering](arkts-connectivity-connection-isbluetoothdiscovering-f.md#isbluetoothdiscovering) |
| [offAclStateChange](arkts-connectivity-connection-offaclstatechange-f.md#offaclstatechange) |
| [offBatteryChange](arkts-connectivity-connection-offbatterychange-f.md#offbatterychange) |
| [offBluetoothDeviceFind](arkts-connectivity-connection-offbluetoothdevicefind-f.md#offbluetoothdevicefind) |
| [offBondStateChange](arkts-connectivity-connection-offbondstatechange-f.md#offbondstatechange) |
| [offDiscoveryResult](arkts-connectivity-connection-offdiscoveryresult-f.md#offdiscoveryresult) |
| [offPinRequired](arkts-connectivity-connection-offpinrequired-f.md#offpinrequired) |
| [offScanModeChange](arkts-connectivity-connection-offscanmodechange-f.md#offscanmodechange) |
| [off_batteryChange](arkts-connectivity-connection-offbatterychange-f.md#offbatterychange) |
| [off_bluetoothDeviceFind](arkts-connectivity-connection-offbluetoothdevicefind-f.md#offbluetoothdevicefind) |
| [off_bondStateChange](arkts-connectivity-connection-offbondstatechange-f.md#offbondstatechange) |
| [off_pinRequired](arkts-connectivity-connection-offpinrequired-f.md#offpinrequired) |
| [onAclStateChange](arkts-connectivity-connection-onaclstatechange-f.md#onaclstatechange) |
| [onBatteryChange](arkts-connectivity-connection-onbatterychange-f.md#onbatterychange) |
| [onBluetoothDeviceFind](arkts-connectivity-connection-onbluetoothdevicefind-f.md#onbluetoothdevicefind) |
| [onBondStateChange](arkts-connectivity-connection-onbondstatechange-f.md#onbondstatechange) |
| [onDiscoveryResult](arkts-connectivity-connection-ondiscoveryresult-f.md#ondiscoveryresult) |
| [onPinRequired](arkts-connectivity-connection-onpinrequired-f.md#onpinrequired) |
| [onScanModeChange](arkts-connectivity-connection-onscanmodechange-f.md#onscanmodechange) |
| [on_batteryChange](arkts-connectivity-connection-onbatterychange-f.md#onbatterychange) |
| [on_bluetoothDeviceFind](arkts-connectivity-connection-onbluetoothdevicefind-f.md#onbluetoothdevicefind) |
| [on_bondStateChange](arkts-connectivity-connection-onbondstatechange-f.md#onbondstatechange) |
| [on_pinRequired](arkts-connectivity-connection-onpinrequired-f.md#onpinrequired) |
| [pairDevice](arkts-connectivity-connection-pairdevice-f.md#pairdevice) |
| [pairDevice](arkts-connectivity-connection-pairdevice-f.md#pairdevice) |
| [pairDevice](arkts-connectivity-connection-pairdevice-f.md#pairdevice) |
| [setBluetoothScanMode](arkts-connectivity-connection-setbluetoothscanmode-f.md#setbluetoothscanmode) |
| [setDevicePairingConfirmation](arkts-connectivity-connection-setdevicepairingconfirmation-f.md#setdevicepairingconfirmation) |
| [setDevicePinCode](arkts-connectivity-connection-setdevicepincode-f.md#setdevicepincode) |
| [setDevicePinCode](arkts-connectivity-connection-setdevicepincode-f.md#setdevicepincode) |
| [setLocalName](arkts-connectivity-connection-setlocalname-f.md#setlocalname) |
| [setRemoteDeviceName](arkts-connectivity-connection-setremotedevicename-f.md#setremotedevicename) |
| [startBluetoothDiscovery](arkts-connectivity-connection-startbluetoothdiscovery-f.md#startbluetoothdiscovery) |
| [stopBluetoothDiscovery](arkts-connectivity-connection-stopbluetoothdiscovery-f.md#stopbluetoothdiscovery) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cancelPairedDevice](arkts-connectivity-connection-cancelpaireddevice-f-sys.md#cancelpaireddevice-system-api) |
| [cancelPairedDevice](arkts-connectivity-connection-cancelpaireddevice-f-sys.md#cancelpaireddevice-system-api) |
| [cancelPairingDevice](arkts-connectivity-connection-cancelpairingdevice-f-sys.md#cancelpairingdevice-system-api) |
| [cancelPairingDevice](arkts-connectivity-connection-cancelpairingdevice-f-sys.md#cancelpairingdevice-system-api) |
| [connectAllowedProfiles](arkts-connectivity-connection-connectallowedprofiles-f-sys.md#connectallowedprofiles-system-api) |
| [connectAllowedProfiles](arkts-connectivity-connection-connectallowedprofiles-f-sys.md#connectallowedprofiles-system-api) |
| [controlDeviceAction](arkts-connectivity-connection-controldeviceaction-f-sys.md#controldeviceaction-system-api) |
| [disconnectAllowedProfiles](arkts-connectivity-connection-disconnectallowedprofiles-f-sys.md#disconnectallowedprofiles-system-api) |
| [disconnectAllowedProfiles](arkts-connectivity-connection-disconnectallowedprofiles-f-sys.md#disconnectallowedprofiles-system-api) |
| [generateLocalOobData](arkts-connectivity-connection-generatelocaloobdata-f-sys.md#generatelocaloobdata-system-api) |
| [getCarKeyDfxData](arkts-connectivity-connection-getcarkeydfxdata-f-sys.md#getcarkeydfxdata-system-api) |
| [getLocalProfileUuids](arkts-connectivity-connection-getlocalprofileuuids-f-sys.md#getlocalprofileuuids-system-api) |
| [getLocalProfileUuids](arkts-connectivity-connection-getlocalprofileuuids-f-sys.md#getlocalprofileuuids-system-api) |
| [getRemoteDeviceType](arkts-connectivity-connection-getremotedevicetype-f-sys.md#getremotedevicetype-system-api) |
| [getRemoteProductId](arkts-connectivity-connection-getremoteproductid-f-sys.md#getremoteproductid-system-api) |
| [getRemoteProfileUuids](arkts-connectivity-connection-getremoteprofileuuids-f-sys.md#getremoteprofileuuids-system-api) |
| [getRemoteProfileUuids](arkts-connectivity-connection-getremoteprofileuuids-f-sys.md#getremoteprofileuuids-system-api) |
| [off_discoveryResult](arkts-connectivity-connection-offdiscoveryresult-f-sys.md#offdiscoveryresult) |
| [on_discoveryResult](arkts-connectivity-connection-ondiscoveryresult-f-sys.md#ondiscoveryresult) |
| [pairCredibleDevice](arkts-connectivity-connection-paircredibledevice-f-sys.md#paircredibledevice-system-api) |
| [pairCredibleDevice](arkts-connectivity-connection-paircredibledevice-f-sys.md#paircredibledevice-system-api) |
| [pairDeviceOutOfBand](arkts-connectivity-connection-pairdeviceoutofband-f-sys.md#pairdeviceoutofband-system-api) |
| [setCarKeyDfxData](arkts-connectivity-connection-setcarkeydfxdata-f-sys.md#setcarkeydfxdata-system-api) |
| [setRemoteDeviceType](arkts-connectivity-connection-setremotedevicetype-f-sys.md#setremotedevicetype-system-api) |
| [startPairOutOfBand](arkts-connectivity-connection-startpairoutofband-f-sys.md#startpairoutofband-system-api) |
| [updateCloudBluetoothDevice](arkts-connectivity-connection-updatecloudbluetoothdevice-f-sys.md#updatecloudbluetoothdevice-system-api) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AclStateResult](arkts-connectivity-connection-aclstateresult-i.md) |
| [BatteryInfo](arkts-connectivity-connection-batteryinfo-i.md) |
| [BondStateParam](arkts-connectivity-connection-bondstateparam-i.md) |
| [DeviceClass](arkts-connectivity-connection-deviceclass-i.md) |
| [PinRequiredParam](arkts-connectivity-connection-pinrequiredparam-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BatteryInfo](arkts-connectivity-connection-batteryinfo-i-sys.md) |
| [ControlDeviceActionParams](arkts-connectivity-connection-controldeviceactionparams-i-sys.md) |
| [DiscoveryResult](arkts-connectivity-connection-discoveryresult-i-sys.md) |
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

<!--Del-->
### Types（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ProfileUuids](arkts-connectivity-connection-profileuuids-t-sys.md) |
<!--DelEnd-->
