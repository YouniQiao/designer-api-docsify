# ComposeTitleBarV2

Declaration of the composable title bar. Composable title bar represents a common title bar that contains a title, subtitle (optional), and profile picture (optional). It can come with a Back button for switching between pages of different levels.

**Since:** 26.0.0

<!--Device-unnamed-export declare struct ComposeTitleBarV2--><!--Device-unnamed-export declare struct ComposeTitleBarV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ComposeTitleBarV2 } from 'ComposeTitleBarV2';
import { ComposeTitleBarV2MenuItem } from 'ComposeTitleBarV2MenuItem';
import { ComposeTitleBarV2MenuItemParams } from 'ComposeTitleBarV2MenuItemParams';
```

## item

```TypeScript
@Param
  item?: ComposeTitleBarV2MenuItem
```

A single menu item for the profile picture on the left.

**Type:** [ComposeTitleBarV2MenuItem](arkts-arkui-arkui-advanced-composetitlebarv2-composetitlebarv2menuitem-c.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ComposeTitleBarV2-@Param  item?: ComposeTitleBarV2MenuItem--><!--Device-ComposeTitleBarV2-@Param  item?: ComposeTitleBarV2MenuItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## menuItems

```TypeScript
@Param
  menuItems?: Array<ComposeTitleBarV2MenuItem>
```

Menu items on the right side.

**Type:** Array&lt;[ComposeTitleBarV2MenuItem](arkts-arkui-arkui-advanced-composetitlebarv2-composetitlebarv2menuitem-c.md)&gt;

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ComposeTitleBarV2-@Param  menuItems?: Array<ComposeTitleBarV2MenuItem>--><!--Device-ComposeTitleBarV2-@Param  menuItems?: Array<ComposeTitleBarV2MenuItem>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## subtitle

```TypeScript
@Param
  subtitle?: ResourceStr
```

Sub-title of this title bar.

**Type:** ResourceStr

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ComposeTitleBarV2-@Param  subtitle?: ResourceStr--><!--Device-ComposeTitleBarV2-@Param  subtitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
@Param
  title: ResourceStr
```

Title of this title bar.

**Type:** ResourceStr

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ComposeTitleBarV2-@Param  title: ResourceStr--><!--Device-ComposeTitleBarV2-@Param  title: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

