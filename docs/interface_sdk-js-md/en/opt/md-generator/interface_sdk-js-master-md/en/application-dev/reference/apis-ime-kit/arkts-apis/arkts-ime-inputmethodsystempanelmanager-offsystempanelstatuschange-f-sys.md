# offSystemPanelStatusChange (System API)

## Modules to Import

```TypeScript
import { inputMethodSystemPanelManager } from 'kits/@kit.IMEKit';
```

## offSystemPanelStatusChange

```TypeScript
function offSystemPanelStatusChange(callback?: Callback<SystemPanelStatus>): void
```

Unsubscribe from the system panel status change event.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputMethodSystemPanelManager-function offSystemPanelStatusChange(callback?: Callback<SystemPanelStatus>): void--><!--Device-inputMethodSystemPanelManager-function offSystemPanelStatusChange(callback?: Callback<SystemPanelStatus>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SystemPanelStatus&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
