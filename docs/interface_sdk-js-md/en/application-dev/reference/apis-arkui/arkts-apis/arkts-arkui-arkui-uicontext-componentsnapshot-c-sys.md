# ComponentSnapshot

Provides APIs for obtaining component snapshots, including snapshots of components that have been loaded and snapshots of components that have not been loaded yet.

> **NOTE：**&gt;
> - The initial APIs of this class are supported since API version 12.&gt;
> - In the following API examples, you must first use [getComponentSnapshot()](arkts-arkui-arkui-uicontext-uicontext-c.md#getcomponentsnapshot)
> in **UIContext** to obtain a **ComponentSnapshot** instance, and then call the APIs using the obtained instance.&gt;
> - Transformation properties such as scaling, translation, and rotation only apply to the child components of the
> target component. Applying these transformation properties directly to the target component itself has no effect;
> the snapshot will still display the component as it appears before any transformations are applied.

**Since:** 12

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AtomicServiceBar, ComponentUtils, ContextMenuController, CursorController, DialogPresenter, DragController, Font, KeyboardAvoidMode, MediaQuery, OverlayManager, PromptAction, Router, UIContext, UIInspector, UIObserver, PageInfo, SwiperDynamicSyncScene, SwiperDynamicSyncSceneType, MarqueeDynamicSyncScene, MarqueeDynamicSyncSceneType, MeasureUtils, FrameCallback, OverlayManagerOptions, TargetInfo, TextMenuController, NodeIdentity, NodeRenderState, NodeRenderStateChangeCallback, Magnifier, ResolvedUIContext, TextSelectionClearPolicy, CustomKeyboardContinueFeature, BackgroundLuminanceSamplingConfigs, LuminanceSampler } from 'kits/@kit.ArkUI';
import { GestureListenerType, GestureActionPhase, GestureTriggerInfo, GestureObserverConfigs, GestureListenerCallback } from 'kits/@kit.ArkUI';
import { SwiperContentInfo, SwiperItemInfo } from 'kits/@kit.ArkUI';
import { BackPressActionProposal, BaseGestureHandlingProposal, ClickActionProposal, GestureHandlingResolution, NoneActionProposal, PageSwitchActionProposal, ScrollActionProposal, SelectActionProposal, SmartGestureController, TargetedGestureProposal } from 'kits/@kit.ArkUI';
```

## getWithRange

```TypeScript
getWithRange(start: NodeIdentity, end: NodeIdentity, isStartRect: boolean,
    options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>
```

Captures a snapshot of the area between two specified components. This API uses a promise to return the result.

> **NOTE：**&gt;
> The components corresponding to **start** and **end** must belong to the same component tree, and the **start**
> component must be an ancestor of the **end** component.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | [NodeIdentity](arkts-arkui-nodeidentity-t.md) | Yes |
| end | [NodeIdentity](arkts-arkui-nodeidentity-t.md) | Yes |
| isStartRect | boolean | Yes |
| options | componentSnapshot.SnapshotOptions | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [160003](../errorcode-snapshot.md#160003-provided-color-space-or-dynamic-range-mode-is-not-supported) |
