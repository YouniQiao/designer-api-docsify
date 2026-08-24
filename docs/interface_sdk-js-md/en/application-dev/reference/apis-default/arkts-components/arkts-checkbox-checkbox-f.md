# Checkbox

## Checkbox

```TypeScript
@ComponentBuilder
export declare function Checkbox(
    options?: CheckboxOptions,
    content_?: CustomBuilder,
): CheckboxAttribute
```

Defines Checkbox Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @ComponentBuilder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Checkbox(    options?: CheckboxOptions,    content_?: CustomBuilder,): CheckboxAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Checkbox(    options?: CheckboxOptions,    content_?: CustomBuilder,): CheckboxAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [CheckboxOptions](arkts-checkbox-checkboxoptions-i.md) | No | the options of Checkbox. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [CheckboxAttribute](arkts-checkbox-attribute.md) |  |


## Checkbox

```TypeScript
@Builder
export declare function Checkbox(
    style_: CustomBuilderT<CheckboxAttribute>,
    content_?: CustomBuilder,
): CheckboxAttribute
```

Defines Checkbox Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Checkbox(    style_: CustomBuilderT<CheckboxAttribute>,    content_?: CustomBuilder,): CheckboxAttribute--><!--Device-unnamed-@Builderexport declare function Checkbox(    style_: CustomBuilderT<CheckboxAttribute>,    content_?: CustomBuilder,): CheckboxAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[CheckboxAttribute](arkts-checkbox-attribute.md)&gt; | Yes | checkbox attribute instance |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [CheckboxAttribute](arkts-checkbox-attribute.md) |  |

