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
| [getState](arkts-connectivity-bluetoothmanager-getstate-f.md#getState) |
| [getBtConnectionState](arkts-connectivity-bluetoothmanager-getbtconnectionstate-f.md#getBtConnectionState) |
| [pairDevice](arkts-connectivity-bluetoothmanager-pairdevice-f.md#pairDevice) |
| [getRemoteDeviceName](arkts-connectivity-bluetoothmanager-getremotedevicename-f.md#getRemoteDeviceName) |
| [getRemoteDeviceClass](arkts-connectivity-bluetoothmanager-getremotedeviceclass-f.md#getRemoteDeviceClass) |
| [enableBluetooth](arkts-connectivity-bluetoothmanager-enablebluetooth-f.md#enableBluetooth) |
| [disableBluetooth](arkts-connectivity-bluetoothmanager-disablebluetooth-f.md#disableBluetooth) |
| [getLocalName](arkts-connectivity-bluetoothmanager-getlocalname-f.md#getLocalName) |
| [getPairedDevices](arkts-connectivity-bluetoothmanager-getpaireddevices-f.md#getPairedDevices) |
| [getProfileConnectionState](arkts-connectivity-bluetoothmanager-getprofileconnectionstate-f.md#getProfileConnectionState) |
| [setDevicePairingConfirmation](arkts-connectivity-bluetoothmanager-setdevicepairingconfirmation-f.md#setDevicePairingConfirmation) |
| [setLocalName](arkts-connectivity-bluetoothmanager-setlocalname-f.md#setLocalName) |
| [setBluetoothScanMode](arkts-connectivity-bluetoothmanager-setbluetoothscanmode-f.md#setBluetoothScanMode) |
| [getBluetoothScanMode](arkts-connectivity-bluetoothmanager-getbluetoothscanmode-f.md#getBluetoothScanMode) |
| [startBluetoothDiscovery](arkts-connectivity-bluetoothmanager-startbluetoothdiscovery-f.md#startBluetoothDiscovery) |
| [stopBluetoothDiscovery](arkts-connectivity-bluetoothmanager-stopbluetoothdiscovery-f.md#stopBluetoothDiscovery) |
| [on_bluetoothDeviceFind](arkts-connectivity-bluetoothmanager-onbluetoothdevicefind-f.md#on_bluetoothDeviceFind) |
| [off_bluetoothDeviceFind](arkts-connectivity-bluetoothmanager-offbluetoothdevicefind-f.md#off_bluetoothDeviceFind) |
| [on_bondStateChange](arkts-connectivity-bluetoothmanager-onbondstatechange-f.md#on_bondStateChange) |
| [off_bondStateChange](arkts-connectivity-bluetoothmanager-offbondstatechange-f.md#off_bondStateChange) |
| [on_pinRequired](arkts-connectivity-bluetoothmanager-onpinrequired-f.md#on_pinRequired) |
| [off_pinRequired](arkts-connectivity-bluetoothmanager-offpinrequired-f.md#off_pinRequired) |
| [on_stateChange](arkts-connectivity-bluetoothmanager-onstatechange-f.md#on_stateChange) |
| [off_stateChange](arkts-connectivity-bluetoothmanager-offstatechange-f.md#off_stateChange) |
| [sppListen](arkts-connectivity-bluetoothmanager-spplisten-f.md#sppListen) |
| [sppAccept](arkts-connectivity-bluetoothmanager-sppaccept-f.md#sppAccept) |
| [sppConnect](arkts-connectivity-bluetoothmanager-sppconnect-f.md#sppConnect) |
| [sppCloseServerSocket](arkts-connectivity-bluetoothmanager-sppcloseserversocket-f.md#sppCloseServerSocket) |
| [sppCloseClientSocket](arkts-connectivity-bluetoothmanager-sppcloseclientsocket-f.md#sppCloseClientSocket) |
| [sppWrite](arkts-connectivity-bluetoothmanager-sppwrite-f.md#sppWrite) |
| [on_sppRead](arkts-connectivity-bluetoothmanager-onsppread-f.md#on_sppRead) |
| [off_sppRead](arkts-connectivity-bluetoothmanager-offsppread-f.md#off_sppRead) |
| [getProfileInstance](arkts-connectivity-bluetoothmanager-getprofileinstance-f.md#getProfileInstance) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cancelPairedDevice](arkts-connectivity-bluetoothmanager-cancelpaireddevice-f-sys.md#cancelPairedDevice-(System-API)) |
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
