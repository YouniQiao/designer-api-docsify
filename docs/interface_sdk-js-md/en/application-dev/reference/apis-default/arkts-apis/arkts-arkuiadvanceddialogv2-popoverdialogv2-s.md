# PopoverDialogV2

Declare struct PopoverDialogV2

@struct { PopoverDialogV2 }

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare struct PopoverDialogV2--><!--Device-unnamed-export declare struct PopoverDialogV2-End-->

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

<!--Device-PopoverDialogV2-@Builder  build(): void--><!--Device-PopoverDialogV2-@Builder  build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $visible

```TypeScript
@Event
  $visible?: PopoverDialogV2OnVisibleChange
```

Sets the callback when visibility changed.

**Type:** [PopoverDialogV2OnVisibleChange](../../apis-arkui/arkts-apis/arkts-arkui-popoverdialogv2onvisiblechange-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopoverDialogV2-@Event  $visible?: PopoverDialogV2OnVisibleChange--><!--Device-PopoverDialogV2-@Event  $visible?: PopoverDialogV2OnVisibleChange-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## popover

```TypeScript
@Require
  @Param
  popover: PopoverDialogV2Options
```

Sets the PopoverDialogV2 options.

**Type:** [PopoverDialogV2Options](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvanceddialogv2-popoverdialogv2options-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopoverDialogV2-@Require  @Param  popover: PopoverDialogV2Options--><!--Device-PopoverDialogV2-@Require  @Param  popover: PopoverDialogV2Options-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## targetBuilder

```TypeScript
@BuilderParam
  targetBuilder: CustomBuilder
```

Sets the targetBuilder content.

**Type:** CustomBuilder

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopoverDialogV2-@BuilderParam  targetBuilder: CustomBuilder--><!--Device-PopoverDialogV2-@BuilderParam  targetBuilder: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## visible

```TypeScript
@Require
  @Param
  visible: boolean
```

Sets the PopoverDialogV2 Visible Status.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopoverDialogV2-@Require  @Param  visible: boolean--><!--Device-PopoverDialogV2-@Require  @Param  visible: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

