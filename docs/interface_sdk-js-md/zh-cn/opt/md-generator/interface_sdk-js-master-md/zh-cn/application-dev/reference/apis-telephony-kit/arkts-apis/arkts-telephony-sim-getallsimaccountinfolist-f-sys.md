# getAllSimAccountInfoList（系统接口）

## getAllSimAccountInfoList

```TypeScript
function getAllSimAccountInfoList(callback: AsyncCallback<Array<IccAccountInfo>>): void
```

Get the list of all SIM card account information.

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

<!--Device-sim-function getAllSimAccountInfoList(callback: AsyncCallback<Array<IccAccountInfo>>): void--><!--Device-sim-function getAllSimAccountInfoList(callback: AsyncCallback<Array<IccAccountInfo>>): void-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[IccAccountInfo](arkts-telephony-sim-iccaccountinfo-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
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

sim.getAllSimAccountInfoList((err: BusinessError) => {
    console.info(`callback: err->${JSON.stringify(err)}`);
});
```


## getAllSimAccountInfoList

```TypeScript
function getAllSimAccountInfoList(): Promise<Array<IccAccountInfo>>
```

Get the list of all SIM card account information.

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

<!--Device-sim-function getAllSimAccountInfoList(): Promise<Array<IccAccountInfo>>--><!--Device-sim-function getAllSimAccountInfoList(): Promise<Array<IccAccountInfo>>-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[IccAccountInfo](arkts-telephony-sim-iccaccountinfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8300004](../errorcode-telephony.md#8300004-未识别sim卡) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

async getAllSimAccountInfoList(): Promise<ResponseData<sim.IccAccountInfo[] | null>> {
    try {
      const accountInfoList: sim.IccAccountInfo[] =
        await sim.getAllSimAccountInfoList();
      return { success: true, code: CommonConstant.DEFAULT_SUCCESS_CODE, data: accountInfoList };
    } catch (err) {
      return this.handleError(this.getAllSimAccountInfoList.name, err);
    }
  }
```
