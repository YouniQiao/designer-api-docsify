# destroyVirtualScreen (System API)

## Modules to Import

```TypeScript
import { screen } from '@kit.ArkUI';
import { screenshot } from '@kit.ArkUI';
```

## destroyVirtualScreen

```TypeScript
function destroyVirtualScreen(screenId:long, callback: AsyncCallback<void>): void
```

Destroys a virtual screen. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-screen-function destroyVirtualScreen(screenId:long, callback: AsyncCallback<void>): void--><!--Device-screen-function destroyVirtualScreen(screenId:long, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| screenId | long | Yes | ID of the virtual screen. The value must be an integer. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the virtual screen is destroyed, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) | Invalid display or screen. |
| [1400002](../errorcode-display.md#1400002-unauthorized-operation) | Unauthorized operation. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let screenId: number = 1;
screen.destroyVirtualScreen(screenId, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to destroy the virtual screen. Code:${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in destroying the virtual screen.');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let screenId: number = 1;
screen.destroyVirtualScreen(screenId).then(() => {
  console.info('Succeeded in destroying the virtual screen.');
}).catch((err: BusinessError) => {
  console.error(`Failed to destroy the virtual screen.Code:${err.code}, message is ${err.message}`);
});
```


## destroyVirtualScreen

```TypeScript
function destroyVirtualScreen(screenId:long): Promise<void>
```

Destroys a virtual screen. This API uses a promise to return the result.

**Since:** 23

<!--Device-screen-function destroyVirtualScreen(screenId:long): Promise<void>--><!--Device-screen-function destroyVirtualScreen(screenId:long): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| screenId | long | Yes | ID of the virtual screen. The value must be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) | Invalid display or screen. |
| [1400002](../errorcode-display.md#1400002-unauthorized-operation) | Unauthorized operation. |

**Examples**

See [destroyVirtualScreen](#destroyvirtualscreen)

