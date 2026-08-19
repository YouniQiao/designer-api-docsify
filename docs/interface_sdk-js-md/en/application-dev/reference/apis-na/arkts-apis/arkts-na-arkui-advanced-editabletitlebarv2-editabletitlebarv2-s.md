# EditableTitleBarV2

Declaration of the editable title bar.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare struct EditableTitleBarV2--><!--Device-unnamed-export declare struct EditableTitleBarV2-End-->

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

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarV2-@Builder  build(): void--><!--Device-EditableTitleBarV2-@Builder  build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageItem

```TypeScript
@Param
  imageItem?: EditableTitleBarItemV2
```

Image item configuration, displayed on the left side of the title.

**Type:** [EditableTitleBarItemV2](arkts-na-editabletitlebaritemv2-t.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarV2-@Param  imageItem?: EditableTitleBarItemV2--><!--Device-EditableTitleBarV2-@Param  imageItem?: EditableTitleBarItemV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## leftIcon

```TypeScript
@Param
  leftIcon?: EditableLeftIconV2
```

Left icon configuration.

**Type:** [EditableLeftIconV2](arkts-na-arkui-advanced-editabletitlebarv2-editablelefticonv2-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarV2-@Param  leftIcon?: EditableLeftIconV2--><!--Device-EditableTitleBarV2-@Param  leftIcon?: EditableLeftIconV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## menuItems

```TypeScript
@Param
  menuItems?: Array<EditableTitleBarMenuItemV2>
```

Custom menu items array, maximum 2-3 items.

**Type:** Array&lt;[EditableTitleBarMenuItemV2](arkts-na-arkui-advanced-editabletitlebarv2-editabletitlebarmenuitemv2-c.md)&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarV2-@Param  menuItems?: Array<EditableTitleBarMenuItemV2>--><!--Device-EditableTitleBarV2-@Param  menuItems?: Array<EditableTitleBarMenuItemV2>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## options

```TypeScript
@Param
  options: EditableTitleBarStyleV2
```

Style and layout configuration.

**Type:** [EditableTitleBarStyleV2](arkts-na-arkui-advanced-editabletitlebarv2-editabletitlebarstylev2-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarV2-@Param  options: EditableTitleBarStyleV2--><!--Device-EditableTitleBarV2-@Param  options: EditableTitleBarStyleV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## saveButton

```TypeScript
@Param
  saveButton?: EditableSaveButtonV2
```

Save button configuration.

**Type:** [EditableSaveButtonV2](arkts-na-arkui-advanced-editabletitlebarv2-editablesavebuttonv2-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarV2-@Param  saveButton?: EditableSaveButtonV2--><!--Device-EditableTitleBarV2-@Param  saveButton?: EditableSaveButtonV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
@Param
  @Require
  title: ResourceStr | EditableTitleV2
```

Title configuration, supports string or object form.

**Type:** ResourceStr \| [EditableTitleV2](arkts-na-arkui-advanced-editabletitlebarv2-editabletitlev2-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarV2-@Param  @Require  title: ResourceStr | EditableTitleV2--><!--Device-EditableTitleBarV2-@Param  @Require  title: ResourceStr | EditableTitleV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

