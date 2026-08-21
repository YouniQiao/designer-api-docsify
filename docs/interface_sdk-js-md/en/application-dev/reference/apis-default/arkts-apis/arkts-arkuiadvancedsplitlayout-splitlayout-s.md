# SplitLayout

Declare SplitLayout.The SplitLayout is used for upper and lower graphic layouts. @struct { SplitLayout }

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare struct SplitLayout--><!--Device-unnamed-export declare struct SplitLayout-End-->

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

<!--Device-SplitLayout-@Builder    build(): void--><!--Device-SplitLayout-@Builder    build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## container

```TypeScript
@BuilderParam
    container: () => void
```

Container in the user-defined splitlayout display area.

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SplitLayout-@BuilderParam    container: () => void--><!--Device-SplitLayout-@BuilderParam    container: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## mainImage

```TypeScript
@State
    mainImage: ResourceStr
```

Image in the layout.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SplitLayout-@State    mainImage: ResourceStr--><!--Device-SplitLayout-@State    mainImage: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## primaryText

```TypeScript
@PropRef
    primaryText: ResourceStr
```

Title text in the layout.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SplitLayout-@PropRef    primaryText: ResourceStr--><!--Device-SplitLayout-@PropRef    primaryText: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## secondaryText

```TypeScript
@PropRef
    secondaryText?: ResourceStr
```

Description text in the layout.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SplitLayout-@PropRef    secondaryText?: ResourceStr--><!--Device-SplitLayout-@PropRef    secondaryText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## tertiaryText

```TypeScript
@PropRef
    tertiaryText?: ResourceStr
```

Auxiliary text in the layout.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SplitLayout-@PropRef    tertiaryText?: ResourceStr--><!--Device-SplitLayout-@PropRef    tertiaryText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

