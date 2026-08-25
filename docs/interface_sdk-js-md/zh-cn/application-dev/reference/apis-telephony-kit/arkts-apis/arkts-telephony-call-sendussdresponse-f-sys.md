# sendUssdResponse（系统接口）

## 导入模块

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## sendUssdResponse

```TypeScript
function sendUssdResponse(slotId: number, content: string): void
```

用于向运营商发送USSD业务（Unstructured Supplementary Service Data，非结构化补充数据业务）的响应消息。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| content | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 8400001 |
| 8400002 |
| 8400003 |
