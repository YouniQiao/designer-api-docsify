# createPanel

## 导入模块

```TypeScript
import { selectionManager } from 'kits/@kit.BasicServicesKit';
```

## createPanel

```TypeScript
function createPanel(ctx: Context, info: PanelInfo): Promise<Panel>
```

创建划词面板，用于向用户展示业务相关的操作界面或文本处理结果，使用完毕后需调用[destroyPanel](arkts-basicservices-selectionmanager-destroypanel-f.md)销毁面板释放资源。使用Promise异步回调。单个划词应用仅允许创建一个[MENU_PANEL](arkts-basicservices-selectioninput-selectionpanel-paneltype-e.md)和一个 [MAIN_PANEL](arkts-basicservices-selectioninput-selectionpanel-paneltype-e.md)。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [33600001](../errorcode-selection.md#33600001-划词服务调用异常) |
| [33600003](../errorcode-selection.md#33600003-调用接口的应用与系统设置中选择的应用不匹配) |
