# ContainerSpan

## ContainerSpan

```TypeScript
@ComponentBuilder
export declare function ContainerSpan(
    content_?: CustomBuilder,
): ContainerSpanAttribute
```

Defines ContainerSpan Component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function ContainerSpan(    content_?: CustomBuilder,): ContainerSpanAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function ContainerSpan(    content_?: CustomBuilder,): ContainerSpanAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ContainerSpanAttribute](arkts-arkui-containerspan-attribute.md) |  |


## ContainerSpan

```TypeScript
@Builder
export declare function ContainerSpan(
    style: CustomBuilderT<ContainerSpanAttribute>,
    content_?: CustomBuilder,
): ContainerSpanAttribute
```

Defines ContainerSpan Component.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function ContainerSpan(    style: CustomBuilderT<ContainerSpanAttribute>,    content_?: CustomBuilder,): ContainerSpanAttribute--><!--Device-unnamed-@Builderexport declare function ContainerSpan(    style: CustomBuilderT<ContainerSpanAttribute>,    content_?: CustomBuilder,): ContainerSpanAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;[ContainerSpanAttribute](arkts-arkui-containerspan-attribute.md)&gt; | Yes | containerspan attribute instance. |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No | container. |

**Return value:**

| Type | Description |
| --- | --- |
| [ContainerSpanAttribute](arkts-arkui-containerspan-attribute.md) |  |

