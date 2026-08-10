# getAllNetsSync

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getAllNetsSync

```TypeScript
function getAllNetsSync(): Array<NetHandle>
```

Obtains the list of data networks that are activated.To call this method, you must have the {@code ohos.permission.GET_NETWORK_INFO} permission.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_NETWORK_INFO

<!--Device-connection-function getAllNetsSync(): Array<NetHandle>--><!--Device-connection-function getAllNetsSync(): Array<NetHandle>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;NetHandle&gt; | Returns data networks that are activated. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 201 | Permission denied. |

## 示例

```TypeScript
import { connection } from '@kit.NetworkKit';

// 获取所有处于连接状态的网络列表
let netHandle = connection.getAllNetsSync();
console.info("Succeeded to get netHandle: " + JSON.stringify(netHandle));
```

