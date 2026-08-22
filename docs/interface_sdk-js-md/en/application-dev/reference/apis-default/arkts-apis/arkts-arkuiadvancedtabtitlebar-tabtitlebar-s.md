# TabTitleBar

The **TabTitleBar** component is a tab title bar used to switch between tabs pages. It is applicable only to level-1 pages.

> **NOTE：**
> 
> - If the **TabTitleBar** component has universal attributes and
> universal events configured, the compiler toolchain automatically
> generates an additional **__Common__** node and mounts the universal attributes and universal events on this node
> rather than the **TabTitleBar** component itself. As a result, the configured universal attributes and universal
> events may fail to take effect or behave as intended. For this reason, avoid using universal attributes and events
> with the **TabTitleBar** component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare struct TabTitleBar--><!--Device-unnamed-export declare struct TabTitleBar-End-->

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

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabTitleBar-@Builder  build(): void--><!--Device-TabTitleBar-@Builder  build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## menuItems

```TypeScript
menuItems?: Array<TabTitleBarMenuItem>
```

List of menu items on the right of the title bar.

**Type:** Array&lt;[TabTitleBarMenuItem](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedtabtitlebar-tabtitlebarmenuitem-c.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabTitleBar-menuItems?: Array<TabTitleBarMenuItem>--><!--Device-TabTitleBar-menuItems?: Array<TabTitleBarMenuItem>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## swiperContent

```TypeScript
@BuilderParam
  swiperContent: () => void
```

Constructor for page content pertaining to the tab list.

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabTitleBar-@BuilderParam  swiperContent: () => void--><!--Device-TabTitleBar-@BuilderParam  swiperContent: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## tabItems

```TypeScript
tabItems: Array<TabTitleBarTabItem>
```

List of tab items on the left of the title bar.

**Type:** Array&lt;[TabTitleBarTabItem](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedtabtitlebar-tabtitlebartabitem-c.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabTitleBar-tabItems: Array<TabTitleBarTabItem>--><!--Device-TabTitleBar-tabItems: Array<TabTitleBarTabItem>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

