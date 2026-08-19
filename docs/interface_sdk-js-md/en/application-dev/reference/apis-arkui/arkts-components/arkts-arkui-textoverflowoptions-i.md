# TextOverflowOptions

Defines the configuration object for text overflow behavior. &gt; **NOTE：**&gt; &gt; To standardize anonymous object definitions, the element definitions here have been revised in API version 18. &gt; While historical version information is preserved for anonymous objects, there may be cases where the outer element &gt; 's @since version number is higher than inner elements'. This does not affect interface usability.

**Since:** 18

<!--Device-unnamed-declare interface TextOverflowOptions--><!--Device-unnamed-declare interface TextOverflowOptions-End-->

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

## overflow

```TypeScript
overflow: TextOverflow
```

Display mode of overflowing text. Default value: **TextOverflow.Clip**

**Type:** TextOverflow

**Default:** TextOverflow.Clip [since 18]

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-TextOverflowOptions-overflow: TextOverflow--><!--Device-TextOverflowOptions-overflow: TextOverflow-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

