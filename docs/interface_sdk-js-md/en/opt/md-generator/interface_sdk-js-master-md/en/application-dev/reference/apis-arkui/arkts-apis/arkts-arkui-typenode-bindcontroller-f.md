# bindController

## bindController

```TypeScript
export function bindController(node: FrameNode, controller: TextController, nodeType: 'Text'): void
```

Binds a [TextController](../arkts-components/arkts-arkui-textcontroller-c.md/arkts-arkui-textcontroller-c.md) instance to a [Text](arkts-arkui-typenode-text-t.md) node. Cross-language access must be enabled for nodes not created via ArkTS; otherwise, an exception will be thrown. This API does not support declaratively created nodes.

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
| nodeType | 'Text' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |
| [100023](../errorcode-node.md#100023-parameter-error) |


## bindController

```TypeScript
export function bindController(node: FrameNode, controller: SwiperController, nodeType: 'Swiper'): void
```

Binds a [SwiperController](../arkts-components/arkts-arkui-swipercontroller-c.md/arkts-arkui-swipercontroller-c.md) instance to the [Swiper](arkts-arkui-typenode-swiper-t.md) node. Cross-language access must be enabled for nodes not created via ArkTS; otherwise, an exception will be thrown. This API does not support declaratively created nodes.

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
| nodeType | 'Swiper' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |
| [100023](../errorcode-node.md#100023-parameter-error) |


## bindController

```TypeScript
function bindController(node: FrameNode, controller: Scroller, nodeType: 'Scroll'): void
```

Binds the [Scroller](../arkts-components/arkts-arkui-scroller-c.md/arkts-arkui-scroller-c.md) to the [Scroll](arkts-arkui-typenode-scroll-t.md) node. Cross-language access must be enabled for nodes not created via ArkTS; otherwise, an exception will be thrown. This API supports declaratively created nodes since API version 26.0.0.

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
| nodeType | 'Scroll' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |


## bindController

```TypeScript
export function bindController(node: FrameNode, controller: Scroller, nodeType: 'List'): void
```

Binds a [Scroller](../arkts-components/arkts-arkui-scroller-c.md/arkts-arkui-scroller-c.md) instance to the [List](arkts-arkui-typenode-list-t.md) node. Cross-language access must be enabled for nodes not created via ArkTS; otherwise, an exception will be thrown. This API supports declaratively created nodes since API version 26.0.0.

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
| nodeType | 'List' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |
| [100023](../errorcode-node.md#100023-parameter-error) |


## bindController

```TypeScript
export function bindController(node: FrameNode, controller: TextInputController, nodeType: 'TextInput'): void
```

Binds the [TextInputController](../arkts-components/arkts-arkui-textinputcontroller-c.md/arkts-arkui-textinputcontroller-c.md) to the [TextInput](arkts-arkui-typenode-textinput-t.md) node. Cross  
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
| nodeType | 'TextInput' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |
| [100023](../errorcode-node.md#100023-parameter-error) |


## bindController

```TypeScript
export function bindController(node: FrameNode, controller: Scroller, nodeType: 'WaterFlow'): void
```

Binds a [Scroller](../arkts-components/arkts-arkui-scroller-c.md/arkts-arkui-scroller-c.md) instance to the [WaterFlow](arkts-arkui-typenode-waterflow-t.md) node. Cross-language access must be enabled for nodes not created via ArkTS; otherwise, an exception will be thrown. This API supports declaratively created nodes since API version 26.0.0.

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
| nodeType | 'WaterFlow' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |
| [100023](../errorcode-node.md#100023-parameter-error) |


## bindController

```TypeScript
export function bindController(node: FrameNode, controller: TextAreaController, nodeType: 'TextArea'): void
```

Binds a [TextAreaController](../arkts-components/arkts-arkui-textareacontroller-c.md/arkts-arkui-textareacontroller-c.md) instance to the [TextArea](arkts-arkui-typenode-textarea-t.md) node.Cross-language access must be enabled for nodes not created via ArkTS; otherwise, an exception will be thrown. This API supports declaratively created nodes since API version 26.0.0.

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
| nodeType | 'TextArea' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |
| [100023](../errorcode-node.md#100023-parameter-error) |


## bindController

```TypeScript
export function bindController(node: FrameNode, controller: Scroller, nodeType: 'Grid'): void
```

Binds a [Scroller](../arkts-components/arkts-arkui-scroller-c.md/arkts-arkui-scroller-c.md) instance to the [Grid](arkts-arkui-typenode-grid-t.md) node. Cross-language access must be enabled for nodes not created via ArkTS; otherwise, an exception will be thrown. This API supports declaratively created nodes since API version 26.0.0.

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
| nodeType | 'Grid' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |
| [100023](../errorcode-node.md#100023-parameter-error) |
