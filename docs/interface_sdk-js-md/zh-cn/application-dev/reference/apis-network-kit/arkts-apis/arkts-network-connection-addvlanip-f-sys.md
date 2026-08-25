# addVlanIp（系统接口）

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## addVlanIp

```TypeScript
function addVlanIp(ifName: string, vlanId: number, address: LinkAddress): Promise<void>
```

为以太网网卡上对应vlanId的虚拟局域网配置指定的IP地址及子网掩码。使用Promise异步回调。

> **说明：**&gt;
> - 本接口当前仅支持PC设备，其他设备类型上调用本接口返回错误码2100002。

**起始版本：** 23

**需要权限：** ohos.permission.CONNECTIVITY_INTERNAL

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ifName | string | 是 |
| vlanId | number | 是 |
| address | [LinkAddress](arkts-network-vpnextension-linkaddress-t.md) | 是 |

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
| [2100400](../errorcode-net-connection.md#2100400-传入网卡名不正确非以太网) |
