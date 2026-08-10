# getAppNetSync

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getAppNetSync

```TypeScript
function getAppNetSync(): NetHandle
```

Obtains the {@link NetHandle} bound to a process using {@link setAppNet}.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为26.0.0。

<!--Device-connection-function getAppNetSync(): NetHandle--><!--Device-connection-function getAppNetSync(): NetHandle-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NetHandle](arkts-network-connection-nethandle-i.md) | Returns the { |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

## 示例

```TypeScript
import { connection } from '@kit.NetworkKit';

// 获取App绑定的网络信息
let netHandle = connection.getAppNetSync();
console.info('Succeeded to getAppNetSync:' + JSON.stringify(netHandle));
```

