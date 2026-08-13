# setFontWeightScale (System API)

## Modules to Import

```TypeScript
import { uiAppearance } from '@kit.ArkUI';
```

## setFontWeightScale

```TypeScript
function setFontWeightScale(fontWeightScale: number): Promise<void>
```

Sets the system font weight scale. **Permission required**: ohos.permission.UPDATE_CONFIGURATION

**Since:** 12

**Deprecated since:** -1

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-uiAppearance-function setFontWeightScale(fontWeightScale: number): Promise<void>--><!--Device-uiAppearance-function setFontWeightScale(fontWeightScale: number): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.UiAppearance

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [fontWeightScale](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-configuration-configuration-i.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [500001](../errorcode-uiappearance.md#500001-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { uiAppearance } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let fontWeightScale = 1;

try {
  uiAppearance.setFontWeightScale(fontWeightScale).then(() => {
    console.info('Set fontWeightScale successfully.');
  }).catch((error: BusinessError) => {
    console.error(`Set fontWeightScale failed. Code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  let err = error as BusinessError;
  console.error(`Set fontWeightScale failed. Code: ${err.code}, message: ${err.message}`);
}
```
