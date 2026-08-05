# installFont (System API)

## installFont

```TypeScript
function installFont(path: string): Promise<int>
```

Installs a font file from a specified path into the system font library. This API uses a promise to return the result. After successful installation, applications can use the font by its font name.

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.UPDATE_FONT

<!--Device-fontManager-function installFont(path: string): Promise<int>--><!--Device-fontManager-function installFont(path: string): Promise<int>-End-->

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Path to the font file to be installed. Only .ttf and .ttc font files are supported. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：Promise&lt;int&gt; | Promise used to return the installation result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system application. |
| [31100101](../errorcode-font-manager.md#31100101-font-file-not-exist) | Font does not exist. |
| [31100102](../errorcode-font-manager.md#31100102-failed-to-install-font-file) | Font is not supported. |
| [31100103](../errorcode-font-manager.md#31100103-failed-to-copy-font-file) | Font file copy failed. |
| [31100104](../errorcode-font-manager.md#31100104-font-file-already-installed) | Font file installed. |
| [31100105](../errorcode-font-manager.md#31100105-number-of-installed-font-files-reaching-the-maximum) | Exceeded maximum number of installed files. |
| [31100106](../errorcode-font-manager.md#31100106-font-file-installation-failed-due-to-other-errors) | Other error. |

