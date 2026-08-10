# GattClientDevice

Manages GATT client. Before calling an Gatt client method, you must use {@link createGattClientDevice} to create an GattClientDevice instance.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-ble-interface GattClientDevice--><!--Device-ble-interface GattClientDevice-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { ble } from 'kits/@kit.ConnectivityKit';
```

## writeCharacteristicValueWithContext

```TypeScript
writeCharacteristicValueWithContext(
      characteristic: BLECharacteristic, writeType: GattWriteType): Promise<GattRspContext>
```

Writes the characteristic of a BLE peripheral device with context.

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GattClientDevice-writeCharacteristicValueWithContext(      characteristic: BLECharacteristic, writeType: GattWriteType): Promise<GattRspContext>--><!--Device-GattClientDevice-writeCharacteristicValueWithContext(      characteristic: BLECharacteristic, writeType: GattWriteType): Promise<GattRspContext>-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| characteristic | [BLECharacteristic](arkts-connectivity-bluetooth-blecharacteristic-i.md) | 是 | Indicates the characteristic to write. |
| writeType | [GattWriteType](arkts-connectivity-ble-gattwritetype-e.md) | 是 | Write type of the characteristic. The interface currently only supports {@link GattWriteType#WRITE} mode. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;GattRspContext&gt; | Promise used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
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

## 示例

```TypeScript
let descriptors: Array<ble.BLEDescriptor>  = [];
let bufferDesc = new ArrayBuffer(2);
let descV = new Uint8Array(bufferDesc);
descV[0] = 0; // 以Client Characteristic Configuration描述符为例，表示bit0、bit1均为0，notification和indication均不开启
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

