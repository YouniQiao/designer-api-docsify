# getSelectionContent

## Modules to Import

```TypeScript
import { selectionManager } from 'kits/@kit.BasicServicesKit';
```

## getSelectionContent

```TypeScript
function getSelectionContent(): Promise<string>
```

Obtains the content of the selected text. This API uses a promise to return the result. This API must be called in the on('selectionCompleted') callback and is valid only after the word selection completion event is triggered.

**Since:** 24

**System capability:** SystemCapability.SelectionInput.Selection

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [33600001](../errorcode-selection.md#33600001-word-selection-service-invocation-error) |
| [33600004](../errorcode-selection.md#33600004-the-api-is-called-too-frequently) |
| [33600005](../errorcode-selection.md#33600005-incorrect-api-call-timing) |
| [33600006](../errorcode-selection.md#33600006-word-selection-prohibited-in-the-current-application) |
| [33600007](../errorcode-selection.md#33600007-selected-text-is-out-of-range) |
| [33600008](../errorcode-selection.md#33600008-content-acquisition-timed-out) |
