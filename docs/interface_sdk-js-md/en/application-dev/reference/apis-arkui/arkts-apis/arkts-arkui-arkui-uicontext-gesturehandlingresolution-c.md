# GestureHandlingResolution

Class for declaring the result of smart gesture handling.

**Since:** 26.0.0

<!--Device-unnamed-export class GestureHandlingResolution--><!--Device-unnamed-export class GestureHandlingResolution-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AtomicServiceBar, ComponentUtils, ContextMenuController, CursorController, DialogPresenter, DragController, Font, KeyboardAvoidMode, MediaQuery, OverlayManager, PromptAction, Router, UIContext, UIInspector, UIObserver, PageInfo, SwiperDynamicSyncScene, SwiperDynamicSyncSceneType, MarqueeDynamicSyncScene, MarqueeDynamicSyncSceneType, MeasureUtils, FrameCallback, OverlayManagerOptions, TargetInfo, TextMenuController, NodeIdentity, NodeRenderState, NodeRenderStateChangeCallback, Magnifier, ResolvedUIContext, TextSelectionClearPolicy, CustomKeyboardContinueFeature, BackgroundLuminanceSamplingConfigs, LuminanceSampler } from '@kit.ArkUI';
import { GestureListenerType, GestureActionPhase, GestureTriggerInfo, GestureObserverConfigs, GestureListenerCallback } from '@kit.ArkUI';
import { SwiperContentInfo, SwiperItemInfo } from '@kit.ArkUI';
import { BackPressActionProposal, BaseGestureHandlingProposal, ClickActionProposal, GestureHandlingResolution, NoneActionProposal, PageSwitchActionProposal, ScrollActionProposal, SelectActionProposal, SmartGestureController, TargetedGestureProposal } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(isConsumed: boolean)
```

Constructor for the smart gesture handling result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-GestureHandlingResolution-constructor(isConsumed: boolean)--><!--Device-GestureHandlingResolution-constructor(isConsumed: boolean)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isConsumed | boolean | Yes | Whether to consume the current smart gesture.<br/>**true**: The smart gesture is consumed. If [selectedProposal](../../apis-default/arkts-apis/arkts-arkui-uicontext-gesturehandlingresolution-c.md#selectedproposal) is not set, the system default action handling is used. If **selectedProposal** is set, the custom action handling is used.<br/>**false**: The smart gesture is not consumed, and the system treats it as unhandled. |

**Examples**

```TypeScript
import { UIContext } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

function GetUIContextByAtomicInterface(): UIContext {
  let callingScopeUIContext = UIContext.getCallingScopeUIContext();
  if (callingScopeUIContext) {
    hilog.info(0x00, 'testTag', `Get UIContext of calling scope.`)
    return callingScopeUIContext;
  }
  let allContexts = UIContext.getAllUIContexts();
  let length = allContexts.length;
  if (length === 1) {
    hilog.info(0x00, 'testTag', `Get UIContext of unique UI instance.`)
    return allContexts[0];
  }
  let lastFocusedUIContext = UIContext.getLastFocusedUIContext();
  if (lastFocusedUIContext) {
    hilog.info(0x00, 'testTag', `Get UIContext of last focused instance.`)
    return lastFocusedUIContext;
  }
  let lastForegroundUIContext = UIContext.getLastForegroundUIContext();
  if (lastForegroundUIContext) {
    hilog.info(0x00, 'testTag', `Get UIContext of last foregrounded instance.`)
    return lastForegroundUIContext;
  }
  if (length !== 0) {
    hilog.info(0x00, 'testTag', `Get UIContext with maximum instanceId.`)
    return allContexts[length - 1];
  }
  hilog.info(0x00, 'testTag', `Get UIContext of undefined calling scope.`)
  return new UIContext();
}

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  aboutToAppear() {
    let uiContext = this.getUIContext();
    hilog.info(0x00, 'testTag', `aboutToAppear UIContext: ${uiContext.getId()}`)
  }

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          let resolvedUIContext = UIContext.resolveUIContext();
          let contextByAtomicInterface = GetUIContextByAtomicInterface();
          hilog.info(0x00, 'testTag',
            `UIContext id: ${resolvedUIContext.getId()}, strategy: ${resolvedUIContext.strategy}}, contextByAtomicInterface: ${contextByAtomicInterface.getId()}`);
          this.message = 'Welcome';
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

## isConsumed

```TypeScript
isConsumed: boolean
```

Whether to consume the current smart gesture.

**true**: The smart gesture is consumed. If **selectedProposal** is not set, the system default action handling is used. If **selectedProposal** is set, the custom action handling is used.

**false**: The smart gesture is not consumed, and the system treats it as unhandled.

**Type:** boolean

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-GestureHandlingResolution-isConsumed: boolean--><!--Device-GestureHandlingResolution-isConsumed: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedProposal

```TypeScript
selectedProposal?: BaseGestureHandlingProposal
```

The smart gesture handling behavior specified by the user.

When **isConsumed** is **true**: If **selectedProposal** is not set, the system default action handling is used. If **selectedProposal** is set, the custom action handling is used.

When **isConsumed** is **false**, the **selectedProposal** setting does not take effect.

**Type:** [BaseGestureHandlingProposal](../../apis-default/arkts-apis/arkts-arkui-uicontext-basegesturehandlingproposal-c.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-GestureHandlingResolution-selectedProposal?: BaseGestureHandlingProposal--><!--Device-GestureHandlingResolution-selectedProposal?: BaseGestureHandlingProposal-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

