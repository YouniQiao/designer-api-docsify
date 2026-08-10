# GattClientDevice

Manages GATT client. Before calling an Gatt client method, you must use {@link createGattClientDevice} to create an GattClientDevice instance.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ble-interface GattClientDevice--><!--Device-ble-interface GattClientDevice-End-->

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

**ArkTS mode:** ArkTS-Dyn since version 23; ArkTS-Sta since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-GattClientDevice-writeCharacteristicValueWithContext(      characteristic: BLECharacteristic, writeType: GattWriteType): Promise<GattRspContext>--><!--Device-GattClientDevice-writeCharacteristicValueWithContext(      characteristic: BLECharacteristic, writeType: GattWriteType): Promise<GattRspContext>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| characteristic | [BLECharacteristic](arkts-connectivity-bluetooth-blecharacteristic-i.md) | Yes | Indicates the characteristic to write. |
| writeType | [GattWriteType](arkts-connectivity-ble-gattwritetype-e.md) | Yes | Write type of the characteristic. The interface currently only supports {@link GattWriteType#WRITE} mode. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;GattRspContext&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 2901004 | The connection is congested. |
| 801 | Capability not supported. |
| 2901005 | The connection is not encrypted. |
| 2901006 | The connection is not authenticated. |
| 2901007 | The connection is not authorized. |
| 2901001 | Write forbidden. |
| 2900011 | The operation is busy. The last operation is not complete. |
| 2901003 | The connection is not established. |
| 201 | Permission denied. |
| 202 | Non-system applications are not allowed to use system APIs. |
| 2900099 | Operation failed. |

## Examples

```TypeScript
let descriptors: Array<ble.BLEDescriptor>  = [];
let bufferDesc = new ArrayBuffer(2);
let descV = new Uint8Array(bufferDesc);
descV[0] = 0; // Use the Client Characteristic Configuration descriptor as an example. When bit 0 and bit 1 are both set to 0, the notification and indication functions are disabled.
let descriptor: ble.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
descriptors[0] = descriptor;

let bufferCCC = new ArrayBuffer(8);
let cccV = new Uint8Array(bufferCCC);
cccV[0] = 1;
let characteristic: ble.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  characteristicValue: bufferCCC, descriptors:descriptors};
try {
    let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.writeCharacteristicValueWithContext(characteristic, ble.GattWriteType.WRITE).then((rspContext: ble.GattRspContext) => {
        console.info('timestamp is: ' + rspContext.timestamp);
    });
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

