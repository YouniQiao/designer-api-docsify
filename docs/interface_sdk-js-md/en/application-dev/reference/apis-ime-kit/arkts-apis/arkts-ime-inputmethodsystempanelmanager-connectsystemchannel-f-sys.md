# connectSystemChannel (System API)

## Modules to Import

```TypeScript
import { inputMethodSystemPanelManager } from '@kit.IMEKit';
```

## connectSystemChannel

```TypeScript
function connectSystemChannel(): Promise<void>
```

Connects to the system channel for communication between the input method system panel and the system-default input method application. This API can be called only by the input method system panel.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.CONNECT_IME_ABILITY

**Model restriction:** This API can be used only in the stage model.

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
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| [12800026](../errorcode-inputmethod-framework.md#12800026-input-method-system-panel-error) |
