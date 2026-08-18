# @ohos.arkui.advanced.ComposeTitleBar

## Modules to Import

```TypeScript
import { ComposeTitleBar, ComposeTitleBarMenuItem } from '@kit.ArkUI';
import { ComposeTitleBarV2, ComposeTitleBarV2MenuItem, ComposeTitleBarV2MenuItemParams } from '@kit.ArkUI';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [ComposeTitleBarMenuItem](arkts-arkui-arkui-advanced-composetitlebar-composetitlebarmenuitem-c.md) | Declaration of the menu item on the right side. |

### Structs

| Name | Description |
| --- | --- |
| [ComposeTitleBar](arkts-arkui-arkui-advanced-composetitlebar-composetitlebar-s.md) | **ComposeTitleBar** represents a common title bar that contains a title, subtitle (optional), and profile picture ( optional). It can come with a Back button for switching between pages of different levels. > **NOTE：**> > - This component can be used only in the stage model. > > - If the **ComposeTitleBar** component has universal attributes and > universal events configured, the compiler toolchain automatically > generates an additional **__Common__** node and mounts the universal attributes and universal events on this node > rather than the **ComposeTitleBar** component itself. As a result, the configured universal attributes and > universal events may fail to take effect or behave as intended. For this reason, avoid using universal attributes > and events with the **ComposeTitleBar** component. |

