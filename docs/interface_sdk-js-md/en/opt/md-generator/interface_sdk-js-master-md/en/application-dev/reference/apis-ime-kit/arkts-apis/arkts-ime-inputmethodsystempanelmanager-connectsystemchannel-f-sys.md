# connectSystemChannel (System API)

## Modules to Import

```TypeScript
```

## connectSystemChannel

```TypeScript
function connectSystemChannel(): Promise<void>
```

Connect system channel for the panel and input method.

**Since:** 26.0.0

**Required permissions:** ohos.permission.CONNECT_IME_ABILITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputMethodSystemPanelManager-function connectSystemChannel(): Promise<void>--><!--Device-inputMethodSystemPanelManager-function connectSystemChannel(): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12800026](../errorcode-inputmethod-framework.md#12800026-input-method-system-panel-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
