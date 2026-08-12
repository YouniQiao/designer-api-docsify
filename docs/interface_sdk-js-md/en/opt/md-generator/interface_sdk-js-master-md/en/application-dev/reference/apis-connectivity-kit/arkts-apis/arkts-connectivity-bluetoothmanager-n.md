# bluetoothManager

Provides methods to operate or manage Bluetooth.

**Since:** 9

**Deprecated since:** 10

<!--Device-unnamed-declare namespace bluetoothManager--><!--Device-unnamed-declare namespace bluetoothManager-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { bluetoothManager } from '@kit.ConnectivityKit';
```

## Summary

### Namespaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BLE](arkts-connectivity-bluetoothmanager-ble-n.md) |

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getState](arkts-connectivity-bluetoothmanager-getstate-f.md#getstate) |
| [getBtConnectionState](arkts-connectivity-bluetoothmanager-getbtconnectionstate-f.md#getbtconnectionstate) |
| [pairDevice](arkts-connectivity-bluetoothmanager-pairdevice-f.md#pairdevice) |
| [getRemoteDeviceName](arkts-connectivity-bluetoothmanager-getremotedevicename-f.md#getremotedevicename) |
| [getRemoteDeviceClass](arkts-connectivity-bluetoothmanager-getremotedeviceclass-f.md#getremotedeviceclass) |
| [enableBluetooth](arkts-connectivity-bluetoothmanager-enablebluetooth-f.md#enablebluetooth) |
| [disableBluetooth](arkts-connectivity-bluetoothmanager-disablebluetooth-f.md#disablebluetooth) |
| [getLocalName](arkts-connectivity-bluetoothmanager-getlocalname-f.md#getlocalname) |
| [getPairedDevices](arkts-connectivity-bluetoothmanager-getpaireddevices-f.md#getpaireddevices) |
| [getProfileConnectionState](arkts-connectivity-bluetoothmanager-getprofileconnectionstate-f.md#getprofileconnectionstate) |
| [setDevicePairingConfirmation](arkts-connectivity-bluetoothmanager-setdevicepairingconfirmation-f.md#setdevicepairingconfirmation) |
| [setLocalName](arkts-connectivity-bluetoothmanager-setlocalname-f.md#setlocalname) |
| [setBluetoothScanMode](arkts-connectivity-bluetoothmanager-setbluetoothscanmode-f.md#setbluetoothscanmode) |
| [getBluetoothScanMode](arkts-connectivity-bluetoothmanager-getbluetoothscanmode-f.md#getbluetoothscanmode) |
| [startBluetoothDiscovery](arkts-connectivity-bluetoothmanager-startbluetoothdiscovery-f.md#startbluetoothdiscovery) |
| [stopBluetoothDiscovery](arkts-connectivity-bluetoothmanager-stopbluetoothdiscovery-f.md#stopbluetoothdiscovery) |
| [on](arkts-connectivity-bluetoothmanager-on-f.md#on) |
| [off](arkts-connectivity-bluetoothmanager-off-f.md#off) |
| [on](arkts-connectivity-bluetoothmanager-on-f.md#on-1) |
| [off](arkts-connectivity-bluetoothmanager-off-f.md#off-1) |
| [on](arkts-connectivity-bluetoothmanager-on-f.md#on-2) |
| [off](arkts-connectivity-bluetoothmanager-off-f.md#off-2) |
| [on](arkts-connectivity-bluetoothmanager-on-f.md#on-3) |
| [off](arkts-connectivity-bluetoothmanager-off-f.md#off-3) |
| [sppListen](arkts-connectivity-bluetoothmanager-spplisten-f.md#spplisten) |
| [sppAccept](arkts-connectivity-bluetoothmanager-sppaccept-f.md#sppaccept) |
| [sppConnect](arkts-connectivity-bluetoothmanager-sppconnect-f.md#sppconnect) |
| [sppCloseServerSocket](arkts-connectivity-bluetoothmanager-sppcloseserversocket-f.md#sppcloseserversocket) |
| [sppCloseClientSocket](arkts-connectivity-bluetoothmanager-sppcloseclientsocket-f.md#sppcloseclientsocket) |
| [sppWrite](arkts-connectivity-bluetoothmanager-sppwrite-f.md#sppwrite) |
| [on](arkts-connectivity-bluetoothmanager-on-f.md#on-4) |
| [off](arkts-connectivity-bluetoothmanager-off-f.md#off-4) |
| [getProfileInstance](arkts-connectivity-bluetoothmanager-getprofileinstance-f.md#getprofileinstance) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cancelPairedDevice](arkts-connectivity-bluetoothmanager-cancelpaireddevice-f-sys.md#cancelpaireddevice) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BaseProfile](arkts-connectivity-bluetoothmanager-baseprofile-i.md) |
| [A2dpSourceProfile](arkts-connectivity-bluetoothmanager-a2dpsourceprofile-i.md) |
| [HandsFreeAudioGatewayProfile](arkts-connectivity-bluetoothmanager-handsfreeaudiogatewayprofile-i.md) |
| [HidHostProfile](arkts-connectivity-bluetoothmanager-hidhostprofile-i.md) |
| [PanProfile](arkts-connectivity-bluetoothmanager-panprofile-i.md) |
| [GattServer](arkts-connectivity-bluetoothmanager-gattserver-i.md) |
| [GattClientDevice](arkts-connectivity-bluetoothmanager-gattclientdevice-i.md) |
| [GattService](arkts-connectivity-bluetoothmanager-gattservice-i.md) |
| [BLECharacteristic](arkts-connectivity-bluetoothmanager-blecharacteristic-i.md) |
| [BLEDescriptor](arkts-connectivity-bluetoothmanager-bledescriptor-i.md) |
| [NotifyCharacteristic](arkts-connectivity-bluetoothmanager-notifycharacteristic-i.md) |
| [CharacteristicReadRequest](arkts-connectivity-bluetoothmanager-characteristicreadrequest-i.md) |
| [CharacteristicWriteRequest](arkts-connectivity-bluetoothmanager-characteristicwriterequest-i.md) |
| [DescriptorReadRequest](arkts-connectivity-bluetoothmanager-descriptorreadrequest-i.md) |
| [DescriptorWriteRequest](arkts-connectivity-bluetoothmanager-descriptorwriterequest-i.md) |
| [ServerResponse](arkts-connectivity-bluetoothmanager-serverresponse-i.md) |
| [BLEConnectChangedState](arkts-connectivity-bluetoothmanager-bleconnectchangedstate-i.md) |
| [ScanResult](arkts-connectivity-bluetoothmanager-scanresult-i.md) |
| [AdvertiseSetting](arkts-connectivity-bluetoothmanager-advertisesetting-i.md) |
| [AdvertiseData](arkts-connectivity-bluetoothmanager-advertisedata-i.md) |
| [ManufactureData](arkts-connectivity-bluetoothmanager-manufacturedata-i.md) |
| [ServiceData](arkts-connectivity-bluetoothmanager-servicedata-i.md) |
| [ScanFilter](arkts-connectivity-bluetoothmanager-scanfilter-i.md) |
| [ScanOptions](arkts-connectivity-bluetoothmanager-scanoptions-i.md) |
| [SppOption](arkts-connectivity-bluetoothmanager-sppoption-i.md) |
| [PinRequiredParam](arkts-connectivity-bluetoothmanager-pinrequiredparam-i.md) |
| [DeviceClass](arkts-connectivity-bluetoothmanager-deviceclass-i.md) |
| [BondStateParam](arkts-connectivity-bluetoothmanager-bondstateparam-i.md) |
| [StateChangeParam](arkts-connectivity-bluetoothmanager-statechangeparam-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [HidHostProfile](arkts-connectivity-bluetoothmanager-hidhostprofile-i-sys.md) |
| [PanProfile](arkts-connectivity-bluetoothmanager-panprofile-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ScanDuty](arkts-connectivity-bluetoothmanager-scanduty-e.md) |
| [MatchMode](arkts-connectivity-bluetoothmanager-matchmode-e.md) |
| [ProfileConnectionState](arkts-connectivity-bluetoothmanager-profileconnectionstate-e.md) |
| [BluetoothState](arkts-connectivity-bluetoothmanager-bluetoothstate-e.md) |
| [SppType](arkts-connectivity-bluetoothmanager-spptype-e.md) |
| [ScanMode](arkts-connectivity-bluetoothmanager-scanmode-e.md) |
| [BondState](arkts-connectivity-bluetoothmanager-bondstate-e.md) |
| [MajorClass](arkts-connectivity-bluetoothmanager-majorclass-e.md) |
| [MajorMinorClass](arkts-connectivity-bluetoothmanager-majorminorclass-e.md) |
| [PlayingState](arkts-connectivity-bluetoothmanager-playingstate-e.md) |
| [ProfileId](arkts-connectivity-bluetoothmanager-profileid-e.md) |
