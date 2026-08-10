# isRinging（系统接口）

## 导入模块

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## isRinging

```TypeScript
function isRinging(callback: AsyncCallback<boolean>): void
```

Judge whether there is a ringing call.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function isRinging(callback: AsyncCallback<boolean>): void--><!--Device-call-function isRinging(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 | The callback of isRinging. Returns {@code true} if the device is ringing; returns {@code false} otherwise. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 201 | Permission denied. |
| 8300999 | Unknown error code. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

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

Judge whether there is a ringing call.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function isRinging(): Promise<boolean>--><!--Device-call-function isRinging(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Returns { |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 8300999 | Unknown error code. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.isRinging().then((data: boolean) => {
    console.info(`isRinging success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`isRinging fail, promise: err->${JSON.stringify(err)}`);
});
```

