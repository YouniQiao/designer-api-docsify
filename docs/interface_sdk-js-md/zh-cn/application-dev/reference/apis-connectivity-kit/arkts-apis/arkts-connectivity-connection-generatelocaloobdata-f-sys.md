# generateLocalOobData（系统接口）

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.ConnectivityKit';
```

## generateLocalOobData

```TypeScript
function generateLocalOobData(transport: BluetoothTransport): Promise<OobData>
```

Generate out-of-band data of the local device.

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-connection-function generateLocalOobData(transport: BluetoothTransport): Promise<OobData>--><!--Device-connection-function generateLocalOobData(transport: BluetoothTransport): Promise<OobData>-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transport | [BluetoothTransport](arkts-connectivity-ble-bluetoothtransport-t.md) | 是 | Indicates the transport of a remote Bluetooth device. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;OobData&gt; | Returns the out-of-band data. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 202 | Non-system applications are not allowed to use system APIs. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
    let transport: connection.BluetoothTransport = connection.BluetoothTransport.TRANSPORT_LE;
    connection.generateLocalOobData(transport).then((oobData: connection.OobData) => {
        console.info(`generateLocalOobData: ${JSON.stringify(oobData)}`);
    }, (err: BusinessError) => {
        console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
    });
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

