# getEvent

## getEvent

```TypeScript
function getEvent(node: FrameNode, nodeType: 'Scroll'): UIScrollEvent | undefined
```

Obtains the **UIScrollEvent** object associated with the **Scroll** node for configuring scroll events. The scroll events configured through this API coexist with declarative events without overriding them. If both event callbacks are registered, the declaratively defined event callback takes precedence.

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-typeNode-function getEvent(node: FrameNode, nodeType: 'Scroll'): UIScrollEvent | undefined--><!--Device-typeNode-function getEvent(node: FrameNode, nodeType: 'Scroll'): UIScrollEvent | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Scroll' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [UIScrollEvent](../arkts-components/arkts-arkui-uiscrollevent-i.md) |

**Examples**

See Scroll Event Example.


## getEvent

```TypeScript
function getEvent(node: FrameNode, nodeType: 'List'): UIListEvent | undefined
```

Obtains the **UIListEvent** object associated with the **List** node for configuring scroll events. The scroll events configured through this API coexist with declarative events without overriding them. If both event callbacks are registered, the declaratively defined event callback takes precedence.

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-typeNode-function getEvent(node: FrameNode, nodeType: 'List'): UIListEvent | undefined--><!--Device-typeNode-function getEvent(node: FrameNode, nodeType: 'List'): UIListEvent | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'List' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [UIListEvent](../arkts-components/arkts-arkui-uilistevent-i.md) |

**Examples**

See Scroll Event Example.


## getEvent

```TypeScript
function getEvent(node: FrameNode, nodeType: 'WaterFlow'): UIWaterFlowEvent | undefined
```

Obtains the **UIWaterFlowEvent** object associated with the [WaterFlow](arkts-arkui-typenode-waterflow-t.md#waterflow) node for configuring scroll events. The scroll events configured through this API coexist with declarative events without overriding them. If both event callbacks are registered, the declaratively defined event callback takes precedence.

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-typeNode-function getEvent(node: FrameNode, nodeType: 'WaterFlow'): UIWaterFlowEvent | undefined--><!--Device-typeNode-function getEvent(node: FrameNode, nodeType: 'WaterFlow'): UIWaterFlowEvent | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'WaterFlow' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [UIWaterFlowEvent](../arkts-components/arkts-arkui-uiwaterflowevent-i.md) |

**Examples**

See Scroll Event Example.


## getEvent

```TypeScript
function getEvent(node: FrameNode, nodeType: 'Grid'): UIGridEvent | undefined
```

Obtains the **UIGridEvent** object associated with the **Grid** node for configuring scroll events. The scroll events configured through this API coexist with declarative events without overriding them. If both event callbacks are registered, the declaratively defined event callback takes precedence.

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-typeNode-function getEvent(node: FrameNode, nodeType: 'Grid'): UIGridEvent | undefined--><!--Device-typeNode-function getEvent(node: FrameNode, nodeType: 'Grid'): UIGridEvent | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes |
| [nodeType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenenodes-node-i.md) | 'Grid' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [UIGridEvent](../arkts-components/arkts-arkui-uigridevent-i.md) |

**Examples**

See Scroll Event Example.
