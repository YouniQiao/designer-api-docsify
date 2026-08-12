# ContainerReader

## Modules to Import

```TypeScript
import { BreakpointOptions, ContainerReader, ContainerReaderAttribute } from '@kit.ArkUI';
```

## ContainerReader

```TypeScript
export declare function ContainerReader(
    value: ContainerReaderInfo,
    content_?: CustomBuilder,
): ContainerReaderAttribute
```

Defines ContainerReader Component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ContainerReader(    value: ContainerReaderInfo,    content_?: CustomBuilder,): ContainerReaderAttribute--><!--Device-unnamed-export declare function ContainerReader(    value: ContainerReaderInfo,    content_?: CustomBuilder,): ContainerReaderAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ContainerReaderInfo](arkts-arkui-arkui-components-containerreader-containerreaderinfo-i.md) | Yes | ContainerReader options. |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ContainerReaderAttribute](arkts-arkui-arkui-components-containerreader-containerreaderattribute-c.md) |  |


## ContainerReader

```TypeScript
export declare function ContainerReader(
    style_: CustomBuilderT<ContainerReaderInfo>,
    content_?: CustomBuilder
): ContainerReaderAttribute
```

Defines ContainerReader Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ContainerReader(    style_: CustomBuilderT<ContainerReaderInfo>,    content_?: CustomBuilder): ContainerReaderAttribute--><!--Device-unnamed-export declare function ContainerReader(    style_: CustomBuilderT<ContainerReaderInfo>,    content_?: CustomBuilder): ContainerReaderAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | CustomBuilderT&lt;[ContainerReaderInfo](arkts-arkui-arkui-components-containerreader-containerreaderinfo-i.md)&gt; | Yes | The custom builder function for container content. |
| content_ | CustomBuilder | No | The configuration options for containerreader. |

**Return value:**

| Type | Description |
| --- | --- |
| [ContainerReaderAttribute](arkts-arkui-arkui-components-containerreader-containerreaderattribute-c.md) | The attribute of the containerreader |

