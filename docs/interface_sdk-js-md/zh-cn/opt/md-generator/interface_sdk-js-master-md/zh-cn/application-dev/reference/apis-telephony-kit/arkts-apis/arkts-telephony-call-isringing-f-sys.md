# isRinging（系统接口）

## isRinging

```TypeScript
function isRinging(callback: AsyncCallback<boolean>): void
```

判断是否正在响铃。使用callback异步回调。

**起始版本：** 8

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function isRinging(callback: AsyncCallback<boolean>): void--><!--Device-call-function isRinging(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.isRinging((err: BusinessError, data: boolean) => {
    if (err) {
        console.error(`isRinging fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`isRinging success, data->${JSON.stringify(data)}`);
    }
});
```


## isRinging

```TypeScript
function isRinging(): Promise<boolean>
```

判断是否正在响铃。使用Promise异步回调。

**起始版本：** 8

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function isRinging(): Promise<boolean>--><!--Device-call-function isRinging(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.isRinging().then((data: boolean) => {
    console.info(`isRinging success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`isRinging fail, promise: err->${JSON.stringify(err)}`);
});
```
