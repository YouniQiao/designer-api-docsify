# Magnifier

Provides the capability of displaying and hiding of the magnifier. The magnifier enlarges the component content for you to view the component details.

> **NOTE：**&gt;
> - In the following API examples, you must first use [getMagnifier()](arkts-arkui-arkui-uicontext-uicontext-c.md#getmagnifier) in **UIContext**
> to obtain a **Magnifier** instance, and then call the APIs using the obtained instance.&gt;
> - The magnifier capability of this class does not affect that of text components. For text components, you are
> advised to use the built-in magnifier capability.

**Since:** 22

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AtomicServiceBar, ComponentUtils, ContextMenuController, CursorController, DialogPresenter, DragController, Font, KeyboardAvoidMode, MediaQuery, OverlayManager, PromptAction, Router, UIContext, UIInspector, UIObserver, PageInfo, SwiperDynamicSyncScene, SwiperDynamicSyncSceneType, MarqueeDynamicSyncScene, MarqueeDynamicSyncSceneType, MeasureUtils, FrameCallback, OverlayManagerOptions, TargetInfo, TextMenuController, NodeIdentity, NodeRenderState, NodeRenderStateChangeCallback, Magnifier, ResolvedUIContext, TextSelectionClearPolicy, CustomKeyboardContinueFeature, BackgroundLuminanceSamplingConfigs, LuminanceSampler } from 'kits/@kit.ArkUI';
import { GestureListenerType, GestureActionPhase, GestureTriggerInfo, GestureObserverConfigs, GestureListenerCallback } from 'kits/@kit.ArkUI';
import { SwiperContentInfo, SwiperItemInfo } from 'kits/@kit.ArkUI';
import { BackPressActionProposal, BaseGestureHandlingProposal, ClickActionProposal, GestureHandlingResolution, NoneActionProposal, PageSwitchActionProposal, ScrollActionProposal, SelectActionProposal, SmartGestureController, TargetedGestureProposal } from 'kits/@kit.ArkUI';
```

## bind

```TypeScript
bind(id: string): void
```

Binds the magnifier to the component with the specified ID.

> **NOTE：**&gt;
> Obtain the Magnifier instance by using the getMagnifier() method in UIContext.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |

## show

```TypeScript
show(x: number, y: number): void
```

Sets the position of the component content displayed by the magnifier relative to the upper left corner of the component. After the setting is successful, the magnifier displays the content centered at the coordinate point.

> **NOTE：**&gt;
> When the content of the component bound to the magnifier changes, the magnifier does not automatically update the
> displayed content. You need to call the **show** API to update the displayed content of the magnifier.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

## unbind

```TypeScript
unbind(): void
```

Unbinds the magnifier from the current component.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
