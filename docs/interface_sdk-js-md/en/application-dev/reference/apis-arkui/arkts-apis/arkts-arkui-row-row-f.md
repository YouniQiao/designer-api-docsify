# Row

## Row

```TypeScript
@ComponentBuilder
export declare function Row(
    options?: RowOptions | RowOptions | RowOptionsV2,
    content_?: CustomBuilder,
): RowAttribute
```

Defines Row Component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Row(    options?: RowOptions | RowOptions | RowOptionsV2,    content_?: CustomBuilder,): RowAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Row(    options?: RowOptions | RowOptions | RowOptionsV2,    content_?: CustomBuilder,): RowAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RowOptions](arkts-arkui-row-rowoptions-i.md) \| [RowOptions](arkts-arkui-row-rowoptions-i.md) \| [RowOptionsV2](arkts-arkui-row-rowoptionsv2-i.md) | No | Row options. |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| RowAttribute |  |


## Row

```TypeScript
@Builder
export declare function Row(
    style: CustomBuilderT<RowAttribute>,
    content_?: CustomBuilder,
): RowAttribute
```

Defines Row Component.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Row(    style: CustomBuilderT<RowAttribute>,    content_?: CustomBuilder,): RowAttribute--><!--Device-unnamed-@Builderexport declare function Row(    style: CustomBuilderT<RowAttribute>,    content_?: CustomBuilder,): RowAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | CustomBuilderT&lt;RowAttribute&gt; | Yes | the callback to set up component's attributes. |
| content_ | CustomBuilder | No | container. |

**Return value:**

| Type | Description |
| --- | --- |
| RowAttribute |  |

