# SelectionContainer

## Modules to Import

```TypeScript
import { SelectionContainerInstance, SelectionContainer, OnMenuItemClickWithTextCallback, SelectionContainerOptions, SelectionContainerAttribute, SelectionContainerEditMenuOptions, SelectionContainerTextJoinStyle, SelectionContainerController, SelectionContainerMenuOptions } from 'kits/@kit.ArkUI';
```

## SelectionContainer

```TypeScript
export declare function SelectionContainer(content_?: CustomBuilder): SelectionContainerAttribute
```

创建一个SelectionContainer组件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function SelectionContainer(content_?: CustomBuilder): SelectionContainerAttribute--><!--Device-unnamed-export declare function SelectionContainer(content_?: CustomBuilder): SelectionContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 容器。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SelectionContainerAttribute](arkts-arkui-arkui-components-selectioncontainer-selectioncontainerattribute-c.md) |  |


## SelectionContainer

```TypeScript
export declare function SelectionContainer(
    style: CustomBuilderT<SelectionContainerAttribute>
): SelectionContainerAttribute
```

创建一个SelectionContainer组件。需要在组件属性设置开始时调用setSelectionContainerOptions，并在组件属性设置结束时调用applyAttributesFinish。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function SelectionContainer(    style: CustomBuilderT<SelectionContainerAttribute>): SelectionContainerAttribute--><!--Device-unnamed-export declare function SelectionContainer(    style: CustomBuilderT<SelectionContainerAttribute>): SelectionContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;SelectionContainerAttribute&gt; | Yes | 设置SelectionContainer属性的回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SelectionContainerAttribute](arkts-arkui-arkui-components-selectioncontainer-selectioncontainerattribute-c.md) | returns the instance of the SelectionContainerAttribute. |

