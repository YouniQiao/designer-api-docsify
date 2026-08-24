# SplitLayout

Declare SplitLayout.The SplitLayout is used for upper and lower graphic layouts. @struct { SplitLayout }

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Component

<!--Device-unnamed-export declare struct SplitLayout--><!--Device-unnamed-export declare struct SplitLayout-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## build

```TypeScript
build(): void
```

The method to build component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-SplitLayout-@Builder    build(): void--><!--Device-SplitLayout-@Builder    build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## container

```TypeScript
container: () => void
```

Container in the user-defined splitlayout display area.

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @BuilderParam

**Model restriction:** This API can be used only in the stage model.

<!--Device-SplitLayout-@BuilderParam    container: () => void--><!--Device-SplitLayout-@BuilderParam    container: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## mainImage

```TypeScript
mainImage: ResourceStr
```

Image in the layout.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @State

**Model restriction:** This API can be used only in the stage model.

<!--Device-SplitLayout-@State    mainImage: ResourceStr--><!--Device-SplitLayout-@State    mainImage: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## primaryText

```TypeScript
primaryText: ResourceStr
```

Title text in the layout.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @PropRef

**Model restriction:** This API can be used only in the stage model.

<!--Device-SplitLayout-@PropRef    primaryText: ResourceStr--><!--Device-SplitLayout-@PropRef    primaryText: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## secondaryText

```TypeScript
secondaryText?: ResourceStr
```

Description text in the layout.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @PropRef

**Model restriction:** This API can be used only in the stage model.

<!--Device-SplitLayout-@PropRef    secondaryText?: ResourceStr--><!--Device-SplitLayout-@PropRef    secondaryText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## tertiaryText

```TypeScript
tertiaryText?: ResourceStr
```

Auxiliary text in the layout.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @PropRef

**Model restriction:** This API can be used only in the stage model.

<!--Device-SplitLayout-@PropRef    tertiaryText?: ResourceStr--><!--Device-SplitLayout-@PropRef    tertiaryText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

