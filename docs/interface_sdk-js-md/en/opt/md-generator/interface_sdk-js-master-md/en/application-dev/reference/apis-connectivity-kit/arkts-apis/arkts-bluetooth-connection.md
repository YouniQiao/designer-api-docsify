# @ohos.bluetooth.connection

Provides methods to operate or manage Bluetooth.

**Since:** 23

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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getBluetoothScanMode](arkts-connectivity-connection-getbluetoothscanmode-f.md#getBluetoothScanMode) |
| [getLastConnectionTime](arkts-connectivity-connection-getlastconnectiontime-f.md#getLastConnectionTime) |
| [getLocalName](arkts-connectivity-connection-getlocalname-f.md#getLocalName) |
| [getPairState](arkts-connectivity-connection-getpairstate-f.md#getPairState) |
| [getPairedDevices](arkts-connectivity-connection-getpaireddevices-f.md#getPairedDevices) |
| [getProfileConnectionState](arkts-connectivity-connection-getprofileconnectionstate-f.md#getProfileConnectionState) |
| [getRemoteDeviceBatteryInfo](arkts-connectivity-connection-getremotedevicebatteryinfo-f.md#getRemoteDeviceBatteryInfo) |
| [getRemoteDeviceClass](arkts-connectivity-connection-getremotedeviceclass-f.md#getRemoteDeviceClass) |
| [getRemoteDeviceName](arkts-connectivity-connection-getremotedevicename-f.md#getRemoteDeviceName) |
| [getRemoteDeviceName](arkts-connectivity-connection-getremotedevicename-f.md#getRemoteDeviceName) |
| [getRemoteDeviceTransport](arkts-connectivity-connection-getremotedevicetransport-f.md#getRemoteDeviceTransport) |
| [getVirtualAddressByHash](arkts-connectivity-connection-getvirtualaddressbyhash-f.md#getVirtualAddressByHash) |
| [isBluetoothDiscovering](arkts-connectivity-connection-isbluetoothdiscovering-f.md#isBluetoothDiscovering) |
| [offAclStateChange](arkts-connectivity-connection-offaclstatechange-f.md#offAclStateChange) |
| [offBatteryChange](arkts-connectivity-connection-offbatterychange-f.md#offBatteryChange) |
| [offBluetoothDeviceFind](arkts-connectivity-connection-offbluetoothdevicefind-f.md#offBluetoothDeviceFind) |
| [offBondStateChange](arkts-connectivity-connection-offbondstatechange-f.md#offBondStateChange) |
| [offDiscoveryResult](arkts-connectivity-connection-offdiscoveryresult-f.md#offDiscoveryResult) |
| [offPinRequired](arkts-connectivity-connection-offpinrequired-f.md#offPinRequired) |
| [offScanModeChange](arkts-connectivity-connection-offscanmodechange-f.md#offScanModeChange) |
| [off_batteryChange](arkts-connectivity-connection-offbatterychange-f.md) |
| off_bluetoothDeviceFind |
| off_bondStateChange |
| off_pinRequired |
| [onAclStateChange](arkts-connectivity-connection-onaclstatechange-f.md#onAclStateChange) |
| [onBatteryChange](arkts-connectivity-connection-onbatterychange-f.md#onBatteryChange) |
| [onBluetoothDeviceFind](arkts-connectivity-connection-onbluetoothdevicefind-f.md#onBluetoothDeviceFind) |
| [onBondStateChange](arkts-connectivity-connection-onbondstatechange-f.md#onBondStateChange) |
| [onDiscoveryResult](arkts-connectivity-connection-ondiscoveryresult-f.md#onDiscoveryResult) |
| [onPinRequired](arkts-connectivity-connection-onpinrequired-f.md#onPinRequired) |
| [onScanModeChange](arkts-connectivity-connection-onscanmodechange-f.md#onScanModeChange) |
| [on_batteryChange](arkts-connectivity-connection-onbatterychange-f.md) |
| on_bluetoothDeviceFind |
| on_bondStateChange |
| on_pinRequired |
| [pairDevice](arkts-connectivity-connection-pairdevice-f.md#pairDevice) |
| [pairDevice](arkts-connectivity-connection-pairdevice-f.md#pairDevice) |
| [pairDevice](arkts-connectivity-connection-pairdevice-f.md#pairDevice) |
| [setBluetoothScanMode](arkts-connectivity-connection-setbluetoothscanmode-f.md#setBluetoothScanMode) |
| [setDevicePairingConfirmation](arkts-connectivity-connection-setdevicepairingconfirmation-f.md#setDevicePairingConfirmation) |
| [setDevicePinCode](arkts-connectivity-connection-setdevicepincode-f.md#setDevicePinCode) |
| [setDevicePinCode](arkts-connectivity-connection-setdevicepincode-f.md#setDevicePinCode) |
| [setLocalName](arkts-connectivity-connection-setlocalname-f.md#setLocalName) |
| [setRemoteDeviceName](arkts-connectivity-connection-setremotedevicename-f.md#setRemoteDeviceName) |
| [startBluetoothDiscovery](arkts-connectivity-connection-startbluetoothdiscovery-f.md#startBluetoothDiscovery) |
| [stopBluetoothDiscovery](arkts-connectivity-connection-stopbluetoothdiscovery-f.md#stopBluetoothDiscovery) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cancelPairedDevice](arkts-connectivity-connection-cancelpaireddevice-f-sys.md#cancelPairedDevice-(System-API)) |
| [cancelPairedDevice](arkts-connectivity-connection-cancelpaireddevice-f-sys.md#cancelPairedDevice-(System-API)) |
| [cancelPairingDevice](arkts-connectivity-connection-cancelpairingdevice-f-sys.md#cancelPairingDevice-(System-API)) |
| [cancelPairingDevice](arkts-connectivity-connection-cancelpairingdevice-f-sys.md#cancelPairingDevice-(System-API)) |
| [connectAllowedProfiles](arkts-connectivity-connection-connectallowedprofiles-f-sys.md#connectAllowedProfiles-(System-API)) |
| [connectAllowedProfiles](arkts-connectivity-connection-connectallowedprofiles-f-sys.md#connectAllowedProfiles-(System-API)) |
| [controlDeviceAction](arkts-connectivity-connection-controldeviceaction-f-sys.md#controlDeviceAction-(System-API)) |
| [disconnectAllowedProfiles](arkts-connectivity-connection-disconnectallowedprofiles-f-sys.md#disconnectAllowedProfiles-(System-API)) |
| [disconnectAllowedProfiles](arkts-connectivity-connection-disconnectallowedprofiles-f-sys.md#disconnectAllowedProfiles-(System-API)) |
| [generateLocalOobData](arkts-connectivity-connection-generatelocaloobdata-f-sys.md#generateLocalOobData-(System-API)) |
| [getCarKeyDfxData](arkts-connectivity-connection-getcarkeydfxdata-f-sys.md#getCarKeyDfxData-(System-API)) |
| [getLocalProfileUuids](arkts-connectivity-connection-getlocalprofileuuids-f-sys.md#getLocalProfileUuids-(System-API)) |
| [getLocalProfileUuids](arkts-connectivity-connection-getlocalprofileuuids-f-sys.md#getLocalProfileUuids-(System-API)) |
| [getRemoteDeviceType](arkts-connectivity-connection-getremotedevicetype-f-sys.md#getRemoteDeviceType-(System-API)) |
| [getRemoteProductId](arkts-connectivity-connection-getremoteproductid-f-sys.md#getRemoteProductId-(System-API)) |
| [getRemoteProfileUuids](arkts-connectivity-connection-getremoteprofileuuids-f-sys.md#getRemoteProfileUuids-(System-API)) |
| [getRemoteProfileUuids](arkts-connectivity-connection-getremoteprofileuuids-f-sys.md#getRemoteProfileUuids-(System-API)) |
| [off_discoveryResult](arkts-connectivity-connection-offdiscoveryresult-f-sys.md#off_discoveryResult) |
| [on_discoveryResult](arkts-connectivity-connection-ondiscoveryresult-f-sys.md#on_discoveryResult) |
| [pairCredibleDevice](arkts-connectivity-connection-paircredibledevice-f-sys.md#pairCredibleDevice-(System-API)) |
| [pairCredibleDevice](arkts-connectivity-connection-paircredibledevice-f-sys.md#pairCredibleDevice-(System-API)) |
| [pairDeviceOutOfBand](arkts-connectivity-connection-pairdeviceoutofband-f-sys.md#pairDeviceOutOfBand-(System-API)) |
| [setCarKeyDfxData](arkts-connectivity-connection-setcarkeydfxdata-f-sys.md#setCarKeyDfxData-(System-API)) |
| [setRemoteDeviceType](arkts-connectivity-connection-setremotedevicetype-f-sys.md#setRemoteDeviceType-(System-API)) |
| [startPairOutOfBand](arkts-connectivity-connection-startpairoutofband-f-sys.md#startPairOutOfBand-(System-API)) |
| [updateCloudBluetoothDevice](arkts-connectivity-connection-updatecloudbluetoothdevice-f-sys.md#updateCloudBluetoothDevice-(System-API)) |
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
