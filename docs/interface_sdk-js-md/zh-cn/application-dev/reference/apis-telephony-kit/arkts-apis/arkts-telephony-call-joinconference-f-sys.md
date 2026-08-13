# joinConference（系统接口）

## joinConference

```TypeScript
function joinConference(mainCallId: int, callNumberList: Array<string>, callback: AsyncCallback<void>): void
```

加入会议。使用callback异步回调。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-call-function joinConference(mainCallId: int, callNumberList: Array<string>, callback: AsyncCallback<void>): void--><!--Device-call-function joinConference(mainCallId: int, callNumberList: Array<string>, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mainCallId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 主通话Id。 |
| callNumberList | Array&lt;string&gt; | 是 | 呼叫号码列表。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 以回调函数的方式返回加入会议的结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| [8300999](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) | Unknown error code. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Non-system applications use system APIs. |
| [8300002](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) | Operation failed. Cannot connect to service. |
| [8300003](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) | System internal error. |
| [8300001](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) | Invalid parameter value. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let callNumberList: Array<string> = [
    "138XXXXXXXX"
];
call.joinConference(1, callNumberList, (err: BusinessError) => {
    if (err) {
        console.error(`joinConference fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`joinConference success.`);
    }
});
```


## joinConference

```TypeScript
function joinConference(mainCallId: int, callNumberList: Array<string>): Promise<void>
```

加入会议。使用Promise异步回调。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-call-function joinConference(mainCallId: int, callNumberList: Array<string>): Promise<void>--><!--Device-call-function joinConference(mainCallId: int, callNumberList: Array<string>): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mainCallId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 主通话Id。 |
| callNumberList | Array&lt;string&gt; | 是 | 呼叫号码列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 以Promise形式异步返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| [8300999](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) | Unknown error code. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Non-system applications use system APIs. |
| [8300002](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) | Operation failed. Cannot connect to service. |
| [8300003](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) | System internal error. |
| [8300001](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) | Invalid parameter value. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let callNumberList: Array<string> = [
    "138XXXXXXXX"
];
call.joinConference(1, callNumberList).then(() => {
    console.info(`joinConference success.`);
}).catch((err: BusinessError) => {
    console.error(`joinConference fail, promise: err->${JSON.stringify(err)}`);
});
```

