# ToolBarV2

The **Toolbar** component is designed to present a set of action options related to the current screen, displayed at the bottom of the screen. It can display up to five child components. If there are six or more child components, the first four are shown directly, and the additional ones are grouped under a **More** item on the rightmost side of the toolbar.

This component is implemented based on [state management V2](../../../ui/state-management/arkts-state-management-overview.md#state-management-v2). Compared with [state management V1](../../../ui/state-management/arkts-state-management-overview.md#state-management-v1), V2 offers a higher level of observation and management over data objects beyond the component level. You can now more easily manage toolbar data and states with greater flexibility, leading to faster UI updates.

> **NOTE：**
> 
> - This component can be used only in the stage model.
> 
> - If the **ToolBarV2** component has universal attributes and
> universal events configured, the compiler toolchain automatically
> generates an additional **__Common__** node and mounts the universal attributes and universal events on this node
> rather than the **ToolBarV2** component itself. As a result, the configured universal attributes and universal
> events may fail to take effect or behave as intended. For this reason, avoid using universal attributes and events
> with the **ToolBarV2** component.
> 
> - The toolbar background color does not automatically switch when the system changes between light and dark modes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare struct ToolBarV2--><!--Device-unnamed-export declare struct ToolBarV2-End-->

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

<!--Device-ToolBarV2-@Builder  build(): void--><!--Device-ToolBarV2-@Builder  build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## activatedIndex

```TypeScript
@Param
  activatedIndex?: int
```

Define toolbarV2 activate item index, default is -1.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarV2-@Param  activatedIndex?: int--><!--Device-ToolBarV2-@Param  activatedIndex?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dividerModifier

```TypeScript
@Param
  dividerModifier?: DividerModifier
```

Define divider Modifier.

**Type:** [DividerModifier](../../apis-arkui/arkts-apis/arkts-arkui-dividermodifier-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarV2-@Param  dividerModifier?: DividerModifier--><!--Device-ToolBarV2-@Param  dividerModifier?: DividerModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## toolBarList

```TypeScript
@Require
  @Param
  toolBarList: ToolBarV2Item[]
```

Define toolbarV2 item list.

**Type:** [ToolBarV2Item](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedtoolbarv2-toolbarv2item-c.md)[]

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarV2-@Require  @Param  toolBarList: ToolBarV2Item[]--><!--Device-ToolBarV2-@Require  @Param  toolBarList: ToolBarV2Item[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## toolBarModifier

```TypeScript
@Param
  toolBarModifier?: ToolBarV2Modifier
```

Define toolbarV2 modifier.

**Type:** [ToolBarV2Modifier](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedtoolbarv2-toolbarv2modifier-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarV2-@Param  toolBarModifier?: ToolBarV2Modifier--><!--Device-ToolBarV2-@Param  toolBarModifier?: ToolBarV2Modifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

