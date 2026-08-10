# GestureHandler

手势处理器的基础类型。

**Inheritance/Implementation:** GestureHandler implements [GestureInterface<T>](GestureInterface<T>)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare class GestureHandler<T> implements GestureInterface<T>--><!--Device-unnamed-declare class GestureHandler<T> implements GestureInterface<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## allowedTypes

```TypeScript
allowedTypes(types: Array<SourceTool>): T
```

设置手势处理器所支持的事件输入源。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-GestureHandler-allowedTypes(types: Array<SourceTool>): T--><!--Device-GestureHandler-allowedTypes(types: Array<SourceTool>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| types | Array&lt;[SourceTool](../arkts-components/arkts-arkui-sourcetool-e.md)&gt; | Yes | 手势处理器所支持的事件输入源。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回当前组件。 |

## tag

```TypeScript
tag(tag: string): T
```

设置手势处理器的标志。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GestureHandler-tag(tag: string): T--><!--Device-GestureHandler-tag(tag: string): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tag | string | Yes | 手势处理器的标志。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回当前组件。 |

