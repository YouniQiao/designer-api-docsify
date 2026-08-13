# offSystemPrivateCommand (System API)

## Modules to Import

```TypeScript
import { inputMethodSystemPanelManager } from '@kit.IMEKit';
```

## offSystemPrivateCommand

```TypeScript
function offSystemPrivateCommand(callback?: Callback<Record<string, CommandDataType>>): void
```

Unsubscribe from the event when the input method application sends private data commands.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputMethodSystemPanelManager-function offSystemPrivateCommand(callback?: Callback<Record<string, CommandDataType>>): void--><!--Device-inputMethodSystemPanelManager-function offSystemPrivateCommand(callback?: Callback<Record<string, CommandDataType>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, CommandDataType&gt;&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
