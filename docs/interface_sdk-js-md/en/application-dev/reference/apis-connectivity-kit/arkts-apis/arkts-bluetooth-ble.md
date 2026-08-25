# @ohos.bluetooth.ble

Provides methods to operate or manage Bluetooth.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { ble } from '@kit.ConnectivityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createBleScanner](arkts-connectivity-ble-createblescanner-f.md) |
| [createGattClientDevice](arkts-connectivity-ble-creategattclientdevice-f.md) |
| [createGattClientDevice](arkts-connectivity-ble-creategattclientdevice-f.md) |
| [createGattServer](arkts-connectivity-ble-creategattserver-f.md) |
| [disableAdvertising](arkts-connectivity-ble-disableadvertising-f.md) |
| [disableAdvertising](arkts-connectivity-ble-disableadvertising-f.md) |
| [enableAdvertising](arkts-connectivity-ble-enableadvertising-f.md) |
| [enableAdvertising](arkts-connectivity-ble-enableadvertising-f.md) |
| [getConnectedBLEDevices](arkts-connectivity-ble-getconnectedbledevices-f.md) |
| [getConnectedBLEDevices](arkts-connectivity-ble-getconnectedbledevices-f.md) |
| off |
| [off](arkts-connectivity-ble-off-f.md#offbledevicefind) |
| on |
| [on](arkts-connectivity-ble-on-f.md#onbledevicefind) |
| [startAdvertising](arkts-connectivity-ble-startadvertising-f.md) |
| [startAdvertising](arkts-connectivity-ble-startadvertising-f.md) |
| [startAdvertising](arkts-connectivity-ble-startadvertising-f.md) |
| [startBLEScan](arkts-connectivity-ble-startblescan-f.md) |
| [startBLEScan](arkts-connectivity-ble-startblescan-f.md) |
| [stopAdvertising](arkts-connectivity-ble-stopadvertising-f.md) |
| [stopAdvertising](arkts-connectivity-ble-stopadvertising-f.md) |
| [stopAdvertising](arkts-connectivity-ble-stopadvertising-f.md) |
| [stopBLEScan](arkts-connectivity-ble-stopblescan-f.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AdvertiseData](arkts-connectivity-ble-advertisedata-i.md) |
| [AdvertiseSetting](arkts-connectivity-ble-advertisesetting-i.md) |
| [AdvertisingDisableParams](arkts-connectivity-ble-advertisingdisableparams-i.md) |
| [AdvertisingEnableParams](arkts-connectivity-ble-advertisingenableparams-i.md) |
| [AdvertisingParams](arkts-connectivity-ble-advertisingparams-i.md) |
| [AdvertisingStateChangeInfo](arkts-connectivity-ble-advertisingstatechangeinfo-i.md) |
| [BLECharacteristic](arkts-connectivity-ble-blecharacteristic-i.md) |
| [BLEConnectionChangeState](arkts-connectivity-ble-bleconnectionchangestate-i.md) |
| [BLEDescriptor](arkts-connectivity-ble-bledescriptor-i.md) |
| [BleScanner](arkts-connectivity-ble-blescanner-i.md) |
| [CharacteristicReadRequest](arkts-connectivity-ble-characteristicreadrequest-i.md) |
| [CharacteristicWriteRequest](arkts-connectivity-ble-characteristicwriterequest-i.md) |
| [DescriptorReadRequest](arkts-connectivity-ble-descriptorreadrequest-i.md) |
| [DescriptorWriteRequest](arkts-connectivity-ble-descriptorwriterequest-i.md) |
| [GattClientDevice](arkts-connectivity-ble-gattclientdevice-i.md) |
| [GattPermissions](arkts-connectivity-ble-gattpermissions-i.md) |
| [GattProperties](arkts-connectivity-ble-gattproperties-i.md) |
| [GattServer](arkts-connectivity-ble-gattserver-i.md) |
| [GattService](arkts-connectivity-ble-gattservice-i.md) |
| [GattSetting](arkts-connectivity-ble-gattsetting-i.md) |
| [ManufactureData](arkts-connectivity-ble-manufacturedata-i.md) |
| [NotifyCharacteristic](arkts-connectivity-ble-notifycharacteristic-i.md) |
| [PhyValue](arkts-connectivity-ble-phyvalue-i.md) |
| [ScanFilter](arkts-connectivity-ble-scanfilter-i.md) |
| [ScanOptions](arkts-connectivity-ble-scanoptions-i.md) |
| [ScanReport](arkts-connectivity-ble-scanreport-i.md) |
| [ScanResult](arkts-connectivity-ble-scanresult-i.md) |
| [ServerResponse](arkts-connectivity-ble-serverresponse-i.md) |
| [ServiceData](arkts-connectivity-ble-servicedata-i.md) |

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [GattClientDevice](arkts-connectivity-ble-gattclientdevice-i-sys.md) |
| [GattRspContext](arkts-connectivity-ble-gattrspcontext-i-sys.md) |
| [ScanEnhanceMode](arkts-connectivity-ble-scanenhancemode-i-sys.md) |
| [ScanFilter](arkts-connectivity-ble-scanfilter-i-sys.md) |
| [ScanOptions](arkts-connectivity-ble-scanoptions-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AdvertisingState](arkts-connectivity-ble-advertisingstate-e.md) |
| [BlePhy](arkts-connectivity-ble-blephy-e.md) |
| [BleProfile](arkts-connectivity-ble-bleprofile-e.md) |
| [CodedPhyMode](arkts-connectivity-ble-codedphymode-e.md) |
| [ConnectionParam](arkts-connectivity-ble-connectionparam-e.md) |
| [GattDisconnectReason](arkts-connectivity-ble-gattdisconnectreason-e.md) |
| [GattWriteType](arkts-connectivity-ble-gattwritetype-e.md) |
| [MatchMode](arkts-connectivity-ble-matchmode-e.md) |
| [PhyType](arkts-connectivity-ble-phytype-e.md) |
| [ScanDuty](arkts-connectivity-ble-scanduty-e.md) |
| [ScanReportMode](arkts-connectivity-ble-scanreportmode-e.md) |
| [ScanReportType](arkts-connectivity-ble-scanreporttype-e.md) |

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EnhanceMode](arkts-connectivity-ble-enhancemode-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BluetoothAddress](arkts-connectivity-ble-bluetoothaddress-t.md) |
| [BluetoothTransport](arkts-connectivity-ble-bluetoothtransport-t.md) |
| [ProfileConnectionState](arkts-connectivity-ble-profileconnectionstate-t.md) |
