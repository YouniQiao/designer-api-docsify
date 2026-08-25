# bindController

## bindController

```TypeScript
export function bindController(node: FrameNode, controller: TextController, nodeType: 'Text'): void
```

Binds a [TextController](../arkts-components/arkts-arkui-textcontroller-c.md) instance to a [Text](arkts-arkui-typenode-text-t.md) node. Cross-language access must be enabled for nodes not created via ArkTS; otherwise, an exception will be thrown. This API does not support declaratively created nodes.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

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
| [100023](../errorcode-node.md#100023-parameter-error) |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |


## bindController

```TypeScript
export function bindController(node: FrameNode, controller: SwiperController, nodeType: 'Swiper'): void
```

Binds a [SwiperController](../arkts-components/arkts-arkui-swipercontroller-c.md) instance to the [Swiper](arkts-arkui-typenode-swiper-t.md) node. Cross- language access must be enabled for nodes not created via ArkTS; otherwise, an exception will be thrown. This API does not support declaratively created nodes.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

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
| [100023](../errorcode-node.md#100023-parameter-error) |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |


## bindController

```TypeScript
function bindController(node: FrameNode, controller: Scroller, nodeType: 'Scroll'): void
```

Binds the [Scroller](../arkts-components/arkts-arkui-scroller-c.md) to the [Scroll](arkts-arkui-typenode-scroll-t.md) node. Cross-language access must be enabled for nodes not created via ArkTS; otherwise, an exception will be thrown. This API supports declaratively created nodes since API version 26.0.0.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |


## bindController

```TypeScript
export function bindController(node: FrameNode, controller: Scroller, nodeType: 'List'): void
```

Binds a [Scroller](../arkts-components/arkts-arkui-scroller-c.md) instance to the [List](arkts-arkui-typenode-list-t.md) node. Cross-language access must be enabled for nodes not created via ArkTS; otherwise, an exception will be thrown. This API supports declaratively created nodes since API version 26.0.0.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

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
| [100023](../errorcode-node.md#100023-parameter-error) |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |


## bindController

```TypeScript
export function bindController(node: FrameNode, controller: TextInputController, nodeType: 'TextInput'): void
```

Binds the [TextInputController](../arkts-components/arkts-arkui-textinputcontroller-c.md) to the [TextInput](arkts-arkui-typenode-textinput-t.md) node. Cross -language access must be enabled for nodes not created via ArkTS; otherwise, an exception will be thrown. This API supports declaratively created nodes since API version 26.0.0.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

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
| [100023](../errorcode-node.md#100023-parameter-error) |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |


## bindController

```TypeScript
export function bindController(node: FrameNode, controller: Scroller, nodeType: 'WaterFlow'): void
```

Binds a [Scroller](../arkts-components/arkts-arkui-scroller-c.md) instance to the [WaterFlow](arkts-arkui-typenode-waterflow-t.md) node. Cross-language access must be enabled for nodes not created via ArkTS; otherwise, an exception will be thrown. This API supports declaratively created nodes since API version 26.0.0.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

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
| [100023](../errorcode-node.md#100023-parameter-error) |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |


## bindController

```TypeScript
export function bindController(node: FrameNode, controller: TextAreaController, nodeType: 'TextArea'): void
```

Binds a [TextAreaController](../arkts-components/arkts-arkui-textareacontroller-c.md) instance to the [TextArea](arkts-arkui-typenode-textarea-t.md) node. Cross-language access must be enabled for nodes not created via ArkTS; otherwise, an exception will be thrown. This API supports declaratively created nodes since API version 26.0.0.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

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
| [100023](../errorcode-node.md#100023-parameter-error) |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |


## bindController

```TypeScript
export function bindController(node: FrameNode, controller: Scroller, nodeType: 'Grid'): void
```

Binds a [Scroller](../arkts-components/arkts-arkui-scroller-c.md) instance to the [Grid](arkts-arkui-typenode-grid-t.md) node. Cross-language access must be enabled for nodes not created via ArkTS; otherwise, an exception will be thrown. This API supports declaratively created nodes since API version 26.0.0.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

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
| [100023](../errorcode-node.md#100023-parameter-error) |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |
