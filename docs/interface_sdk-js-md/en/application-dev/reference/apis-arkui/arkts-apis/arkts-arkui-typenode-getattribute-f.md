# getAttribute

## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'Text'): TextAttribute | undefined
```

获取Text节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Text'): TextAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Text'): TextAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'Text' | Yes | 获取Text节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [TextAttribute](../arkts-components/arkts-arkui-text-attribute.md) | Text节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'Column'): ColumnAttribute | undefined
```

获取Column节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Column'): ColumnAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Column'): ColumnAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'Column' | Yes | 获取Column节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ColumnAttribute](../arkts-components/arkts-arkui-column-attribute.md) | Column节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'Row'): RowAttribute | undefined
```

获取Row节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Row'): RowAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Row'): RowAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'Row' | Yes | 获取Row节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RowAttribute](../arkts-components/arkts-arkui-row-attribute.md) | Row节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'Stack'): StackAttribute | undefined
```

获取Stack节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Stack'): StackAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Stack'): StackAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'Stack' | Yes | 获取Stack节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [StackAttribute](../arkts-components/arkts-arkui-stack-attribute.md) | Stack节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'Flex'): FlexAttribute | undefined
```

获取Flex节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Flex'): FlexAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Flex'): FlexAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'Flex' | Yes | 获取Flex节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [FlexAttribute](../arkts-components/arkts-arkui-flex-attribute.md) | Flex节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'Swiper'): SwiperAttribute | undefined
```

获取Swiper节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Swiper'): SwiperAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Swiper'): SwiperAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'Swiper' | Yes | 获取Swiper节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SwiperAttribute](../arkts-components/arkts-arkui-swiper-attribute.md) | Swiper节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'Progress'): ProgressAttribute | undefined
```

获取Progress节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Progress'): ProgressAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Progress'): ProgressAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'Progress' | Yes | 获取Progress节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ProgressAttribute](../arkts-components/arkts-arkui-progress-attribute.md) | Progress节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
function getAttribute(node: FrameNode, nodeType: 'Scroll'): ScrollAttribute | undefined
```

获取Scroll节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-typeNode-function getAttribute(node: FrameNode, nodeType: 'Scroll'): ScrollAttribute | undefined--><!--Device-typeNode-function getAttribute(node: FrameNode, nodeType: 'Scroll'): ScrollAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'Scroll' | Yes | 获取Scroll节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ScrollAttribute](../arkts-components/arkts-arkui-scroll-attribute.md) | Scroll节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'RelativeContainer'): RelativeContainerAttribute | undefined
```

获取RelativeContainer节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'RelativeContainer'): RelativeContainerAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'RelativeContainer'): RelativeContainerAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'RelativeContainer' | Yes | 获取RelativeContainer节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RelativeContainerAttribute](../arkts-components/arkts-arkui-relativecontainer-attribute.md) | RelativeContainer节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'LoadingProgress'): LoadingProgressAttribute | undefined
```

获取[LoadingProgress](../../apis-arkui/arkts-components/arkts-arkui-loading_progress-i)节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'LoadingProgress'): LoadingProgressAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'LoadingProgress'): LoadingProgressAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'LoadingProgress' | Yes | 获取LoadingProgress节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [LoadingProgressAttribute](../arkts-components/arkts-arkui-loadingprogress-attribute.md) | LoadingProgress节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'Image'): ImageAttribute | undefined
```

获取Image节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Image'): ImageAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Image'): ImageAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'Image' | Yes | 获取Image节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageAttribute](../arkts-components/arkts-arkui-image-attribute.md) | Image节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'List'): ListAttribute | undefined
```

获取List节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'List'): ListAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'List'): ListAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'List' | Yes | 获取List节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ListAttribute](../arkts-components/arkts-arkui-list-attribute.md) | List节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'ListItem'): ListItemAttribute | undefined
```

获取ListItem节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'ListItem'): ListItemAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'ListItem'): ListItemAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'ListItem' | Yes | 获取ListItem节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ListItemAttribute](../arkts-components/arkts-arkui-listitem-attribute.md) | ListItem节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'TextInput'): TextInputAttribute | undefined
```

获取TextInput节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'TextInput'): TextInputAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'TextInput'): TextInputAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'TextInput' | Yes | 获取TextInput节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [TextInputAttribute](../arkts-components/arkts-arkui-textinput-attribute.md) | TextInput节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'Button'): ButtonAttribute | undefined
```

获取Button节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Button'): ButtonAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Button'): ButtonAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'Button' | Yes | 获取Button节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ButtonAttribute](../arkts-components/arkts-arkui-button-attribute.md) | Button节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'ListItemGroup'): ListItemGroupAttribute | undefined
```

获取ListItemGroup节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'ListItemGroup'): ListItemGroupAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'ListItemGroup'): ListItemGroupAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'ListItemGroup' | Yes | 获取ListItemGroup节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ListItemGroupAttribute](../arkts-components/arkts-arkui-listitemgroup-attribute.md) | ListItemGroup节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'WaterFlow'): WaterFlowAttribute | undefined
```

获取WaterFlow节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'WaterFlow'): WaterFlowAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'WaterFlow'): WaterFlowAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'WaterFlow' | Yes | 获取WaterFlow节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [WaterFlowAttribute](../arkts-components/arkts-arkui-waterflow-attribute.md) | WaterFlow节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'FlowItem'): FlowItemAttribute | undefined
```

获取FlowItem节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'FlowItem'): FlowItemAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'FlowItem'): FlowItemAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'FlowItem' | Yes | 获取FlowItem节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [FlowItemAttribute](../arkts-components/arkts-arkui-flowitem-attribute.md) | FlowItem节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'XComponent'): XComponentAttribute | undefined
```

获取XComponent节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'XComponent'): XComponentAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'XComponent'): XComponentAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'XComponent' | Yes | 获取XComponent节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [XComponentAttribute](../arkts-components/arkts-arkui-xcomponent-attribute.md) | XComponent节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'Checkbox'): CheckboxAttribute | undefined
```

获取Checkbox节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Checkbox'): CheckboxAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Checkbox'): CheckboxAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'Checkbox' | Yes | 获取Checkbox节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [CheckboxAttribute](../arkts-components/arkts-arkui-checkbox-attribute.md) | Checkbox节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'Radio'): RadioAttribute | undefined
```

获取Radio节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Radio'): RadioAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Radio'): RadioAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'Radio' | Yes | 获取Radio节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RadioAttribute](../arkts-components/arkts-arkui-radio-attribute.md) | Radio节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'Slider'): SliderAttribute | undefined
```

获取Slider节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Slider'): SliderAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Slider'): SliderAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'Slider' | Yes | 获取Slider节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SliderAttribute](../arkts-components/arkts-arkui-slider-attribute.md) | Slider节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'Toggle'): ToggleAttribute | undefined
```

获取Toggle节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Toggle'): ToggleAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Toggle'): ToggleAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'Toggle' | Yes | 获取Toggle节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ToggleAttribute](../arkts-components/arkts-arkui-toggle-attribute.md) | Toggle节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'TextArea'): TextAreaAttribute | undefined
```

获取TextArea节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'TextArea'): TextAreaAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'TextArea'): TextAreaAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'TextArea' | Yes | 获取TextArea节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [TextAreaAttribute](../arkts-components/arkts-arkui-textarea-attribute.md) | TextArea节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'Grid'): GridAttribute | undefined
```

获取Grid节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Grid'): GridAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'Grid'): GridAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'Grid' | Yes | 获取Grid节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [GridAttribute](../arkts-components/arkts-arkui-grid-attribute.md) | Grid节点类型的属性，若获取失败，则返回undefined。 |


## getAttribute

```TypeScript
export function getAttribute(node: FrameNode, nodeType: 'GridItem'): GridItemAttribute | undefined
```

获取GridItem节点的属性。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'GridItem'): GridItemAttribute | undefined--><!--Device-typeNode-export function getAttribute(node: FrameNode, nodeType: 'GridItem'): GridItemAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取属性时所需的目标节点。 |
| nodeType | 'GridItem' | Yes | 获取GridItem节点类型的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [GridItemAttribute](../arkts-components/arkts-arkui-griditem-attribute.md) | GridItem节点类型的属性，若获取失败，则返回undefined。 |

