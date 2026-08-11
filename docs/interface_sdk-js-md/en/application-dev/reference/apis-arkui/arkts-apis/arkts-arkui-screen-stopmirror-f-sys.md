# stopMirror (System API)

## Modules to Import

```TypeScript
import { screen } from 'kits/@kit.ArkUI';
```

## stopMirror

```TypeScript
function stopMirror(mirrorScreen:Array<long>, callback: AsyncCallback<void>): void
```

Stops mirror mode. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-screen-function stopMirror(mirrorScreen:Array<long>, callback: AsyncCallback<void>): void--><!--Device-screen-function stopMirror(mirrorScreen:Array<long>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mirrorScreen | ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;long&gt; | Yes | Array of IDs of secondary screens. Each ID must be an integer. The size of the **mirrorScreen** array cannot exceed 1000. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If mirror mode is stopped, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. 3. Parameter verification failed. |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) | Invalid display or screen. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let mirrorScreenIds: Array<number> = [1, 2, 3];
screen.stopMirror(mirrorScreenIds, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to stop mirror screens. Code:${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in stopping mirror screens.');
});
```


## stopMirror

```TypeScript
function stopMirror(mirrorScreen:Array<long>): Promise<void>
```

Stops mirror mode. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-screen-function stopMirror(mirrorScreen:Array<long>): Promise<void>--><!--Device-screen-function stopMirror(mirrorScreen:Array<long>): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mirrorScreen | ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;long&gt; | Yes | Array of IDs of secondary screens. Each ID must be an integer. The size of the **mirrorScreen** array cannot exceed 1000. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) | Invalid display or screen. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let mirrorScreenIds: Array<number> = [1, 2, 3];
screen.stopMirror(mirrorScreenIds).then(() => {
  console.info('Succeeded in stopping mirror screens.');
}).catch((err: BusinessError) => {
  console.error(`Failed to stop mirror screens.Code:${err.code}, message is ${err.message}`);
});
```

