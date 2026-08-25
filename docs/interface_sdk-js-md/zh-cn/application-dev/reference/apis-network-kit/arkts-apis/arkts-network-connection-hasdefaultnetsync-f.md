# hasDefaultNetSync

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## hasDefaultNetSync

```TypeScript
function hasDefaultNetSync(): boolean
```

获取当前是否有可用网络。使用同步方式返回。

**起始版本：** 10

**需要权限：** ohos.permission.GET_NETWORK_INFO

**系统能力：** SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
