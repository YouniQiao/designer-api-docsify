# TargetInfo

指定组件绑定的目标节点。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface TargetInfo--><!--Device-unnamed-export interface TargetInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from 'kits/@kit.ArkUI';
```

## componentId

```TypeScript
componentId?: int
```

目标节点所在的自定义组件的UniqueID。当上述id指定为string类型时，可通过此属性圈定范围。方便开发者在一定范围内保证id: string的唯一性。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TargetInfo-componentId?: int--><!--Device-TargetInfo-componentId?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
id: string | int
```

指定popup或menu绑定的目标节点。  
**说明：**1. 当id是number时，对应组件实例的UniqueID，此id由系统保证唯一性。2. 当id是string时，对应[通用属性id](arkts-arkui-common-commonmethod-i.md#id)所指定的组件，此id的唯一性需由开发者确保，但实际可能会有多个。

**Type:** string \| int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TargetInfo-id: string | int--><!--Device-TargetInfo-id: string | int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

