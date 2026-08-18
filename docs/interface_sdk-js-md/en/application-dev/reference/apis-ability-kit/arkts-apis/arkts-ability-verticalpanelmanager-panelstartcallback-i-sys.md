# PanelStartCallback (System API)

The callback of start vertical panel.

**Since:** 23

<!--Device-verticalPanelManager-interface PanelStartCallback--><!--Device-verticalPanelManager-interface PanelStartCallback-End-->

**System capability:** SystemCapability.Ability.AppExtension.VerticalPanel

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { verticalPanelManager } from '@kit.AbilityKit';
```

## onError

```TypeScript
onError: OnErrorFn
```

Called when some error occurred except disconnected from UIAbility or UIExtensionAbility.

**Type:** [OnErrorFn](arkts-ability-onerrorfn-t-sys.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanelStartCallback-onError: OnErrorFn--><!--Device-PanelStartCallback-onError: OnErrorFn-End-->

**System capability:** SystemCapability.Ability.AppExtension.VerticalPanel

**System API:** This is a system API.

## onResult

```TypeScript
onResult?: OnResultFn
```

Called when UIExtensionAbility terminate with result.

**Type:** [OnResultFn](arkts-ability-onresultfn-t-sys.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanelStartCallback-onResult?: OnResultFn--><!--Device-PanelStartCallback-onResult?: OnResultFn-End-->

**System capability:** SystemCapability.Ability.AppExtension.VerticalPanel

**System API:** This is a system API.

