# startEthEap

## 导入模块

```TypeScript
import { eap } from 'kits/@kit.NetworkKit';
```

## startEthEap

```TypeScript
function startEthEap(netId: number, profile: EthEapProfile): void
```

该接口用于指定一个以太网卡发起EAP认证。

**起始版本：** 20

**需要权限：** ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION

**系统能力：** SystemCapability.Communication.NetManager.Eap

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| netId | number | 是 |
| profile | [EthEapProfile](arkts-network-eap-etheapprofile-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [33200001](../errorcode-net-eap.md#33200001-无效的netid值) |
| [33200003](../errorcode-net-eap.md#33200003-无效的eth-eap配置) |
| [33200009](../errorcode-net-eap.md#33200009-netmanager进程不存在) |
| [33200010](../errorcode-net-eap.md#33200010-无效的eth状态) |
| [33200099](../errorcode-net-eap.md#33200099-程序内部错误) |
