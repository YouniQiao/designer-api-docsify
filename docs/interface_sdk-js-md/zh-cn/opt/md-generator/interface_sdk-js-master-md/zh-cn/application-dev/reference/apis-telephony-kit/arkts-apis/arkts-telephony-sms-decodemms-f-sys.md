# decodeMms（系统接口）

## decodeMms

```TypeScript
function decodeMms(mmsFilePathName: string | Array<number>, callback: AsyncCallback<MmsInformation>): void
```

彩信解码。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-sms-function decodeMms(mmsFilePathName: string | Array<int>, callback: AsyncCallback<MmsInformation>): void--><!--Device-sms-function decodeMms(mmsFilePathName: string | Array<int>, callback: AsyncCallback<MmsInformation>): void-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mmsFilePathName | string \| Array & lt;number & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[MmsInformation](arkts-telephony-sms-mmsinformation-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mmsFilePathName: string = "filename";
sms.decodeMms(mmsFilePathName, (err: BusinessError, data: sms.MmsInformation) => {
      console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});

const mmsPdu: Array<number> = [0x8c, 0x80, 0x98, 0x31, 0x00, 0x8d, 0x92, 0x89, 0x09, 0x80, 0x07, 0xea, 0x31, 0x30, 0x30, 0x38, 0x36, 0x00, 0x97, 0x07, 0xea, 0x31, 0x30, 0x30,0x31, 0x30, 0x00, 0x84, 0x74, 0x79, 0x70, 0x65, 0x00, 0x00];
sms.decodeMms(mmsPdu, (err: BusinessError, data: sms.MmsInformation) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## decodeMms

```TypeScript
function decodeMms(mmsFilePathName: string | Array<number>): Promise<MmsInformation>
```

彩信解码。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-sms-function decodeMms(mmsFilePathName: string | Array<int>): Promise<MmsInformation>--><!--Device-sms-function decodeMms(mmsFilePathName: string | Array<int>): Promise<MmsInformation>-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mmsFilePathName | string \| Array & lt;number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[MmsInformation](arkts-telephony-sms-mmsinformation-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mmsFilePathName: string = "filename";
let promise = sms.decodeMms(mmsFilePathName);
promise.then((data: sms.MmsInformation) => {
    console.info(`decodeMms success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`decodeMms failed, promise: err->${JSON.stringify(err)}`);
});

const mmsPdu: Array<number> = [0x8c, 0x80, 0x98, 0x31, 0x00, 0x8d, 0x92, 0x89, 0x09, 0x80, 0x07, 0xea, 0x31, 0x30, 0x30, 0x38, 0x36, 0x00, 0x97, 0x07, 0xea, 0x31, 0x30, 0x30,0x31, 0x30, 0x00, 0x84, 0x74, 0x79, 0x70, 0x65, 0x00, 0x00];
let promiseArr = sms.decodeMms(mmsPdu);
promiseArr.then((data: sms.MmsInformation) => {
    console.info(`decodeMms success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`decodeMms failed, promise: err->${JSON.stringify(err)}`);
});
```
