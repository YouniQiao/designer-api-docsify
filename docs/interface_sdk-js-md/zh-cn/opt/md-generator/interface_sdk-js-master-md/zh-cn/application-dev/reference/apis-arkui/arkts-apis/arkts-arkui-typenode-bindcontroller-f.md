# bindController

## bindController

```TypeScript
export function bindController(node: FrameNode, controller: TextController, nodeType: 'Text'): void
```

将文本控制器[TextController](../arkts-components/arkts-arkui-textcontroller-c.md/arkts-arkui-textcontroller-c.md)绑定到[Text](arkts-arkui-typenode-text-t.md)节点。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则抛出异常。该接口不支持声明式方式创建的节点。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-export function bindController(node: FrameNode, controller: TextController, nodeType: 'Text'): void--><!--Device-typeNode-export function bindController(node: FrameNode, controller: TextController, nodeType: 'Text'): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | 是 |
| controller | [TextController](../arkts-components/arkts-arkui-textcontroller-c.md) | 是 |
| nodeType | 'Text' | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode节点不可修改) |
| [100023](../errorcode-node.md#100023-参数错误) |


## bindController

```TypeScript
export function bindController(node: FrameNode, controller: SwiperController, nodeType: 'Swiper'): void
```

将控制器[SwiperController](../arkts-components/arkts-arkui-swipercontroller-c.md/arkts-arkui-swipercontroller-c.md)绑定到[Swiper](arkts-arkui-typenode-swiper-t.md)节点。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则抛出异常。该接口不支持声明式方式创建的节点。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-export function bindController(node: FrameNode, controller: SwiperController, nodeType: 'Swiper'): void--><!--Device-typeNode-export function bindController(node: FrameNode, controller: SwiperController, nodeType: 'Swiper'): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | 是 |
| controller | [SwiperController](../arkts-components/arkts-arkui-swipercontroller-c.md) | 是 |
| nodeType | 'Swiper' | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode节点不可修改) |
| [100023](../errorcode-node.md#100023-参数错误) |


## bindController

```TypeScript
function bindController(node: FrameNode, controller: Scroller, nodeType: 'Scroll'): void
```

将滚动控制器[Scroller](../arkts-components/arkts-arkui-scroller-c.md/arkts-arkui-scroller-c.md)绑定到[Scroll](arkts-arkui-typenode-scroll-t.md)节点。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则抛出异常。从API version 26.0.0开始，该接口支持声明式方式创建的节点，API version 26.0.0以下版本不支持。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-function bindController(node: FrameNode, controller: Scroller, nodeType: 'Scroll'): void--><!--Device-typeNode-function bindController(node: FrameNode, controller: Scroller, nodeType: 'Scroll'): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | 是 |
| controller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | 是 |
| nodeType | 'Scroll' | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [100021](../errorcode-node.md#100021-framenode节点不可修改) |


## bindController

```TypeScript
export function bindController(node: FrameNode, controller: Scroller, nodeType: 'List'): void
```

将滚动控制器[Scroller](../arkts-components/arkts-arkui-scroller-c.md/arkts-arkui-scroller-c.md)绑定到[List](arkts-arkui-typenode-list-t.md)节点。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则抛出异常。从API version 26.0.0开始，该接口支持声明式方式创建的节点，API version 26.0.0以下版本不支持。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-export function bindController(node: FrameNode, controller: Scroller, nodeType: 'List'): void--><!--Device-typeNode-export function bindController(node: FrameNode, controller: Scroller, nodeType: 'List'): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | 是 |
| controller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | 是 |
| nodeType | 'List' | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode节点不可修改) |
| [100023](../errorcode-node.md#100023-参数错误) |


## bindController

```TypeScript
export function bindController(node: FrameNode, controller: TextInputController, nodeType: 'TextInput'): void
```

将输入框控制器[TextInputController](../arkts-components/arkts-arkui-textinputcontroller-c.md/arkts-arkui-textinputcontroller-c.md)绑定到[TextInput](arkts-arkui-typenode-textinput-t.md)节点。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则抛出异常。从API版本26.0.0开始，该接口支持声明式方式创建的节点，API版本26.0.0以下版本不支持。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-export function bindController(node: FrameNode, controller: TextInputController, nodeType: 'TextInput'): void--><!--Device-typeNode-export function bindController(node: FrameNode, controller: TextInputController, nodeType: 'TextInput'): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | 是 |
| controller | [TextInputController](../arkts-components/arkts-arkui-textinputcontroller-c.md) | 是 |
| nodeType | 'TextInput' | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode节点不可修改) |
| [100023](../errorcode-node.md#100023-参数错误) |


## bindController

```TypeScript
export function bindController(node: FrameNode, controller: Scroller, nodeType: 'WaterFlow'): void
```

将滚动控制器[Scroller](../arkts-components/arkts-arkui-scroller-c.md/arkts-arkui-scroller-c.md)绑定到[WaterFlow](arkts-arkui-typenode-waterflow-t.md)节点。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则抛出异常。从API version 26.0.0开始，该接口支持声明式方式创建的节点，API version 26.0.0以下版本不支持。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-export function bindController(node: FrameNode, controller: Scroller, nodeType: 'WaterFlow'): void--><!--Device-typeNode-export function bindController(node: FrameNode, controller: Scroller, nodeType: 'WaterFlow'): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | 是 |
| controller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | 是 |
| nodeType | 'WaterFlow' | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode节点不可修改) |
| [100023](../errorcode-node.md#100023-参数错误) |


## bindController

```TypeScript
export function bindController(node: FrameNode, controller: TextAreaController, nodeType: 'TextArea'): void
```

将输入框控制器[TextAreaController](../arkts-components/arkts-arkui-textareacontroller-c.md/arkts-arkui-textareacontroller-c.md)绑定到[TextArea](arkts-arkui-typenode-textarea-t.md)节点。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则抛出异常。从API版本26.0.0开始，该接口支持声明式方式创建的节点，API版本26.0.0以下版本不支持。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-export function bindController(node: FrameNode, controller: TextAreaController, nodeType: 'TextArea'): void--><!--Device-typeNode-export function bindController(node: FrameNode, controller: TextAreaController, nodeType: 'TextArea'): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | 是 |
| controller | [TextAreaController](../arkts-components/arkts-arkui-textareacontroller-c.md) | 是 |
| nodeType | 'TextArea' | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode节点不可修改) |
| [100023](../errorcode-node.md#100023-参数错误) |


## bindController

```TypeScript
export function bindController(node: FrameNode, controller: Scroller, nodeType: 'Grid'): void
```

将滚动控制器[Scroller](../arkts-components/arkts-arkui-scroller-c.md/arkts-arkui-scroller-c.md)绑定到[Grid](arkts-arkui-typenode-grid-t.md)节点。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则抛出异常。从API version 26.0.0开始，该接口支持声明式方式创建的节点，API version 26.0.0以下版本不支持。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-typeNode-export function bindController(node: FrameNode, controller: Scroller, nodeType: 'Grid'): void--><!--Device-typeNode-export function bindController(node: FrameNode, controller: Scroller, nodeType: 'Grid'): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | 是 |
| controller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | 是 |
| nodeType | 'Grid' | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode节点不可修改) |
| [100023](../errorcode-node.md#100023-参数错误) |
