# ComponentSnapshot

提供获取组件截图的能力，包括已加载的组件的截图和没有加载的组件的截图。

> **说明：**&gt;
> - 本Class首批接口从API version 12开始支持。&gt;
> - 以下API需先使用UIContext中的[getComponentSnapshot()](arkts-arkui-arkui-uicontext-uicontext-c.md#getcomponentsnapshot)方法获取ComponentSnapshot对象，再通过此实例调用对应方法。&gt;
> - 缩放、平移、旋转等图形变换属性只对被截图组件的子组件生效；对目标组件本身应用图形变换属性不生效，显示的还是图形变换前的效果。

**起始版本：** 12

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

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

传入两个组件的ID，获取范围内的组件的截图，并通过Promise返回结果。

> **说明：**&gt;
> start对应的组件和end对应的组件必须为同一棵组件树上的组件，且start对应的组件需要为end对应的组件的祖先组件。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | [NodeIdentity](arkts-arkui-nodeidentity-t.md) | 是 |
| end | [NodeIdentity](arkts-arkui-nodeidentity-t.md) | 是 |
| isStartRect | boolean | 是 |
| options | componentSnapshot.SnapshotOptions | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;image.PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [160003](../errorcode-snapshot.md#160003-截图选项中设置的色彩空间或动态范围模式不受支持) |
