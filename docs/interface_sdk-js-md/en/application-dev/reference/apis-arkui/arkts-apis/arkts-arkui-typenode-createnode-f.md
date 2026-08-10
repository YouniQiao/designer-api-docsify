# createNode

## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Text'): Text
```

创建Text类型的FrameNode节点。使用typeNode创建Text节点时，当传入的UIContext对应的UI实例销毁后，调用该接口会返回一个无效的FrameNode节点，无法正常挂载和显示。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Text'): Text--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Text'): Text-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Text' | Yes | 创建Text类型的FrameNode节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Text](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-text-c.md) | Text类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Column'): Column
```

创建Column类型的FrameNode节点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Column'): Column--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Column'): Column-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Column' | Yes | 创建Column类型的FrameNode节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Column](arkts-arkui-typenode-column-t.md) | Column类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Row'): Row
```

创建Row类型的FrameNode节点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Row'): Row--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Row'): Row-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Row' | Yes | 创建Row类型的FrameNode节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Row](arkts-arkui-typenode-row-t.md) | Row类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Stack'): Stack
```

创建Stack类型的FrameNode节点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Stack'): Stack--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Stack'): Stack-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Stack' | Yes | 创建Stack类型的FrameNode节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Stack](arkts-arkui-typenode-stack-t.md) | Stack类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'GridRow'): GridRow
```

创建GridRow类型的FrameNode节点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'GridRow'): GridRow--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'GridRow'): GridRow-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'GridRow' | Yes | 创建GridRow类型的FrameNode节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [GridRow](arkts-arkui-typenode-gridrow-t.md) | GridRow类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'GridCol'): GridCol
```

创建GridCol类型的FrameNode节点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'GridCol'): GridCol--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'GridCol'): GridCol-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'GridCol' | Yes | 创建GridCol类型的FrameNode节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [GridCol](arkts-arkui-typenode-gridcol-t.md) | GridCol类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Flex'): Flex
```

创建Flex类型的FrameNode节点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Flex'): Flex--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Flex'): Flex-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Flex' | Yes | 创建Flex类型的FrameNode节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Flex](arkts-arkui-typenode-flex-t.md) | Flex类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Swiper'): Swiper
```

创建Swiper类型的FrameNode节点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Swiper'): Swiper--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Swiper'): Swiper-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Swiper' | Yes | 创建Swiper类型的FrameNode节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Swiper](arkts-arkui-typenode-swiper-t.md) | Swiper类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Progress'): Progress
```

创建Progress类型的FrameNode节点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Progress'): Progress--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Progress'): Progress-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Progress' | Yes | 创建Progress类型的FrameNode节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Progress](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-progress-i.md) | Progress类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Scroll'): Scroll
```

创建Scroll类型的FrameNode节点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Scroll'): Scroll--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Scroll'): Scroll-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Scroll' | Yes | 创建Scroll类型的FrameNode节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Scroll](arkts-arkui-typenode-scroll-t.md) | Scroll类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'RelativeContainer'): RelativeContainer
```

创建RelativeContainer类型的FrameNode节点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'RelativeContainer'): RelativeContainer--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'RelativeContainer'): RelativeContainer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'RelativeContainer' | Yes | 创建RelativeContainer类型的FrameNode节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RelativeContainer](arkts-arkui-typenode-relativecontainer-t.md) | RelativeContainer类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Divider'): Divider
```

创建Divider类型的FrameNode节点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Divider'): Divider--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Divider'): Divider-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Divider' | Yes | 创建Divider类型的FrameNode节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Divider](arkts-arkui-typenode-divider-t.md) | Divider类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'LoadingProgress'): LoadingProgress
```

创建LoadingProgress类型的FrameNode节点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'LoadingProgress'): LoadingProgress--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'LoadingProgress'): LoadingProgress-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'LoadingProgress' | Yes | 创建LoadingProgress类型的FrameNode节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [LoadingProgress](arkts-arkui-typenode-loadingprogress-t.md) | LoadingProgress类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Search'): Search
```

创建Search类型的FrameNode节点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Search'): Search--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Search'): Search-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Search' | Yes | 创建Search类型的FrameNode节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Search](arkts-arkui-typenode-search-t.md) | Search类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Blank'): Blank
```

创建Blank类型的FrameNode节点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Blank'): Blank--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Blank'): Blank-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Blank' | Yes | 创建Blank类型的FrameNode节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Blank](arkts-arkui-typenode-blank-t.md) | Blank类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Image'): Image
```

创建Image类型的FrameNode节点。使用typeNode创建Image节点时，当传入的UIContext对应的UI实例销毁后，调用该接口会返回一个无效的FrameNode节点，无法正常挂载和显示。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Image'): Image--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Image'): Image-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Image' | Yes | 创建Image类型的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Image](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-image-i.md) | Image类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'List'): List
```

创建List类型的FrameNode节点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'List'): List--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'List'): List-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'List' | Yes | 创建List类型的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [List](../../apis-arkts/arkts-apis/arkts-arkts-util-list-list-c.md) | List类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'ListItem'): ListItem
```

创建ListItem类型的FrameNode节点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'ListItem'): ListItem--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'ListItem'): ListItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'ListItem' | Yes | 创建ListItem类型的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ListItem](arkts-arkui-typenode-listitem-t.md) | ListItem类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'TextInput'): TextInput
```

创建TextInput类型的FrameNode节点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'TextInput'): TextInput--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'TextInput'): TextInput-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'TextInput' | Yes | 创建TextInput类型的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [TextInput](arkts-arkui-typenode-textinput-t.md) | TextInput类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Button'): Button
```

创建Button类型的FrameNode节点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Button'): Button--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Button'): Button-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Button' | Yes | 创建Button类型的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Button](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-mouseevent-button-e.md) | Button类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'ListItemGroup'): ListItemGroup
```

创建ListItemGroup类型的FrameNode节点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'ListItemGroup'): ListItemGroup--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'ListItemGroup'): ListItemGroup-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'ListItemGroup' | Yes | 创建ListItemGroup类型的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ListItemGroup](arkts-arkui-typenode-listitemgroup-t.md) | ListItemGroup类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'WaterFlow'): WaterFlow
```

创建WaterFlow类型的FrameNode节点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'WaterFlow'): WaterFlow--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'WaterFlow'): WaterFlow-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'WaterFlow' | Yes | 创建WaterFlow类型的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [WaterFlow](arkts-arkui-typenode-waterflow-t.md) | WaterFlow类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'FlowItem'): FlowItem
```

创建FlowItem类型的FrameNode节点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'FlowItem'): FlowItem--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'FlowItem'): FlowItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'FlowItem' | Yes | 创建FlowItem类型的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [FlowItem](arkts-arkui-typenode-flowitem-t.md) | FlowItem类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'XComponent'): XComponent
```

创建XComponent类型的FrameNode节点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'XComponent'): XComponent--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'XComponent'): XComponent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'XComponent' | Yes | 创建XComponent类型的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [XComponent](arkts-arkui-typenode-xcomponent-t.md) | XComponent类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'XComponent', options: XComponentOptions): XComponent
```

按照options中的配置参数创建XComponent类型的FrameNode节点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'XComponent', options: XComponentOptions): XComponent--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'XComponent', options: XComponentOptions): XComponent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'XComponent' | Yes | 创建XComponent类型的节点。 |
| options | [XComponentOptions](../arkts-components/arkts-arkui-xcomponentoptions-i.md) | Yes | 定义XComponent的具体配置参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [XComponent](arkts-arkui-typenode-xcomponent-t.md) | XComponent类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'XComponent', parameters: NativeXComponentParameters): XComponent
```

按照parameters中的配置参数创建XComponent类型的FrameNode节点。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'XComponent', parameters: NativeXComponentParameters): XComponent--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'XComponent', parameters: NativeXComponentParameters): XComponent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'XComponent' | Yes | 创建XComponent类型的节点。 |
| parameters | [NativeXComponentParameters](../arkts-components/arkts-arkui-nativexcomponentparameters-i.md) | Yes | 定义XComponent的具体配置参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [XComponent](arkts-arkui-typenode-xcomponent-t.md) | XComponent类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Checkbox'): Checkbox
```

创建Checkbox类型的FrameNode节点。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Checkbox'): Checkbox--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Checkbox'): Checkbox-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Checkbox' | Yes | 创建Checkbox类型的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Checkbox](arkts-arkui-typenode-checkbox-t.md) | Checkbox类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'CheckboxGroup'): CheckboxGroup
```

创建CheckboxGroup类型的FrameNode节点。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'CheckboxGroup'): CheckboxGroup--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'CheckboxGroup'): CheckboxGroup-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'CheckboxGroup' | Yes | 创建CheckboxGroup类型的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [CheckboxGroup](arkts-arkui-typenode-checkboxgroup-t.md) | CheckboxGroup类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Radio'): Radio
```

创建Radio类型的FrameNode节点。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Radio'): Radio--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Radio'): Radio-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Radio' | Yes | 创建Radio类型的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Radio](arkts-arkui-typenode-radio-t.md) | Radio类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Rating'): Rating
```

创建Rating类型的FrameNode节点。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Rating'): Rating--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Rating'): Rating-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Rating' | Yes | 创建Rating类型的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Rating](arkts-arkui-typenode-rating-t.md) | Rating类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Select'): Select
```

创建Select类型的FrameNode节点。使用typeNode创建Select节点时，当传入的UIContext对应的UI实例销毁后，调用该接口会返回一个无效的FrameNode节点，无法正常挂载和显示。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Select'): Select--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Select'): Select-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Select' | Yes | 创建Select类型的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Select](arkts-arkui-typenode-select-t.md) | Select类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Slider'): Slider
```

创建Slider类型的FrameNode节点。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Slider'): Slider--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Slider'): Slider-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Slider' | Yes | 创建Slider类型的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Slider](arkts-arkui-typenode-slider-t.md) | Slider类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Toggle', options?: ToggleOptions): Toggle
```

创建Toggle类型的FrameNode节点。使用typeNode创建Toggle节点时，当传入的UIContext对应的UI实例销毁后，调用该接口会返回一个无效的FrameNode节点，无法正常挂载和显示。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Toggle', options?: ToggleOptions): Toggle--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Toggle', options?: ToggleOptions): Toggle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Toggle' | Yes | 创建Toggle类型的节点。 |
| options | [ToggleOptions](../arkts-components/arkts-arkui-toggleoptions-i.md) | No | 创建Toggle节点的接口参数，仅可通过ToggleOptions中的type属性设置开关样式。不传入该参数时，需通过initialize接口设置 Toggle的type属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Toggle](arkts-arkui-typenode-toggle-t.md) | Toggle类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Marquee'): Marquee
```

创建Marquee类型的FrameNode节点。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Marquee'): Marquee--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Marquee'): Marquee-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Marquee' | Yes | 创建Marquee类型的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Marquee](arkts-arkui-typenode-marquee-t.md) | Marquee类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'TextArea'): TextArea
```

创建TextArea类型的FrameNode节点。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'TextArea'): TextArea--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'TextArea'): TextArea-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'TextArea' | Yes | 创建TextArea类型的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [TextArea](arkts-arkui-typenode-textarea-t.md) | TextArea类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'SymbolGlyph'): SymbolGlyph
```

创建SymbolGlyph类型的FrameNode节点。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'SymbolGlyph'): SymbolGlyph--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'SymbolGlyph'): SymbolGlyph-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'SymbolGlyph' | Yes | 创建SymbolGlyph类型的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SymbolGlyph](arkts-arkui-typenode-symbolglyph-t.md) | SymbolGlyph类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'QRCode'): QRCode
```

创建QRCode类型的FrameNode节点。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'QRCode'): QRCode--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'QRCode'): QRCode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'QRCode' | Yes | 创建QRCode类型的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [QRCode](arkts-arkui-typenode-qrcode-t.md) | QRCode类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Badge'): Badge
```

创建Badge类型的FrameNode节点。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Badge'): Badge--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Badge'): Badge-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Badge' | Yes | 创建Badge类型的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Badge](arkts-arkui-typenode-badge-t.md) | Badge类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'TextClock'): TextClock
```

创建TextClock类型的FrameNode节点。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'TextClock'): TextClock--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'TextClock'): TextClock-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'TextClock' | Yes | 创建TextClock类型的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [TextClock](arkts-arkui-typenode-textclock-t.md) | TextClock类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'TextTimer'): TextTimer
```

创建TextTimer类型的FrameNode节点。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'TextTimer'): TextTimer--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'TextTimer'): TextTimer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'TextTimer' | Yes | 创建TextTimer类型的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [TextTimer](arkts-arkui-typenode-texttimer-t.md) | TextTimer类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'Grid'): Grid
```

创建Grid类型的FrameNode节点。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Grid'): Grid--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'Grid'): Grid-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'Grid' | Yes | 创建Grid类型的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Grid](arkts-arkui-typenode-grid-t.md) | Grid类型的FrameNode节点。 |


## createNode

```TypeScript
function createNode(context: UIContext, nodeType: 'GridItem'): GridItem
```

创建GridItem类型的FrameNode节点。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-typeNode-function createNode(context: UIContext, nodeType: 'GridItem'): GridItem--><!--Device-typeNode-function createNode(context: UIContext, nodeType: 'GridItem'): GridItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 创建对应节点时所需的UI上下文。 |
| nodeType | 'GridItem' | Yes | 创建GridItem类型的节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| [GridItem](arkts-arkui-typenode-griditem-t.md) | GridItem类型的FrameNode节点。 |

