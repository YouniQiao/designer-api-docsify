# replyCustomEapData

## 导入模块

```TypeScript
import { eap } from 'kits/@kit.NetworkKit';
```

## replyCustomEapData

```TypeScript
function replyCustomEapData(result: CustomResult, data: EapData): void
```

该接口用于通知系统已完成该步定制化处理。

> **说明：**:&gt;
> - 若用于处理收EAP数据包(rx)时的callback，传给系统的EAP数据需要剥离服务器添加的定制部分。&gt;
> - 若用于处理发EAP数据包(tx)时的callback，传给系统的EAP数据为经过添加定制部分后的EAP数据。

**起始版本：** 20

**需要权限：** ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION

**系统能力：** SystemCapability.Communication.NetManager.Eap

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| result | [CustomResult](arkts-network-eap-customresult-e.md) | 是 |
| data | [EapData](arkts-network-eap-eapdata-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [33200004](../errorcode-net-eap.md#33200004-无效的eap结果值) |
| [33200005](../errorcode-net-eap.md#33200005-无效的eap数据长度) |
| [33200009](../errorcode-net-eap.md#33200009-netmanager进程不存在) |
| [33200099](../errorcode-net-eap.md#33200099-程序内部错误) |
