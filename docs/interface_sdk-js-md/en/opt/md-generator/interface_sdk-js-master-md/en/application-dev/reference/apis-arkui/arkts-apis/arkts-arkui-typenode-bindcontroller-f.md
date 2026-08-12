# bindController

## bindController

```TypeScript
export function bindController(node: FrameNode, controller: TextController, nodeType: 'Text'): void
```

Binds a [TextController](../arkts-components/arkts-arkui-textcontroller-c.md#TextController) instance to a [Text](arkts-arkui-typenode-text-t.md#Text) node. Cross-language access must be enabled for nodes not created via ArkTS; otherwise, an exception will be thrown. This API does not support declaratively created nodes.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function bindController(node: FrameNode, controller: TextController, nodeType: 'Text'): void--><!--Device-typeNode-export function bindController(node: FrameNode, controller: TextController, nodeType: 'Text'): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes |
| controller | [TextController](../arkts-components/arkts-arkui-textcontroller-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Text' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100021](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-node.md#100021-framenode-not-modifiable) |
| [100023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-node.md#100023-parameter-error) |

## Examples

```TypeScript
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  // Configure the TextController instance, which can be obtained from an external source.
  controller: TextController = new TextController()

  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 });
    node.appendChild(col);
    // Create a Text node.
    let text = typeNode.createNode(uiContext, 'Text');
    text.initialize('Hello').fontColor(Color.Blue).fontSize(14);
    typeNode.getAttribute(text, 'Text')?.fontWeight(FontWeight.Bold)
    // Bind a TextController instance.
    typeNode.bindController(text, this.controller, 'Text');
    col.appendChild(text);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  @State line: number = 0
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('Text bindController Sample')
      NodeContainer(this.myNodeController)
      Text(`Current line count: ${this.line}`)
      Button(`Obtain Line Count`)
        .onClick(() => {
          this.line = this.myNodeController.controller.getLayoutManager().getLineCount()
        })
    }
  }
}
```


## bindController

```TypeScript
export function bindController(node: FrameNode, controller: SwiperController, nodeType: 'Swiper'): void
```

Binds a [SwiperController](../arkts-components/arkts-arkui-swipercontroller-c.md#SwiperController) instance to the [Swiper](arkts-arkui-typenode-swiper-t.md#Swiper) node. Cross-language access must be enabled for nodes not created via ArkTS; otherwise, an exception will be thrown. This API does not support declaratively created nodes.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function bindController(node: FrameNode, controller: SwiperController, nodeType: 'Swiper'): void--><!--Device-typeNode-export function bindController(node: FrameNode, controller: SwiperController, nodeType: 'Swiper'): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes |
| controller | [SwiperController](../arkts-components/arkts-arkui-swipercontroller-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Swiper' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100021](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-node.md#100021-framenode-not-modifiable) |
| [100023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-node.md#100023-parameter-error) |

## Examples

See the example for [createNode('Swiper')12+](#createnodeswiper12).


## bindController

```TypeScript
function bindController(node: FrameNode, controller: Scroller, nodeType: 'Scroll'): void
```

Binds the [Scroller](../arkts-components/arkts-arkui-scroller-c.md#Scroller) to the [Scroll](arkts-arkui-typenode-scroll-t.md#Scroll) node. Cross-language access must be enabled for nodes not created via ArkTS; otherwise, an exception will be thrown. This API supports declaratively created nodes since API version 26.0.0.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-typeNode-function bindController(node: FrameNode, controller: Scroller, nodeType: 'Scroll'): void--><!--Device-typeNode-function bindController(node: FrameNode, controller: Scroller, nodeType: 'Scroll'): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes |
| controller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Scroll' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [100021](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-node.md#100021-framenode-not-modifiable) |

## Examples

```TypeScript
typeNode.bindController(node, scroller, 'Scroll');
```


## bindController

```TypeScript
export function bindController(node: FrameNode, controller: Scroller, nodeType: 'List'): void
```

Binds a [Scroller](../arkts-components/arkts-arkui-scroller-c.md#Scroller) instance to the [List](arkts-arkui-typenode-list-t.md#List) node. Cross-language access must be enabled for nodes not created via ArkTS; otherwise, an exception will be thrown. This API supports declaratively created nodes since API version 26.0.0.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function bindController(node: FrameNode, controller: Scroller, nodeType: 'List'): void--><!--Device-typeNode-export function bindController(node: FrameNode, controller: Scroller, nodeType: 'List'): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes |
| controller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'List' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100021](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-node.md#100021-framenode-not-modifiable) |
| [100023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-node.md#100023-parameter-error) |

## Examples

```TypeScript
typeNode.bindController(node, scroller, 'List');
```


## bindController

```TypeScript
export function bindController(node: FrameNode, controller: TextInputController, nodeType: 'TextInput'): void
```

Binds the [TextInputController](../arkts-components/arkts-arkui-textinputcontroller-c.md#TextInputController) to the [TextInput](arkts-arkui-typenode-textinput-t.md#TextInput) node. Cross  
-language access must be enabled for nodes not created via ArkTS; otherwise, an exception will be thrown. This API  
supports declaratively created nodes since API version 26.0.0.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function bindController(node: FrameNode, controller: TextInputController, nodeType: 'TextInput'): void--><!--Device-typeNode-export function bindController(node: FrameNode, controller: TextInputController, nodeType: 'TextInput'): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes |
| controller | [TextInputController](../arkts-components/arkts-arkui-textinputcontroller-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'TextInput' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100021](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-node.md#100021-framenode-not-modifiable) |
| [100023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-node.md#100023-parameter-error) |

## Examples

```TypeScript
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 });
    node.appendChild(col);
    // Create and initialize TextInput. By default, the focus is obtained.
    let textInput = typeNode.createNode(uiContext, 'TextInput');
    textInput.initialize({ text: 'TextInput' })
      .defaultFocus(true)
    col.appendChild(textInput);
    // Bind TextInputController and set the cursor position.
    let controller: TextInputController = new TextInputController();
    typeNode.bindController(textInput, controller, 'TextInput');
    controller.caretPosition(3);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('TextInput bindController sample');
      NodeContainer(this.myNodeController);
    }
  }
}
```


## bindController

```TypeScript
export function bindController(node: FrameNode, controller: Scroller, nodeType: 'WaterFlow'): void
```

Binds a [Scroller](../arkts-components/arkts-arkui-scroller-c.md#Scroller) instance to the [WaterFlow](arkts-arkui-typenode-waterflow-t.md#WaterFlow) node. Cross-language access must be enabled for nodes not created via ArkTS; otherwise, an exception will be thrown. This API supports declaratively created nodes since API version 26.0.0.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function bindController(node: FrameNode, controller: Scroller, nodeType: 'WaterFlow'): void--><!--Device-typeNode-export function bindController(node: FrameNode, controller: Scroller, nodeType: 'WaterFlow'): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes |
| controller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'WaterFlow' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100021](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-node.md#100021-framenode-not-modifiable) |
| [100023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-node.md#100023-parameter-error) |

## Examples

```TypeScript
typeNode.bindController(node, scroller, 'WaterFlow');
```


## bindController

```TypeScript
export function bindController(node: FrameNode, controller: TextAreaController, nodeType: 'TextArea'): void
```

Binds a [TextAreaController](../arkts-components/arkts-arkui-textareacontroller-c.md#TextAreaController) instance to the [TextArea](arkts-arkui-typenode-textarea-t.md#TextArea) node.Cross-language access must be enabled for nodes not created via ArkTS; otherwise, an exception will be thrown. This API supports declaratively created nodes since API version 26.0.0.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function bindController(node: FrameNode, controller: TextAreaController, nodeType: 'TextArea'): void--><!--Device-typeNode-export function bindController(node: FrameNode, controller: TextAreaController, nodeType: 'TextArea'): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes |
| controller | [TextAreaController](../arkts-components/arkts-arkui-textareacontroller-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'TextArea' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100021](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-node.md#100021-framenode-not-modifiable) |
| [100023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-node.md#100023-parameter-error) |

## Examples

```TypeScript
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 });
    node.appendChild(col);
    // Create and initialize a TextArea node. By default, the node is focused.
    let textArea = typeNode.createNode(uiContext, 'TextArea');
    textArea.initialize({ text: 'TextArea' })
      .defaultFocus(true)
    col.appendChild(textArea);
    // Bind a TextAreaController instance and set the cursor position.
    let controller: TextAreaController = new TextAreaController()
    typeNode.bindController(textArea, controller, 'TextArea');
    controller.caretPosition(3);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('TextArea bindController sample');
      NodeContainer(this.myNodeController);
    }
  }
}
```


## bindController

```TypeScript
export function bindController(node: FrameNode, controller: Scroller, nodeType: 'Grid'): void
```

Binds a [Scroller](../arkts-components/arkts-arkui-scroller-c.md#Scroller) instance to the [Grid](arkts-arkui-typenode-grid-t.md#Grid) node. Cross-language access must be enabled for nodes not created via ArkTS; otherwise, an exception will be thrown. This API supports declaratively created nodes since API version 26.0.0.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function bindController(node: FrameNode, controller: Scroller, nodeType: 'Grid'): void--><!--Device-typeNode-export function bindController(node: FrameNode, controller: Scroller, nodeType: 'Grid'): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes |
| controller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Grid' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100021](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-node.md#100021-framenode-not-modifiable) |
| [100023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-node.md#100023-parameter-error) |

## Examples

```TypeScript
typeNode.bindController(node, scroller, 'Grid');
```
