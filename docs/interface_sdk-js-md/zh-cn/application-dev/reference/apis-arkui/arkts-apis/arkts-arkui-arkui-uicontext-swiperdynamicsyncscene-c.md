# SwiperDynamicSyncScene

提供Swiper组件动态帧率场景的相关配置，适用于为动画过渡和手势跟手等不同交互场景设置差异化帧率范围，以兼顾流畅度和功耗，继承自[DynamicSyncScene](arkts-arkui-arkui-uicontext-dynamicsyncscene-c.md)。

**继承/实现关系：** SwiperDynamicSyncScene extends [DynamicSyncScene](arkts-arkui-arkui-uicontext-dynamicsyncscene-c.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare class SwiperDynamicSyncScene extends DynamicSyncScene--><!--Device-unnamed-export declare class SwiperDynamicSyncScene extends DynamicSyncScene-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from 'kits/@kit.ArkUI';
```

## type

```TypeScript
readonly type: SwiperDynamicSyncSceneType
```

Swiper的动态帧率场景类型。

**类型：** [SwiperDynamicSyncSceneType](arkts-arkui-arkui-uicontext-swiperdynamicsyncscenetype-e.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SwiperDynamicSyncScene-readonly type: SwiperDynamicSyncSceneType--><!--Device-SwiperDynamicSyncScene-readonly type: SwiperDynamicSyncSceneType-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

