# createNode

## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Text'): Text
```

创建Text类型的FrameNode节点。使用typeNode创建Text节点时，当传入的UIContext对应的UI实例销毁后，调用该接口会返回一个无效的FrameNode节点，无法正常挂载和显示。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Text'): Text--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Text'): Text-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Text' | 是 |

**返回值：**

| 类型 |
| --- |
| [Text](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-text-c.md) |

**示例**

```TypeScript
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 });
    node.appendChild(col);
    // 创建Text
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

创建Column类型的FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Column'): Column--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Column'): Column-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Column' | 是 |

**返回值：**

| 类型 |
| --- |
| [Column](arkts-arkui-typenode-column-t.md) |

**示例**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Column控制器
class MyColumnController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute
    // 创建Column
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

创建Row类型的FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Row'): Row--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Row'): Row-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Row' | 是 |

**返回值：**

| 类型 |
| --- |
| [Row](../../apis-na/arkts-apis/arkts-na-typenode-row-t.md) |

**示例**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Row控制器
class MyRowController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    // 创建row
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

创建Stack类型的FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Stack'): Stack--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Stack'): Stack-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Stack' | 是 |

**返回值：**

| 类型 |
| --- |
| [Stack](../../apis-na/arkts-apis/arkts-na-typenode-stack-t.md) |

**示例**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Stack控制器
class MyStackController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    // 创建Stack
    let stack = typeNode.createNode(uiContext, 'Stack')
    stack.initialize({ alignContent: Alignment.Top })
      .width('50%')
      .height('50%')
      .backgroundColor(Color.Gray)
    node.appendChild(stack)
    let text = typeNode.createNode(uiContext, 'Text')
    text.initialize('This is Text')
    // 向stack添加text
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

创建GridRow类型的FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'GridRow'): GridRow--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'GridRow'): GridRow-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'GridRow' | 是 |

**返回值：**

| 类型 |
| --- |
| [GridRow](../../apis-na/arkts-apis/arkts-na-typenode-gridrow-t.md) |

**示例**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义GridRow控制器
class MyGridRowController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    // 创建GridRow
    let gridRow = typeNode.createNode(uiContext, 'GridRow')
    gridRow.initialize({ columns: 12 })
      .width('50%')
      .height('50%')
      .backgroundColor(Color.Gray)
    node.appendChild(gridRow)
    // 创建GridCol
    let gridCol = typeNode.createNode(uiContext, 'GridCol')
    gridCol.initialize({ span: 2, offset: 4 })
      .height('100%')
      .backgroundColor(Color.Red)
    // 向gridRow添加gridCol
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

创建GridCol类型的FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'GridCol'): GridCol--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'GridCol'): GridCol-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'GridCol' | 是 |

**返回值：**

| 类型 |
| --- |
| [GridCol](arkts-arkui-typenode-gridcol-t.md) |

**示例**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义GridRow控制器
class MyGridRowController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    // 创建GridRow
    let gridRow = typeNode.createNode(uiContext, 'GridRow')
    gridRow.initialize({ columns: 12 })
      .width('50%')
      .height('50%')
      .backgroundColor(Color.Gray)
    node.appendChild(gridRow)
    // 创建GridCol
    let gridCol = typeNode.createNode(uiContext, 'GridCol')
    gridCol.initialize({ span: 2, offset: 4 })
      .height('100%')
      .backgroundColor(Color.Red)
    // 向gridRow添加gridCol
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

创建Flex类型的FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Flex'): Flex--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Flex'): Flex-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Flex' | 是 |

**返回值：**

| 类型 |
| --- |
| [Flex](../../apis-na/arkts-apis/arkts-na-typenode-flex-t.md) |

**示例**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Flex控制器
class MyFlexController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    // 创建Flex
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

创建Swiper类型的FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Swiper'): Swiper--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Swiper'): Swiper-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Swiper' | 是 |

**返回值：**

| 类型 |
| --- |
| [Swiper](arkts-arkui-typenode-swiper-t.md) |

**示例**

```TypeScript
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Swiper控制器
class MySwiperController extends NodeController {
  swiperController: SwiperController = new SwiperController()

  makeNode(uiContext: UIContext): FrameNode | null {
    // 创建Swiper
    let swiperNode = typeNode.createNode(uiContext, 'Swiper')

    // 创建Text
    let text0 = typeNode.createNode(uiContext, 'Text')
    text0.initialize('0')
      .width('100%')
      .height('100%')
      .textAlign(TextAlign.Center)
    // 向swiper添加text0
    swiperNode.appendChild(text0)
    // 创建另一个Text用于切换
    let text1 = typeNode.createNode(uiContext, 'Text')
    text1.initialize('1')
      .width('100%')
      .height('100%')
      .textAlign(TextAlign.Center)
    // 向swiper添加text1
    swiperNode.appendChild(text1)
    swiperNode.commonAttribute.width('100%')
      .height('20%')
      .backgroundColor(0xAFEEEE)
    // 向swiper绑定控制器
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

创建Progress类型的FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Progress'): Progress--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Progress'): Progress-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Progress' | 是 |

**返回值：**

| 类型 |
| --- |
| [Progress](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-progress-i.md) |

**示例**

```TypeScript
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Progress控制器
class MyProgressNodeController extends NodeController {
  public uiContext: UIContext | null = null;
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.uiContext = uiContext;
    this.rootNode = new FrameNode(uiContext);
    // 创建Progress
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

创建Scroll类型的FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Scroll'): Scroll--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Scroll'): Scroll-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Scroll' | 是 |

**返回值：**

| 类型 |
| --- |
| [Scroll](../../apis-na/arkts-apis/arkts-na-typenode-scroll-t.md) |

**示例**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Scroll控制器
class MyScrollController extends NodeController {
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    // 创建Scroll
    let scroller: Scroller = new Scroller();
    // 创建Scroll并设置属性
    let scrollNode = typeNode.createNode(uiContext, 'Scroll');
    scrollNode.initialize(scroller).size({ width: '100%', height: 500 });
    typeNode.getAttribute(scrollNode, 'Scroll')?.friction(0.6);

    let colNode = typeNode.createNode(uiContext, 'Column');
    // 向scroll添加column
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

创建RelativeContainer类型的FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'RelativeContainer'): RelativeContainer--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'RelativeContainer'): RelativeContainer-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'RelativeContainer' | 是 |

**返回值：**

| 类型 |
| --- |
| [RelativeContainer](arkts-arkui-typenode-relativecontainer-t.md) |

**示例**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Relative控制器
class MyRelativeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    // 创建RelativeContainer
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

创建Divider类型的FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Divider'): Divider--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Divider'): Divider-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Divider' | 是 |

**返回值：**

| 类型 |
| --- |
| [Divider](arkts-arkui-typenode-divider-t.md) |

**示例**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Divider控制器
class MyDividerController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // 创建divider
    let divider = typeNode.createNode(uiContext, 'Divider')
    divider.initialize()
      .strokeWidth(1)
    // 向col添加divider
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

创建LoadingProgress类型的FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'LoadingProgress'): LoadingProgress--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'LoadingProgress'): LoadingProgress-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'LoadingProgress' | 是 |

**返回值：**

| 类型 |
| --- |
| [LoadingProgress](arkts-arkui-typenode-loadingprogress-t.md) |

**示例**

```TypeScript
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义LoadingProgress控制器
class MyLoadingProgressNodeController extends NodeController {
  public uiContext: UIContext | null = null;
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.uiContext = uiContext;
    this.rootNode = new FrameNode(uiContext);
    // 创建LoadingProgress
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

创建Search类型的FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Search'): Search--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Search'): Search-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Search' | 是 |

**返回值：**

| 类型 |
| --- |
| [Search](arkts-arkui-typenode-search-t.md) |

**示例**

```TypeScript
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 });
    node.appendChild(col);
    // 创建Search
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

创建Blank类型的FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Blank'): Blank--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Blank'): Blank-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Blank' | 是 |

**返回值：**

| 类型 |
| --- |
| [Blank](arkts-arkui-typenode-blank-t.md) |

**示例**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Blank控制器
class MyBlankController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // 创建Blank
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

创建Image类型的FrameNode节点。使用typeNode创建Image节点时，当传入的UIContext对应的UI实例销毁后，调用该接口会返回一个无效的FrameNode节点，无法正常挂载和显示。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Image'): Image--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Image'): Image-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Image' | 是 |

**返回值：**

| 类型 |
| --- |
| [Image](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-image-i.md) |

**示例**

```TypeScript
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Image控制器
class MyImageController extends NodeController {
  public uiContext: UIContext | null = null;
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.uiContext = uiContext;
    this.rootNode = new FrameNode(uiContext);
    // 创建Image
    let imageNode = typeNode.createNode(uiContext, 'Image');
    imageNode
      // $r('app.media.img')需要替换为开发者所需的图像资源文件
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

创建List类型的FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'List'): List--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'List'): List-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'List' | 是 |

**返回值：**

| 类型 |
| --- |
| [List](../../apis-arkts/arkts-apis/arkts-arkts-util-list-list-c.md) |

**示例**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义List控制器
class MyListController extends NodeController {
  public rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    // 创建list节点
    this.rootNode = new FrameNode(uiContext);
    // 创建List
    let listNode = typeNode.createNode(uiContext, 'List');
    listNode.initialize({ space: 3 }).size({ width: '100%', height: '100%' });
    typeNode.getAttribute(listNode, 'List')?.friction(0.6);

    // 在list下创建ListItemGroup节点
    let listItemGroupNode = typeNode.createNode(uiContext, 'ListItemGroup');
    listItemGroupNode.initialize({ space: 3 });
    listNode.appendChild(listItemGroupNode);

    // 在ListItemGroup中放入ListItem节点
    let listItemNode1 = typeNode.createNode(uiContext, 'ListItem');
    listItemNode1.initialize({ style: ListItemStyle.NONE }).height(100).borderWidth(1).backgroundColor('#FF00FF');
    let text1 = typeNode.createNode(uiContext, 'Text');
    text1.initialize('ListItem1');
    listItemNode1.appendChild(text1);
    listItemGroupNode.appendChild(listItemNode1);

    // 创建ListItem，添加Text至ListItem，添加至listItemGroup
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

创建ListItem类型的FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'ListItem'): ListItem--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'ListItem'): ListItem-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'ListItem' | 是 |

**返回值：**

| 类型 |
| --- |
| [ListItem](../../apis-na/arkts-apis/arkts-na-typenode-listitem-t.md) |

**示例**

参考createNode('List')示例。


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'TextInput'): TextInput
```

创建TextInput类型的FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'TextInput'): TextInput--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'TextInput'): TextInput-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'TextInput' | 是 |

**返回值：**

| 类型 |
| --- |
| [TextInput](arkts-arkui-typenode-textinput-t.md) |

**示例**

```TypeScript
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 });
    node.appendChild(col);
    // 创建TextInput
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

创建Button类型的FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Button'): Button--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Button'): Button-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Button' | 是 |

**返回值：**

| 类型 |
| --- |
| [Button](../../apis-na/arkts-apis/arkts-na-typenode-button-t.md) |

**示例**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Button控制器
class MyButtonController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // 创建Button
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

创建ListItemGroup类型的FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'ListItemGroup'): ListItemGroup--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'ListItemGroup'): ListItemGroup-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'ListItemGroup' | 是 |

**返回值：**

| 类型 |
| --- |
| [ListItemGroup](arkts-arkui-typenode-listitemgroup-t.md) |

**示例**

参考createNode('List')示例。


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'WaterFlow'): WaterFlow
```

创建WaterFlow类型的FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'WaterFlow'): WaterFlow--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'WaterFlow'): WaterFlow-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'WaterFlow' | 是 |

**返回值：**

| 类型 |
| --- |
| [WaterFlow](../../apis-na/arkts-apis/arkts-na-typenode-waterflow-t.md) |

**示例**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义WaterFlow控制器
class MyWaterFlowController extends NodeController {
  public rootNode: FrameNode | null = null;
  private minHeight: number = 80;
  private maxHeight: number = 180;

  // 计算FlowItem高
  private getHeight() {
    let randomHeight = Math.floor(Math.random() * this.maxHeight);
    return (randomHeight > this.minHeight ? randomHeight : this.minHeight);
  }

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    // 创建WaterFlow并设置属性
    let waterFlowNode = typeNode.createNode(uiContext, 'WaterFlow');
    waterFlowNode.attribute.size({ width: '100%', height: '100%' })
      .columnsTemplate('1fr 1fr')
      .columnsGap(10)
      .rowsGap(5);
    typeNode.getAttribute(waterFlowNode, 'WaterFlow')?.friction(0.6);

    // 创建FlowItem并设置属性
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

创建FlowItem类型的FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'FlowItem'): FlowItem--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'FlowItem'): FlowItem-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'FlowItem' | 是 |

**返回值：**

| 类型 |
| --- |
| [FlowItem](../../apis-na/arkts-apis/arkts-na-typenode-flowitem-t.md) |

**示例**

参考createNode('WaterFlow')示例。


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'XComponent'): XComponent
```

创建XComponent类型的FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'XComponent'): XComponent--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'XComponent'): XComponent-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'XComponent' | 是 |

**返回值：**

| 类型 |
| --- |
| [XComponent](../../apis-na/arkts-apis/arkts-na-typenode-xcomponent-t.md) |

**示例**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col);
    // 创建XComponent
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

按照options中的配置参数创建XComponent类型的FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'XComponent', options: XComponentOptions): XComponent--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'XComponent', options: XComponentOptions): XComponent-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'XComponent' | 是 |
| options | [XComponentOptions](../arkts-components/arkts-arkui-xcomponentoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [XComponent](../../apis-na/arkts-apis/arkts-na-typenode-xcomponent-t.md) |

**示例**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  controller: XComponentController = new XComponentController();
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col);
    // 设置XComponent参数对象
    let options: XComponentOptions = {
      type: XComponentType.SURFACE,
      controller: this.controller
    };
    // 创建XComponent
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

按照parameters中的配置参数创建XComponent类型的FrameNode节点。

**起始版本：** 19

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'XComponent', parameters: NativeXComponentParameters): XComponent--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'XComponent', parameters: NativeXComponentParameters): XComponent-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'XComponent' | 是 |
| parameters | [NativeXComponentParameters](../arkts-components/arkts-arkui-nativexcomponentparameters-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [XComponent](../../apis-na/arkts-apis/arkts-na-typenode-xcomponent-t.md) |

**示例**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
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
    // 创建XComponent
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

创建Checkbox类型的FrameNode节点。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Checkbox'): Checkbox--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Checkbox'): Checkbox-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Checkbox' | 是 |

**返回值：**

| 类型 |
| --- |
| [Checkbox](../../apis-na/arkts-apis/arkts-na-typenode-checkbox-t.md) |

**示例**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Checkbox控制器
class MyCheckboxController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // 创建Checkbox
    let checkbox = typeNode.createNode(uiContext, 'Checkbox')
    checkbox.initialize({ name: 'checkbox1', group: 'checkboxGroup1' })

    // 创建另一个Checkbox
    let checkbox1 = typeNode.createNode(uiContext, 'Checkbox')
    checkbox1.initialize({ name: 'checkbox2', group: 'checkboxGroup1' })

    // 将两个checkbox添加至col进行比较
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

创建CheckboxGroup类型的FrameNode节点。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'CheckboxGroup'): CheckboxGroup--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'CheckboxGroup'): CheckboxGroup-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'CheckboxGroup' | 是 |

**返回值：**

| 类型 |
| --- |
| [CheckboxGroup](arkts-arkui-typenode-checkboxgroup-t.md) |

**示例**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义CheckboxGroup控制器
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

    // 创建checkboxGroup
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

创建Radio类型的FrameNode节点。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Radio'): Radio--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Radio'): Radio-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Radio' | 是 |

**返回值：**

| 类型 |
| --- |
| [Radio](arkts-arkui-typenode-radio-t.md) |

**示例**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Radio控制器
class MyRadioController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // 创建Radio
    let radio1 = typeNode.createNode(uiContext, 'Radio')
    radio1.initialize({ value: 'radio1', group: 'radioGroup' })

    // 创建另一个Radio用于对比
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

创建Rating类型的FrameNode节点。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Rating'): Rating--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Rating'): Rating-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Rating' | 是 |

**返回值：**

| 类型 |
| --- |
| [Rating](arkts-arkui-typenode-rating-t.md) |

**示例**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Rating控制器
class MyRatingController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // 创建rating
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

创建Select类型的FrameNode节点。使用typeNode创建Select节点时，当传入的UIContext对应的UI实例销毁后，调用该接口会返回一个无效的FrameNode节点，无法正常挂载和显示。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Select'): Select--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Select'): Select-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Select' | 是 |

**返回值：**

| 类型 |
| --- |
| [Select](arkts-arkui-typenode-select-t.md) |

**示例**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Select控制器
class MySelectController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // 创建Select并设置选项
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

创建Slider类型的FrameNode节点。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Slider'): Slider--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Slider'): Slider-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Slider' | 是 |

**返回值：**

| 类型 |
| --- |
| [Slider](arkts-arkui-typenode-slider-t.md) |

**示例**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Slider控制器
class MySliderController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // 创建Slider
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

创建Toggle类型的FrameNode节点。使用typeNode创建Toggle节点时，当传入的UIContext对应的UI实例销毁后，调用该接口会返回一个无效的FrameNode节点，无法正常挂载和显示。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Toggle', options?: ToggleOptions): Toggle--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Toggle', options?: ToggleOptions): Toggle-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Toggle' | 是 |
| options | [ToggleOptions](../arkts-components/arkts-arkui-toggleoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [Toggle](arkts-arkui-typenode-toggle-t.md) |

**示例**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Toggle控制器
class MyToggleController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext)
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column')
    col.initialize({ space: 5 })
      .width('100%')
      .height('100%')
    node.appendChild(col)
    // 创建Toggle
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

创建Marquee类型的FrameNode节点。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Marquee'): Marquee--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Marquee'): Marquee-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Marquee' | 是 |

**返回值：**

| 类型 |
| --- |
| [Marquee](../../apis-na/arkts-apis/arkts-na-typenode-marquee-t.md) |

**示例**

```TypeScript
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 })
    node.appendChild(col);
    // 创建marquee
    let marquee = typeNode.createNode(uiContext, 'Marquee');
    marquee.initialize({ start: true, src: 'Marquee, if need display, src shall be long' })
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

创建TextArea类型的FrameNode节点。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'TextArea'): TextArea--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'TextArea'): TextArea-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'TextArea' | 是 |

**返回值：**

| 类型 |
| --- |
| [TextArea](arkts-arkui-typenode-textarea-t.md) |

**示例**

```TypeScript
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 })
    node.appendChild(col);
    // 创建textArea
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

创建SymbolGlyph类型的FrameNode节点。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'SymbolGlyph'): SymbolGlyph--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'SymbolGlyph'): SymbolGlyph-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'SymbolGlyph' | 是 |

**返回值：**

| 类型 |
| --- |
| [SymbolGlyph](../../apis-na/arkts-apis/arkts-na-typenode-symbolglyph-t.md) |

**示例**

```TypeScript
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义UI控制器
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.commonAttribute;
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize({ space: 5 });
    node.appendChild(col);
    // 创建SymbolGlyph
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

创建QRCode类型的FrameNode节点。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'QRCode'): QRCode--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'QRCode'): QRCode-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'QRCode' | 是 |

**返回值：**

| 类型 |
| --- |
| [QRCode](arkts-arkui-typenode-qrcode-t.md) |

**示例**

```TypeScript
typeNode.createNode(uiContext, 'QRCode');
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Badge'): Badge
```

创建Badge类型的FrameNode节点。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Badge'): Badge--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Badge'): Badge-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Badge' | 是 |

**返回值：**

| 类型 |
| --- |
| [Badge](../../apis-na/arkts-apis/arkts-na-typenode-badge-t.md) |

**示例**

```TypeScript
typeNode.createNode(uiContext, 'Badge');
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'TextClock'): TextClock
```

创建TextClock类型的FrameNode节点。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'TextClock'): TextClock--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'TextClock'): TextClock-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'TextClock' | 是 |

**返回值：**

| 类型 |
| --- |
| [TextClock](../../apis-na/arkts-apis/arkts-na-typenode-textclock-t.md) |

**示例**

```TypeScript
typeNode.createNode(uiContext, 'TextClock');
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'TextTimer'): TextTimer
```

创建TextTimer类型的FrameNode节点。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'TextTimer'): TextTimer--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'TextTimer'): TextTimer-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'TextTimer' | 是 |

**返回值：**

| 类型 |
| --- |
| [TextTimer](../../apis-na/arkts-apis/arkts-na-typenode-texttimer-t.md) |

**示例**

```TypeScript
typeNode.createNode(uiContext, 'TextTimer');
```


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Grid'): Grid
```

创建Grid类型的FrameNode节点。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Grid'): Grid--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Grid'): Grid-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Grid' | 是 |

**返回值：**

| 类型 |
| --- |
| [Grid](../../apis-na/arkts-apis/arkts-na-typenode-grid-t.md) |

**示例**

```TypeScript
import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// 继承NodeController实现自定义Grid控制器
class MyGridController extends NodeController {
  public rootNode: FrameNode | null = null;
  private scroller: Scroller = new Scroller();

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    // 创建Grid设置属性
    let gridNode = typeNode.createNode(uiContext, 'Grid');
    gridNode.initialize(this.scroller, { regularSize: [1, 1] })
      .size({ width: '90%', height: 300 })
      .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
      .rowsTemplate('1fr 1fr 1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10);
    typeNode.getAttribute(gridNode, 'Grid')?.friction(0.6);

    // 创建GridItem并设置属性
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

创建GridItem类型的FrameNode节点。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'GridItem'): GridItem--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'GridItem'): GridItem-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'GridItem' | 是 |

**返回值：**

| 类型 |
| --- |
| [GridItem](../../apis-na/arkts-apis/arkts-na-typenode-griditem-t.md) |

**示例**

参考createNode('Grid')示例。
