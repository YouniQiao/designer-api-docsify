# OverlayManager

提供绘制浮层的能力。  
> **说明：**
> 
> - 本Class首批接口从API version 12开始支持。
> - 以下API需先使用UIContext中的[getOverlayManager()](arkts-arkui-arkui-uicontext-uicontext-c.md#getoverlaymanager)方法获取到
> OverlayManager对象，再通过该对象调用对应方法。
> 
> - OverlayManager上节点的层级在Page页面层级之上，在Dialog、Popup、Menu、BindSheet、BindContentCover和Toast等之下。
> 
> - OverlayManager上节点安全区域内外的绘制方式与Page一致，键盘避让方式与Page一致。
> 
> - 与OverlayManager相关的属性推荐采用AppStorage来进行应用全局存储，以免切换页面后属性值发生变化从而导致业务错误。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class OverlayManager--><!--Device-unnamed-export declare class OverlayManager-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from 'kits/@kit.ArkUI';
```

## addComponentContent

```TypeScript
addComponentContent<T>(content: ComponentContent<T>, index?: int): void
```

在OverlayManager上新增指定节点。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OverlayManager-addComponentContent<T>(content: ComponentContent<T>, index?: int): void--><!--Device-OverlayManager-addComponentContent<T>(content: ComponentContent<T>, index?: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | [ComponentContent](../arkts-components/arkts-arkui-componentcontent-t.md)&lt;T&gt; | Yes | 在OverlayManager的指定节点上添加此content。 &lt;br&gt;**说明：** &lt;br/&gt; 新增的节点默认处于页面居中，按层级堆叠。 |
| index | int | No |  |

## addComponentContentWithOrder

```TypeScript
addComponentContentWithOrder<T>(content: ComponentContent<T>, levelOrder?: LevelOrder): void
```

创建浮层节点时，指定显示顺序。支持在浮层节点创建时指定显示的顺序。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OverlayManager-addComponentContentWithOrder<T>(content: ComponentContent<T>, levelOrder?: LevelOrder): void--><!--Device-OverlayManager-addComponentContentWithOrder<T>(content: ComponentContent<T>, levelOrder?: LevelOrder): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | [ComponentContent](../arkts-components/arkts-arkui-componentcontent-t.md)&lt;T&gt; | Yes | 在OverlayManager的指定节点上添加此content。 &lt;br&gt;**说明：** &lt;br/&gt; 新增的节点默认处于页面居中位置，按层级堆叠。 |
| levelOrder | [LevelOrder](arkts-arkui-promptaction-levelorder-c.md) | No |  |

## hideAllComponentContents

```TypeScript
hideAllComponentContents(): void
```

隐藏OverlayManager上的所有ComponentContent。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OverlayManager-hideAllComponentContents(): void--><!--Device-OverlayManager-hideAllComponentContents(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hideComponentContent

```TypeScript
hideComponentContent<T>(content: ComponentContent<T>): void
```

隐藏OverlayManager上的指定节点。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OverlayManager-hideComponentContent<T>(content: ComponentContent<T>): void--><!--Device-OverlayManager-hideComponentContent<T>(content: ComponentContent<T>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | [ComponentContent](../arkts-components/arkts-arkui-componentcontent-t.md)&lt;T&gt; | Yes | 在OverlayManager上隐藏此content。 |

## openOrderOverlay

```TypeScript
openOrderOverlay(content: ComponentContent<Object>, options?: OrderOverlayOptions): Promise<void>
```

打开具有指定ComponentContent和选项的浮层。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OverlayManager-openOrderOverlay(content: ComponentContent<Object>, options?: OrderOverlayOptions): Promise<void>--><!--Device-OverlayManager-openOrderOverlay(content: ComponentContent<Object>, options?: OrderOverlayOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | [ComponentContent](../arkts-components/arkts-arkui-componentcontent-t.md)&lt;Object&gt; | Yes | 该内容将被添加到OverlayManager中。 |
| options | [OrderOverlayOptions](arkts-arkui-arkui-uicontext-orderoverlayoptions-i.md) | No | Options for the overlay. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 103307 | The overlay cannot be opened due to the system pop-up window. |

## removeComponentContent

```TypeScript
removeComponentContent<T>(content: ComponentContent<T>): void
```

删除overlay上的指定节点。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OverlayManager-removeComponentContent<T>(content: ComponentContent<T>): void--><!--Device-OverlayManager-removeComponentContent<T>(content: ComponentContent<T>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | [ComponentContent](../arkts-components/arkts-arkui-componentcontent-t.md)&lt;T&gt; | Yes | 在OverlayManager上删除此content。 |

## showAllComponentContents

```TypeScript
showAllComponentContents(): void
```

显示OverlayManager上所有的ComponentContent。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OverlayManager-showAllComponentContents(): void--><!--Device-OverlayManager-showAllComponentContents(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showComponentContent

```TypeScript
showComponentContent<T>(content: ComponentContent<T>): void
```

在OverlayManager上显示指定节点。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OverlayManager-showComponentContent<T>(content: ComponentContent<T>): void--><!--Device-OverlayManager-showComponentContent<T>(content: ComponentContent<T>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | [ComponentContent](../arkts-components/arkts-arkui-componentcontent-t.md)&lt;T&gt; | Yes | 在OverlayManager上显示此content。 |

