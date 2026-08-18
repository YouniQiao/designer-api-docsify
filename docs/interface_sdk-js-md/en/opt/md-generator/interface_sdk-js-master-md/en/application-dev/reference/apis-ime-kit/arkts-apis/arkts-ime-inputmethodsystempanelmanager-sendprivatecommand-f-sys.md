# sendPrivateCommand (System API)

## Modules to Import

```TypeScript
```

## sendPrivateCommand

```TypeScript
function sendPrivateCommand(commandData: Record<string, CommandDataType>): Promise<void>
```

Send private command.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputMethodSystemPanelManager-function sendPrivateCommand(commandData: Record<string, CommandDataType>): Promise<void>--><!--Device-inputMethodSystemPanelManager-function sendPrivateCommand(commandData: Record<string, CommandDataType>): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| commandData | [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, CommandDataType&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800026](../errorcode-inputmethod-framework.md#12800026-input-method-system-panel-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
