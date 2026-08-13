# Display

Implements a Display instance, with attributes and APIs defined. Before calling any API in Display, you must use [getAllDisplays()](arkts-arkui-display-getalldisplays-f.md#getAllDisplays) or [getDefaultDisplaySync()](arkts-arkui-display-getdefaultdisplaysync-f.md#getDefaultDisplaySync) to obtain a Display instance.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-display-interface Display--><!--Device-display-interface Display-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## hasImmersiveWindow

```TypeScript
hasImmersiveWindow(callback: AsyncCallback<boolean>): void
```

Checks whether this display contains an immersive window. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-Display-hasImmersiveWindow(callback: AsyncCallback<boolean>): void--><!--Device-Display-hasImmersiveWindow(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. **true** if the display contains an immersive window, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) | Invalid display or screen. |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

let displayClass: display.Display | null = null;
displayClass = display.getDefaultDisplaySync();
displayClass.hasImmersiveWindow((err: BusinessError, data) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error(`Failed to check whether there is immersive window. Code: ${err.code} , message : ${err.message}`);
      return;
    }
    console.info(`Succeeded in checking whether there is immersive window. data: ${data}`);
});
```

## hasImmersiveWindow

```TypeScript
hasImmersiveWindow(): Promise<boolean>
```

Checks whether this display contains an immersive window. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-Display-hasImmersiveWindow(): Promise<boolean>--><!--Device-Display-hasImmersiveWindow(): Promise<boolean>-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. **true** if the display contains an immersive window, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) | Invalid display or screen. |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

let displayClass: display.Display | null = null;
displayClass = display.getDefaultDisplaySync();
let promise = displayClass.hasImmersiveWindow();
promise.then((data) => {
  console.info(`Succeeded in checking whether there is immersive window. data: ${data}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to check whether there is immersive window. Code: ${err.code} , message: ${err.message}`);
})
```

