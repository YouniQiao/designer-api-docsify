# off（系统接口）

## 导入模块

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## off('imsRegStateChange')

```TypeScript
function off(type: 'imsRegStateChange', slotId: number, imsType: ImsServiceType, callback?: Callback<ImsRegInfo>): void
```

Unsubscribe from imsRegStateChange event.

**起始版本：** 9

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'imsRegStateChange' | 是 |
| slotId | number | 是 |
| imsType | [ImsServiceType](arkts-telephony-radio-imsservicetype-e-sys.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ImsRegInfo](arkts-telephony-radio-imsreginfo-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
