# TextController

Defines the controller of the **Text** component.

## Objects to Import ```ts controller: TextController = new TextController() ```

**Since:** 11

<!--Device-unnamed-declare class TextController--><!--Device-unnamed-declare class TextController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { WindowExtensionAbility, WindowExtensionContext } from '@kit.ArkUI';
import { NodeRenderType, RenderOptions, BuilderNode, ReactiveBuilderNode, BuildOptions, NodeController, FrameNode, DrawContext, Size, Offset, Position, Pivot, Scale, Translation, Matrix4, Rotation, Frame, RenderNode, XComponentNode, LengthMetrics, ColorMetrics, BackgroundBlur, ContentBlur, ForegroundBlur, LengthUnit, LengthMetricsUnit, LayoutConstraint, ComponentContent, ReactiveComponentContent, NodeContent, Content, typeNode, NodeAdapter, ShapeMask, ShapeClip, Rect, RoundRect, edgeColors, edgeWidths, borderStyles, borderRadiuses, ExpandMode, ChildrenCountMode, UIState, InputEventType } from '@kit.ArkUI';
import { AppStorageV2, PersistenceV2, Type, UIUtils, ConnectOptions, Binding, MutableBinding, CustomComponentLifecycle, CustomComponentLifecycleObserver, CustomComponentLifecycleState, ComponentInit, ComponentAppear, ComponentBuilt, ComponentReuse, ComponentActive, ComponentInactive, ComponentRecycle, ComponentDisappear, CollectionType, ConnectOptionsCollections, CustomComponentContext, IReusePool, IReusableInfo } from '@kit.ArkUI';
import { AtomicServiceBar, ComponentUtils, ContextMenuController, CursorController, DialogPresenter, DragController, Font, KeyboardAvoidMode, MediaQuery, OverlayManager, PromptAction, Router, UIContext, UIInspector, UIObserver, PageInfo, SwiperDynamicSyncScene, SwiperDynamicSyncSceneType, MarqueeDynamicSyncScene, MarqueeDynamicSyncSceneType, MeasureUtils, FrameCallback, OverlayManagerOptions, TargetInfo, TextMenuController, NodeIdentity, NodeRenderState, NodeRenderStateChangeCallback, Magnifier, ResolvedUIContext, TextSelectionClearPolicy, CustomKeyboardContinueFeature, BackgroundLuminanceSamplingConfigs, LuminanceSampler } from '@kit.ArkUI';
import { GestureListenerType, GestureActionPhase, GestureTriggerInfo, GestureObserverConfigs, GestureListenerCallback } from '@kit.ArkUI';
import { SwiperContentInfo, SwiperItemInfo } from '@kit.ArkUI';
import { BackPressActionProposal, BaseGestureHandlingProposal, ClickActionProposal, GestureHandlingResolution, NoneActionProposal, PageSwitchActionProposal, ScrollActionProposal, SelectActionProposal, SmartGestureController, TargetedGestureProposal } from '@kit.ArkUI';
```

## closeSelectionMenu

```TypeScript
closeSelectionMenu(): void
```

Closes the custom or default text selection menu.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextController-closeSelectionMenu(): void--><!--Device-TextController-closeSelectionMenu(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getLayoutManager

```TypeScript
getLayoutManager(): LayoutManager
```

Obtains the **LayoutManager** object.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextController-getLayoutManager(): LayoutManager--><!--Device-TextController-getLayoutManager(): LayoutManager-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| LayoutManager | LayoutManager** object. |

## setStyledString

```TypeScript
setStyledString(value: StyledString): void
```

Binds to or updates the specified styled string.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextController-setStyledString(value: StyledString): void--><!--Device-TextController-setStyledString(value: StyledString): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | StyledString | Yes | Styled string.<br>**NOTE：**<br>The child class MutableStyledString of **StyledString** can also serve as the argument. |

## setTextSelection

```TypeScript
setTextSelection(selectionStart: number | undefined, selectionEnd: number | undefined,
                   options?: SelectionOptions): void
```

Sets the text selection area, which will be highlighted. &gt; **NOTE：**&gt; &gt; If [copyOption](arkts-arkui-text-attribute.md#copyoption) is set to **CopyOptions.None**, the setting of &gt; **setTextSelection** does not take effect. &gt; &gt; If [textOverflow](arkts-arkui-text-attribute.md#textoverflow) is set to **TextOverflow.MARQUEE**, the setting of &gt; **setTextSelection** does not take effect. &gt; &gt; If the value of **selectionStart** is greater than or equal to that of **selectionEnd**, no text will be &gt; selected. The value range is [0, textSize], where **textSize** indicates the maximum number of characters in the &gt; text content. If the value is less than 0, the value **0** will be used. If the value is greater than &gt; **textSize**, **textSize** will be used. &gt; &gt; If the selection range falls within a truncated or invisible area, selection is ignored. When truncation is &gt; disabled, selection can extend beyond the parent component's bounds. &gt; &gt; On PC or 2-in-1 devices, calling **setTextSelection** does not show the menu even if **options** is set to &gt; **MenuPolicy.SHOW**. &gt; &gt; When an emoji is truncated by the selection range, the emoji is selected if its start position is within the &gt; specified text selection range.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TextController-setTextSelection(selectionStart: number | undefined, selectionEnd: number | undefined,                   options?: SelectionOptions): void--><!--Device-TextController-setTextSelection(selectionStart: number | undefined, selectionEnd: number | undefined,                   options?: SelectionOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectionStart | number \| undefined | Yes | Start position of the text selection range.<br>Value range: [0, +∞). Negative values and **undefined** are treated as **0**. |
| selectionEnd | number \| undefined | Yes | End position of the text selection range.<br>Value range: [0, +∞). Negative values and **undefined** are treated as **0**. |
| options | SelectionOptions | No | Configuration options for text selection.<br>Default value: **MenuPolicy.DEFAULT** in **SelectionOptions |

