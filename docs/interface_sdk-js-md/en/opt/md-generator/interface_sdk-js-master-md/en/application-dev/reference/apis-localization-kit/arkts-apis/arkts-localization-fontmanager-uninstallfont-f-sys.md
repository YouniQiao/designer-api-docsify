# uninstallFont (System API)

## Modules to Import

```TypeScript
import { fontManager } from '@kit.LocalizationKit';
```

## uninstallFont

```TypeScript
function uninstallFont(fullName: string): Promise<number>
```

Uninstalls an installed font file from the system font library by font name. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.UPDATE_FONT

<!--Device-fontManager-function uninstallFont(fullName: string): Promise<int>--><!--Device-fontManager-function uninstallFont(fullName: string): Promise<int>-End-->

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fullName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [31100107](../errorcode-font-manager.md#31100107-uninstalled-font-file-not-exist) |
| [31100108](../errorcode-font-manager.md#31100108-failed-to-delete-font-file) |
| [31100109](../errorcode-font-manager.md#31100109-uninstallation-failed-due-to-other-errors) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
