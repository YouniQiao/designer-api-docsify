# addIccDiallingNumbers（系统接口）

## addIccDiallingNumbers

```TypeScript
function addIccDiallingNumbers(slotId: number, type: ContactType, diallingNumbers: DiallingNumbersInfo, callback: AsyncCallback<void>): void
```

Add dialing number information to SIM card.

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.WRITE_CONTACTS

<!--Device-sim-function addIccDiallingNumbers(slotId: int, type: ContactType, diallingNumbers: DiallingNumbersInfo, callback: AsyncCallback<void>): void--><!--Device-sim-function addIccDiallingNumbers(slotId: int, type: ContactType, diallingNumbers: DiallingNumbersInfo, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| type | [ContactType](arkts-telephony-sim-contacttype-e-sys.md) | 是 |
| diallingNumbers | [DiallingNumbersInfo](arkts-telephony-sim-diallingnumbersinfo-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8301002](../errorcode-telephony.md#8301002-sim卡读取数据或者更新数据失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8300004](../errorcode-telephony.md#8300004-未识别sim卡) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

let diallingNumbersInfo: sim.DiallingNumbersInfo = {
    alphaTag: "alpha",
    number: "138xxxxxxxx",
    pin2: "1234"
};
sim.addIccDiallingNumbers(0, sim.ContactType.GENERAL_CONTACT, diallingNumbersInfo, (err: BusinessError) => {
    console.info(`callback: err->${JSON.stringify(err)}`);
});
```


## addIccDiallingNumbers

```TypeScript
function addIccDiallingNumbers(slotId: number, type: ContactType, diallingNumbers: DiallingNumbersInfo): Promise<void>
```

Add dialing number information to SIM card.

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.WRITE_CONTACTS

<!--Device-sim-function addIccDiallingNumbers(slotId: int, type: ContactType, diallingNumbers: DiallingNumbersInfo): Promise<void>--><!--Device-sim-function addIccDiallingNumbers(slotId: int, type: ContactType, diallingNumbers: DiallingNumbersInfo): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| type | [ContactType](arkts-telephony-sim-contacttype-e-sys.md) | 是 |
| diallingNumbers | [DiallingNumbersInfo](arkts-telephony-sim-diallingnumbersinfo-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8301002](../errorcode-telephony.md#8301002-sim卡读取数据或者更新数据失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8300004](../errorcode-telephony.md#8300004-未识别sim卡) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

let diallingNumbersInfo: sim.DiallingNumbersInfo = {
    alphaTag: "alpha",
    number: "138xxxxxxxx"
};
sim.addIccDiallingNumbers(0, sim.ContactType.GENERAL_CONTACT, diallingNumbersInfo).then(() => {
    console.info(`addIccDiallingNumbers success.`);
}).catch((err: BusinessError) => {
    console.error(`addIccDiallingNumbers failed, promise: err->${JSON.stringify(err)}`);
});
```
