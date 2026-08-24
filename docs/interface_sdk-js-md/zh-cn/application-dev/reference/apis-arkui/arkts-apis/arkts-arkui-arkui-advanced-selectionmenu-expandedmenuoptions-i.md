# ExpandedMenuOptions

扩展下拉菜单。继承自MenuItemOptions。

**继承/实现关系：** ExpandedMenuOptions extends MenuItemOptions

**起始版本：** 11

<!--Device-unnamed-export interface ExpandedMenuOptions--><!--Device-unnamed-export interface ExpandedMenuOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { EditorEventInfo, EditorMenuOptions, ExpandedMenuOptions, SelectionMenu, SelectionMenuOptions } from '@kit.ArkUI';
```

## action

```TypeScript
action?: () => void
```

点击菜单项的事件回调。同时配置builder和action时，点击图标会同时响应。不设置时点击无响应。

**类型：** () =&gt; void

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ExpandedMenuOptions-action?: () => void--><!--Device-ExpandedMenuOptions-action?: () => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

