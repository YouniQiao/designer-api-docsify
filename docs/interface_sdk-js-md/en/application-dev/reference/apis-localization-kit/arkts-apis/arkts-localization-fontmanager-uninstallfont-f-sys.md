# uninstallFont (System API)

## Modules to Import

```TypeScript
import { fontManager } from 'kits/@kit.LocalizationKit';
```

## uninstallFont

```TypeScript
function uninstallFont(fullName: string): Promise<int>
```

Uninstalls an installed font file from the system font library by font name. This API uses a promise to return the result.

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.UPDATE_FONT

<!--Device-fontManager-function uninstallFont(fullName: string): Promise<int>--><!--Device-fontManager-function uninstallFont(fullName: string): Promise<int>-End-->

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fullName | string | Yes | Name of the font to be uninstalled. You can open the .ttf or .ttc font file to obtain the name. &lt;br&gt;The font name is case-sensitive. Ensure that it exactly matches the actual font name. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise used to return the uninstallation result. &lt;br&gt;- The value **0** indicates that the uninstallation is successful and the font has been removed from the system font library. &lt;br&gt;- Any other value indicates that the uninstallation failed. Troubleshoot based on the error code. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [31100107](../errorcode-font-manager.md#31100107-uninstalled-font-file-not-exist) | Font file does not exist. |
| [31100108](../errorcode-font-manager.md#31100108-failed-to-delete-font-file) | Font file delete error. |
| [31100109](../errorcode-font-manager.md#31100109-uninstallation-failed-due-to-other-errors) | Other error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system application. |

