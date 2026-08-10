# setPreviewSurface（系统接口）

## 导入模块

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## setPreviewSurface

```TypeScript
function setPreviewSurface(callId: int, surfaceId: string): Promise<void>
```

Set preview surface when video call.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function setPreviewSurface(callId: int, surfaceId: string): Promise<void>--><!--Device-call-function setPreviewSurface(callId: int, surfaceId: string): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the identifier of the call. |
| surfaceId | string | 是 | Indicates the identifier of the preview surface id. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the setPreviewWindow. |

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

call.setPreviewSurface(1, "surfaceId1").then(() => {
    console.info(`setPreviewSurface success.`);
}).catch((err: BusinessError) => {
    console.error(`setPreviewSurface fail, promise: err->${JSON.stringify(err)}`);
});
```

