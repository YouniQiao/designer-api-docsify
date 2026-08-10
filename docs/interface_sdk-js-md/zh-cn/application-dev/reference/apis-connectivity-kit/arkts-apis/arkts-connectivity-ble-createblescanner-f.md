# createBleScanner

## 导入模块

```TypeScript
import { ble } from 'kits/@kit.ConnectivityKit';
```

## createBleScanner

```TypeScript
function createBleScanner(): BleScanner
```

Create a ble scanner instance. Each ble scanner instance can be independently started or stopped.

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-ble-function createBleScanner(): BleScanner--><!--Device-ble-function createBleScanner(): BleScanner-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BleScanner](arkts-connectivity-ble-blescanner-i.md) | Returns the promise object. |

## 示例

```TypeScript
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
import { ble } from '@kit.ConnectivityKit';
let bleScanner: ble.BleScanner = ble.createBleScanner();
console.info('create bleScanner success');
```

