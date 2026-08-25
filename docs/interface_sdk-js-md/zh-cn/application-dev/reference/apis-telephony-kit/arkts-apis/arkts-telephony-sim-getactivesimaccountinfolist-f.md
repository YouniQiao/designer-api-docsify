# getActiveSimAccountInfoList

## 导入模块

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## getActiveSimAccountInfoList

```TypeScript
function getActiveSimAccountInfoList(callback: AsyncCallback<Array<IccAccountInfo>>): void
```

获取激活SIM卡账户信息列表。使用callback异步回调。

> **说明：**&gt;
> 获取ICCID和号码信息时需要GET_TELEPHONY_STATE权限，ICCID和号码信息为敏感数据，不向三方应用开放。调用接口时，获取到的ICCID和号码信息为空。

**起始版本：** 10

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[IccAccountInfo](arkts-telephony-sim-iccaccountinfo-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300004](../errorcode-telephony.md#8300004-未识别sim卡) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |


## getActiveSimAccountInfoList

```TypeScript
function getActiveSimAccountInfoList(): Promise<Array<IccAccountInfo>>
```

获取激活SIM卡账户信息列表。使用Promise异步回调。

> **说明：**&gt;
> 获取ICCID和号码信息时需要GET_TELEPHONY_STATE权限，ICCID和号码信息为敏感数据，不向三方应用开放。调用接口时，获取到的ICCID和号码信息为空。

**起始版本：** 10

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

**系统能力：** SystemCapability.Telephony.CoreService

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[IccAccountInfo](arkts-telephony-sim-iccaccountinfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300004](../errorcode-telephony.md#8300004-未识别sim卡) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
