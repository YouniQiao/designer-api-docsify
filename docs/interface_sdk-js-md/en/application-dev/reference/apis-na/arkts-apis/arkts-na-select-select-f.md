# Select

## Select

```TypeScript
@ComponentBuilder
export declare function Select(
    options: Array<SelectOption>,
    content_?: CustomBuilder,
): SelectAttribute
```

Defines Select Component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Select(    options: Array<SelectOption>,    content_?: CustomBuilder,): SelectAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Select(    options: Array<SelectOption>,    content_?: CustomBuilder,): SelectAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | Array&lt;[SelectOption](arkts-na-select-selectoption-i.md)&gt; | Yes | the options of Select. |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [SelectAttribute](arkts-na-select-selectattribute-i.md) |  |


## Select

```TypeScript
@Builder
export declare function Select(
    style_: CustomBuilderT<SelectAttribute>,
    content_?: CustomBuilder,
): SelectAttribute
```

Defines Select Component.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Select(    style_: CustomBuilderT<SelectAttribute>,    content_?: CustomBuilder,): SelectAttribute--><!--Device-unnamed-@Builderexport declare function Select(    style_: CustomBuilderT<SelectAttribute>,    content_?: CustomBuilder,): SelectAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | CustomBuilderT&lt;[SelectAttribute](arkts-na-select-selectattribute-i.md)&gt; | Yes | select attribute instance |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [SelectAttribute](arkts-na-select-selectattribute-i.md) |  |

