# muteRinger（系统接口）

## muteRinger

```TypeScript
function muteRinger(callback: AsyncCallback<void>): void
```

如果来电铃声响起，设备将停止铃声。否则，此方法不起作用。使用callback异步回调。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function muteRinger(callback: AsyncCallback<void>): void--><!--Device-call-function muteRinger(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 以回调函数的方式返回停止铃声的结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [8300999](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) | Unknown error code. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Non-system applications use system APIs. |
| [8300002](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) | Operation failed. Cannot connect to service. |
| [8300003](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) | System internal error. |
| [8300001](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) | Invalid parameter value. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.muteRinger((err: BusinessError) => {
    if (err) {
        console.error(`muteRinger fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`muteRinger success.`);
    }
});
```


## muteRinger

```TypeScript
function muteRinger(): Promise<void>
```

如果来电铃声响起，设备将停止铃声。否则，此方法不起作用。使用Promise异步回调。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function muteRinger(): Promise<void>--><!--Device-call-function muteRinger(): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 以Promise形式异步返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [8300999](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) | Unknown error code. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Non-system applications use system APIs. |
| [8300002](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) | Operation failed. Cannot connect to service. |
| [8300003](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) | System internal error. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.muteRinger().then(() => {
    console.info(`muteRinger success.`);
}).catch((err: BusinessError) => {
    console.error(`muteRinger fail, promise: err->${JSON.stringify(err)}`);
});
```

