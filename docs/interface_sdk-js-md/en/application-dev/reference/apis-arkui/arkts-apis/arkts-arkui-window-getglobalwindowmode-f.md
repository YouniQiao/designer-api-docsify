# getGlobalWindowMode

## Modules to Import

```TypeScript
import { floatingBall } from '@kit.ArkUI';
import { floatView } from '@kit.ArkUI';
import { window } from '@kit.ArkUI';
```

## getGlobalWindowMode

```TypeScript
function getGlobalWindowMode(displayId?: long): Promise<int>
```

Obtains the window mode of the window that is in the foreground lifecycle on the specified screen. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-window-function getGlobalWindowMode(displayId?: long): Promise<int>--><!--Device-window-function getGlobalWindowMode(displayId?: long): Promise<int>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayId | long | No | Optional display ID, which is used to obtain the window mode information on the corresponding screen. This parameter must be an integer greater than or equal to 0. If it is less than 0, error code 1300016 is returned. If this parameter is not passed or is set to null or undefined, all screens are queried. If a non-integer is passed, the decimal part is ignored. If the specified screen does not exist, the return value is 0. You are advised to call [getWindowProperties()](arkts-arkui-window-window-i.md#getwindowproperties) to obtain the display ID of the window. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the window mode. Each binary bit represents a window mode. For details about the supported window modes, see [GlobalWindowMode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. function getGlobalWindowMode can not work correctly due to limited device capabilities. |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) | This window manager service works abnormally. Possible cause: Internal task error. |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) | Parameter error. Possible cause: 1. Invalid parameter range; 2. The parameter format is incorrect. |

**Examples**

```TypeScript
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let displayId = 0;
  let promise = window.getGlobalWindowMode(displayId);
  promise.then((data) => {
    console.info(`Succeeded in obtaining global window mode. Data: ${data}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to obtain global window mode. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to obtain global window mode. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

