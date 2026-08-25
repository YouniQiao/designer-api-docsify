# setFontWeightScale (System API)

## Modules to Import

```TypeScript
import { uiAppearance } from 'kits/@kit.ArkUI';
```

## setFontWeightScale

```TypeScript
function setFontWeightScale(fontWeightScale: number): Promise<void>
```

Sets the system font weight scale.  
**Permission required**: ohos.permission.UPDATE_CONFIGURATION

**Since:** 12

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [500001](../errorcode-uiappearance.md#500001-internal-error) |
