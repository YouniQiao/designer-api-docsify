# SelectFrameNode

定义Select类型的FrameNode。

**Inheritance/Implementation:** SelectFrameNode extends [TypedFrameNode<SelectAttribute>](TypedFrameNode<SelectAttribute>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-typeNode-abstract class SelectFrameNode extends TypedFrameNode<SelectAttribute>--><!--Device-typeNode-abstract class SelectFrameNode extends TypedFrameNode<SelectAttribute>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(value: Array<SelectOption>): SelectAttribute
```

初始化Select类型的FrameNode。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectFrameNode-abstract initialize(value: Array<SelectOption>): SelectAttribute--><!--Device-SelectFrameNode-abstract initialize(value: Array<SelectOption>): SelectAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;[SelectOption](../arkts-components/arkts-arkui-selectoption-i.md)&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [SelectAttribute](../arkts-components/arkts-arkui-select-attribute.md) |  |

