# SelectDialogV2

Declare CustomDialog SelectDialogV2

@struct { SelectDialogV2 }

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare struct SelectDialogV2--><!--Device-unnamed-export declare struct SelectDialogV2-End-->

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

<!--Device-SelectDialogV2-@Builder  build(): void--><!--Device-SelectDialogV2-@Builder  build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## confirm

```TypeScript
@Param
  confirm?: AdvancedDialogV2Button
```

Sets the SelectDialogV2 confirm button.

**Type:** [AdvancedDialogV2Button](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-dialogv2-advanceddialogv2button-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectDialogV2-@Param  confirm?: AdvancedDialogV2Button--><!--Device-SelectDialogV2-@Param  confirm?: AdvancedDialogV2Button-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
@Param
  content?: ResourceStr
```

Sets the SelectDialogV2 content.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectDialogV2-@Param  content?: ResourceStr--><!--Device-SelectDialogV2-@Param  content?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## radioContent

```TypeScript
@Require
  @Param
  radioContent: SheetInfo[]
```

Sets the SelectDialog sheets.

**Type:** SheetInfo[]

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectDialogV2-@Require  @Param  radioContent: SheetInfo[]--><!--Device-SelectDialogV2-@Require  @Param  radioContent: SheetInfo[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedIndex

```TypeScript
@Param
  selectedIndex?: int
```

Sets the SelectDialogV2 selected index.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectDialogV2-@Param  selectedIndex?: int--><!--Device-SelectDialogV2-@Param  selectedIndex?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
@Require
  @Param
  title: ResourceStr
```

Sets the SelectDialogV2 title.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectDialogV2-@Require  @Param  title: ResourceStr--><!--Device-SelectDialogV2-@Require  @Param  title: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

