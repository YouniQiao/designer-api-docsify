# createConnection

## createConnection

```TypeScript
function createConnection(deviceId: string, name: string): Connection
```

作为客户端的设备创建连接对象，以便后续向服务端设备发起连接。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-linkEnhance-function createConnection(deviceId: string, name: string): Connection--><!--Device-linkEnhance-function createConnection(deviceId: string, name: string): Connection-End-->

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Connection](arkts-distributedservice-linkenhance-connection-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [32390206](../../apis-distributedservice-kit/errorcode-link-enhance.md#32390206-参数非法) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

在客户端设备上，应用需要主动调用createConnection()接口创建连接对象。

```TypeScript
import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55"; // BLE MAC地址，需通过蓝牙扫描获取，详见参数说明
  hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
```
