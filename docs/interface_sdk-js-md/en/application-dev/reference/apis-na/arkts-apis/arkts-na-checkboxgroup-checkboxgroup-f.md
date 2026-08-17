# CheckboxGroup

## CheckboxGroup

```TypeScript
@ComponentBuilder
export declare function CheckboxGroup(
    options?: CheckboxGroupOptions,
    content_?: CustomBuilder,
): CheckboxGroupAttribute
```

Defines CheckboxGroup Component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function CheckboxGroup(    options?: CheckboxGroupOptions,    content_?: CustomBuilder,): CheckboxGroupAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function CheckboxGroup(    options?: CheckboxGroupOptions,    content_?: CustomBuilder,): CheckboxGroupAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [CheckboxGroupOptions](arkts-na-checkboxgroup-checkboxgroupoptions-i.md) | No | the options of CheckboxGroup. |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [CheckboxGroupAttribute](arkts-na-checkboxgroup-checkboxgroupattribute-i.md) |  |


## CheckboxGroup

```TypeScript
@Builder
export declare function CheckboxGroup(
    style_: CustomBuilderT<CheckboxGroupAttribute>,
    content_?: CustomBuilder,
): CheckboxGroupAttribute
```

Defines CheckboxGroup Component.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function CheckboxGroup(    style_: CustomBuilderT<CheckboxGroupAttribute>,    content_?: CustomBuilder,): CheckboxGroupAttribute--><!--Device-unnamed-@Builderexport declare function CheckboxGroup(    style_: CustomBuilderT<CheckboxGroupAttribute>,    content_?: CustomBuilder,): CheckboxGroupAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | CustomBuilderT&lt;[CheckboxGroupAttribute](arkts-na-checkboxgroup-checkboxgroupattribute-i.md)&gt; | Yes | checkboxgroup attribute instance |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [CheckboxGroupAttribute](arkts-na-checkboxgroup-checkboxgroupattribute-i.md) |  |

