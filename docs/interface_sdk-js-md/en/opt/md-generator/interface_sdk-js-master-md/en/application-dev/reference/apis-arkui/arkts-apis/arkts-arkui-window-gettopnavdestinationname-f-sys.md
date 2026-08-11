# getTopNavDestinationName (System API)

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## getTopNavDestinationName

```TypeScript
function getTopNavDestinationName(windowId: number): Promise<string>
```

Obtains the name of [NavDestination](NavDestination) in the current top-level  
[Navigation](Navigation) component of the specified foreground window. This API uses a promise to return the result.

**Since:** 20

<!--Device-window-function getTopNavDestinationName(windowId: int): Promise<string>--><!--Device-window-function getTopNavDestinationName(windowId: int): Promise<string>-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let windowId = 10;
  let promise = window.getTopNavDestinationName(windowId);
  promise.then((data) => {
    console.info(`Succeeded, data: ${data}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed, cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed, exception code: ${exception.code}, message: ${exception.message}`);
}
```
