# setMultiScreenRelativePosition (System API)

## Modules to Import

```TypeScript
import { screen } from '@kit.ArkUI';
```

## setMultiScreenRelativePosition

```TypeScript
function setMultiScreenRelativePosition(mainScreenOptions: MultiScreenPositionOptions,
    secondaryScreenOptions: MultiScreenPositionOptions): Promise<void>
```

Sets the positions of the primary and secondary screens in extend mode. This API uses a promise to return the result.

**Since:** 13

<!--Device-screen-function setMultiScreenRelativePosition(mainScreenOptions: MultiScreenPositionOptions,    secondaryScreenOptions: MultiScreenPositionOptions): Promise<void>--><!--Device-screen-function setMultiScreenRelativePosition(mainScreenOptions: MultiScreenPositionOptions,    secondaryScreenOptions: MultiScreenPositionOptions): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mainScreenOptions | [MultiScreenPositionOptions](arkts-arkui-screen-multiscreenpositionoptions-i-sys.md) | Yes |
| secondaryScreenOptions | [MultiScreenPositionOptions](arkts-arkui-screen-multiscreenpositionoptions-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [1400001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-display.md#1400001-invalid-display-or-screen) |
| [1400003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-display.md#1400003-abnormal-display-manager-service) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the screen ID using getAllScreens().
let mainScreenOptions: screen.MultiScreenPositionOptions = {
  id: 0, // Main screen ID.
  startX : 0,
  startY : 0
}; // Position of the main screen.

let secondaryScreenOptions: screen.MultiScreenPositionOptions = {
  id : 12,  // Secondary screen ID.
  startX : 1000,
  startY : 1000
}; // Position of the secondary screen.

// Set the positions of the main and secondary screens.
screen.setMultiScreenRelativePosition(mainScreenOptions, secondaryScreenOptions).then(() => {
  console.info('Succeeded in setting multi screen relative position.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set multi screen relative position. Code: ${err.code}, message: ${err.message}`);
});
```
