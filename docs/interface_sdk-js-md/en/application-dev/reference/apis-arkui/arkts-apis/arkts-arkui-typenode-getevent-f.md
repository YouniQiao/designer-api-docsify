# getEvent

## getEvent

```TypeScript
function getEvent(node: FrameNode, nodeType: 'Scroll'): UIScrollEvent | undefined
```

获取Scroll节点中持有的UIScrollEvent对象，用于设置滚动事件。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。设置的滚动事件与声明式定义的事件平行；设置的滚动事件不覆盖原有的声明式事件。同时设置两个事件回调的时候，优先回调声明式事件。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-typeNode-function getEvent(node: FrameNode, nodeType: 'Scroll'): UIScrollEvent | undefined--><!--Device-typeNode-function getEvent(node: FrameNode, nodeType: 'Scroll'): UIScrollEvent | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取事件时所需的目标节点。 |
| nodeType | 'Scroll' | Yes | 获取Scroll节点类型的滚动事件。 |

**Return value:**

| Type | Description |
| --- | --- |
| [UIScrollEvent](../arkts-components/arkts-arkui-uiscrollevent-i.md) | Scroll节点类型的滚动事件，若获取失败，则返回undefined。 |


## getEvent

```TypeScript
function getEvent(node: FrameNode, nodeType: 'List'): UIListEvent | undefined
```

获取List节点中持有的UIListEvent对象，用于设置滚动事件。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。设置的滚动事件与声明式定义的事件平行；设置的滚动事件不覆盖原有的声明式事件。同时设置两个事件回调的时候，优先回调声明式事件。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-typeNode-function getEvent(node: FrameNode, nodeType: 'List'): UIListEvent | undefined--><!--Device-typeNode-function getEvent(node: FrameNode, nodeType: 'List'): UIListEvent | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取事件时所需的目标节点。 |
| nodeType | 'List' | Yes | 获取List节点类型的滚动事件。 |

**Return value:**

| Type | Description |
| --- | --- |
| [UIListEvent](../arkts-components/arkts-arkui-uilistevent-i.md) | List节点类型的滚动事件，若获取失败，则返回undefined。 |


## getEvent

```TypeScript
function getEvent(node: FrameNode, nodeType: 'WaterFlow'): UIWaterFlowEvent | undefined
```

获取[WaterFlow](arkts-arkui-typenode-waterflow-t.md)节点中持有的UIWaterFlowEvent对象，用于设置滚动事件。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。设置的滚动事件与声明式定义的事件平行；设置的滚动事件不覆盖原有的声明式事件。同时设置两个事件回调的时候，优先回调声明式事件。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-typeNode-function getEvent(node: FrameNode, nodeType: 'WaterFlow'): UIWaterFlowEvent | undefined--><!--Device-typeNode-function getEvent(node: FrameNode, nodeType: 'WaterFlow'): UIWaterFlowEvent | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取事件时所需的目标节点。 |
| nodeType | 'WaterFlow' | Yes | 获取WaterFlow节点类型的滚动事件。 |

**Return value:**

| Type | Description |
| --- | --- |
| [UIWaterFlowEvent](../arkts-components/arkts-arkui-uiwaterflowevent-i.md) | WaterFlow节点类型的滚动事件，若获取失败，则返回undefined。 |


## getEvent

```TypeScript
function getEvent(node: FrameNode, nodeType: 'Grid'): UIGridEvent | undefined
```

获取Grid节点中持有的UIGridEvent对象，用于设置滚动事件。若该节点非ArkTS语言创建，则需要设置是否支持跨语言访问，如果不支持跨语言访问，则返回undefined。该接口不支持声明式方式创建的节点。设置的滚动事件与声明式定义的事件平行；设置的滚动事件不覆盖原有的声明式事件。同时设置两个事件回调的时候，优先回调声明式事件。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-typeNode-function getEvent(node: FrameNode, nodeType: 'Grid'): UIGridEvent | undefined--><!--Device-typeNode-function getEvent(node: FrameNode, nodeType: 'Grid'): UIGridEvent | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 获取事件时所需的目标节点。 |
| nodeType | 'Grid' | Yes | 获取Grid节点类型的滚动事件。 |

**Return value:**

| Type | Description |
| --- | --- |
| [UIGridEvent](../arkts-components/arkts-arkui-uigridevent-i.md) | Grid节点类型的滚动事件，若获取失败，则返回undefined。 |

