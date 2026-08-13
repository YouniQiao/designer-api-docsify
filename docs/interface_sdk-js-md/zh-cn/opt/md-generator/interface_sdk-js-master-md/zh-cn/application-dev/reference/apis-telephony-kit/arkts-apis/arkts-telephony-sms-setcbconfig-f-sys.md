# setCBConfig（系统接口）

## setCBConfig

```TypeScript
function setCBConfig(options: CBConfigOptions, callback: AsyncCallback<void>): void
```

设置小区广播配置。使用callback异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.RECEIVE_SMS

<!--Device-sms-function setCBConfig(options: CBConfigOptions, callback: AsyncCallback<void>): void--><!--Device-sms-function setCBConfig(options: CBConfigOptions, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [CBConfigOptions](arkts-telephony-sms-cbconfigoptions-i-sys.md) | 是 |
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

let cbConfigOptions: sms.CBConfigOptions = {
    slotId: 0,
    enable: true,
    startMessageId: 100,
    endMessageId: 200,
    ranType: sms.RanType.TYPE_GSM
};
sms.setCBConfig(cbConfigOptions, (err: BusinessError) => {
      console.info(`callback: err->${JSON.stringify(err)}`);
});
```


## setCBConfig

```TypeScript
function setCBConfig(options: CBConfigOptions): Promise<void>
```

设置小区广播配置。使用Promise异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.RECEIVE_SMS

<!--Device-sms-function setCBConfig(options: CBConfigOptions): Promise<void>--><!--Device-sms-function setCBConfig(options: CBConfigOptions): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [CBConfigOptions](arkts-telephony-sms-cbconfigoptions-i-sys.md) | 是 |

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

let cbConfigOptions: sms.CBConfigOptions = {
    slotId: 0,
    enable: true,
    startMessageId: 100,
    endMessageId: 200,
    ranType: sms.RanType.TYPE_GSM
};
let promise = sms.setCBConfig(cbConfigOptions);
promise.then(() => {
    console.info(`setCBConfig success.`);
}).catch((err: BusinessError) => {
    console.error(`setCBConfig failed, promise: err->${JSON.stringify(err)}`);
});
```
