# getRadioTechSync

## 导入模块

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## getRadioTechSync

```TypeScript
function getRadioTechSync(slotId: number): NetworkRadioTech
```

获取当前接入的CS域和PS域无线接入技术。CS域为电路交换域，PS为分组交换域。

**起始版本：** 18

**需要权限：** ohos.permission.GET_NETWORK_INFO

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |

**返回值：**

| 类型 |
| --- |
| [NetworkRadioTech](arkts-telephony-radio-networkradiotech-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
