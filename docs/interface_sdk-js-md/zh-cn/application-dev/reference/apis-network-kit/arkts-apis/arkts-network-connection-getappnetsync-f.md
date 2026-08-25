# getAppNetSync

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getAppNetSync

```TypeScript
function getAppNetSync(): NetHandle
```

获取App绑定的网络信息。使用同步方式返回。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 |
| --- |
| [NetHandle](arkts-network-connection-nethandle-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
