# Line

## Line

```TypeScript
@ComponentBuilder
export declare function Line(
    options?: LineOptions
): LineAttribute
```

Line is returned when the parameter is transferred.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Line(    options?: LineOptions): LineAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Line(    options?: LineOptions): LineAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [LineOptions](arkts-arkui-line-lineoptions-i.md) | No | The options to create a Line |

**Return value:**

| Type | Description |
| --- | --- |
| [LineAttribute](arkts-arkui-line-lineattribute-i.md) | The attribute of the Line. |


## Line

```TypeScript
@Builder
export declare function Line(
    style: CustomBuilderT<LineAttribute>
): LineAttribute
```

Defines Line Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Line(    style: CustomBuilderT<LineAttribute>): LineAttribute--><!--Device-unnamed-@Builderexport declare function Line(    style: CustomBuilderT<LineAttribute>): LineAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | CustomBuilderT&lt;[LineAttribute](arkts-arkui-line-lineattribute-i.md)&gt; | Yes | the callback to set up component's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| [LineAttribute](arkts-arkui-line-lineattribute-i.md) |  |

