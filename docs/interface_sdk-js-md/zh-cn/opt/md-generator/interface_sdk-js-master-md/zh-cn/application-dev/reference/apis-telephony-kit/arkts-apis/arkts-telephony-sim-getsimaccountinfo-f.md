# getSimAccountInfo

## 导入模块

```TypeScript
```

## getSimAccountInfo

```TypeScript
function getSimAccountInfo(slotId: number, callback: AsyncCallback<IccAccountInfo>): void
```

Get account information of SIM card.

**起始版本：** 23

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

<!--Device-sim-function getSimAccountInfo(slotId: int, callback: AsyncCallback<IccAccountInfo>): void--><!--Device-sim-function getSimAccountInfo(slotId: int, callback: AsyncCallback<IccAccountInfo>): void-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[IccAccountInfo](arkts-telephony-sim-iccaccountinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8301002](../errorcode-telephony.md#8301002-sim卡读取数据或者更新数据失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [8300004](../errorcode-telephony.md#8300004-未识别sim卡) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimAccountInfo(0, (err:BusinessError , data: sim.IccAccountInfo) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## getSimAccountInfo

```TypeScript
function getSimAccountInfo(slotId: number): Promise<IccAccountInfo>
```

Get account information of SIM card.

**起始版本：** 23

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

<!--Device-sim-function getSimAccountInfo(slotId: int): Promise<IccAccountInfo>--><!--Device-sim-function getSimAccountInfo(slotId: int): Promise<IccAccountInfo>-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[IccAccountInfo](arkts-telephony-sim-iccaccountinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8301002](../errorcode-telephony.md#8301002-sim卡读取数据或者更新数据失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [8300004](../errorcode-telephony.md#8300004-未识别sim卡) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimAccountInfo(0).then((data: sim.IccAccountInfo) => {
    console.info(`getSimAccountInfo success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getSimAccountInfo failed, promise: err->${JSON.stringify(err)}`);
});
```
