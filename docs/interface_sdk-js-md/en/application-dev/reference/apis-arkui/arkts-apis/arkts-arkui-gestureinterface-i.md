# GestureInterface

定义Gesture接口。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-interface GestureInterface<T>--><!--Device-unnamed-interface GestureInterface<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## allowedTypes

```TypeScript
allowedTypes(types: Array<SourceTool>): T
```

设置手势响应的输入类型。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-GestureInterface-allowedTypes(types: Array<SourceTool>): T--><!--Device-GestureInterface-allowedTypes(types: Array<SourceTool>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| types | Array&lt;[SourceTool](../arkts-components/arkts-arkui-sourcetool-e.md)&gt; | Yes | 手势响应的输入类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回当前组件。 |

## tag

```TypeScript
tag(tag: string): T
```

设置手势的标志。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-GestureInterface-tag(tag: string): T--><!--Device-GestureInterface-tag(tag: string): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tag | string | Yes | 手势的标志。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回当前组件。 |

