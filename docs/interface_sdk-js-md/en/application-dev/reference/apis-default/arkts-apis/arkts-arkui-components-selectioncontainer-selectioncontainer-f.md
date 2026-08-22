# SelectionContainer

## Modules to Import

```TypeScript
```

## SelectionContainer

```TypeScript
@ComponentBuilder
export declare function SelectionContainer(content_?: CustomBuilder): SelectionContainerAttribute
```

Defines SelectionContainer component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function SelectionContainer(content_?: CustomBuilder): SelectionContainerAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function SelectionContainer(content_?: CustomBuilder): SelectionContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content_ | CustomBuilder | No | container. |

**Return value:**

| Type | Description |
| --- | --- |
| [SelectionContainerAttribute](../../apis-arkui/arkts-apis/arkts-arkui-arkui-components-selectioncontainer-selectioncontainerattribute-c.md) |  |


## SelectionContainer

```TypeScript
@Builder
export declare function SelectionContainer(
    style: CustomBuilderT<SelectionContainerAttribute>
): SelectionContainerAttribute
```

Defines SelectionContainer component. It requires calling setSelectionContainerOptions at start of the component attribute set-up, and it requires calling applyAttributesFinish at the end of the component attribute set-up.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function SelectionContainer(    style: CustomBuilderT<SelectionContainerAttribute>): SelectionContainerAttribute--><!--Device-unnamed-@Builderexport declare function SelectionContainer(    style: CustomBuilderT<SelectionContainerAttribute>): SelectionContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | CustomBuilderT&lt;[SelectionContainerAttribute](../../apis-arkui/arkts-apis/arkts-arkui-arkui-components-selectioncontainer-selectioncontainerattribute-c.md)&gt; | Yes | the callback to set up SelectionContainer's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| [SelectionContainerAttribute](../../apis-arkui/arkts-apis/arkts-arkui-arkui-components-selectioncontainer-selectioncontainerattribute-c.md) | returns the instance of the SelectionContainerAttribute. |

