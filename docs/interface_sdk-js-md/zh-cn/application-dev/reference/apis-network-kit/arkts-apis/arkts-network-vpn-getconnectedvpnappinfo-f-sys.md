# getConnectedVpnAppInfo（系统接口）

## 导入模块

```TypeScript
import { vpn } from 'kits/@kit.NetworkKit';
```

## getConnectedVpnAppInfo

```TypeScript
function getConnectedVpnAppInfo(): Promise<Array<string>>
```

获取已连接的VPN应用信息。

**起始版本：** 20

**需要权限：** ohos.permission.MANAGE_VPN

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [19900001](../errorcode-net-vpn.md#19900001-无效参数) |
| [19900002](../errorcode-net-vpn.md#19900002-系统内部错误) |
