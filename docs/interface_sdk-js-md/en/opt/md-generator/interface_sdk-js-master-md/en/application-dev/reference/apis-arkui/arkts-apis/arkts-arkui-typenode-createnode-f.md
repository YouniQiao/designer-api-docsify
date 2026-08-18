# createNode

## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Text'): Text
```

Creates a FrameNode of the **Text** type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Text'): Text--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Text'): Text-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Text' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Text](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-text-c.md) |

**Examples**

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
    // Create a Text node.
    let text = typeNode.createNode(uiContext, 'Text');
    text.initialize('Hello').fontColor(Color.Blue).fontSize(14);
    typeNode.getAttribute(text, 'Text')?.fontWeight(FontWeight.Bold);
    col.appendChild(text);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('Text sample');
      NodeContainer(this.myNodeController);
    }
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Column'): Column
```

Creates a FrameNode of the **Column** type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Column'): Column--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Column'): Column-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Column' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Column](arkts-arkui-typenode-column-t.md) |

**Examples**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom Column controller by extending NodeController.
class MyColumnController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute
    // Create a Column node.
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('50%')
      .height('50%')
      .backgroundColor(Color.Gray)
    node.appendChild(col)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myColumnController: MyColumnController = new MyColumnController();

  build() {
    Column({ space: 5 }) {
      Text('ColumnSample')
      NodeContainer(this.myColumnController);
    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Row'): Row
```

Creates a FrameNode of the Row type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Row'): Row--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Row'): Row-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Row' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Row](../../apis-na/arkts-apis/arkts-na-typenode-row-t.md) |

**Examples**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom Row controller by extending NodeController.
class MyRowController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    // Create a row.
    let row = typeNode.createNode(uiContext, 'Row')
    row.initialize({ space: 5 })
      .width('50%')
      .height('50%')
      .backgroundColor(Color.Gray)
    node.appendChild(row)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myRowController: MyRowController = new MyRowController();

  build() {
    Column({ space: 5 }) {
      Text('RowSample')
      NodeContainer(this.myRowController);
    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Stack'): Stack
```

Creates a FrameNode of the **Stack** type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Stack'): Stack--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Stack'): Stack-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Stack' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Stack](../../apis-na/arkts-apis/arkts-na-typenode-stack-t.md) |

**Examples**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom Stack controller by extending NodeController.
class MyStackController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    // Create a Stack node.
    let stack = typeNode.createNode(uiContext, 'Stack')
    stack.initialize({ alignContent: Alignment.Top })
      .width('50%')
      .height('50%')
      .backgroundColor(Color.Gray)
    node.appendChild(stack)
    let text = typeNode.createNode(uiContext, 'Text')
    text.initialize('This is Text')
    // Add a Text node to the Stack node.
    stack.appendChild(text)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myStackController: MyStackController = new MyStackController();

  build() {
    Column({ space: 5 }) {
      Text('StackSample')
      NodeContainer(this.myStackController);
    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'GridRow'): GridRow
```

Creates a FrameNode of the **GridRow** type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'GridRow'): GridRow--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'GridRow'): GridRow-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'GridRow' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [GridRow](../../apis-na/arkts-apis/arkts-na-typenode-gridrow-t.md) |

**Examples**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom GridRow controller by extending NodeController.
class MyGridRowController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    // Create a GridRow.
    let gridRow = typeNode.createNode(uiContext, 'GridRow')
    gridRow.initialize({ columns: 12 })
      .width('50%')
      .height('50%')
      .backgroundColor(Color.Gray)
    node.appendChild(gridRow)
    // Create a GridCol node.
    let gridCol = typeNode.createNode(uiContext, 'GridCol')
    gridCol.initialize({ span: 2, offset: 4 })
      .height('100%')
      .backgroundColor(Color.Red)
    // Add gridCol to gridRow.
    gridRow.appendChild(gridCol)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myGridRowController: MyGridRowController = new MyGridRowController();

  build() {
    Column({ space: 5 }) {
      Text('GridRowSample')
      NodeContainer(this.myGridRowController);
    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'GridCol'): GridCol
```

Creates a FrameNode of the **GridCol** type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'GridCol'): GridCol--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'GridCol'): GridCol-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'GridCol' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [GridCol](../../apis-na/arkts-apis/arkts-na-typenode-gridcol-t.md) |

**Examples**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom GridRow controller by extending NodeController.
class MyGridRowController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    // Create a GridRow.
    let gridRow = typeNode.createNode(uiContext, 'GridRow')
    gridRow.initialize({ columns: 12 })
      .width('50%')
      .height('50%')
      .backgroundColor(Color.Gray)
    node.appendChild(gridRow)
    // Create a GridCol node.
    let gridCol = typeNode.createNode(uiContext, 'GridCol')
    gridCol.initialize({ span: 2, offset: 4 })
      .height('100%')
      .backgroundColor(Color.Red)
    // Add gridCol to gridRow.
    gridRow.appendChild(gridCol)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myGridRowController: MyGridRowController = new MyGridRowController();

  build() {
    Column({ space: 5 }) {
      Text('GridColSample')
      NodeContainer(this.myGridRowController);
    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Flex'): Flex
```

Creates a FrameNode of the Flex type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Flex'): Flex--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Flex'): Flex-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Flex' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Flex](../../apis-na/arkts-apis/arkts-na-typenode-flex-t.md) |

**Examples**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom Flex controller by extending NodeController.
class MyFlexController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    // Create a Flex.
    let flex = typeNode.createNode(uiContext, 'Flex')
    flex.initialize()
      .width('50%')
      .height('50%')
      .backgroundColor(Color.Gray)
    node.appendChild(flex)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myFlexController: MyFlexController = new MyFlexController();

  build() {
    Column({ space: 5 }) {
      Text('FlexSample')
      NodeContainer(this.myFlexController);
    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Swiper'): Swiper
```

Creates a FrameNode of the **Swiper** type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Swiper'): Swiper--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Swiper'): Swiper-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Swiper' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Swiper](arkts-arkui-typenode-swiper-t.md) |

**Examples**

```TypeScript
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// Implement a custom Swiper controller by extending NodeController.
class MySwiperController extends NodeController {
  swiperController: SwiperController = new SwiperController()

  makeNode(uiContext: UIContext): FrameNode | null {
    // Create a Swiper node.
    let swiperNode = typeNode.createNode(uiContext, 'Swiper')

    // Create a Text node.
    let text0 = typeNode.createNode(uiContext, 'Text')
    text0.initialize('0')
      .width('100%')
      .height('100%')
      .textAlign(TextAlign.Center)
    // Add text0 to the Swiper.
    swiperNode.appendChild(text0)
    // Create another Text node for switching.
    let text1 = typeNode.createNode(uiContext, 'Text')
    text1.initialize('1')
      .width('100%')
      .height('100%')
      .textAlign(TextAlign.Center)
    // Add text1 to the swiper.
    swiperNode.appendChild(text1)
    swiperNode.commonAttribute.width('100%')
      .height('20%')
      .backgroundColor(0xAFEEEE)
    // Bind the swiper to the controller.
    typeNode.bindController(swiperNode, this.swiperController, 'Swiper')
    typeNode.getAttribute(swiperNode, 'Swiper')?.loop(false)
    return swiperNode;

  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private mySwiperController: MySwiperController = new MySwiperController();

  build() {
    Column({ space: 5 }) {
      Text('SwiperSample')
      NodeContainer(this.mySwiperController);
    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Progress'): Progress
```

Creates a FrameNode of the **Progress** type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Progress'): Progress--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Progress'): Progress-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Progress' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Progress](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-progress-i.md) |

**Examples**

```TypeScript
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// Implement a custom Progress controller by extending NodeController.
class MyProgressNodeController extends NodeController {
  public uiContext: UIContext | null = null;
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.uiContext = uiContext;
    this.rootNode = new FrameNode(uiContext);
    // Create a Progress node.
    let node = typeNode.createNode(uiContext, 'Progress');
    node.initialize({
      value: 15,
      total: 200,
      type: ProgressType.ScaleRing
    }).width(100)
      .height(100)
    this!.rootNode!.appendChild(node);
    return this.rootNode;
  }
}

@Entry
@Component
struct Sample {
  build() {
    Column({ space: 10 }) {
      NodeContainer(new MyProgressNodeController()).margin(5)
    }.width('100%').height('100%')

  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Scroll'): Scroll
```

Creates a FrameNode of the **Scroll** type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Scroll'): Scroll--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Scroll'): Scroll-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Scroll' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Scroll](../../apis-na/arkts-apis/arkts-na-typenode-scroll-t.md) |

**Examples**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom Scroll controller by extending NodeController.
class MyScrollController extends NodeController {
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    // Create a Scroll node.
    let scroller: Scroller = new Scroller();
    // Create a Scroll node and set its properties.
    let scrollNode = typeNode.createNode(uiContext, 'Scroll');
    scrollNode.initialize(scroller).size({ width: '100%', height: 500 });
    typeNode.getAttribute(scrollNode, 'Scroll')?.friction(0.6);

    let colNode = typeNode.createNode(uiContext, 'Column');
    // Add a Column node to Scroll.
    scrollNode.appendChild(colNode);

    for (let i = 0; i < 10; i++) {
      let text = typeNode.createNode(uiContext, 'Text');
      text.initialize('item' + i)
        .size({ width: '90%', height: 100 })
        .textAlign(TextAlign.Center)
        .backgroundColor(0xF9CF93);
      colNode.appendChild(text);
    }

    this!.rootNode!.appendChild(scrollNode);
    return this.rootNode;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myScrollController: MyScrollController = new MyScrollController();

  build() {
    Column({ space: 5 }) {
      Text('ScrollSample')
      NodeContainer(this.myScrollController)

    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'RelativeContainer'): RelativeContainer
```

Creates a FrameNode of the **RelativeContainer** type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'RelativeContainer'): RelativeContainer--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'RelativeContainer'): RelativeContainer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'RelativeContainer' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RelativeContainer](arkts-arkui-typenode-relativecontainer-t.md) |

**Examples**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom RelativeContainer controller by extending NodeController.
class MyRelativeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    // Create a RelativeContainer node.
    let relative = typeNode.createNode(uiContext, 'RelativeContainer')
    relative.initialize()
      .width('50%')
      .height('50%')
      .backgroundColor(Color.Gray)
    node.appendChild(relative)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myRelativeController: MyRelativeController = new MyRelativeController();

  build() {
    Column({ space: 5 }) {
      Text('RelativeContainerSample')
      NodeContainer(this.myRelativeController);
    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Divider'): Divider
```

Creates a FrameNode of the **Divider** type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Divider'): Divider--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Divider'): Divider-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Divider' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Divider](../../apis-na/arkts-apis/arkts-na-typenode-divider-t.md) |

**Examples**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom Divider controller by extending NodeController.
class MyDividerController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // Create a Divider node.
    let divider = typeNode.createNode(uiContext, 'Divider')
    divider.initialize()
      .strokeWidth(1)
    // Add the Divider node to col.
    col.appendChild(divider)

    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myDividerController: MyDividerController = new MyDividerController();

  build() {
    Column({ space: 5 }) {
      Text('DividerSample')
      NodeContainer(this.myDividerController);

    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'LoadingProgress'): LoadingProgress
```

Creates a FrameNode of the **LoadingProgress** type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'LoadingProgress'): LoadingProgress--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'LoadingProgress'): LoadingProgress-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'LoadingProgress' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [LoadingProgress](arkts-arkui-typenode-loadingprogress-t.md) |

**Examples**

```TypeScript
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// Implement a custom LoadingProgress controller by extending NodeController.
class MyLoadingProgressNodeController extends NodeController {
  public uiContext: UIContext | null = null;
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.uiContext = uiContext;
    this.rootNode = new FrameNode(uiContext);
    // Create LoadingProgress node.
    let node = typeNode.createNode(uiContext, 'LoadingProgress');
    node.initialize()
      .width(100)
      .height(100)
      .color(Color.Red)
      .enableLoading(true)
    this!.rootNode!.appendChild(node);
    return this.rootNode;
  }
}

@Entry
@Component
struct Sample {
  build() {
    Column({ space: 10 }) {
      NodeContainer(new MyLoadingProgressNodeController()).margin(5)
    }.width('100%').height('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Search'): Search
```

Creates a FrameNode of the **Search** type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Search'): Search--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Search'): Search-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Search' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Search](arkts-arkui-typenode-search-t.md) |

**Examples**

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
    // Create a Search node.
    let search = typeNode.createNode(uiContext, 'Search');
    search.initialize({ value: 'Search' })
      .searchButton('SEARCH')
      .textFont({ size: 14, weight: 400 })
    col.appendChild(search);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('Search sample');
      NodeContainer(this.myNodeController);
    }
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Blank'): Blank
```

Creates a FrameNode of the **Blank** type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Blank'): Blank--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Blank'): Blank-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Blank' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Blank](arkts-arkui-typenode-blank-t.md) |

**Examples**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom Blank controller by extending NodeController.
class MyBlankController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // Create a Blank node.
    let blank = typeNode.createNode(uiContext, 'Blank')
    blank.initialize()
      .width('50%')
      .height('50%')
      .backgroundColor(Color.Blue)
    col.appendChild(blank)

    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myBlankController: MyBlankController = new MyBlankController();

  build() {
    Column({ space: 5 }) {
      Text('BlankSample')
      NodeContainer(this.myBlankController);

    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Image'): Image
```

Creates a FrameNode of the **Image** type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Image'): Image--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Image'): Image-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Image' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Image](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-image-i.md) |

**Examples**

```TypeScript
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// Implement a custom Image controller by extending NodeController.
class MyImageController extends NodeController {
  public uiContext: UIContext | null = null;
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.uiContext = uiContext;
    this.rootNode = new FrameNode(uiContext);
    // Create an Image node.
    let imageNode = typeNode.createNode(uiContext, 'Image');
    imageNode
      // Replace $r('app.media.img') with the image resource file you use.
      .initialize($r('app.media.img'))
      .width(100)
      .height(100)
      .fillColor(Color.Red)
      .objectFit(ImageFit.Contain)
      .renderMode(ImageRenderMode.Template)
      .fitOriginalSize(true)
      .matchTextDirection(true)
      .objectRepeat(ImageRepeat.X)
      .autoResize(true)

    this!.rootNode!.appendChild(imageNode);
    return this.rootNode;

  }
}

@Entry
@Component
struct Sample {
  build() {
    Column({ space: 10 }) {
      NodeContainer(new MyImageController()).margin(5)
    }.width('100%').height('100%')

  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'List'): List
```

Creates a FrameNode of the **List** type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'List'): List--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'List'): List-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'List' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [List](../../apis-arkts/arkts-apis/arkts-arkts-util-list-list-c.md) |

**Examples**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom List controller by extending NodeController.
class MyListController extends NodeController {
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    // Create a List node.
    this.rootNode = new FrameNode(uiContext);
    // Create a List node.
    let listNode = typeNode.createNode(uiContext, 'List');
    listNode.initialize({ space: 3 }).size({ width: '100%', height: '100%' });
    typeNode.getAttribute(listNode, 'List')?.friction(0.6);

    // Create a ListItemGroup node in the List.
    let listItemGroupNode = typeNode.createNode(uiContext, 'ListItemGroup');
    listItemGroupNode.initialize({ space: 3 });
    listNode.appendChild(listItemGroupNode);

    // Add ListItem nodes to ListItemGroup.
    let listItemNode1 = typeNode.createNode(uiContext, 'ListItem');
    listItemNode1.initialize({ style: ListItemStyle.NONE }).height(100).borderWidth(1).backgroundColor('#FF00FF');
    let text1 = typeNode.createNode(uiContext, 'Text');
    text1.initialize('ListItem1');
    listItemNode1.appendChild(text1);
    listItemGroupNode.appendChild(listItemNode1);

    // Create a ListItem, add a Text to the ListItem, and add the ListItem to listItemGroup.
    let listItemNode2 = typeNode.createNode(uiContext, 'ListItem');
    listItemNode2.initialize({ style: ListItemStyle.CARD }).borderWidth(1).backgroundColor('#FF00FF');
    typeNode.getAttribute(listItemNode2, 'ListItem')?.height(100);
    let text2 = typeNode.createNode(uiContext, 'Text');
    text2.initialize('ListItem2');
    listItemNode2.appendChild(text2);
    listItemGroupNode.appendChild(listItemNode2);

    this!.rootNode!.appendChild(listNode);
    return this.rootNode;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myListController: MyListController = new MyListController();

  build() {
    Column({ space: 5 }) {
      Text('ListSample')
      NodeContainer(this.myListController)

    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'ListItem'): ListItem
```

Creates a FrameNode of the **ListItem** type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'ListItem'): ListItem--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'ListItem'): ListItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'ListItem' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ListItem](../../apis-na/arkts-apis/arkts-na-typenode-listitem-t.md) |

**Examples**

See the example for createNode('List').


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'TextInput'): TextInput
```

Creates a FrameNode of the **TextInput** type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'TextInput'): TextInput--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'TextInput'): TextInput-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'TextInput' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextInput](arkts-arkui-typenode-textinput-t.md) |

**Examples**

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
    // Create a TextInput.
    let textInput = typeNode.createNode(uiContext, 'TextInput');
    textInput.initialize({ text: 'TextInput' });
    col.appendChild(textInput);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('TextInput sample')
      NodeContainer(this.myNodeController);
    }
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Button'): Button
```

Creates a FrameNode of the **Button** type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Button'): Button--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Button'): Button-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Button' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Button](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-mouseevent-button-e.md) |

**Examples**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom Button controller by extending NodeController.
class MyButtonController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // Create a Button node.
    let button = typeNode.createNode(uiContext, 'Button')
    button.initialize('This is Button')
      .onClick(() => {
        uiContext.getPromptAction().showToast({ message: 'Button clicked' })
      })
    col.appendChild(button)

    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myButtonController: MyButtonController = new MyButtonController();

  build() {
    Column({ space: 5 }) {
      Text('ButtonSample')
      NodeContainer(this.myButtonController);

    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'ListItemGroup'): ListItemGroup
```

Creates a FrameNode of the **ListItemGroup** type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'ListItemGroup'): ListItemGroup--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'ListItemGroup'): ListItemGroup-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'ListItemGroup' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ListItemGroup](../../apis-na/arkts-apis/arkts-na-typenode-listitemgroup-t.md) |

**Examples**

See the example for createNode('List').


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'WaterFlow'): WaterFlow
```

Creates a FrameNode of the **WaterFlow** type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'WaterFlow'): WaterFlow--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'WaterFlow'): WaterFlow-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'WaterFlow' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WaterFlow](../../apis-na/arkts-apis/arkts-na-typenode-waterflow-t.md) |

**Examples**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom WaterFlow controller by extending NodeController.
class MyWaterFlowController extends NodeController {
  public rootNode: FrameNode | null = null;
  private minHeight: number = 80;
  private maxHeight: number = 180;

  // Calculate the FlowItem height.
  private getHeight() {
    let randomHeight = Math.floor(Math.random() * this.maxHeight);
    return (randomHeight > this.minHeight ? randomHeight : this.minHeight);
  }

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    // Create a WaterFlow node and set its properties.
    let waterFlowNode = typeNode.createNode(uiContext, 'WaterFlow');
    waterFlowNode.attribute.size({ width: '100%', height: '100%' })
      .columnsTemplate('1fr 1fr')
      .columnsGap(10)
      .rowsGap(5);
    typeNode.getAttribute(waterFlowNode, 'WaterFlow')?.friction(0.6);

    // Create a FlowItem node and set its properties.
    for (let i = 0; i < 20; i++) {
      let flowItemNode = typeNode.createNode(uiContext, 'FlowItem');
      flowItemNode.attribute.size({ height: this.getHeight() });
      typeNode.getAttribute(flowItemNode, 'FlowItem')?.width('100%');
      waterFlowNode.appendChild(flowItemNode);

      let text = typeNode.createNode(uiContext, 'Text');
      text.initialize('N' + i)
        .size({ width: '100%', height: '100%' })
        .textAlign(TextAlign.Center)
        .backgroundColor(0xF9CF93);
      flowItemNode.appendChild(text);
    }

    this!.rootNode!.appendChild(waterFlowNode);
    return this.rootNode;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myWaterFlowController: MyWaterFlowController = new MyWaterFlowController();

  build() {
    Column({ space: 5 }) {
      Text('WaterFlowSample')
      NodeContainer(this.myWaterFlowController);

    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'FlowItem'): FlowItem
```

Creates a FrameNode of the **FlowItem** type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'FlowItem'): FlowItem--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'FlowItem'): FlowItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'FlowItem' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FlowItem](../../apis-na/arkts-apis/arkts-na-typenode-flowitem-t.md) |

**Examples**

See the example for createNode('WaterFlow').


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'XComponent'): XComponent
```

Creates a FrameNode of the **XComponent** type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'XComponent'): XComponent--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'XComponent'): XComponent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'XComponent' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [XComponent](../../apis-na/arkts-apis/arkts-na-typenode-xcomponent-t.md) |

**Examples**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col);
    // Create an XComponent object.
    let xcomponent = typeNode.createNode(uiContext, 'XComponent');
    xcomponent.attribute.backgroundColor(Color.Red);
    col.appendChild(xcomponent);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('XComponentSample')
      NodeContainer(this.myNodeController)
    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'XComponent', options: XComponentOptions): XComponent
```

Creates a FrameNode of the **XComponent** type based on the settings specified in **options**.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'XComponent', options: XComponentOptions): XComponent--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'XComponent', options: XComponentOptions): XComponent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'XComponent' | Yes |
| options | [XComponentOptions](../arkts-components/arkts-arkui-xcomponentoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [XComponent](../../apis-na/arkts-apis/arkts-na-typenode-xcomponent-t.md) |

**Examples**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  controller: XComponentController = new XComponentController();
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col);
    // Set the XComponent parameter object.
    let options: XComponentOptions = {
      type: XComponentType.SURFACE,
      controller: this.controller
    };
    // Create an XComponent object.
    let xcomponent = typeNode.createNode(uiContext, 'XComponent', options);
    xcomponent.attribute.backgroundColor(Color.Red);
    col.appendChild(xcomponent);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('XComponentSample')
      NodeContainer(this.myNodeController)
    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'XComponent', parameters: NativeXComponentParameters): XComponent
```

Creates a FrameNode of the **XComponent** type based on the settings specified in **parameters**.

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'XComponent', parameters: NativeXComponentParameters): XComponent--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'XComponent', parameters: NativeXComponentParameters): XComponent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'XComponent' | Yes |
| parameters | [NativeXComponentParameters](../arkts-components/arkts-arkui-nativexcomponentparameters-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [XComponent](../../apis-na/arkts-apis/arkts-na-typenode-xcomponent-t.md) |

**Examples**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  controller: XComponentController = new XComponentController();
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col);
    let parameters: NativeXComponentParameters = {
      type: XComponentType.SURFACE
    };
    // Create an XComponent object.
    let xcomponent = typeNode.createNode(uiContext, 'XComponent', parameters);
    xcomponent.attribute.backgroundColor(Color.Red);
    col.appendChild(xcomponent);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('XComponentSample')
      NodeContainer(this.myNodeController)
    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Checkbox'): Checkbox
```

Creates a FrameNode of the **Checkbox** type.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Checkbox'): Checkbox--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Checkbox'): Checkbox-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Checkbox' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Checkbox](../../apis-na/arkts-apis/arkts-na-typenode-checkbox-t.md) |

**Examples**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom Checkbox controller by extending NodeController.
class MyCheckboxController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // Create a Checkbox node.
    let checkbox = typeNode.createNode(uiContext, 'Checkbox')
    checkbox.initialize({ name: 'checkbox1', group: 'checkboxGroup1' })

    // Create another Checkbox node.
    let checkbox1 = typeNode.createNode(uiContext, 'Checkbox')
    checkbox1.initialize({ name: 'checkbox2', group: 'checkboxGroup1' })

    // Add the two Checkbox nodes to col for comparison.
    col.appendChild(checkbox)
    col.appendChild(checkbox1)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myCheckboxController: MyCheckboxController = new MyCheckboxController();

  build() {
    Column({ space: 5 }) {
      Text('CheckboxSample')
      NodeContainer(this.myCheckboxController);
    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'CheckboxGroup'): CheckboxGroup
```

Creates a FrameNode of the **CheckboxGroup** type.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'CheckboxGroup'): CheckboxGroup--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'CheckboxGroup'): CheckboxGroup-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'CheckboxGroup' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CheckboxGroup](arkts-arkui-typenode-checkboxgroup-t.md) |

**Examples**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom CheckboxGroup controller by extending NodeController.
class MyCheckboxGroupController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    let checkbox = typeNode.createNode(uiContext, 'Checkbox')
    checkbox.initialize({ name: 'checkbox1', group: 'checkboxGroup1' })

    let checkbox1 = typeNode.createNode(uiContext, 'Checkbox')
    checkbox1.initialize({ name: 'checkbox2', group: 'checkboxGroup1' })

    // Create a CheckboxGroup node.
    let checkboxGroup = typeNode.createNode(uiContext, 'CheckboxGroup')
    checkboxGroup.initialize({ group: 'checkboxGroup1' })

    col.appendChild(checkbox)
    col.appendChild(checkbox1)
    col.appendChild(checkboxGroup)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myCheckboxGroupController: MyCheckboxGroupController = new MyCheckboxGroupController();

  build() {
    Column({ space: 5 }) {
      Text('CheckboxGroupSample')
      NodeContainer(this.myCheckboxGroupController);
    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Radio'): Radio
```

Creates a FrameNode of the **Radio** type.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Radio'): Radio--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Radio'): Radio-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Radio' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Radio](arkts-arkui-typenode-radio-t.md) |

**Examples**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom Radio controller by extending NodeController.
class MyRadioController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // Create a Radio node.
    let radio1 = typeNode.createNode(uiContext, 'Radio')
    radio1.initialize({ value: 'radio1', group: 'radioGroup' })

    // Create another Radio node for comparison.
    let radio2 = typeNode.createNode(uiContext, 'Radio')
    radio2.initialize({ value: 'radio2', group: 'radioGroup' })

    col.appendChild(radio1)
    col.appendChild(radio2)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myRadioController: MyRadioController = new MyRadioController();

  build() {
    Column({ space: 5 }) {
      Text('RadioSample')
      NodeContainer(this.myRadioController);
    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Rating'): Rating
```

Creates a FrameNode of the **Rating** type.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Rating'): Rating--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Rating'): Rating-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Rating' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Rating](../../apis-na/arkts-apis/arkts-na-typenode-rating-t.md) |

**Examples**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom Rating controller by extending NodeController.
class MyRatingController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // Create a Rating node.
    let rating = typeNode.createNode(uiContext, 'Rating')
    rating.initialize({ rating: 0 })
    col.appendChild(rating)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myRatingController: MyRatingController = new MyRatingController();

  build() {
    Column({ space: 5 }) {
      Text('RatingSample')

      NodeContainer(this.myRatingController);

    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Select'): Select
```

Creates a FrameNode of the **Select** type.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Select'): Select--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Select'): Select-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Select' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Select](arkts-arkui-typenode-select-t.md) |

**Examples**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom Select controller by extending NodeController.
class MySelectController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // Create a Select node and set its options.
    let select = typeNode.createNode(uiContext, 'Select')
    select.initialize([{ value: 'option one' }, { value: 'option two' }, { value: 'option three' }])
    col.appendChild(select)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private mySelectController: MySelectController = new MySelectController();

  build() {
    Column({ space: 5 }) {
      Text('SelectSample')
      NodeContainer(this.mySelectController);
    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Slider'): Slider
```

Creates a FrameNode of the **Slider** type.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Slider'): Slider--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Slider'): Slider-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Slider' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Slider](../../apis-na/arkts-apis/arkts-na-typenode-slider-t.md) |

**Examples**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom Slider controller by extending NodeController.
class MySliderController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // Create a Slider node.
    let slider = typeNode.createNode(uiContext, 'Slider')
    slider.initialize({value:50})
    col.appendChild(slider)
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private mySliderController: MySliderController = new MySliderController();

  build() {
    Column({ space: 5 }) {
      Text('SliderSample')
      NodeContainer(this.mySliderController);

    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Toggle', options?: ToggleOptions): Toggle
```

Creates a FrameNode of the **Toggle** type.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Toggle', options?: ToggleOptions): Toggle--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Toggle', options?: ToggleOptions): Toggle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Toggle' | Yes |
| options | [ToggleOptions](../arkts-components/arkts-arkui-toggleoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Toggle](arkts-arkui-typenode-toggle-t.md) |

**Examples**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom Toggle controller by extending NodeController.
class MyToggleController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // Create a Toggle node.
    let toggleSwitch = typeNode.createNode(uiContext, 'Toggle')
    toggleSwitch.initialize({ type: ToggleType.Switch })
    col.appendChild(toggleSwitch)

    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myToggleController: MyToggleController = new MyToggleController();

  build() {
    Column({ space: 5 }) {
      Text('ToggleSample')
      NodeContainer(this.myToggleController);

    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Marquee'): Marquee
```

Creates a FrameNode of the **Marquee** type.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Marquee'): Marquee--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Marquee'): Marquee-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Marquee' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Marquee](../../apis-na/arkts-apis/arkts-na-typenode-marquee-t.md) |

**Examples**

```TypeScript
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 })
    node.appendChild(col);
    // Create a Marquee node.
    let marquee = typeNode.createNode(uiContext, 'Marquee');
    marquee.initialize({ start: true, src: 'Marquee, if need display, src shall be long' });
      .width(100);
    col.appendChild(marquee);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('Marquee createNode sample');
      NodeContainer(this.myNodeController);
    }
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'TextArea'): TextArea
```

Creates a FrameNode of the **TextArea** type.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'TextArea'): TextArea--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'TextArea'): TextArea-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'TextArea' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextArea](arkts-arkui-typenode-textarea-t.md) |

**Examples**

```TypeScript
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 })
    node.appendChild(col);
    // Create a TextArea node.
    let textArea = typeNode.createNode(uiContext, 'TextArea');
    textArea.initialize({ text: 'TextArea' });
    col.appendChild(textArea);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('TextArea create sample')
      NodeContainer(this.myNodeController);
    }
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'SymbolGlyph'): SymbolGlyph
```

Creates a FrameNode of the **SymbolGlyph** type.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'SymbolGlyph'): SymbolGlyph--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'SymbolGlyph'): SymbolGlyph-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'SymbolGlyph' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SymbolGlyph](../../apis-na/arkts-apis/arkts-na-typenode-symbolglyph-t.md) |

**Examples**

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
    // Create a SymbolGlyph node.
    let symbolGlyph = typeNode.createNode(uiContext, 'SymbolGlyph');
    symbolGlyph.initialize($r('sys.symbol.ohos_trash'));
    col.appendChild(symbolGlyph);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 5 }) {
      Text('SymbolGlyph sample');
      NodeContainer(this.myNodeController);
    }
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'QRCode'): QRCode
```

Creates a FrameNode of the **QRCode** type.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'QRCode'): QRCode--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'QRCode'): QRCode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'QRCode' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [QRCode](arkts-arkui-typenode-qrcode-t.md) |

**Examples**

```TypeScript
typeNode.createNode(uiContext, 'QRCode');
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Badge'): Badge
```

Creates a FrameNode of the **Badge** type.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Badge'): Badge--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Badge'): Badge-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Badge' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Badge](../../apis-na/arkts-apis/arkts-na-typenode-badge-t.md) |

**Examples**

```TypeScript
typeNode.createNode(uiContext, 'Badge');
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'TextClock'): TextClock
```

Creates a FrameNode of the **TextClock** type.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'TextClock'): TextClock--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'TextClock'): TextClock-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'TextClock' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextClock](../../apis-na/arkts-apis/arkts-na-typenode-textclock-t.md) |

**Examples**

```TypeScript
typeNode.createNode(uiContext, 'TextClock');
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'TextTimer'): TextTimer
```

Creates a FrameNode of the **TextTimer** type.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'TextTimer'): TextTimer--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'TextTimer'): TextTimer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'TextTimer' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextTimer](arkts-arkui-typenode-texttimer-t.md) |

**Examples**

```TypeScript
typeNode.createNode(uiContext, 'TextTimer');
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Grid'): Grid
```

Creates a FrameNode of the **Grid** type.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Grid'): Grid--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Grid'): Grid-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Grid' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Grid](../../apis-na/arkts-apis/arkts-na-typenode-grid-t.md) |

**Examples**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom Grid controller by extending NodeController.
class MyGridController extends NodeController {
  public rootNode: FrameNode | null = null;
  private scroller: Scroller = new Scroller();

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    // Create a Grid node and set its properties.
    let gridNode = typeNode.createNode(uiContext, 'Grid');
    gridNode.initialize(this.scroller, { regularSize: [1, 1] })
      .size({ width: '90%', height: 300 })
      .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
      .rowsTemplate('1fr 1fr 1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10);
    typeNode.getAttribute(gridNode, 'Grid')?.friction(0.6);

    // Create a GridItem node and set its properties.
    for (let i = 0; i < 25; i++) {
      let gridItemNode = typeNode.createNode(uiContext, 'GridItem');
      gridItemNode.initialize({ style: GridItemStyle.NONE }).size({ height: '100%' });
      typeNode.getAttribute(gridItemNode, 'GridItem')?.width('100%');

      let text = typeNode.createNode(uiContext, 'Text');
      text.initialize((i % 5).toString())
        .size({ width: '100%', height: '100%' })
        .textAlign(TextAlign.Center)
        .backgroundColor(0xF9CF93);
      gridItemNode.appendChild(text);
      gridNode.appendChild(gridItemNode);
    }

    this!.rootNode!.appendChild(gridNode);
    return this.rootNode;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myGridController: MyGridController = new MyGridController();

  build() {
    Column({ space: 5 }) {
      Text('GridSample')
      NodeContainer(this.myGridController)

    }.width('100%')
  }
}
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'GridItem'): GridItem
```

Creates a FrameNode of the **GridItem** type.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'GridItem'): GridItem--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'GridItem'): GridItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'GridItem' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [GridItem](../../apis-na/arkts-apis/arkts-na-typenode-griditem-t.md) |

**Examples**

See the example for createNode('Grid').
