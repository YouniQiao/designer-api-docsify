# setFontScale (System API)

## Modules to Import

```TypeScript
import { uiAppearance } from '@kit.ArkUI';
```

## setFontScale

```TypeScript
function setFontScale(fontScale: number): Promise<void>
```

Sets the system font scale. **Permission required**: ohos.permission.UPDATE_CONFIGURATION

**Since:** 12

**Deprecated since:** -1

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-uiAppearance-function setFontScale(fontScale: number): Promise<void>--><!--Device-uiAppearance-function setFontScale(fontScale: number): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.UiAppearance

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fontScale | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [500001](../errorcode-uiappearance.md#500001-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { uiAppearance } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let fontScale = 1.5;

try {
  uiAppearance.setFontScale(fontScale).then(() => {
    console.info('Set fontScale successfully.');
  }).catch((error: BusinessError) => {
    console.error(`Set fontScale failed. Code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  let err = error as BusinessError;
  console.error(`Set fontScale failed. Code: ${err.code}, message: ${err.message}`);
}
```
