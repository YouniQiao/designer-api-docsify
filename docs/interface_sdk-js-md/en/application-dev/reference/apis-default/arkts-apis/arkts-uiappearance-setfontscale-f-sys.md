# setFontScale (System API)

## Modules to Import

```TypeScript
```

## setFontScale

```TypeScript
function setFontScale(fontScale: double): Promise<void>
```

Set the system font-scale.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

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
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [500001](../../apis-arkui/errorcode-uiappearance.md#500001-internal-error) | Internal error. |

