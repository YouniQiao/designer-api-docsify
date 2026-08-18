# getSelectionContent (System API)

## Modules to Import

```TypeScript
```

## getSelectionContent

```TypeScript
function getSelectionContent(): Promise<string>
```

Obtains the content of the selected text. This API uses a promise to return the result. This API must be called in the [on('selectionCompleted')](arkts-basicservices-selectionmanager-onselectioncompleted-f-sys.md#onselectioncompleted) callback and is valid only after the word selection completion event is triggered.

**Since:** 24

<!--Device-selectionManager-function getSelectionContent(): Promise<string>--><!--Device-selectionManager-function getSelectionContent(): Promise<string>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [33600001](../../apis-basic-services-kit/errorcode-selection.md#33600001-word-selection-service-invocation-error) |
| [33600004](../../apis-basic-services-kit/errorcode-selection.md#33600004-the-api-is-called-too-frequently) |
| [33600005](../../apis-basic-services-kit/errorcode-selection.md#33600005-incorrect-api-call-timing) |
| [33600006](../../apis-basic-services-kit/errorcode-selection.md#33600006-word-selection-prohibited-in-the-current-application) |
| [33600007](../../apis-basic-services-kit/errorcode-selection.md#33600007-selected-text-is-out-of-range) |
| [33600008](../../apis-basic-services-kit/errorcode-selection.md#33600008-content-acquisition-timed-out) |

**Examples**

```TypeScript
import { selectionManager } from '@kit.BasicServicesKit';

// Subscribe to the word selection completion event and obtain the selected text in the callback.
selectionManager.on('selectionCompleted', async (info: selectionManager.SelectionInfo) => {
  try {
    // Obtain the content of the selected text.
    let content = await selectionManager.getSelectionContent();
    console.info(`Succeeded in getting selection content: ${content}`);
  } catch (err) {
    console.error(`Failed to get selection content. Error code: ${err.code}, error message: ${err.message}`);
  }
});
```
