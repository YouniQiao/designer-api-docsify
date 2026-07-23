# SwiperDynamicSyncScene

提供Swiper组件动态帧率场景的相关配置，适用于为动画过渡和手势跟手等不同交互场景设置差异化帧率范围，以兼顾流畅度和功耗。
> **说明**  
> SwiperDynamicSyncScene继承自[DynamicSyncScene](arkts-arkui-uicontext.md)，对应Swiper的动态帧率场景。使用前需先通过UIContext的requireDynamicSyncScene方法获取实例，再调用继承的方法设置对应场景的帧率范围。

**继承/实现关系：** SwiperDynamicSyncScene extends [DynamicSyncScene](arkts-arkui-arkui-uicontext-dynamicsyncscene-c.md)

**起始版本：** 12

<!--Device-unnamed-export class SwiperDynamicSyncScene extends DynamicSyncScene--><!--Device-unnamed-export class SwiperDynamicSyncScene extends DynamicSyncScene-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from '@kit.ArkUI';
```

## type

```TypeScript
readonly type: SwiperDynamicSyncSceneType
```

Swiper的动态帧率场景类型。

**类型：** SwiperDynamicSyncSceneType

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-SwiperDynamicSyncScene-readonly type: SwiperDynamicSyncSceneType--><!--Device-SwiperDynamicSyncScene-readonly type: SwiperDynamicSyncSceneType-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

