# createPanel

## createPanel

```TypeScript
function createPanel(ctx: Context, info: PanelInfo): Promise<Panel>
```

创建划词面板，用于向用户展示业务相关的操作界面或文本处理结果，使用完毕后需调用[destroyPanel](arkts-basicservices-selectionmanager-destroypanel-f.md#destroyPanel)销毁面板释放资源。使用Promise异步回调。

单个划词应用仅允许创建一个[MENU_PANEL](arkts-basicservices-selectioninput-selectionpanel-paneltype-e.md#PanelType)和一个  
[MAIN_PANEL](arkts-basicservices-selectioninput-selectionpanel-paneltype-e.md#PanelType)。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-selectionManager-function createPanel(ctx: Context, info: PanelInfo): Promise<Panel>--><!--Device-selectionManager-function createPanel(ctx: Context, info: PanelInfo): Promise<Panel>-End-->

**系统能力：** SystemCapability.SelectionInput.Selection

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [ctx](../../apis-arkui/arkts-apis/arkts-arkui-window-configuration-i.md) | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| info | [PanelInfo](arkts-basicservices-selectioninput-selectionpanel-panelinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Panel & gt; |

**错误码：**

| 错误码ID |
| --- |
| [33600001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-selection.md#33600001-划词服务调用异常) |
| [33600003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-selection.md#33600003-调用接口的应用与系统设置中选择的应用不匹配) |

## 示例

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
    // 配置划词面板信息，包括面板类型、位置和尺寸
    let panelInfo: PanelInfo = {
      panelType: PanelType.MENU_PANEL,
      x: 0,
      y: 0,
      width: 500,
      height: 200
    };
    let selectionPanel: selectionManager.Panel | undefined = undefined;
    // 创建划词面板。this.context通过继承SelectionExtensionAbility获取
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
