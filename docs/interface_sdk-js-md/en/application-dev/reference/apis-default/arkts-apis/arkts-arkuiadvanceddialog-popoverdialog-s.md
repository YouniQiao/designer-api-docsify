# PopoverDialog

Declare struct PopoverDialog @struct { PopoverDialog }

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare struct PopoverDialog--><!--Device-unnamed-export declare struct PopoverDialog-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## build

```TypeScript
@Builder build(): void
```

The method to build component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopoverDialog-@Builder build(): void--><!--Device-PopoverDialog-@Builder build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## popover

```TypeScript
@Require @PropRef
  popover: PopoverOptions
```

Sets the PopoverDialog options.

**Type:** [PopoverOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvanceddialog-popoveroptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopoverDialog-@Require @PropRef  popover: PopoverOptions--><!--Device-PopoverDialog-@Require @PropRef  popover: PopoverOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## targetBuilder

```TypeScript
@Require @BuilderParam
  targetBuilder: () => void
```

Sets the targetBuilder content.

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopoverDialog-@Require @BuilderParam  targetBuilder: () => void--><!--Device-PopoverDialog-@Require @BuilderParam  targetBuilder: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## visible

```TypeScript
@Link visible: boolean
```

Sets the PopoverDialog Visible Status.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopoverDialog-@Link visible: boolean--><!--Device-PopoverDialog-@Link visible: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

