# ExceptionPromptV2

Declare struct ExceptionPromptV2 higher-order component. The exception prompt component is used to show an error message when an error arises. @struct { ExceptionPromptV2 }

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Decorator:** @ComponentV2

<!--Device-unnamed-export declare struct ExceptionPromptV2--><!--Device-unnamed-export declare struct ExceptionPromptV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## build

```TypeScript
build(): void
```

The method to build component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExceptionPromptV2-@Builder  build(): void--><!--Device-ExceptionPromptV2-@Builder  build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onActionTextClick

```TypeScript
onActionTextClick?: OnActionTextClickCallback
```

Callback invoked when the icon on the right is clicked.

**Type:** [OnActionTextClickCallback](arkts-onactiontextclickcallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Decorator:** @Event

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExceptionPromptV2-@Event  onActionTextClick?: OnActionTextClickCallback--><!--Device-ExceptionPromptV2-@Event  onActionTextClick?: OnActionTextClickCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onTipClick

```TypeScript
onTipClick?: OnTipClickCallback
```

Callback invoked when the prompt text on the left is clicked.

**Type:** [OnTipClickCallback](arkts-ontipclickcallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Decorator:** @Event

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExceptionPromptV2-@Event  onTipClick?: OnTipClickCallback--><!--Device-ExceptionPromptV2-@Event  onTipClick?: OnTipClickCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## options

```TypeScript
options: PromptOptionsV2
```

ExceptionPromptV2 configuration.

**Type:** [PromptOptionsV2](arkts-arkui-advanced-exceptionpromptv2-promptoptionsv2-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExceptionPromptV2-@Param  options: PromptOptionsV2--><!--Device-ExceptionPromptV2-@Param  options: PromptOptionsV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

