# installFont (System API)

## Modules to Import

```TypeScript
import { fontManager } from '@kit.LocalizationKit';
```

## installFont

```TypeScript
function installFont(path: string): Promise<int>
```

Installs a font file from a specified path into the system font library. This API uses a promise to return the result. After successful installation, applications can use the font by its font name.

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.UPDATE_FONT

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| ArkTS-Dyn: Promise & lt;number & gt;<br>ArkTS-Sta：Promise & lt;int & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [31100101](../errorcode-font-manager.md#31100101-font-file-not-exist) |
| [31100102](../errorcode-font-manager.md#31100102-failed-to-install-font-file) |
| [31100103](../errorcode-font-manager.md#31100103-failed-to-copy-font-file) |
| [31100104](../errorcode-font-manager.md#31100104-font-file-already-installed) |
| [31100105](../errorcode-font-manager.md#31100105-number-of-installed-font-files-reaching-the-maximum) |
| [31100106](../errorcode-font-manager.md#31100106-font-file-installation-failed-due-to-other-errors) |

**Examples**

```TypeScript
import { fontManager } from '@kit.LocalizationKit';

async installFont() {
  try {
    let res = await fontManager.installFont('fontPath');
    console.info('installFont suc. res is ' + res);
  } catch (error) {
    console.error('installFont err.' + error.code);
  }
  return;
}
```
