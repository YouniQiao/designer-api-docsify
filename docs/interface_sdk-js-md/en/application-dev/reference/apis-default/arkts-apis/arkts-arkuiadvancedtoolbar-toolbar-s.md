# ToolBar

The **Toolbar** component is designed to present a set of action options related to the current screen, displayed at the bottom of the screen. It can display up to five child components. If there are six or more child components, the first four are shown directly, and the additional ones are grouped under a **More** item on the rightmost side of the toolbar.

> **NOTE：**
> 
> - This component can be used only in the stage model.
> 
> - If the **ToolBar** component has universal attributes and
> universal events configured, the compiler toolchain automatically
> generates an additional **__Common__** node and mounts the universal attributes and universal events on this node
> rather than the **ToolBar** component itself. As a result, the configured universal attributes and universal events
> may fail to take effect or behave as intended. For this reason, avoid using universal attributes and events with
> the **ToolBar** component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare struct ToolBar--><!--Device-unnamed-export declare struct ToolBar-End-->

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

<!--Device-ToolBar-@Builder  build(): void--><!--Device-ToolBar-@Builder  build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## activateIndex

```TypeScript
@PropRef
  activateIndex?: int
```

Index of the active item.

The value must be greater than or equal to -1.

The default value is **-1**, indicating that there is no active item. Values less than -1 are treated as no active item.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBar-@PropRef  activateIndex?: int--><!--Device-ToolBar-@PropRef  activateIndex?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## controller

```TypeScript
controller: TabsController
```

Toolbar controller, which cannot be used for controlling individual toolbar items.

**Type:** TabsController

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBar-controller: TabsController--><!--Device-ToolBar-controller: TabsController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dividerModifier

```TypeScript
@PropRef
  dividerModifier?: DividerModifier
```

Modifier for the toolbar header divider, which can be used to customize the divider's height, color, and other attributes.

Default value: system default value

**Type:** [DividerModifier](../../apis-arkui/arkts-apis/arkts-arkui-dividermodifier-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBar-@PropRef  dividerModifier?: DividerModifier--><!--Device-ToolBar-@PropRef  dividerModifier?: DividerModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## toolBarList

```TypeScript
@ObjectLink
  toolBarList: ToolBarOptions
```

Toolbar list.

**Type:** [ToolBarOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedtoolbar-toolbaroptions-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBar-@ObjectLink  toolBarList: ToolBarOptions--><!--Device-ToolBar-@ObjectLink  toolBarList: ToolBarOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## toolBarModifier

```TypeScript
@PropRef
  toolBarModifier?: ToolBarModifier
```

Modifier for the toolbar, which can be used to set the toolbar's height, background color, padding (which only takes effect when there are fewer than five toolbar items), and whether to display the pressed state.

Default value:

Height of the toolbar: **56vp**

Background color: **ohos_id_toolbar_bg**

Padding: **24vp**

Whether to display the pressed state: yes

**Type:** [ToolBarModifier](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedtoolbar-toolbarmodifier-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBar-@PropRef  toolBarModifier?: ToolBarModifier--><!--Device-ToolBar-@PropRef  toolBarModifier?: ToolBarModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

