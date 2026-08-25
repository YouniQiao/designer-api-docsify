# destroyPanel

## Modules to Import

```TypeScript
import { selectionManager } from 'kits/@kit.BasicServicesKit';
```

## destroyPanel

```TypeScript
function destroyPanel(panel: Panel): Promise<void>
```

Destroys the word selection panel. This API is used together with [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md) to destroy the panel object created by **createPanel()**. This API uses a promise to return the result.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| panel | [Panel](arkts-basicservices-selectionmanager-panel-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [33600001](../errorcode-selection.md#33600001-word-selection-service-invocation-error) |
