# ContainerReader

## ContainerReader

```TypeScript
@ComponentBuilder
export declare function ContainerReader(
    value: ContainerReaderInfo,
    content_?: CustomBuilder,
): ContainerReaderAttribute
```

Defines ContainerReader Component.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function ContainerReader(    value: ContainerReaderInfo,    content_?: CustomBuilder,): ContainerReaderAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function ContainerReader(    value: ContainerReaderInfo,    content_?: CustomBuilder,): ContainerReaderAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ContainerReaderInfo](arkts-na-arkui-components-containerreader-containerreaderinfo-i.md) | Yes | ContainerReader options. |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ContainerReaderAttribute](arkts-na-arkui-components-containerreader-containerreaderattribute-i.md) |  |


## ContainerReader

```TypeScript
@Builder
export declare function ContainerReader(
    style_: CustomBuilderT<ContainerReaderInfo>,
    content_?: CustomBuilder
): ContainerReaderAttribute
```

Defines ContainerReader Component.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function ContainerReader(    style_: CustomBuilderT<ContainerReaderInfo>,    content_?: CustomBuilder): ContainerReaderAttribute--><!--Device-unnamed-@Builderexport declare function ContainerReader(    style_: CustomBuilderT<ContainerReaderInfo>,    content_?: CustomBuilder): ContainerReaderAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | CustomBuilderT&lt;[ContainerReaderInfo](arkts-na-arkui-components-containerreader-containerreaderinfo-i.md)&gt; | Yes | The custom builder function for container content. |
| content_ | CustomBuilder | No | The configuration options for containerreader. |

**Return value:**

| Type | Description |
| --- | --- |
| [ContainerReaderAttribute](arkts-na-arkui-components-containerreader-containerreaderattribute-i.md) | The attribute of the containerreader |

