# OverlayManager

```TypeScript
export class OverlayManager
```

提供绘制浮层的能力。

> **说明：** 
> 
> - 该类的初始API从API version 12开始支持。
> 
> - 在以下API示例中，必须先在**UIContext**中使用[getOverlayManager()](arkts-arkui-arkui-uicontext-uicontext-c.md#getoverlaymanager)获取**OverlayManager**实例，然后使用该实例调用API。
> 
> - **OverlayManager**上的节点位于页面层级之上，但在**Dialog**、**Popup**、**Menu**、**BindSheet**、**BindContentCover**和**Toast**等组件之下。
> 
> - **OverlayManager**上节点在安全区内外的绘制方式与页面一致，键盘避让方式也与页面相同。
> 
> - 对于与**OverlayManager**相关的属性，建议使用AppStorage在应用内进行全局存储，以避免切换页面时属性值发生变化导致业务错误。

**起始版本：** 12

<!--Device-unnamed-export class OverlayManager--><!--Device-unnamed-export class OverlayManager-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { AtomicServiceBar, ComponentUtils, ContextMenuController, CursorController, DialogPresenter, DragController, Font, KeyboardAvoidMode, MediaQuery, OverlayManager, PromptAction, Router, UIContext, UIInspector, UIObserver, PageInfo, SwiperDynamicSyncScene, SwiperDynamicSyncSceneType, MarqueeDynamicSyncScene, MarqueeDynamicSyncSceneType, MeasureUtils, FrameCallback, OverlayManagerOptions, TargetInfo, TextMenuController, NodeIdentity, NodeRenderState, NodeRenderStateChangeCallback, Magnifier, ResolvedUIContext, TextSelectionClearPolicy, CustomKeyboardContinueFeature, BackgroundLuminanceSamplingConfigs, LuminanceSampler } from '@kit.ArkUI';
import { GestureListenerType, GestureActionPhase, GestureTriggerInfo, GestureObserverConfigs, GestureListenerCallback } from '@kit.ArkUI';
import { SwiperContentInfo, SwiperItemInfo } from '@kit.ArkUI';
import { BackPressActionProposal, BaseGestureHandlingProposal, ClickActionProposal, GestureHandlingResolution, NoneActionProposal, PageSwitchActionProposal, ScrollActionProposal, SelectActionProposal, SmartGestureController, TargetedGestureProposal } from '@kit.ArkUI';
```

## addComponentContent

```TypeScript
addComponentContent(content: ComponentContent, index?: number): void
```

向OverlayManager添加指定的ComponentContent节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-OverlayManager-addComponentContent(content: ComponentContent, index?: number): void--><!--Device-OverlayManager-addComponentContent(content: ComponentContent, index?: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent](arkts-arkui-componentcontent-c.md) | 是 | 添加到**OverlayManager**目标节点上的内容。<br> **注意**<br>默认情况下，新节点在页面中居中，并根据其堆叠级别进行堆叠。 |
| index | number | 否 |  |

**示例**

```TypeScript
import { ComponentContent, OverlayManager } from '@kit.ArkUI';

class Params {
  text: string = '';
  offset: Position;

  constructor(text: string, offset: Position) {
    this.text = text;
    this.offset = offset;
  }
}

@Builder
function builderText(params: Params) {
  Column() {
    Text(params.text)
      .fontSize(30)
      .fontWeight(FontWeight.Bold)
  }.offset(params.offset)
}

@Entry
@Component
struct OverlayExample {
  @State message: string = 'ComponentContent';
  private uiContext: UIContext = this.getUIContext();
  private overlayNode: OverlayManager = this.uiContext.getOverlayManager();
  @StorageLink('contentArray') contentArray: ComponentContent<Params>[] = [];
  @StorageLink('componentContentIndex') componentContentIndex: number = 0;
  @StorageLink('arrayIndex') arrayIndex: number = 0;
  @StorageLink('componentOffset') componentOffset: Position = { x: 0, y: 110 };

  build() {
    Column({ space: 5 }) {
      Button('++componentContentIndex: ' + this.componentContentIndex).onClick(() => {
        ++this.componentContentIndex;
      })
      Button('--componentContentIndex: ' + this.componentContentIndex).onClick(() => {
        --this.componentContentIndex;
      })
      Button('增加ComponentContent' + this.contentArray.length).onClick(() => {
        let componentContent = new ComponentContent(
          this.uiContext, wrapBuilder<[Params]>(builderText),
          new Params(this.message + (this.contentArray.length), this.componentOffset)
        );
        this.contentArray.push(componentContent);
        this.overlayNode.addComponentContent(componentContent, this.componentContentIndex);
      })
      Button('++arrayIndex: ' + this.arrayIndex).onClick(() => {
        ++this.arrayIndex;
      })
      Button('--arrayIndex: ' + this.arrayIndex).onClick(() => {
        --this.arrayIndex;
      })
      Button('删除ComponentContent' + this.arrayIndex).onClick(() => {
        if (this.arrayIndex >= 0 && this.arrayIndex < this.contentArray.length) {
          let componentContent = this.contentArray.splice(this.arrayIndex, 1);
          this.overlayNode.removeComponentContent(componentContent.pop());
        } else {
          console.info('arrayIndex有误');
        }
      })
      Button('显示ComponentContent' + this.arrayIndex).onClick(() => {
        if (this.arrayIndex >= 0 && this.arrayIndex < this.contentArray.length) {
          let componentContent = this.contentArray[this.arrayIndex];
          this.overlayNode.showComponentContent(componentContent);
        } else {
          console.info('arrayIndex有误');
        }
      })
      Button('隐藏ComponentContent' + this.arrayIndex).onClick(() => {
        if (this.arrayIndex >= 0 && this.arrayIndex < this.contentArray.length) {
          let componentContent = this.contentArray[this.arrayIndex];
          this.overlayNode.hideComponentContent(componentContent);
        } else {
          console.info('arrayIndex有误');
        }
      })
      Button('显示所有ComponentContent').onClick(() => {
        this.overlayNode.showAllComponentContents();
      })
      Button('隐藏所有ComponentContent').onClick(() => {
        this.overlayNode.hideAllComponentContents();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

## addComponentContentWithOrder

```TypeScript
addComponentContentWithOrder(content: ComponentContent, levelOrder?: LevelOrder): void
```

创建具有指定显示顺序的浮层节点。该接口允许在创建节点时定义节点的堆叠顺序。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务中使用。

<!--Device-OverlayManager-addComponentContentWithOrder(content: ComponentContent, levelOrder?: LevelOrder): void--><!--Device-OverlayManager-addComponentContentWithOrder(content: ComponentContent, levelOrder?: LevelOrder): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent](arkts-arkui-componentcontent-c.md) | 是 | 添加到**OverlayManager**目标节点上的内容。<br>**注意**<br>默认情况下，新节点在页面中居中，并根据其堆叠级别进行堆叠。 |
| levelOrder | [LevelOrder](arkts-arkui-promptaction-levelorder-c.md) | 否 |  |

**示例**

本示例展示如何调用addComponentContentWithOrder接口创建浮层节点并指定显示顺序。

```TypeScript
import { ComponentContent, PromptAction, LevelOrder, UIContext, OverlayManager } from '@kit.ArkUI';

class Params {
  text: string = '';
  offset: Position;
  constructor(text: string, offset: Position) {
    this.text = text;
    this.offset = offset;
  }
}
@Builder
function builderText(params: Params) {
  Column() {
    Text(params.text)
      .fontSize(30)
      .fontWeight(FontWeight.Bold)
  }.offset(params.offset)
}

@Entry
@Component
struct Index {
  @State message: string = '弹窗';
  private ctx: UIContext = this.getUIContext();
  private promptAction: PromptAction = this.ctx.getPromptAction();
  private overlayNode: OverlayManager = this.ctx.getOverlayManager();
  @StorageLink('contentArray') contentArray: ComponentContent<Params>[] = [];
  @StorageLink('componentContentIndex') componentContentIndex: number = 0;
  @StorageLink('arrayIndex') arrayIndex: number = 0;
  @StorageLink('componentOffset') componentOffset: Position = { x: 0, y: 80 };

  build() {
    Row() {
      Column({ space: 10 }) {
        Button('OverlayManager下面弹窗')
          .fontSize(20)
          .onClick(() => {
            let componentContent = new ComponentContent(
              this.ctx, wrapBuilder<[Params]>(builderText),
              new Params(this.message + (this.contentArray.length), this.componentOffset)
            );
            this.contentArray.push(componentContent);
            this.overlayNode.addComponentContentWithOrder(componentContent, LevelOrder.clamp(100.1));
            let topOrder: LevelOrder = this.promptAction.getTopOrder();
            if (topOrder !== undefined) {
              console.info('topOrder: ' + topOrder.getOrder());
            }
            let bottomOrder: LevelOrder = this.promptAction.getBottomOrder();
            if (bottomOrder !== undefined) {
              console.info('bottomOrder: ' + bottomOrder.getOrder());
            }
          })
        Button('OverlayManager上面弹窗')
          .fontSize(20)
          .onClick(() => {
            let componentContent = new ComponentContent(
              this.ctx, wrapBuilder<[Params]>(builderText),
              new Params(this.message + (this.contentArray.length), this.componentOffset)
            );
            this.contentArray.push(componentContent);
            this.overlayNode.addComponentContentWithOrder(componentContent, LevelOrder.clamp(100.2));
            let topOrder: LevelOrder = this.promptAction.getTopOrder();
            if (topOrder !== undefined) {
              console.info('topOrder: ' + topOrder.getOrder());
            }
            let bottomOrder: LevelOrder = this.promptAction.getBottomOrder();
            if (bottomOrder !== undefined) {
              console.info('bottomOrder: ' + bottomOrder.getOrder());
            }
          })
      }.width('100%')
    }.height('100%')
  }
}
```

## hideAllComponentContents

```TypeScript
hideAllComponentContents(): void
```

隐藏OverlayManager上的所有ComponentContent。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-OverlayManager-hideAllComponentContents(): void--><!--Device-OverlayManager-hideAllComponentContents(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例**

请参考[addComponentContent](#addcomponentcontent)示例。

## hideComponentContent

```TypeScript
hideComponentContent(content: ComponentContent): void
```

隐藏ComponentContent。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-OverlayManager-hideComponentContent(content: ComponentContent): void--><!--Device-OverlayManager-hideComponentContent(content: ComponentContent): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent](arkts-arkui-componentcontent-c.md) | 是 | 要在**OverlayManager**上隐藏的内容。 |

**示例**

请参考[addComponentContent](#addcomponentcontent)示例。

## openOrderOverlay

```TypeScript
openOrderOverlay(content: ComponentContent, options?: OrderOverlayOptions): Promise<void>
```

打开具有指定ComponentContent和选项的浮层。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务中使用。

<!--Device-OverlayManager-openOrderOverlay(content: ComponentContent, options?: OrderOverlayOptions): Promise<void>--><!--Device-OverlayManager-openOrderOverlay(content: ComponentContent, options?: OrderOverlayOptions): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent](arkts-arkui-componentcontent-c.md) | 是 | OverlayManager新增节点需要添加的内容。<p><strong>注意</strong>：。<br>默认情况下，新节点在页面中居中，并根据其堆叠级别进行堆叠。</p> |
| options | [OrderOverlayOptions](arkts-arkui-arkui-uicontext-orderoverlayoptions-i.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 函数返回的promise。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [103307](../errorcode-promptAction.md#103307-系统弹出窗口导致无法打开浮层) | The overlay cannot be opened due to the system pop-up window. |

**示例**

```TypeScript
import { ComponentContent, OverlayManager, LevelOrder, LevelMode } from '@kit.ArkUI';

class Params {
  text: string = '';
  offset: Position;

  constructor(text: string, offset: Position) {
    this.text = text;
    this.offset = offset;
  }
}

@Builder
function builderText(params: Params) {
  Column() {
    Text(params.text)
      .fontSize(30)
      .fontWeight(FontWeight.Bold)
  }.offset(params.offset)
}

@Entry
@Component
struct OverlayExample {
  @State message: string = 'ComponentContent';
  private uiContext: UIContext = this.getUIContext();
  private overlayNode: OverlayManager = this.uiContext.getOverlayManager();
  @StorageLink('contentArray') contentArray: ComponentContent<Params>[] = [];

  build() {
    Column({ space: 5 }) {
      Button('openOrderOverlay').onClick(() => {
        let componentContent = new ComponentContent(
          this.uiContext, wrapBuilder<[Params]>(builderText),
          new Params(this.message, { x: 0, y: 110 })
        );
        this.contentArray.push(componentContent);
        this.overlayNode.openOrderOverlay(componentContent, {
          levelOrder: LevelOrder.clamp(100),
          levelMode: LevelMode.OVERLAY
        });
      })
      Button('close overlay').onClick(() => {
        if (this.contentArray.length > 0) {
          this.overlayNode.removeComponentContent(this.contentArray.pop());
        } else {
          console.info('arrayIndex有误');
        }
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

## removeComponentContent

```TypeScript
removeComponentContent(content: ComponentContent): void
```

从OverlayManager移除指定的ComponentContent节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-OverlayManager-removeComponentContent(content: ComponentContent): void--><!--Device-OverlayManager-removeComponentContent(content: ComponentContent): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent](arkts-arkui-componentcontent-c.md) | 是 | 要从**OverlayManager**中移除的内容。 |

**示例**

请参考[addComponentContent](#addcomponentcontent)示例。

## showAllComponentContents

```TypeScript
showAllComponentContents(): void
```

显示OverlayManager上的所有ComponentContent。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-OverlayManager-showAllComponentContents(): void--><!--Device-OverlayManager-showAllComponentContents(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例**

请参考[addComponentContent](#addcomponentcontent)示例。

## showComponentContent

```TypeScript
showComponentContent(content: ComponentContent): void
```

显示ComponentContent。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-OverlayManager-showComponentContent(content: ComponentContent): void--><!--Device-OverlayManager-showComponentContent(content: ComponentContent): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent](arkts-arkui-componentcontent-c.md) | 是 | 要在**OverlayManager**上显示的内容。 |

**示例**

请参考[addComponentContent](#addcomponentcontent)示例。
