# setFontScale (System API)

## Modules to Import

```TypeScript
import { uiAppearance } from 'kits/@kit.ArkUI';
```

## setFontScale

```TypeScript
function setFontScale(fontScale: double): Promise<void>
```

设置系统字体大小。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-uiAppearance-function setFontScale(fontScale: double): Promise<void>--><!--Device-uiAppearance-function setFontScale(fontScale: double): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.UiAppearance

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fontScale | double | Yes | indicates the font-scale to set |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 500001 | Internal error. |
| 201 | Permission denied. |
| 202 | Permission verification failed. A non-system application calls a system API. |

