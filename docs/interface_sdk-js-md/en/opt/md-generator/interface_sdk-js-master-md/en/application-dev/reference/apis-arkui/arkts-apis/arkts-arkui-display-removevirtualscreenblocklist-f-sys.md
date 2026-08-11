# removeVirtualScreenBlocklist (System API)

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## removeVirtualScreenBlocklist

```TypeScript
function removeVirtualScreenBlocklist(windowIds: Array<number>): Promise<void>
```

Removes windows from the list of windows that are not allowed to be displayed during casting. This API takes effect only for the main window of an application or system windows. This API uses a promise to return the result.

**Since:** 18

<!--Device-display-function removeVirtualScreenBlocklist(windowIds: Array<int>): Promise<void>--><!--Device-display-function removeVirtualScreenBlocklist(windowIds: Array<int>): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowIds | Array&lt;number&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { display, window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage) {
    // ...
    let windowId = windowStage.getMainWindowSync().getWindowProperties().id; // Obtain the window IDs.
    let windowIds = [windowId];

    // Add windows to the list of windows that are not allowed to be displayed during casting.
    let promise = display.addVirtualScreenBlocklist(windowIds);
    promise.then(() => {
      console.info('Succeeded in adding virtual screen blocklist.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to add virtual screen blocklist. Code: ${err.code}, message: ${err.message}`);
    });

    // Remove windows from the list of windows that are not allowed to be displayed during casting.
    promise = display.removeVirtualScreenBlocklist(windowIds);
    promise.then(() => {
      console.info('Succeeded in removing virtual screen blocklist.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to remove virtual screen blocklist. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```
