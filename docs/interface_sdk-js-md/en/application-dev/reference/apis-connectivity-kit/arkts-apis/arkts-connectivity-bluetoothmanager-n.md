# bluetoothManager

Provides methods to operate or manage Bluetooth.

**Since:** 9

**Deprecated since:** 10

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { bluetoothManager } from 'kits/@kit.ConnectivityKit';
```

## Summary

### Namespaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BLE](arkts-connectivity-bluetoothmanager-ble-n.md) |

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getState](arkts-connectivity-bluetoothmanager-getstate-f.md) |
| [getBtConnectionState](arkts-connectivity-bluetoothmanager-getbtconnectionstate-f.md) |
| [pairDevice](arkts-connectivity-bluetoothmanager-pairdevice-f.md) |
| [getRemoteDeviceName](arkts-connectivity-bluetoothmanager-getremotedevicename-f.md) |
| [getRemoteDeviceClass](arkts-connectivity-bluetoothmanager-getremotedeviceclass-f.md) |
| [enableBluetooth](arkts-connectivity-bluetoothmanager-enablebluetooth-f.md) |
| [disableBluetooth](arkts-connectivity-bluetoothmanager-disablebluetooth-f.md) |
| [getLocalName](arkts-connectivity-bluetoothmanager-getlocalname-f.md) |
| [getPairedDevices](arkts-connectivity-bluetoothmanager-getpaireddevices-f.md) |
| [getProfileConnectionState](arkts-connectivity-bluetoothmanager-getprofileconnectionstate-f.md) |
| [setDevicePairingConfirmation](arkts-connectivity-bluetoothmanager-setdevicepairingconfirmation-f.md) |
| [setLocalName](arkts-connectivity-bluetoothmanager-setlocalname-f.md) |
| [setBluetoothScanMode](arkts-connectivity-bluetoothmanager-setbluetoothscanmode-f.md) |
| [getBluetoothScanMode](arkts-connectivity-bluetoothmanager-getbluetoothscanmode-f.md) |
| [startBluetoothDiscovery](arkts-connectivity-bluetoothmanager-startbluetoothdiscovery-f.md) |
| [stopBluetoothDiscovery](arkts-connectivity-bluetoothmanager-stopbluetoothdiscovery-f.md) |
| [on](arkts-connectivity-bluetoothmanager-on-f.md#onbluetoothdevicefind) |
| [off](arkts-connectivity-bluetoothmanager-off-f.md#offbluetoothdevicefind) |
| [on](arkts-connectivity-bluetoothmanager-on-f.md#onbondstatechange) |
| [off](arkts-connectivity-bluetoothmanager-off-f.md#offbondstatechange) |
| [on](arkts-connectivity-bluetoothmanager-on-f.md#onpinrequired) |
| [off](arkts-connectivity-bluetoothmanager-off-f.md#offpinrequired) |
| [on](arkts-connectivity-bluetoothmanager-on-f.md#onstatechange) |
| [off](arkts-connectivity-bluetoothmanager-off-f.md#offstatechange) |
| [sppListen](arkts-connectivity-bluetoothmanager-spplisten-f.md) |
| [sppAccept](arkts-connectivity-bluetoothmanager-sppaccept-f.md) |
| [sppConnect](arkts-connectivity-bluetoothmanager-sppconnect-f.md) |
| [sppCloseServerSocket](arkts-connectivity-bluetoothmanager-sppcloseserversocket-f.md) |
| [sppCloseClientSocket](arkts-connectivity-bluetoothmanager-sppcloseclientsocket-f.md) |
| [sppWrite](arkts-connectivity-bluetoothmanager-sppwrite-f.md) |
| [on](arkts-connectivity-bluetoothmanager-on-f.md#onsppread) |
| [off](arkts-connectivity-bluetoothmanager-off-f.md#offsppread) |
| [getProfileInstance](arkts-connectivity-bluetoothmanager-getprofileinstance-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cancelPairedDevice](arkts-connectivity-bluetoothmanager-cancelpaireddevice-f-sys.md) |
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
### Interfaces(System API)

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
