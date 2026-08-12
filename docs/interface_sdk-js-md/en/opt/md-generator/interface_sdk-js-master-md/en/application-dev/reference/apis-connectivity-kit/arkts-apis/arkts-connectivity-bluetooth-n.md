# bluetooth

Provides methods to operate or manage Bluetooth.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [bluetoothManager](ohos.bluetoothManager)

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
| [getState](arkts-connectivity-bluetooth-getstate-f.md#getstate) |
| [getBtConnectionState](arkts-connectivity-bluetooth-getbtconnectionstate-f.md#getbtconnectionstate) |
| [pairDevice](arkts-connectivity-bluetooth-pairdevice-f.md#pairdevice) |
| [getRemoteDeviceName](arkts-connectivity-bluetooth-getremotedevicename-f.md#getremotedevicename) |
| [getRemoteDeviceClass](arkts-connectivity-bluetooth-getremotedeviceclass-f.md#getremotedeviceclass) |
| [enableBluetooth](arkts-connectivity-bluetooth-enablebluetooth-f.md#enablebluetooth) |
| [disableBluetooth](arkts-connectivity-bluetooth-disablebluetooth-f.md#disablebluetooth) |
| [getLocalName](arkts-connectivity-bluetooth-getlocalname-f.md#getlocalname) |
| [getPairedDevices](arkts-connectivity-bluetooth-getpaireddevices-f.md#getpaireddevices) |
| [getProfileConnState](arkts-connectivity-bluetooth-getprofileconnstate-f.md#getprofileconnstate) |
| [setDevicePairingConfirmation](arkts-connectivity-bluetooth-setdevicepairingconfirmation-f.md#setdevicepairingconfirmation) |
| [setLocalName](arkts-connectivity-bluetooth-setlocalname-f.md#setlocalname) |
| [setBluetoothScanMode](arkts-connectivity-bluetooth-setbluetoothscanmode-f.md#setbluetoothscanmode) |
| [getBluetoothScanMode](arkts-connectivity-bluetooth-getbluetoothscanmode-f.md#getbluetoothscanmode) |
| [startBluetoothDiscovery](arkts-connectivity-bluetooth-startbluetoothdiscovery-f.md#startbluetoothdiscovery) |
| [stopBluetoothDiscovery](arkts-connectivity-bluetooth-stopbluetoothdiscovery-f.md#stopbluetoothdiscovery) |
| [on](arkts-connectivity-bluetooth-on-f.md#on) |
| [off](arkts-connectivity-bluetooth-off-f.md#off) |
| [on](arkts-connectivity-bluetooth-on-f.md#on-1) |
| [off](arkts-connectivity-bluetooth-off-f.md#off-1) |
| [on](arkts-connectivity-bluetooth-on-f.md#on-2) |
| [off](arkts-connectivity-bluetooth-off-f.md#off-2) |
| [on](arkts-connectivity-bluetooth-on-f.md#on-3) |
| [off](arkts-connectivity-bluetooth-off-f.md#off-3) |
| [sppListen](arkts-connectivity-bluetooth-spplisten-f.md#spplisten) |
| [sppAccept](arkts-connectivity-bluetooth-sppaccept-f.md#sppaccept) |
| [sppConnect](arkts-connectivity-bluetooth-sppconnect-f.md#sppconnect) |
| [sppCloseServerSocket](arkts-connectivity-bluetooth-sppcloseserversocket-f.md#sppcloseserversocket) |
| [sppCloseClientSocket](arkts-connectivity-bluetooth-sppcloseclientsocket-f.md#sppcloseclientsocket) |
| [sppWrite](arkts-connectivity-bluetooth-sppwrite-f.md#sppwrite) |
| [on](arkts-connectivity-bluetooth-on-f.md#on-4) |
| [off](arkts-connectivity-bluetooth-off-f.md#off-4) |
| [getProfile](arkts-connectivity-bluetooth-getprofile-f.md#getprofile) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cancelPairedDevice](arkts-connectivity-bluetooth-cancelpaireddevice-f-sys.md#cancelpaireddevice) |
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
