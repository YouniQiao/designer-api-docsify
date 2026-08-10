# setMuted（系统接口）

## 导入模块

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## setMuted

```TypeScript
function setMuted(callback: AsyncCallback<void>): void
```

Set mute during a call.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-call-function setMuted(callback: AsyncCallback<void>): void--><!--Device-call-function setMuted(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | The callback of setMuted. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300999 | Unknown error code. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.setMuted((err: BusinessError) => {
    if (err) {
        console.error(`setMuted fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`setMuted success.`);
    }
});
```


## setMuted

```TypeScript
function setMuted(): Promise<void>
```

Set mute during a call.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-call-function setMuted(): Promise<void>--><!--Device-call-function setMuted(): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the setMuted. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 8300999 | Unknown error code. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.setMuted().then(() => {
    console.info(`setMuted success.`);
}).catch((err: BusinessError) => {
    console.error(`setMuted fail, promise: err->${JSON.stringify(err)}`);
});
```

