# createPanel

## Modules to Import

```TypeScript
import { selectionManager } from 'kits/@kit.BasicServicesKit';
```

## createPanel

```TypeScript
function createPanel(ctx: Context, info: PanelInfo): Promise<Panel>
```

Creates a word selection panel, which is used to display the service-related operation UI or text processing result. After the panel is used, call [destroyPanel](arkts-basicservices-selectionmanager-destroypanel-f.md) to destroy the panel and release resources. This API uses a promise to return the result.Only one [MENU_PANEL](arkts-basicservices-selectioninput-selectionpanel-paneltype-e.md) and one [MAIN_PANEL](arkts-basicservices-selectioninput-selectionpanel-paneltype-e.md) can be created for one word selection application.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [ctx](../../apis-arkui/arkts-apis/arkts-arkui-window-configuration-i.md) | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| info | [PanelInfo](arkts-basicservices-selectioninput-selectionpanel-panelinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Panel & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [33600001](../errorcode-selection.md#33600001-word-selection-service-invocation-error) |
| [33600003](../errorcode-selection.md#33600003-api-caller-and-word-selection-application-mismatched) |
