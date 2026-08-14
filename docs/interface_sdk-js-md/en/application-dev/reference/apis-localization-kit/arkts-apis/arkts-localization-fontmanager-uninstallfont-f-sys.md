# uninstallFont (System API)

## Modules to Import

```TypeScript
import { fontManager } from 'fontManager';
```

## uninstallFont

```TypeScript
function uninstallFont(fullName: string): Promise<int>
```

Uninstalls an installed font file from the system font library by font name. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.UPDATE_FONT

<!--Device-fontManager-function uninstallFont(fullName: string): Promise<int>--><!--Device-fontManager-function uninstallFont(fullName: string): Promise<int>-End-->

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fullName | string | Yes | Name of the font to be uninstalled. You can open the .ttf or .ttc font file to obtain the name. <br>The font name is case-sensitive. Ensure that it exactly matches the actual font name. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the uninstallation result. <br>- The value **0** indicates that the uninstallation is successful and the font has been removed from the system font library. <br>- Any other value indicates that the uninstallation failed. Troubleshoot based on the error code. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [31100107](../errorcode-font-manager.md#31100107-uninstalled-font-file-not-exist) | The font file does not exist. |
| [31100108](../errorcode-font-manager.md#31100108-failed-to-delete-font-file) | Failed to delete the font file. |
| [31100109](../errorcode-font-manager.md#31100109-uninstallation-failed-due-to-other-errors) | The system ability works abnormally. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

