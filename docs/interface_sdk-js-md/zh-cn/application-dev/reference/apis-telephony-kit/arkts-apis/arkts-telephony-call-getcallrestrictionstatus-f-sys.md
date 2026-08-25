# getCallRestrictionStatus（系统接口）

## 导入模块

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## getCallRestrictionStatus

```TypeScript
function getCallRestrictionStatus(slotId: number, type: CallRestrictionType, callback: AsyncCallback<RestrictionStatus>): void
```

获取呼叫限制状态。使用callback异步回调。

**起始版本：** 8

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| type | [CallRestrictionType](arkts-telephony-call-callrestrictiontype-e-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RestrictionStatus](arkts-telephony-call-restrictionstatus-e-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |


## getCallRestrictionStatus

```TypeScript
function getCallRestrictionStatus(slotId: number, type: CallRestrictionType): Promise<RestrictionStatus>
```

获取呼叫限制状态。使用Promise异步回调。

**起始版本：** 8

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| type | [CallRestrictionType](arkts-telephony-call-callrestrictiontype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[RestrictionStatus](arkts-telephony-call-restrictionstatus-e-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
