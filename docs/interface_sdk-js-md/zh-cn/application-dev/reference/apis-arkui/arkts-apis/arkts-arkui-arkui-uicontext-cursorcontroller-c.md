# CursorController

提供光标样式设置的能力。

> **说明：**&gt;
> - 本Class首批接口从API version 12开始支持。&gt;
> - 以下API需先使用UIContext中的[getCursorController()](arkts-arkui-arkui-uicontext-uicontext-c.md#getcursorcontroller)方法获取CursorController实例，再通过此实例调用对应方法。

**起始版本：** 12

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { AtomicServiceBar, ComponentUtils, ContextMenuController, CursorController, DialogPresenter, DragController, Font, KeyboardAvoidMode, MediaQuery, OverlayManager, PromptAction, Router, UIContext, UIInspector, UIObserver, PageInfo, SwiperDynamicSyncScene, SwiperDynamicSyncSceneType, MarqueeDynamicSyncScene, MarqueeDynamicSyncSceneType, MeasureUtils, FrameCallback, OverlayManagerOptions, TargetInfo, TextMenuController, NodeIdentity, NodeRenderState, NodeRenderStateChangeCallback, Magnifier, ResolvedUIContext, TextSelectionClearPolicy, CustomKeyboardContinueFeature, BackgroundLuminanceSamplingConfigs, LuminanceSampler } from 'kits/@kit.ArkUI';
import { GestureListenerType, GestureActionPhase, GestureTriggerInfo, GestureObserverConfigs, GestureListenerCallback } from 'kits/@kit.ArkUI';
import { SwiperContentInfo, SwiperItemInfo } from 'kits/@kit.ArkUI';
import { BackPressActionProposal, BaseGestureHandlingProposal, ClickActionProposal, GestureHandlingResolution, NoneActionProposal, PageSwitchActionProposal, ScrollActionProposal, SelectActionProposal, SmartGestureController, TargetedGestureProposal } from 'kits/@kit.ArkUI';
```

## restoreDefault

```TypeScript
restoreDefault(): void
```

恢复默认的光标样式。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## setCursor

```TypeScript
setCursor(value: PointerStyle): void
```

更改当前的鼠标光标样式。

> **说明：**&gt;
> 该接口调用后不会立即生效，而是在下一帧改变鼠标光标样式。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [PointerStyle](arkts-arkui-pointerstyle-t.md) | 是 |

## setCustomCursor

```TypeScript
setCustomCursor(value: image.PixelMap, focusX?: number, focusY?: number): void
```

设置自定义鼠标光标样式。

> **说明：**&gt;
> 该接口调用后不会立即生效，而是在下一帧改变鼠标光标样式。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | image.PixelMap | 是 |
| [focusX](../../apis-input-kit/arkts-apis/arkts-input-pointer-customcursor-i.md) | number | 否 |
| [focusY](../../apis-input-kit/arkts-apis/arkts-input-pointer-customcursor-i.md) | number | 否 |
