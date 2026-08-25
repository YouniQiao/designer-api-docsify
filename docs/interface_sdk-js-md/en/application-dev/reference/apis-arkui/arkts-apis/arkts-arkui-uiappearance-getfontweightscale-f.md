# getFontWeightScale

## Modules to Import

```TypeScript
import { uiAppearance } from 'kits/@kit.ArkUI';
```

## getFontWeightScale

```TypeScript
function getFontWeightScale(): number
```

Obtains the current font weight scale factor.<!--Del-->

> **NOTE：**

> This API is a system API in API version 19 and earlier. Using this API requires the
> [ohos.permission.UPDATE_CONFIGURATION](../../../security/AccessToken/permissions-for-system-apps.md#ohospermissionupdate_configuration)
> permission.
<!--DelEnd-->

**Since:** 20

**Required permissions:** 
- API version 12 - 19: ohos.permission.UPDATE_CONFIGURATION

**System capability:** SystemCapability.ArkUI.UiAppearance

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [500001](../errorcode-uiappearance.md#500001-internal-error) |
