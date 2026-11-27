# createGattServer

## 导入模块

```TypeScript
import { ble } from '@kit.ConnectivityKit';
```

## createGattServer

```TypeScript
function createGattServer(): GattServer
```

创建[GattServer](arkts-connectivity-ble-gattserver-i.md)实例，表示GATT连接中的server端。

通过该实例可以操作server端的行为，如添加服务[addService](arkts-connectivity-ble-gattserver-i.md#addservice)、通知特征值变化[notifyCharacteristicChanged](arkts-connectivity-ble-gattserver-i.md#notifycharacteristicchanged-1)等。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-ble-function createGattServer(): GattServer--><!--Device-ble-function createGattServer(): GattServer-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [GattServer](arkts-connectivity-ble-gattserver-i.md) | 返回一个Gatt服务的实例。 |

**示例**

```TypeScript
let gattServer: ble.GattServer = ble.createGattServer();
console.info('gatt success');
```
