# ContentCoverOptions

Component content cover options

@extends BindOptions

**Inheritance/Implementation:** ContentCoverOptions extends [BindOptions](arkts-common-bindoptions-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface ContentCoverOptions--><!--Device-unnamed-export declare interface ContentCoverOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableSafeArea

```TypeScript
enableSafeArea?: boolean
```

Set contentCover content adapts to safeArea.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentCoverOptions-enableSafeArea?: boolean--><!--Device-ContentCoverOptions-enableSafeArea?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## modalTransition

```TypeScript
modalTransition?: ModalTransition
```

Defines transition type

**Type:** [ModalTransition](arkts-common-modaltransition-e.md)

**Default:** ModalTransition.Default

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentCoverOptions-modalTransition?: ModalTransition--><!--Device-ContentCoverOptions-modalTransition?: ModalTransition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDismiss

```TypeScript
onWillDismiss?: Callback<DismissContentCoverAction>
```

Callback function when the content cover interactive dismiss

**Type:** [Callback](arkts-callback-t.md)&lt;[DismissContentCoverAction](arkts-common-dismisscontentcoveraction-i.md)&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentCoverOptions-onWillDismiss?: Callback<DismissContentCoverAction>--><!--Device-ContentCoverOptions-onWillDismiss?: Callback<DismissContentCoverAction>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## transition

```TypeScript
transition?: TransitionEffect
```

Defines transition effect param

**Type:** [TransitionEffect](arkts-common-transitioneffect-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentCoverOptions-transition?: TransitionEffect--><!--Device-ContentCoverOptions-transition?: TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

