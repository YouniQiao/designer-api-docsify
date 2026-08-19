# setDarkMode (System API)

## Modules to Import

```TypeScript
```

## setDarkMode

```TypeScript
function setDarkMode(mode: DarkMode, callback: AsyncCallback<void>): void
```

Set the system dark-mode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-uiAppearance-function setDarkMode(mode: DarkMode, callback: AsyncCallback<void>): void--><!--Device-uiAppearance-function setDarkMode(mode: DarkMode, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.UiAppearance

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [DarkMode](arkts-na-uiappearance-darkmode-e.md) | Yes | indicates the dark-mode to set |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | the callback of setDarkMode |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [500001](../../apis-arkui/errorcode-uiappearance.md#500001-internal-error) | Internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |


## setDarkMode

```TypeScript
function setDarkMode(mode: DarkMode): Promise<void>
```

Set the system dark-mode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-uiAppearance-function setDarkMode(mode: DarkMode): Promise<void>--><!--Device-uiAppearance-function setDarkMode(mode: DarkMode): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.UiAppearance

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [DarkMode](arkts-na-uiappearance-darkmode-e.md) | Yes | indicates the dark-mode to set |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [500001](../../apis-arkui/errorcode-uiappearance.md#500001-internal-error) | Internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

