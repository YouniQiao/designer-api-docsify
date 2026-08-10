# GestureHandler

手势处理器的基础类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class GestureHandler--><!--Device-unnamed-export declare class GestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## allowedTypes

```TypeScript
allowedTypes(types: Array<SourceTool>): this
```

设置手势处理器所支持的事件输入源。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureHandler-allowedTypes(types: Array<SourceTool>): this--><!--Device-GestureHandler-allowedTypes(types: Array<SourceTool>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| types | Array&lt;[SourceTool](../arkts-components/arkts-arkui-sourcetool-e.md)&gt; | Yes | 手势处理器所支持的事件输入源。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回当前组件。 |

## tag

```TypeScript
tag(tag: string): this
```

设置手势处理器的标志。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureHandler-tag(tag: string): this--><!--Device-GestureHandler-tag(tag: string): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tag | string | Yes | 手势处理器的标志。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回当前组件。 |

