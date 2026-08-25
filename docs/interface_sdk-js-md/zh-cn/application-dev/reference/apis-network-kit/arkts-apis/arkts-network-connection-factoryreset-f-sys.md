# factoryReset（系统接口）

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## factoryReset

```TypeScript
function factoryReset(): Promise<void>
```

出厂重置网络设置，使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.CONNECTIVITY_INTERNAL

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
