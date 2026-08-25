# regCustomEapHandler

## 导入模块

```TypeScript
import { eap } from 'kits/@kit.NetworkKit';
```

## regCustomEapHandler

```TypeScript
function regCustomEapHandler(netType: number, eapCode: number, eapType: number, callback: Callback<EapData>): void
```

用于指定需要定制化处理的EAP报文类型和对应的处理callback。使用callback异步回调。系统会将符合条件的EAP报文送入callback函数中供企业应用获取。

**起始版本：** 20

**需要权限：** ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION

**系统能力：** SystemCapability.Communication.NetManager.Eap

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [netType](arkts-network-policy-networkmatchrule-i-sys.md) | number | 是 |
| eapCode | number | 是 |
| eapType | number | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[EapData](arkts-network-eap-eapdata-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [33200006](../errorcode-net-eap.md#33200006-无效的网络类型) |
| [33200007](../errorcode-net-eap.md#33200007-无效的eapcode值) |
| [33200008](../errorcode-net-eap.md#33200008-无效的eaptype值) |
| [33200009](../errorcode-net-eap.md#33200009-netmanager进程不存在) |
| [33200099](../errorcode-net-eap.md#33200099-程序内部错误) |
