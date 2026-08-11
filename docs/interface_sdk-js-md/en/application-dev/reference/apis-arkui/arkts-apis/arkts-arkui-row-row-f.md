# Row

## Row

```TypeScript
export declare function Row(
    options?: RowOptions | RowOptions | RowOptionsV2,
    content_?: CustomBuilder,
): RowAttribute
```

Defines Row Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Row(    options?: RowOptions | RowOptions | RowOptionsV2,    content_?: CustomBuilder,): RowAttribute--><!--Device-unnamed-export declare function Row(    options?: RowOptions | RowOptions | RowOptionsV2,    content_?: CustomBuilder,): RowAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RowOptions](../arkts-components/arkts-arkui-rowoptions-i.md) \| RowOptions \| RowOptionsV2 | No | Row options. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [RowAttribute](../arkts-components/arkts-arkui-row-attribute.md) |  |


## Row

```TypeScript
export declare function Row(
    style: CustomBuilderT<RowAttribute>,
    content_?: CustomBuilder,
): RowAttribute
```

Defines Row Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Row(    style: CustomBuilderT<RowAttribute>,    content_?: CustomBuilder,): RowAttribute--><!--Device-unnamed-export declare function Row(    style: CustomBuilderT<RowAttribute>,    content_?: CustomBuilder,): RowAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;RowAttribute&gt; | Yes | the callback to set up component's attributes. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container. |

**Return value:**

| Type | Description |
| --- | --- |
| [RowAttribute](../arkts-components/arkts-arkui-row-attribute.md) |  |

