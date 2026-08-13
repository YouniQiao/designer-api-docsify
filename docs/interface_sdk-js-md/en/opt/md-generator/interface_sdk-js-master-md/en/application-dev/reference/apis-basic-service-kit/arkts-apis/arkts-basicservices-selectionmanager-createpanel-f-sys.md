# createPanel (System API)

## Modules to Import

```TypeScript
import { selectionManager } from '@kit.BasicServicesKit';
```

## createPanel

```TypeScript
function createPanel(ctx: Context, info: PanelInfo): Promise<Panel>
```

Creates a word selection panel, which is used to display the service-related operation UI or text processing result. After the panel is used, call [destroyPanel](arkts-basicservices-selectionmanager-destroypanel-f-sys.md#destroyPanel-(System-API)) to destroy the panel and release resources. This API uses a promise to return the result. Only one [MENU_PANEL](arkts-basicservices-selectioninput-selectionpanel-paneltype-e-sys.md#PanelType-(System-API)) and one [MAIN_PANEL](arkts-basicservices-selectioninput-selectionpanel-paneltype-e-sys.md#PanelType-(System-API)) can be created for one word selection application.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-selectionManager-function createPanel(ctx: Context, info: PanelInfo): Promise<Panel>--><!--Device-selectionManager-function createPanel(ctx: Context, info: PanelInfo): Promise<Panel>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [ctx](../../apis-arkui/arkts-apis/arkts-arkui-window-configuration-i.md) | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| info | [PanelInfo](arkts-basicservices-selectioninput-selectionpanel-panelinfo-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Panel & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [33600001](../../apis-basic-services-kit/errorcode-selection.md#33600001-word-selection-service-invocation-error) |
| [33600003](../../apis-basic-services-kit/errorcode-selection.md#33600003-api-caller-and-word-selection-application-mismatched) |

## Examples

```TypeScript
import { selectionManager, SelectionExtensionAbility, PanelInfo, PanelType, BusinessError } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';
import { Want } from '@kit.AbilityKit';

class SelectionAbilityStub extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(
    code: number,
    data: rpc.MessageSequence,
    reply: rpc.MessageSequence,
    options: rpc.MessageOption
  ): boolean | Promise<boolean> {
    return true;
  }
}

class ServiceExtAbility extends SelectionExtensionAbility {
  onConnect(want: Want): rpc.RemoteObject {
    // Configure the word selection panel, including the panel type, position, and size.
    let panelInfo: PanelInfo = {
      panelType: PanelType.MENU_PANEL,
      x: 0,
      y: 0,
      width: 500,
      height: 200
    };
    let selectionPanel: selectionManager.Panel | undefined = undefined;
    // Create a word selection panel. Obtain this.context by inheriting SelectionExtensionAbility.
    selectionManager.createPanel(this.context, panelInfo)
      .then((panel: selectionManager.Panel) => {
        selectionPanel = panel;
        console.info('Succeed in creating panel.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to create panel. Error code: ${err.code}, error message: ${err.message}`);
    });
    return new SelectionAbilityStub('remote');
  }
}
export default ServiceExtAbility;
```
