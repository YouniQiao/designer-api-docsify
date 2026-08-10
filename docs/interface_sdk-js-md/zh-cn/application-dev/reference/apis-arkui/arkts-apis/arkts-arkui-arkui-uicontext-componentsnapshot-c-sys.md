# ComponentSnapshot

class ComponentSnapshot

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare class ComponentSnapshot--><!--Device-unnamed-export declare class ComponentSnapshot-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from 'kits/@kit.ArkUI';
```

## getWithRange

```TypeScript
getWithRange(start: NodeIdentity, end: NodeIdentity, isStartRect: boolean,
    options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap> | null
```

通过组件范围获取组件截图。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ComponentSnapshot-getWithRange(start: NodeIdentity, end: NodeIdentity, isStartRect: boolean,    options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap> | null--><!--Device-ComponentSnapshot-getWithRange(start: NodeIdentity, end: NodeIdentity, isStartRect: boolean,    options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap> | null-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | [NodeIdentity](arkts-arkui-nodeidentity-t.md) | 是 | the start component ID, set by developer through .id attribute or the unique ID get from FrameNode. |
| end | [NodeIdentity](arkts-arkui-nodeidentity-t.md) | 是 | the end component ID, set by developer through.id attribute or the unique ID get from FrameNode. |
| isStartRect | boolean | 是 | indicating the snapshot rect to use, true for using the rect of the start component, false for using the rect of the end component. |
| options | componentSnapshot.SnapshotOptions | 否 | Define the snapshot options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;image.PixelMap&gt; | A Promise with the snapshot in PixelMap format. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 100001 | Invalid ID detected. |
| 160003 | Unsupported color space or dynamic range mode in snapshot options. |
| 202 | The caller is not a system application. |

