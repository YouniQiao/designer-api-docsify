# GattClientDevice

Manages GATT client. Before calling an Gatt client method, you must use [createGattClientDevice](arkts-connectivity-ble-creategattclientdevice-f.md) to create an GattClientDevice instance.

**Since:** 10

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { ble } from 'kits/@kit.ConnectivityKit';
```

## writeCharacteristicValueWithContext

```TypeScript
writeCharacteristicValueWithContext(
      characteristic: BLECharacteristic, writeType: GattWriteType): Promise<GattRspContext>
```

Writes the characteristic of a BLE peripheral device with context.

**Since:** 23

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| characteristic | [BLECharacteristic](arkts-connectivity-bluetooth-blecharacteristic-i.md) | Yes |
| [writeType](arkts-connectivity-ssap-propertywriterequest-i.md) | [GattWriteType](arkts-connectivity-ble-gattwritetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[GattRspContext](arkts-connectivity-ble-gattrspcontext-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900011 |
| 2900099 |
| 2901001 |
| 2901003 |
| 2901004 |
| 2901005 |
| 2901006 |
| 2901007 |
