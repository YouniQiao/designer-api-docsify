# Column

## Column

```TypeScript
export declare function Column(
    options?: ColumnOptions | ColumnOptions | ColumnOptionsV2,
    content_?: CustomBuilder,
): ColumnAttribute
```

Defines Column Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Column(    options?: ColumnOptions | ColumnOptions | ColumnOptionsV2,    content_?: CustomBuilder,): ColumnAttribute--><!--Device-unnamed-export declare function Column(    options?: ColumnOptions | ColumnOptions | ColumnOptionsV2,    content_?: CustomBuilder,): ColumnAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ColumnOptions](arkts-arkui-column-columnoptions-i.md) \| [ColumnOptions](arkts-arkui-column-columnoptions-i.md) \| [ColumnOptionsV2](arkts-arkui-column-columnoptionsv2-i.md) | No | Column options. |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ColumnAttribute](arkts-arkui-column-columnattribute-i.md) |  |


## Column

```TypeScript
export declare function Column(
    style: CustomBuilderT<ColumnAttribute>,
    content_?: CustomBuilder,
): ColumnAttribute
```

Defines Column Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Column(    style: CustomBuilderT<ColumnAttribute>,    content_?: CustomBuilder,): ColumnAttribute--><!--Device-unnamed-export declare function Column(    style: CustomBuilderT<ColumnAttribute>,    content_?: CustomBuilder,): ColumnAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[ColumnAttribute](arkts-arkui-column-columnattribute-i.md)&gt; | Yes | the callback to set up component's attributes. |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ColumnAttribute](arkts-arkui-column-columnattribute-i.md) |  |

