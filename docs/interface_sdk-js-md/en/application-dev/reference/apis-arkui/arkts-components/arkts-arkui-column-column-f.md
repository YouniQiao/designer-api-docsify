# Column

## Column

```TypeScript
@ComponentBuilder
export declare function Column(
    options?: ColumnOptions | ColumnOptions | ColumnOptionsV2,
    content_?: CustomBuilder,
): ColumnAttribute
```

Defines Column Component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Column(    options?: ColumnOptions | ColumnOptions | ColumnOptionsV2,    content_?: CustomBuilder,): ColumnAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Column(    options?: ColumnOptions | ColumnOptions | ColumnOptionsV2,    content_?: CustomBuilder,): ColumnAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ColumnOptions](arkts-arkui-column-columnoptions-i.md) \| [ColumnOptions](arkts-arkui-column-columnoptions-i.md) \| [ColumnOptionsV2](arkts-arkui-column-columnoptionsv2-i.md) | No | Column options. |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ColumnAttribute](arkts-arkui-column-attribute.md) |  |


## Column

```TypeScript
@Builder
export declare function Column(
    style: CustomBuilderT<ColumnAttribute>,
    content_?: CustomBuilder,
): ColumnAttribute
```

Defines Column Component.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Column(    style: CustomBuilderT<ColumnAttribute>,    content_?: CustomBuilder,): ColumnAttribute--><!--Device-unnamed-@Builderexport declare function Column(    style: CustomBuilderT<ColumnAttribute>,    content_?: CustomBuilder,): ColumnAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;[ColumnAttribute](arkts-arkui-column-attribute.md)&gt; | Yes | the callback to set up component's attributes. |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ColumnAttribute](arkts-arkui-column-attribute.md) |  |

