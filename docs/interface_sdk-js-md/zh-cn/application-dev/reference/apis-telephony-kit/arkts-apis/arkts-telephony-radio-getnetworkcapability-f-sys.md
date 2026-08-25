# getNetworkCapability（系统接口）

## 导入模块

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## getNetworkCapability

```TypeScript
function getNetworkCapability(slotId: number, type: NetworkCapabilityType,
    callback: AsyncCallback<NetworkCapabilityState>): void
```

Get the network capability state according to the specified capability type.

**起始版本：** 10

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| type | [NetworkCapabilityType](arkts-telephony-radio-networkcapabilitytype-e-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[NetworkCapabilityState](arkts-telephony-radio-networkcapabilitystate-e-sys.md)&gt; | 是 |

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


## getNetworkCapability

```TypeScript
function getNetworkCapability(slotId: number, type: NetworkCapabilityType): Promise<NetworkCapabilityState>
```

Get the network capability state according to the specified capability type.

**起始版本：** 10

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| type | [NetworkCapabilityType](arkts-telephony-radio-networkcapabilitytype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[NetworkCapabilityState](arkts-telephony-radio-networkcapabilitystate-e-sys.md)&gt; |

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
