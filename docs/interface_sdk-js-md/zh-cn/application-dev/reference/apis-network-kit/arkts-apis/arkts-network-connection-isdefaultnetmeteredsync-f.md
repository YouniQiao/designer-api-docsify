# isDefaultNetMeteredSync

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## isDefaultNetMeteredSync

```TypeScript
function isDefaultNetMeteredSync(): boolean
```

Checks whether data traffic usage on the current network is metered.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为26.0.0。

**需要权限：** ohos.permission.GET_NETWORK_INFO

<!--Device-connection-function isDefaultNetMeteredSync(): boolean--><!--Device-connection-function isDefaultNetMeteredSync(): boolean-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns true if the current network is metered, else returns false. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 201 | Permission denied. |

## 示例

```TypeScript
import { connection } from '@kit.NetworkKit';

let isMetered = connection.isDefaultNetMeteredSync();
```

