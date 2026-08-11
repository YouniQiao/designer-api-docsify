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
| nodeType | 'Text' | 是 |

**返回值：**

| 类型 |
| --- |
| [Text](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-text-c.md) |


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
| nodeType | 'Column' | 是 |

**返回值：**

| 类型 |
| --- |
| [Column](arkts-arkui-typenode-column-t.md) |


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
| nodeType | 'Row' | 是 |

**返回值：**

| 类型 |
| --- |
| [Row](arkts-arkui-typenode-row-t.md) |


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
| nodeType | 'Stack' | 是 |

**返回值：**

| 类型 |
| --- |
| [Stack](../../apis-arkts/arkts-apis/arkts-arkts-util-stack-stack-c.md) |


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
| nodeType | 'GridRow' | 是 |

**返回值：**

| 类型 |
| --- |
| [GridRow](arkts-arkui-typenode-gridrow-t.md) |


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
| nodeType | 'GridCol' | 是 |

**返回值：**

| 类型 |
| --- |
| [GridCol](arkts-arkui-typenode-gridcol-t.md) |


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
| nodeType | 'Flex' | 是 |

**返回值：**

| 类型 |
| --- |
| [Flex](arkts-arkui-typenode-flex-t.md) |


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
| nodeType | 'Swiper' | 是 |

**返回值：**

| 类型 |
| --- |
| [Swiper](arkts-arkui-typenode-swiper-t.md) |


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
| nodeType | 'Progress' | 是 |

**返回值：**

| 类型 |
| --- |
| [Progress](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-progress-i.md) |


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
| nodeType | 'Scroll' | 是 |

**返回值：**

| 类型 |
| --- |
| [Scroll](arkts-arkui-typenode-scroll-t.md) |


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
| nodeType | 'RelativeContainer' | 是 |

**返回值：**

| 类型 |
| --- |
| [RelativeContainer](arkts-arkui-typenode-relativecontainer-t.md) |


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
| nodeType | 'Divider' | 是 |

**返回值：**

| 类型 |
| --- |
| [Divider](arkts-arkui-typenode-divider-t.md) |


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
| nodeType | 'LoadingProgress' | 是 |

**返回值：**

| 类型 |
| --- |
| [LoadingProgress](arkts-arkui-typenode-loadingprogress-t.md) |


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
| nodeType | 'Search' | 是 |

**返回值：**

| 类型 |
| --- |
| [Search](arkts-arkui-typenode-search-t.md) |


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
| nodeType | 'Blank' | 是 |

**返回值：**

| 类型 |
| --- |
| [Blank](arkts-arkui-typenode-blank-t.md) |


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
| nodeType | 'Image' | 是 |

**返回值：**

| 类型 |
| --- |
| [Image](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-image-i.md) |


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
| nodeType | 'List' | 是 |

**返回值：**

| 类型 |
| --- |
| [List](../../apis-arkts/arkts-apis/arkts-arkts-util-list-list-c.md) |


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
| nodeType | 'ListItem' | 是 |

**返回值：**

| 类型 |
| --- |
| [ListItem](arkts-arkui-typenode-listitem-t.md) |


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
| nodeType | 'TextInput' | 是 |

**返回值：**

| 类型 |
| --- |
| [TextInput](arkts-arkui-typenode-textinput-t.md) |


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
| nodeType | 'Button' | 是 |

**返回值：**

| 类型 |
| --- |
| [Button](arkts-arkui-system-prompt-button-i.md) |


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
| nodeType | 'ListItemGroup' | 是 |

**返回值：**

| 类型 |
| --- |
| [ListItemGroup](arkts-arkui-typenode-listitemgroup-t.md) |


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
| nodeType | 'WaterFlow' | 是 |

**返回值：**

| 类型 |
| --- |
| [WaterFlow](arkts-arkui-typenode-waterflow-t.md) |


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
| nodeType | 'FlowItem' | 是 |

**返回值：**

| 类型 |
| --- |
| [FlowItem](arkts-arkui-typenode-flowitem-t.md) |


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
| nodeType | 'XComponent' | 是 |

**返回值：**

| 类型 |
| --- |
| [XComponent](arkts-arkui-typenode-xcomponent-t.md) |


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
| nodeType | 'XComponent' | 是 |
| options | [XComponentOptions](../arkts-components/arkts-arkui-xcomponentoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [XComponent](arkts-arkui-typenode-xcomponent-t.md) |


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
| nodeType | 'XComponent' | 是 |
| parameters | [NativeXComponentParameters](../arkts-components/arkts-arkui-nativexcomponentparameters-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [XComponent](arkts-arkui-typenode-xcomponent-t.md) |


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
| nodeType | 'Checkbox' | 是 |

**返回值：**

| 类型 |
| --- |
| [Checkbox](arkts-arkui-typenode-checkbox-t.md) |


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
| nodeType | 'CheckboxGroup' | 是 |

**返回值：**

| 类型 |
| --- |
| [CheckboxGroup](arkts-arkui-typenode-checkboxgroup-t.md) |


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
| nodeType | 'Radio' | 是 |

**返回值：**

| 类型 |
| --- |
| [Radio](arkts-arkui-typenode-radio-t.md) |


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
| nodeType | 'Rating' | 是 |

**返回值：**

| 类型 |
| --- |
| [Rating](arkts-arkui-typenode-rating-t.md) |


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
| nodeType | 'Select' | 是 |

**返回值：**

| 类型 |
| --- |
| [Select](arkts-arkui-typenode-select-t.md) |


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
| nodeType | 'Slider' | 是 |

**返回值：**

| 类型 |
| --- |
| [Slider](arkts-arkui-typenode-slider-t.md) |


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
| nodeType | 'Toggle' | 是 |
| options | [ToggleOptions](../arkts-components/arkts-arkui-toggleoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [Toggle](arkts-arkui-typenode-toggle-t.md) |


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
| nodeType | 'Marquee' | 是 |

**返回值：**

| 类型 |
| --- |
| [Marquee](arkts-arkui-typenode-marquee-t.md) |


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
| nodeType | 'TextArea' | 是 |

**返回值：**

| 类型 |
| --- |
| [TextArea](arkts-arkui-typenode-textarea-t.md) |


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
| nodeType | 'SymbolGlyph' | 是 |

**返回值：**

| 类型 |
| --- |
| [SymbolGlyph](arkts-arkui-typenode-symbolglyph-t.md) |


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
| nodeType | 'QRCode' | 是 |

**返回值：**

| 类型 |
| --- |
| [QRCode](arkts-arkui-typenode-qrcode-t.md) |


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
| nodeType | 'Badge' | 是 |

**返回值：**

| 类型 |
| --- |
| [Badge](arkts-arkui-typenode-badge-t.md) |


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
| nodeType | 'TextClock' | 是 |

**返回值：**

| 类型 |
| --- |
| [TextClock](arkts-arkui-typenode-textclock-t.md) |


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
| nodeType | 'TextTimer' | 是 |

**返回值：**

| 类型 |
| --- |
| [TextTimer](arkts-arkui-typenode-texttimer-t.md) |


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
| nodeType | 'Grid' | 是 |

**返回值：**

| 类型 |
| --- |
| [Grid](arkts-arkui-typenode-grid-t.md) |


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
| nodeType | 'GridItem' | 是 |

**返回值：**

| 类型 |
| --- |
| [GridItem](arkts-arkui-typenode-griditem-t.md) |
