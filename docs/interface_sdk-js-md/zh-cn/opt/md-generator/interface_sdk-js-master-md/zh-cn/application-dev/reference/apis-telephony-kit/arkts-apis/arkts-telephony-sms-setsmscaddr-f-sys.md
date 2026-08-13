# setSmscAddr（系统接口）

## setSmscAddr

```TypeScript
function setSmscAddr(slotId: number, smscAddr: string, callback: AsyncCallback<void>): void
```

设置短信服务中心（SMSC）地址。使用callback异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-sms-function setSmscAddr(slotId: int, smscAddr: string, callback: AsyncCallback<void>): void--><!--Device-sms-function setSmscAddr(slotId: int, smscAddr: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| smscAddr | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

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
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
let smscAddr: string = '+861xxxxxxxxxx';
sms.setSmscAddr(slotId, smscAddr, (err: BusinessError) => {
      console.info(`callback: err->${JSON.stringify(err)}`);
});
```


## setSmscAddr

```TypeScript
function setSmscAddr(slotId: number, smscAddr: string): Promise<void>
```

设置短信服务中心（SMSC）地址。使用Promise异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-sms-function setSmscAddr(slotId: int, smscAddr: string): Promise<void>--><!--Device-sms-function setSmscAddr(slotId: int, smscAddr: string): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| smscAddr | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

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
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
let smscAddr: string = '+861xxxxxxxxxx';
sms.setSmscAddr(slotId, smscAddr).then(() => {
    console.info(`setSmscAddr success.`);
}).catch((err: BusinessError) => {
    console.error(`setSmscAddr failed, promise: err->${JSON.stringify(err)}`);
});
```
