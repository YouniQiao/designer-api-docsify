# setAutoTimeStatus (System API)

## Modules to Import

```TypeScript
import { systemDateTime } from 'kits/@kit.BasicServicesKit';
```

## setAutoTimeStatus

```TypeScript
function setAutoTimeStatus(status: boolean): Promise<void>
```

设置自动设置时间开关状态，使用Promise异步回调。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_TIME

<!--Device-systemDateTime-function setAutoTimeStatus(status: boolean): Promise<void>--><!--Device-systemDateTime-function setAutoTimeStatus(status: boolean): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.Time

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| status | boolean | Yes | 设置自动设置时间开关状态。&lt;br/&gt;- true：表示打开自动设置时间开关。 &lt;br/&gt;- false：表示关闭自动设置时间开关。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13000001 | Network connection error or OS error. Possible causes: 1. System memory is insufficient; 2. Calls the underlying system interface failed. |
| 201 | Permission denied |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 204 | Access denied due to user access control policy. Possible causes: 1. The operation is restricted by the OS-account constraint. 2. The required privilege for the operation has not been granted.<br>**Applicable version:** 24 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.setAutoTimeStatus(true).then(() => {
    console.info(`Succeeded in setting autotime.`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to set autotime. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to set autotime. message: ${error.message}, code: ${error.code}`);
}
```

