# Panel

Describes a **Panel** object, which is created using [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md). This method can be used to set, display, hide, and move the panel, as well as subscribe to events. It is applicable to scenarios where a custom operation UI needs to be displayed to users after word selection is complete.

**Since:** 24

**System capability:** SystemCapability.SelectionInput.Selection

## Modules to Import

```TypeScript
import { selectionManager } from 'kits/@kit.BasicServicesKit';
```

## moveTo

```TypeScript
moveTo(x: number, y: number): Promise<void>
```

Moves the word selection panel to the specified coordinates in the global coordinate system of the screen. The panel can be moved to an extended screen. This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md). This API uses a promise to return the result.

**Since:** 20

**Deprecated since:** 24

**Substitutes:** [moveToGlobalDisplay](arkts-basicservices-selectionmanager-panel-i.md#movetoglobaldisplay)

**System capability:** SystemCapability.SelectionInput.Selection

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [33600001](../errorcode-selection.md#33600001-word-selection-service-invocation-error) |
| [33600002](../errorcode-selection.md#33600002-word-selection-panel-has-been-destroyed) |
