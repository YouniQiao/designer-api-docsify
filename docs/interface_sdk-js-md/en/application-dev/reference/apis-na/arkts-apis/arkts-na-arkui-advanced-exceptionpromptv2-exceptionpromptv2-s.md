# ExceptionPromptV2

Declare struct ExceptionPromptV2 higher-order component. The exception prompt component is used to show an error message when an error arises.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare struct ExceptionPromptV2--><!--Device-unnamed-export declare struct ExceptionPromptV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## build

```TypeScript
@Builder
  build(): void
```

The method to build component.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExceptionPromptV2-@Builder  build(): void--><!--Device-ExceptionPromptV2-@Builder  build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onActionTextClick

```TypeScript
@Event
  onActionTextClick?: OnActionTextClickCallback
```

Callback invoked when the icon on the right is clicked.

**Type:** [OnActionTextClickCallback](../../apis-arkui/arkts-apis/arkts-arkui-onactiontextclickcallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExceptionPromptV2-@Event  onActionTextClick?: OnActionTextClickCallback--><!--Device-ExceptionPromptV2-@Event  onActionTextClick?: OnActionTextClickCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onTipClick

```TypeScript
@Event
  onTipClick?: OnTipClickCallback
```

Callback invoked when the prompt text on the left is clicked.

**Type:** [OnTipClickCallback](../../apis-arkui/arkts-apis/arkts-arkui-ontipclickcallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExceptionPromptV2-@Event  onTipClick?: OnTipClickCallback--><!--Device-ExceptionPromptV2-@Event  onTipClick?: OnTipClickCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## options

```TypeScript
@Param
  options: PromptOptionsV2
```

ExceptionPromptV2 configuration.

**Type:** [PromptOptionsV2](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-exceptionpromptv2-promptoptionsv2-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExceptionPromptV2-@Param  options: PromptOptionsV2--><!--Device-ExceptionPromptV2-@Param  options: PromptOptionsV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

