# replyCustomEapData

## 导入模块

```TypeScript
import { eap } from 'kits/@kit.NetworkKit';
```

## replyCustomEapData

```TypeScript
function replyCustomEapData(result: CustomResult, data: EapData): void
```

send Customized eap packets to system

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION

<!--Device-eap-function replyCustomEapData(result: CustomResult, data: EapData): void--><!--Device-eap-function replyCustomEapData(result: CustomResult, data: EapData): void-End-->

**系统能力：** SystemCapability.Communication.NetManager.Eap

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | [CustomResult](arkts-network-eap-customresult-e.md) | 是 | Indicates the result of custom authentication. |
| data | [EapData](arkts-network-eap-eapdata-i.md) | 是 | Indicates eap packet data after customization. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 33200009 | netmanager stop |
| 201 | Permission denied. |
| 33200099 | internal error |
| 33200004 | Invalid result |
| 33200005 | Invalid size of eap data |

