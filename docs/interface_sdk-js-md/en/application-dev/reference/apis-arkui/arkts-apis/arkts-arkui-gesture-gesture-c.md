# Gesture

定义Gesture接口。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class Gesture--><!--Device-unnamed-export declare class Gesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## allowedTypes

```TypeScript
allowedTypes(types: Array<SourceTool>): this
```

设置手势响应的输入类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Gesture-allowedTypes(types: Array<SourceTool>): this--><!--Device-Gesture-allowedTypes(types: Array<SourceTool>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| types | Array&lt;[SourceTool](../arkts-components/arkts-arkui-sourcetool-e.md)&gt; | Yes | 手势响应的输入类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回当前组件。 |

## tag

```TypeScript
tag(tag: string): this
```

设置手势的标志。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Gesture-tag(tag: string): this--><!--Device-Gesture-tag(tag: string): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tag | string | Yes | 手势的标志。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回当前组件。 |

