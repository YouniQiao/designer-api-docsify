# ComposeTitleBar

*ComposeTitleBar** represents a common title bar that contains a title, subtitle (optional), and profile picture ( optional). It can come with a Back button for switching between pages of different levels.

> **NOTE：**
> 
> - This component can be used only in the stage model.
> 
> - If the **ComposeTitleBar** component has universal attributes and &gt; universal events configured, the compiler toolchain automatically &gt; generates an additional **__Common__** node and mounts the universal attributes and universal events on this node &gt; rather than the **ComposeTitleBar** component itself. As a result, the configured universal attributes and &gt; universal events may fail to take effect or behave as intended. For this reason, avoid using universal attributes &gt; and events with the **ComposeTitleBar** component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare struct ComposeTitleBar--><!--Device-unnamed-export declare struct ComposeTitleBar-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## build

```TypeScript
@Builder
  build(): void
```

The method to build component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComposeTitleBar-@Builder  build(): void--><!--Device-ComposeTitleBar-@Builder  build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## item

```TypeScript
item?: ComposeTitleBarMenuItem
```

A single menu item for the profile picture on the left.

**Type:** [ComposeTitleBarMenuItem](arkts-arkui-advanced-composetitlebar-composetitlebarmenuitem-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComposeTitleBar-item?: ComposeTitleBarMenuItem--><!--Device-ComposeTitleBar-item?: ComposeTitleBarMenuItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## menuItems

```TypeScript
menuItems?: Array<ComposeTitleBarMenuItem>
```

List of menu items on the right.

**Type:** Array&lt;[ComposeTitleBarMenuItem](arkts-arkui-advanced-composetitlebar-composetitlebarmenuitem-c.md)&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComposeTitleBar-menuItems?: Array<ComposeTitleBarMenuItem>--><!--Device-ComposeTitleBar-menuItems?: Array<ComposeTitleBarMenuItem>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## subtitle

```TypeScript
subtitle?: ResourceStr
```

Subtitle.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComposeTitleBar-subtitle?: ResourceStr--><!--Device-ComposeTitleBar-subtitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
title: ResourceStr
```

Title.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComposeTitleBar-title: ResourceStr--><!--Device-ComposeTitleBar-title: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

