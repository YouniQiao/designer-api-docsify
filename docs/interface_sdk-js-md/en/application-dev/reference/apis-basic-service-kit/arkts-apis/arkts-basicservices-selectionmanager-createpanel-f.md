# createPanel

## Modules to Import

```TypeScript
import { selectionManager } from 'kits/@kit.BasicServicesKit';
```

## createPanel

```TypeScript
function createPanel(ctx: Context, info: PanelInfo): Promise<Panel>
```

创建划词面板，用于向用户展示业务相关的操作界面或文本处理结果，使用完毕后需调用[destroyPanel](arkts-basicservices-selectionmanager-destroypanel-f.md#destroypanel)销毁面板释放资源。使用Promise异步回调。

单个划词应用仅允许创建一个[MENU_PANEL](arkts-basicservices-selectioninput-selectionpanel-paneltype-e.md)和一个  
[MAIN_PANEL](arkts-basicservices-selectioninput-selectionpanel-paneltype-e.md)。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-selectionManager-function createPanel(ctx: Context, info: PanelInfo): Promise<Panel>--><!--Device-selectionManager-function createPanel(ctx: Context, info: PanelInfo): Promise<Panel>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ctx | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes | 当前划词面板依赖的上下文信息，需使用SelectionExtensionAbility提供的上下文。 |
| info | [PanelInfo](arkts-basicservices-selectioninput-selectionpanel-panelinfo-i.md) | Yes | 划词面板的配置信息，用于指定面板类型、位置和宽高。单个划词应用仅允许创建一个MENU_PANEL和一个MAIN_PANEL。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Panel&gt; | Promise对象，返回当前创建的划词面板对象，可用于面板内容设置、显示、隐藏、移动及事件订阅等管理操作。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 33600001 | Selection service exception. |
| 33600003 | The application calling the API does not match the application selected in the system settings. |

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

