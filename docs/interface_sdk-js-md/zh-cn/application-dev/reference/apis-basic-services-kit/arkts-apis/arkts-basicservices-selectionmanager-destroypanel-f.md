# destroyPanel

## 导入模块

```TypeScript
import { selectionManager } from 'kits/@kit.BasicServicesKit';
```

## destroyPanel

```TypeScript
function destroyPanel(panel: Panel): Promise<void>
```

销毁划词面板。与[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md)搭配使用，用于销毁由createPanel()创建的面板对象。使用Promise异步回调。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.SelectionInput.Selection

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| panel | [Panel](arkts-basicservices-selectionmanager-panel-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [33600001](../errorcode-selection.md#33600001-划词服务调用异常) |
