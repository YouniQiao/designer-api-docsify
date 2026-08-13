# bluetooth

Provides methods to operate or manage Bluetooth.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** bluetoothManager

<!--Device-unnamed-declare namespace bluetooth--><!--Device-unnamed-declare namespace bluetooth-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## Summary

### Namespaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BLE](arkts-connectivity-bluetooth-ble-n.md) |

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getState](arkts-connectivity-bluetooth-getstate-f.md#getState) |
| [getBtConnectionState](arkts-connectivity-bluetooth-getbtconnectionstate-f.md#getBtConnectionState) |
| [pairDevice](arkts-connectivity-bluetooth-pairdevice-f.md#pairDevice) |
| [getRemoteDeviceName](arkts-connectivity-bluetooth-getremotedevicename-f.md#getRemoteDeviceName) |
| [getRemoteDeviceClass](arkts-connectivity-bluetooth-getremotedeviceclass-f.md#getRemoteDeviceClass) |
| [enableBluetooth](arkts-connectivity-bluetooth-enablebluetooth-f.md#enableBluetooth) |
| [disableBluetooth](arkts-connectivity-bluetooth-disablebluetooth-f.md#disableBluetooth) |
| [getLocalName](arkts-connectivity-bluetooth-getlocalname-f.md#getLocalName) |
| [getPairedDevices](arkts-connectivity-bluetooth-getpaireddevices-f.md#getPairedDevices) |
| [getProfileConnState](arkts-connectivity-bluetooth-getprofileconnstate-f.md#getProfileConnState) |
| [setDevicePairingConfirmation](arkts-connectivity-bluetooth-setdevicepairingconfirmation-f.md#setDevicePairingConfirmation) |
| [setLocalName](arkts-connectivity-bluetooth-setlocalname-f.md#setLocalName) |
| [setBluetoothScanMode](arkts-connectivity-bluetooth-setbluetoothscanmode-f.md#setBluetoothScanMode) |
| [getBluetoothScanMode](arkts-connectivity-bluetooth-getbluetoothscanmode-f.md#getBluetoothScanMode) |
| [startBluetoothDiscovery](arkts-connectivity-bluetooth-startbluetoothdiscovery-f.md#startBluetoothDiscovery) |
| [stopBluetoothDiscovery](arkts-connectivity-bluetooth-stopbluetoothdiscovery-f.md#stopBluetoothDiscovery) |
| [on_bluetoothDeviceFind](arkts-connectivity-bluetooth-onbluetoothdevicefind-f.md#on_bluetoothDeviceFind) |
| [off_bluetoothDeviceFind](arkts-connectivity-bluetooth-offbluetoothdevicefind-f.md#off_bluetoothDeviceFind) |
| [on_bondStateChange](arkts-connectivity-bluetooth-onbondstatechange-f.md#on_bondStateChange) |
| [off_bondStateChange](arkts-connectivity-bluetooth-offbondstatechange-f.md#off_bondStateChange) |
| [on_pinRequired](arkts-connectivity-bluetooth-onpinrequired-f.md#on_pinRequired) |
| [off_pinRequired](arkts-connectivity-bluetooth-offpinrequired-f.md#off_pinRequired) |
| [on_stateChange](arkts-connectivity-bluetooth-onstatechange-f.md#on_stateChange) |
| [off_stateChange](arkts-connectivity-bluetooth-offstatechange-f.md#off_stateChange) |
| [sppListen](arkts-connectivity-bluetooth-spplisten-f.md#sppListen) |
| [sppAccept](arkts-connectivity-bluetooth-sppaccept-f.md#sppAccept) |
| [sppConnect](arkts-connectivity-bluetooth-sppconnect-f.md#sppConnect) |
| [sppCloseServerSocket](arkts-connectivity-bluetooth-sppcloseserversocket-f.md#sppCloseServerSocket) |
| [sppCloseClientSocket](arkts-connectivity-bluetooth-sppcloseclientsocket-f.md#sppCloseClientSocket) |
| [sppWrite](arkts-connectivity-bluetooth-sppwrite-f.md#sppWrite) |
| [on_sppRead](arkts-connectivity-bluetooth-onsppread-f.md#on_sppRead) |
| [off_sppRead](arkts-connectivity-bluetooth-offsppread-f.md#off_sppRead) |
| [getProfile](arkts-connectivity-bluetooth-getprofile-f.md#getProfile) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cancelPairedDevice](arkts-connectivity-bluetooth-cancelpaireddevice-f-sys.md#cancelPairedDevice-(System-API)) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BaseProfile](arkts-connectivity-bluetooth-baseprofile-i.md) |
| [A2dpSourceProfile](arkts-connectivity-bluetooth-a2dpsourceprofile-i.md) |
| [HandsFreeAudioGatewayProfile](arkts-connectivity-bluetooth-handsfreeaudiogatewayprofile-i.md) |
| [GattServer](arkts-connectivity-bluetooth-gattserver-i.md) |
| [GattClientDevice](arkts-connectivity-bluetooth-gattclientdevice-i.md) |
| [GattService](arkts-connectivity-bluetooth-gattservice-i.md) |
| [BLECharacteristic](arkts-connectivity-bluetooth-blecharacteristic-i.md) |
| [BLEDescriptor](arkts-connectivity-bluetooth-bledescriptor-i.md) |
| [NotifyCharacteristic](arkts-connectivity-bluetooth-notifycharacteristic-i.md) |
| [CharacteristicReadReq](arkts-connectivity-bluetooth-characteristicreadreq-i.md) |
| [CharacteristicWriteReq](arkts-connectivity-bluetooth-characteristicwritereq-i.md) |
| [DescriptorReadReq](arkts-connectivity-bluetooth-descriptorreadreq-i.md) |
| [DescriptorWriteReq](arkts-connectivity-bluetooth-descriptorwritereq-i.md) |
| [ServerResponse](arkts-connectivity-bluetooth-serverresponse-i.md) |
| [BLEConnectChangedState](arkts-connectivity-bluetooth-bleconnectchangedstate-i.md) |
| [ScanResult](arkts-connectivity-bluetooth-scanresult-i.md) |
| [AdvertiseSetting](arkts-connectivity-bluetooth-advertisesetting-i.md) |
| [AdvertiseData](arkts-connectivity-bluetooth-advertisedata-i.md) |
| [ManufactureData](arkts-connectivity-bluetooth-manufacturedata-i.md) |
| [ServiceData](arkts-connectivity-bluetooth-servicedata-i.md) |
| [ScanFilter](arkts-connectivity-bluetooth-scanfilter-i.md) |
| [ScanOptions](arkts-connectivity-bluetooth-scanoptions-i.md) |
| [SppOption](arkts-connectivity-bluetooth-sppoption-i.md) |
| [PinRequiredParam](arkts-connectivity-bluetooth-pinrequiredparam-i.md) |
| [DeviceClass](arkts-connectivity-bluetooth-deviceclass-i.md) |
| [BondStateParam](arkts-connectivity-bluetooth-bondstateparam-i.md) |
| [StateChangeParam](arkts-connectivity-bluetooth-statechangeparam-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ScanDuty](arkts-connectivity-bluetooth-scanduty-e.md) |
| [MatchMode](arkts-connectivity-bluetooth-matchmode-e.md) |
| [ProfileConnectionState](arkts-connectivity-bluetooth-profileconnectionstate-e.md) |
| [BluetoothState](arkts-connectivity-bluetooth-bluetoothstate-e.md) |
| [SppType](arkts-connectivity-bluetooth-spptype-e.md) |
| [ScanMode](arkts-connectivity-bluetooth-scanmode-e.md) |
| [BondState](arkts-connectivity-bluetooth-bondstate-e.md) |
| [MajorClass](arkts-connectivity-bluetooth-majorclass-e.md) |
| [MajorMinorClass](arkts-connectivity-bluetooth-majorminorclass-e.md) |
| [PlayingState](arkts-connectivity-bluetooth-playingstate-e.md) |
| [ProfileId](arkts-connectivity-bluetooth-profileid-e.md) |
