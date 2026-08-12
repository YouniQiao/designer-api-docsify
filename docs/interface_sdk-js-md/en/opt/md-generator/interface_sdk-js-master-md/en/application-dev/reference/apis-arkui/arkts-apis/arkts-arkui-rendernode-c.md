# RenderNode

The **RenderNode** module provides APIs for creating a RenderNode in custom drawing settings with C APIs.

> **NOTE：**
> 
> - Avoid modifying RenderNodes in [BuilderNode](./BuilderNode). The [FrameNode](./FrameNode) associated
> with BuilderNode is designed solely for mounting the BuilderNode as a child component. Modifying attributes or
> operations on the FrameNode's child nodes or their corresponding RenderNodes may lead to undefined behavior,
> including display, event handling, and stability issues.
> 
> - RenderNode objects do not support JSON serialization.

**Since:** 11

<!--Device-unnamed-export class RenderNode--><!--Device-unnamed-export class RenderNode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## appendChild

```TypeScript
appendChild(node: RenderNode): void
```

Appends a child node to this RenderNode.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-appendChild(node: RenderNode): void--><!--Device-RenderNode-appendChild(node: RenderNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [RenderNode](arkts-arkui-rendernode-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100025](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-node.md#100025-invalid-parameter-value) |

## Examples

```TypeScript
import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 100,
  height: 100
};
renderNode.backgroundColor = 0xffff0000;
const child = new RenderNode();
child.frame = {
  x: 10,
  y: 10,
  width: 50,
  height: 50
};
child.backgroundColor = 0xff00ff00;
renderNode.appendChild(child);

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      // Append a child node to the RenderNode.
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }
  }
}
```

## clearChildren

```TypeScript
clearChildren(): void
```

Clears all child nodes of this RenderNode.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-clearChildren(): void--><!--Device-RenderNode-clearChildren(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Examples

```TypeScript
import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

const renderNode = new RenderNode();
renderNode.size = { width: 200, height: 300 };
for (let i = 0; i < 10; i++) {
  let childNode = new RenderNode();
  childNode.size = { width: i * 10, height: i * 10 };
  childNode.position = { x: i * 10, y: i * 10 };
  childNode.backgroundColor = 0xFF0000FF - 0X11 * i;
  renderNode.appendChild(childNode);
}

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.myNodeController)
        .borderWidth(1)
        .width(200)
        .height(300)
      Button('clearChildren')
        .onClick(() => {
          renderNode.clearChildren(); // Remove all child nodes from the renderNode.
        })
    }.width('100%')
  }
}
```

## constructor

```TypeScript
constructor()
```

Constructor used to create a RenderNode.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-constructor()--><!--Device-RenderNode-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Examples

```TypeScript
import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 100,
  height: 100
};
renderNode.backgroundColor = 0xffff0000;

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }
  }
}
```

## dispose

```TypeScript
dispose(): void
```

Releases this RenderNode immediately.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-dispose(): void--><!--Device-RenderNode-dispose(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Examples

```TypeScript
import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

const renderNode = new RenderNode();
renderNode.frame = { x: 0, y: 100, width: 100, height: 100 };
renderNode.backgroundColor = 0xffff0000;

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode!.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.size = { width: 200, height: 200 };
      rootRenderNode.backgroundColor = 0xff00ff00;
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }

  disposeRenderNode() {
    const rootRenderNode = this.rootNode!.getRenderNode();
    // Remove the renderNode from the parent node rootRenderNode before releasing it.
    if (rootRenderNode !== null) {
      rootRenderNode.removeChild(renderNode);
    }
    renderNode.dispose();
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 4 }) {
      NodeContainer(this.myNodeController)
      Button('RenderNode dispose')
        .onClick(() => {
          this.myNodeController.disposeRenderNode();
        })
        .width('100%')
    }
  }
}
```

## draw

```TypeScript
draw(context: DrawContext): void
```

Performs drawing. You need to implement this API. It is called when the RenderNode performs drawing.

Note: The Canvas provided in the [DrawContext](arkts-arkui-graphics-drawcontext-c.md#DrawContext) parameter is a temporary command-recording canvas, not the actual rendering canvas of the node. For usage instructions, see  
[Adjusting the Transformation Matrix of the Custom Drawing Canvas](../../../ui/arkts-user-defined-arktsNode-renderNode.md#adjusting-the-transformation-matrix-of-the-custom-drawing-canvas).

> **NOTE：**
> 
> During RenderNode initialization, the **draw** method is invoked twice. The first call occurs when the FrameNode
> is initially created, triggering the rendering process. The second call occurs when the modifier is initially
> set, which triggers drawing. All subsequent drawing processes are triggered by the modifier.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-draw(context: DrawContext): void--><!--Device-RenderNode-draw(context: DrawContext): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [DrawContext](arkts-arkui-graphics-drawcontext-c.md) | Yes |

## Examples

Code in ArkTS:

```TypeScript
// Index.ets
import bridge from 'libentry.so'; // The .so file is written and generated from your Node-API implementation.
import { RenderNode, FrameNode, NodeController, DrawContext } from '@kit.ArkUI';

// Extend RenderNode to implement custom drawing.
class MyRenderNode extends RenderNode {
  uiContext: UIContext;

  constructor(uiContext: UIContext) {
    super();
    this.uiContext = uiContext;
  }

  // Invoked when the RenderNode undergoes drawing operations.
  draw(context: DrawContext) {
    // The width and height in the context need to be converted from vp to px.
    bridge.nativeOnDraw(0, context, this.uiContext.vp2px(context.size.width), this.uiContext.vp2px(context.size.height));
  }
}

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      const renderNode = new MyRenderNode(uiContext);
      renderNode.size = { width: 100, height: 100 };
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();
  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }
  }
}
```

The C++ side can obtain the canvas through the Node-API and perform subsequent custom drawing operations.

```TypeScript
// native_bridge.cpp
#include "napi/native_api.h"
#include <native_drawing/drawing_canvas.h>
#include <native_drawing/drawing_color.h>
#include <native_drawing/drawing_path.h>
#include <native_drawing/drawing_pen.h>

static napi_value OnDraw(napi_env env, napi_callback_info info)
{
    size_t argc = 4;
    napi_value args[4] = { nullptr };
    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

    int32_t id;
    napi_get_value_int32(env, args[0], &id);
    
    // Obtain the pointer to the canvas.
    void* temp = nullptr;
    napi_unwrap(env, args[1], &temp);
    OH_Drawing_Canvas *canvas = reinterpret_cast<OH_Drawing_Canvas*>(temp);
    
    // Obtain the canvas width.
    int32_t width;
    napi_get_value_int32(env, args[2], &width);
    
    // Obtain the canvas height.
    int32_t height;
    napi_get_value_int32(env, args[3], &height);
    
    // Pass in information such as the canvas, height, and width to the drawing API for custom drawing.
    auto path = OH_Drawing_PathCreate();
    OH_Drawing_PathMoveTo(path, width / 4, height / 4);
    OH_Drawing_PathLineTo(path, width * 3 / 4, height / 4);
    OH_Drawing_PathLineTo(path, width * 3 / 4, height * 3 / 4);
    OH_Drawing_PathLineTo(path, width / 4, height * 3 / 4);
    OH_Drawing_PathLineTo(path, width / 4, height / 4);
    OH_Drawing_PathClose(path);
    
    auto pen = OH_Drawing_PenCreate();
    OH_Drawing_PenSetWidth(pen, 10);
    OH_Drawing_PenSetColor(pen, OH_Drawing_ColorSetArgb(0xFF, 0xFF, 0x00, 0x00));
    OH_Drawing_CanvasAttachPen(canvas, pen);
    
    OH_Drawing_CanvasDrawPath(canvas, path);
    OH_Drawing_CanvasDetachPen(canvas);
    OH_Drawing_PenDestroy(pen);
    OH_Drawing_PathDestroy(path);

    return nullptr;
}

EXTERN_C_START
static napi_value Init(napi_env env, napi_value exports)
{
    napi_property_descriptor desc[] = {
        { "nativeOnDraw", nullptr, OnDraw, nullptr, nullptr, nullptr, napi_default, nullptr }
    };
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
    return exports;
}
EXTERN_C_END

static napi_module demoModule = {
    .nm_version = 1,
    .nm_flags = 0,
    .nm_filename = nullptr,
    .nm_register_func = Init,
    .nm_modname = "entry",
    .nm_priv = ((void*)0),
    .reserved = { 0 },
};

extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
{
    napi_module_register(&demoModule);
}
```

Add the following content to the src/main/cpp/CMakeLists.txt file of the project:

In the  file of the project, add the definition of the custom drawing API on the ArkTS side, for example:

```TypeScript
import { DrawContext } from '@kit.ArkUI';

export const nativeOnDraw: (id: number, context: DrawContext, width: number, height: number) => number;
```

## getChild

```TypeScript
getChild(index: number): RenderNode | null
```

Obtains the child node in the specified position of this RenderNode.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-getChild(index: number): RenderNode | null--><!--Device-RenderNode-getChild(index: number): RenderNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RenderNode](arkts-arkui-rendernode-c.md) |

## Examples

```TypeScript
import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

const renderNode = new RenderNode();
renderNode.size = { width: 200, height: 300 };
for (let i = 0; i < 10; i++) {
  let childNode = new RenderNode();
  childNode.size = { width: i * 10, height: i * 10 };
  childNode.position = { x: i * 10, y: i * 10 };
  childNode.backgroundColor = 0xFF0000FF - 0X11 * i;
  renderNode.appendChild(childNode);
}

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.myNodeController)
        .borderWidth(1)
        .width(200)
        .height(300)
      Button('getChild')
        .onClick(() => {
          for (let i = 0; i < 11; i++) {
            let childNode: RenderNode | null = renderNode.getChild(i);
            if (childNode === null) {
              // Return null if the renderNode has no child node at index 10.
              console.error(`the ${i} of renderNode's childNode is null`);
            } else {
              // Obtain the child node and log its attributes.
              console.info(`the ${i} of renderNode's childNode has a size of {${childNode.size.width},${childNode.size.height}}`);
            }
          }

        })
    }.width('100%')
  }
}
```

## getFirstChild

```TypeScript
getFirstChild(): RenderNode | null
```

Obtains the first child node of this RenderNode.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-getFirstChild(): RenderNode | null--><!--Device-RenderNode-getFirstChild(): RenderNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RenderNode](arkts-arkui-rendernode-c.md) |

## Examples

```TypeScript
import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 200,
  height: 350
};
renderNode.backgroundColor = 0xffff0000;
for (let i = 0; i < 5; i++) {
  const node = new RenderNode();
  node.frame = {
    x: 10,
    y: 10 + 60 * i,
    width: 50,
    height: 50
  };
  node.backgroundColor = 0xff00ff00;
  renderNode.appendChild(node);
}

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
        .width(200)
        .height(350)
      Button('getFirstChild')
        .onClick(() => {
          // Obtain the first child node of the renderNode.
          const firstChild = renderNode.getFirstChild();
          if (firstChild === null) {
            console.error(`the first child is null`);
          } else {
            console.info(`the position of first child is x: ${firstChild.position.x}, y: ${firstChild.position.y}`);
          }
        })
    }
  }
}
```

## getNextSibling

```TypeScript
getNextSibling(): RenderNode | null
```

Obtains the next sibling node of this RenderNode.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-getNextSibling(): RenderNode | null--><!--Device-RenderNode-getNextSibling(): RenderNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RenderNode](arkts-arkui-rendernode-c.md) |

## Examples

```TypeScript
import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 200,
  height: 350
};
renderNode.backgroundColor = 0xffff0000;
for (let i = 0; i < 5; i++) {
  const node = new RenderNode();
  node.frame = {
    x: 10,
    y: 10 + 60 * i,
    width: 50,
    height: 50
  };
  node.backgroundColor = 0xff00ff00;
  renderNode.appendChild(node);
}

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
        .width(200)
        .height(350)
      Button('getNextSibling')
        .onClick(() => {
          const child = renderNode.getChild(1);
          if (child === null) {
            console.error(`the child is null`);
          } else {
            // Obtain the child node with sequence number 1 of the renderNode, and then obtain its next sibling node.
            const nextSibling = child.getNextSibling();
            if (nextSibling === null) {
              console.error(`the nextSibling is null`);
            } else {
              console.info(`the position of child is x: ${child.position.x}, y: ${child.position.y}, the position of nextSibling is x: ${nextSibling.position.x}, y: ${nextSibling.position.y}`);
            }
          }
        })
    }
  }
}
```

## getPreviousSibling

```TypeScript
getPreviousSibling(): RenderNode | null
```

Obtains the previous sibling node of this RenderNode.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-getPreviousSibling(): RenderNode | null--><!--Device-RenderNode-getPreviousSibling(): RenderNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RenderNode](arkts-arkui-rendernode-c.md) |

## Examples

```TypeScript
import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 200,
  height: 350
};
renderNode.backgroundColor = 0xffff0000;
for (let i = 0; i < 5; i++) {
  const node = new RenderNode();
  node.frame = {
    x: 10,
    y: 10 + 60 * i,
    width: 50,
    height: 50
  };
  node.backgroundColor = 0xff00ff00;
  renderNode.appendChild(node);
}

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
        .width(200)
        .height(350)
      Button('getPreviousSibling')
        .onClick(() => {
          const child = renderNode.getChild(1);
          if (child === null) {
            console.error(`the child is null`);
          } else {
            // Obtain the child node with sequence number 1 of the renderNode, and then obtain its previous sibling node.
            const previousSibling = child.getPreviousSibling();
            if (previousSibling === null) {
              console.error(`the previousSibling is null`);
            } else {
              console.info(`the position of child is x: ${child.position.x}, y: ${child.position.y}, the position of previousSibling is x: ${previousSibling.position.x}, y: ${previousSibling.position.y}`);
            }
          }
        })
    }
  }
}
```

## insertChildAfter

```TypeScript
insertChildAfter(child: RenderNode, sibling: RenderNode | null): void
```

Inserts a child node after the specified child node of this RenderNode.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-insertChildAfter(child: RenderNode, sibling: RenderNode | null): void--><!--Device-RenderNode-insertChildAfter(child: RenderNode, sibling: RenderNode | null): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| child | [RenderNode](arkts-arkui-rendernode-c.md) | Yes |
| sibling | [RenderNode](arkts-arkui-rendernode-c.md) \| null | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100025](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-node.md#100025-invalid-parameter-value) |

## Examples

```TypeScript
import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 200,
  height: 350
};
renderNode.backgroundColor = 0xffff0000;
for (let i = 0; i < 5; i++) {
  const node = new RenderNode();
  node.frame = {
    x: 10,
    y: 10 + 60 * i,
    width: 50,
    height: 50
  };
  node.backgroundColor = 0xff00ff00;
  renderNode.appendChild(node);
}

const child = new RenderNode();
child.frame = {
  x: 70,
  y: 70,
  width: 50,
  height: 50
};
child.backgroundColor = 0xffffff00;
const sibling = renderNode.getChild(1);
// Insert a child node after the sibling node.
renderNode.insertChildAfter(child, sibling);

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }
  }
}
```

## invalidate

```TypeScript
invalidate(): void
```

Triggers the re-rendering of this RenderNode.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-invalidate(): void--><!--Device-RenderNode-invalidate(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Examples

```TypeScript
import bridge from 'libentry.so'; // The .so file is written and generated by your Node-API implementation.
import { RenderNode, FrameNode, NodeController, DrawContext } from '@kit.ArkUI';

// Extend RenderNode to implement custom drawing.
class MyRenderNode extends RenderNode {
  uiContext: UIContext;

  constructor(uiContext: UIContext) {
    super();
    this.uiContext = uiContext;
  }

  draw(context: DrawContext) {
    // The width and height in the context need to be converted from vp to px.
    bridge.nativeOnDraw(0, context, this.uiContext.vp2px(context.size.width), this.uiContext.vp2px(context.size.height));
  }
}

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;
  newNode: MyRenderNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode === null) {
      return this.rootNode;
    }
    this.newNode = new MyRenderNode(uiContext);
    this.newNode.size = { width: 100, height: 100 };
    renderNode.appendChild(this.newNode);
    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      Column() {
        NodeContainer(this.myNodeController)
          .width('100%')
        Button('Invalidate')
          .onClick(() => {
            // Trigger re-rendering of the RenderNode.
            this.myNodeController.newNode?.invalidate();
          })
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}
```

## isDisposed

```TypeScript
isDisposed(): boolean
```

Checks whether this RenderNode object has released its reference to its backend entity node. Frontend nodes maintain references to corresponding backend entity nodes. After a node calls the **dispose** API to release this reference, subsequent API calls may cause crashes or return default values. This API facilitates validation of node validity prior to operations, thereby mitigating risks in scenarios where calls after disposal are required.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-RenderNode-isDisposed(): boolean--><!--Device-RenderNode-isDisposed(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

const renderNode = new RenderNode();
renderNode.frame = { x: 100, y: 100, width: 100, height: 100 };
renderNode.backgroundColor = 0xff2787d9;

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode!.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.size = { width: 300, height: 300 };
      rootRenderNode.backgroundColor = 0xffd5d5d5;
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }

  disposeRenderNode() {
    const rootRenderNode = this.rootNode!.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.removeChild(renderNode);
    }
    renderNode.dispose();
  }

  isDisposed() : string {
    if (renderNode !== null) {
      // Check whether the RenderNode's reference to the backend node is released.
      if (renderNode.isDisposed()) {
        return 'renderNode isDisposed is true';
      } else {
        return 'renderNode isDisposed is false';
      }
    }
    return 'renderNode is null';
  }
}

@Entry
@Component
struct Index {
  @State text: string = ''
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 4 }) {
      NodeContainer(this.myNodeController)
      Button('RenderNode dispose')
        .onClick(() => {
          this.myNodeController.disposeRenderNode();
          this.text = '';
        })
        .width(200)
        .height(50)
      Button('RenderNode isDisposed')
        .onClick(() => {
          this.text = this.myNodeController.isDisposed();
        })
        .width(200)
        .height(50)
      Text(this.text)
        .fontSize(25)
    }
    .width('100%')
    .height('100%')
  }
}
```

## removeChild

```TypeScript
removeChild(node: RenderNode): void
```

Deletes the specified child node from this RenderNode.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-removeChild(node: RenderNode): void--><!--Device-RenderNode-removeChild(node: RenderNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [RenderNode](arkts-arkui-rendernode-c.md) | Yes |

## Examples

```TypeScript
import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 200,
  height: 350
};
renderNode.backgroundColor = 0xffff0000;
for (let i = 0; i < 5; i++) {
  const node = new RenderNode();
  node.frame = {
    x: 10,
    y: 10 + 60 * i,
    width: 50,
    height: 50
  };
  node.backgroundColor = 0xff00ff00;
  renderNode.appendChild(node);
}

// Remove the child node at index 1 from the renderNode.
const node = renderNode.getChild(1);
renderNode.removeChild(node);

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }
  }
}
```

## backgroundBlur

```TypeScript
get backgroundBlur(): BackgroundBlur
```

Get the background blur effect.

**Type:** [BackgroundBlur](arkts-arkui-graphics-backgroundblur-i.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-RenderNode-get backgroundBlur(): BackgroundBlur--><!--Device-RenderNode-get backgroundBlur(): BackgroundBlur-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
get backgroundColor(): number
```

Get the background color of the RenderNode.

**Type:** number

**Default:** 0X00000000 [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get backgroundColor(): number--><!--Device-RenderNode-get backgroundColor(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderColor

```TypeScript
get borderColor(): Edges<number>
```

Get border color of the RenderNode.

**Type:** [Edges](arkts-arkui-graphics-edges-i.md)&lt;number&gt;

**Default:** 0XFF000000

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get borderColor(): Edges<number>--><!--Device-RenderNode-get borderColor(): Edges<number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderRadius

```TypeScript
get borderRadius(): BorderRadiuses
```

Get border radius of the RenderNode.

**Type:** [BorderRadiuses](arkts-arkui-borderradiuses-t.md)

**Default:** 0

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get borderRadius(): BorderRadiuses--><!--Device-RenderNode-get borderRadius(): BorderRadiuses-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderStyle

```TypeScript
get borderStyle(): Edges<BorderStyle>
```

Get border style of the RenderNode.

**Type:** [Edges](arkts-arkui-graphics-edges-i.md)&lt;[BorderStyle](arkts-arkui-borderstyle-e.md)&gt;

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get borderStyle(): Edges<BorderStyle>--><!--Device-RenderNode-get borderStyle(): Edges<BorderStyle>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderWidth

```TypeScript
get borderWidth(): Edges<number>
```

Get border width of the RenderNode.

**Type:** [Edges](arkts-arkui-graphics-edges-i.md)&lt;number&gt;

**Default:** 0

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get borderWidth(): Edges<number>--><!--Device-RenderNode-get borderWidth(): Edges<number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## clipToFrame

```TypeScript
get clipToFrame(): boolean
```

Get whether the RenderNode clip to frame.

**Type:** boolean

**Default:** true [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get clipToFrame(): boolean--><!--Device-RenderNode-get clipToFrame(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentBlur

```TypeScript
get contentBlur(): ContentBlur
```

Get the content blur effect.

**Type:** [ContentBlur](arkts-arkui-graphics-contentblur-i.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-RenderNode-get contentBlur(): ContentBlur--><!--Device-RenderNode-get contentBlur(): ContentBlur-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## foregroundBlur

```TypeScript
get foregroundBlur(): ForegroundBlur
```

Get the foreground blur effect.

**Type:** [ForegroundBlur](arkts-arkui-graphics-foregroundblur-i.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-RenderNode-get foregroundBlur(): ForegroundBlur--><!--Device-RenderNode-get foregroundBlur(): ForegroundBlur-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## frame

```TypeScript
get frame(): Frame
```

Get frame info of the RenderNode.

**Type:** [Frame](arkts-arkui-graphics-frame-i.md)

**Default:** Frame { x: 0, y: 0, width: 0, height: 0 } [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get frame(): Frame--><!--Device-RenderNode-get frame(): Frame-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## label

```TypeScript
get label(): string
```

Get label of the RenderNode.

**Type:** string

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get label(): string--><!--Device-RenderNode-get label(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lengthMetricsUnit

```TypeScript
get lengthMetricsUnit(): LengthMetricsUnit
```

Get the length metrics unit of RenderNode.

**Type:** [LengthMetricsUnit](arkts-arkui-graphics-lengthmetricsunit-e.md)

**Default:** LengthMetricsUnit.DEFAULT

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get lengthMetricsUnit(): LengthMetricsUnit--><!--Device-RenderNode-get lengthMetricsUnit(): LengthMetricsUnit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## markNodeGroup

```TypeScript
get markNodeGroup(): boolean
```

Get whether to preferentially draw the node and its children.

**Type:** boolean

**Default:** false

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get markNodeGroup(): boolean--><!--Device-RenderNode-get markNodeGroup(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## opacity

```TypeScript
get opacity(): number
```

Get opacity of the RenderNode.

**Type:** number

**Default:** 1 [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get opacity(): number--><!--Device-RenderNode-get opacity(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pivot

```TypeScript
get pivot(): Pivot
```

Get pivot vector of the RenderNode.

**Type:** [Pivot](arkts-arkui-pivot-t.md)

**Default:** Pivot { x: 0.5, y: 0.5 } [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get pivot(): Pivot--><!--Device-RenderNode-get pivot(): Pivot-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## position

```TypeScript
get position(): Position
```

Get frame position of the RenderNode.

**Type:** [Position](arkts-arkui-position-t.md)

**Default:** Position { x: 0, y: 0 } [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get position(): Position--><!--Device-RenderNode-get position(): Position-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rotation

```TypeScript
get rotation(): Rotation
```

Get rotation vector of the RenderNode.

**Type:** [Rotation](arkts-arkui-rotation-t.md)

**Default:** Rotation { x: 0, y: 0, z: 0 } [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get rotation(): Rotation--><!--Device-RenderNode-get rotation(): Rotation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scale

```TypeScript
get scale(): Scale
```

Get scale vector of the RenderNode.

**Type:** [Scale](arkts-arkui-scale-t.md)

**Default:** Scale { x: 1, y: 1 } [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get scale(): Scale--><!--Device-RenderNode-get scale(): Scale-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowAlpha

```TypeScript
get shadowAlpha(): number
```

Get shadow alpha of the RenderNode.

**Type:** number

**Default:** 0 [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get shadowAlpha(): number--><!--Device-RenderNode-get shadowAlpha(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowColor

```TypeScript
get shadowColor(): number
```

Get shadow color of the RenderNode.

**Type:** number

**Default:** 0X00000000 [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get shadowColor(): number--><!--Device-RenderNode-get shadowColor(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowElevation

```TypeScript
get shadowElevation(): number
```

Get shadow elevation of the RenderNode.

**Type:** number

**Default:** 0 [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get shadowElevation(): number--><!--Device-RenderNode-get shadowElevation(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowOffset

```TypeScript
get shadowOffset(): Offset
```

Get shadow offset of the RenderNode.

**Type:** [Offset](arkts-arkui-offset-t.md)

**Default:** Offset { x: 0, y: 0 } [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get shadowOffset(): Offset--><!--Device-RenderNode-get shadowOffset(): Offset-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowRadius

```TypeScript
get shadowRadius(): number
```

Get shadow radius of the RenderNode.

**Type:** number

**Default:** 0 [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get shadowRadius(): number--><!--Device-RenderNode-get shadowRadius(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shapeClip

```TypeScript
get shapeClip(): ShapeClip
```

Get shape clip of the RenderNode.

**Type:** [ShapeClip](arkts-arkui-graphics-shapeclip-c.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get shapeClip(): ShapeClip--><!--Device-RenderNode-get shapeClip(): ShapeClip-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shapeMask

```TypeScript
get shapeMask(): ShapeMask
```

Get shape mask of the RenderNode.

**Type:** [ShapeMask](arkts-arkui-graphics-shapemask-c.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get shapeMask(): ShapeMask--><!--Device-RenderNode-get shapeMask(): ShapeMask-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## size

```TypeScript
get size(): Size
```

Get frame size of the RenderNode.

**Type:** [Size](arkts-arkui-graphics-size-i.md)

**Default:** Size { width: 0, height: 0 } [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get size(): Size--><!--Device-RenderNode-get size(): Size-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## transform

```TypeScript
get transform(): Matrix4
```

Get transform info of the RenderNode.

**Type:** [Matrix4](arkts-arkui-matrix4-t.md)

**Default:** Matrix4 [ 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ] [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get transform(): Matrix4--><!--Device-RenderNode-get transform(): Matrix4-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## translation

```TypeScript
get translation(): Translation
```

Get translation vector of the RenderNode.

**Type:** [Translation](arkts-arkui-translation-t.md)

**Default:** Translation { x: 0, y: 0 } [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RenderNode-get translation(): Translation--><!--Device-RenderNode-get translation(): Translation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
