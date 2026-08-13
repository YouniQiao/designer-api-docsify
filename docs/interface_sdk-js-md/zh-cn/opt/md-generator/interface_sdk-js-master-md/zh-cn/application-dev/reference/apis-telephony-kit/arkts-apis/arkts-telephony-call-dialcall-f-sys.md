# dialCall（系统接口）

## dialCall

```TypeScript
function dialCall(phoneNumber: string, options: DialCallOptions, callback: AsyncCallback<void>): void
```

拨打电话，可设置通话参数。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.PLACE_CALL

<!--Device-call-function dialCall(phoneNumber: string, options: DialCallOptions, callback: AsyncCallback<void>): void--><!--Device-call-function dialCall(phoneNumber: string, options: DialCallOptions, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| phoneNumber | string | 是 |
| options | [DialCallOptions](arkts-telephony-call-dialcalloptions-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 8300006 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 8300005 |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let dialCallOptions: call.DialCallOptions = {
    accountId: 0,
    videoState: 0,
    dialScene: 0,
    dialType: 0
}
call.dialCall("138xxxxxxxx", dialCallOptions, (err: BusinessError) => {
    if (err) {
        console.error(`dialCall fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`dialCall success.`);
    }
});
```


## dialCall

```TypeScript
function dialCall(phoneNumber: string, options?: DialCallOptions): Promise<void>
```

拨打电话，可设置通话参数。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.PLACE_CALL

<!--Device-call-function dialCall(phoneNumber: string, options?: DialCallOptions): Promise<void>--><!--Device-call-function dialCall(phoneNumber: string, options?: DialCallOptions): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| phoneNumber | string | 是 |
| options | [DialCallOptions](arkts-telephony-call-dialcalloptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 8300006 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 8300005 |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let dialCallOptions: call.DialCallOptions = {
    accountId: 0,
    videoState: 0,
    dialScene: 0,
    dialType: 0
}
call.dialCall("138xxxxxxxx", dialCallOptions).then(() => {
    console.info(`dialCall success.`);
}).catch((err: BusinessError) => {
    console.error(`dialCall fail, promise: err->${JSON.stringify(err)}`);
});
```


## dialCall

```TypeScript
function dialCall(phoneNumber: string, callback: AsyncCallback<void>): void
```

拨打电话。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.PLACE_CALL

<!--Device-call-function dialCall(phoneNumber: string, callback: AsyncCallback<void>): void--><!--Device-call-function dialCall(phoneNumber: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| phoneNumber | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 8300006 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 8300005 |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.dialCall("138xxxxxxxx", (err: BusinessError) => {
    if (err) {
        console.error(`dialCall fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`dialCall success.`);
    }
});
```
