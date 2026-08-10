# ContainerReaderAttribute

Defines the container reader attribute.

**Inheritance/Implementation:** ContainerReaderAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface ContainerReaderAttribute extends CommonMethod--><!--Device-unnamed-export declare interface ContainerReaderAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { BreakpointOptions, ContainerReader, ContainerReaderAttribute } from 'kits/@kit.ArkUI';
```

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<ContainerReaderAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Sets the attribute modifier.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContainerReaderAttribute-default attributeModifier(modifier: AttributeModifier<ContainerReaderAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-ContainerReaderAttribute-default attributeModifier(modifier: AttributeModifier<ContainerReaderAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ContainerReaderAttribute](arkts-arkui-arkui-components-containerreader-containerreaderattribute-i.md)&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## breakpointConfig

```TypeScript
default breakpointConfig(value?: BreakpointOptions): this
```

Sets the breakpoint configuration for container dimension analysis.Defines a set of threshold values that trigger different layout behaviors based on container size.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContainerReaderAttribute-default breakpointConfig(value?: BreakpointOptions): this--><!--Device-ContainerReaderAttribute-default breakpointConfig(value?: BreakpointOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [BreakpointOptions](arkts-arkui-arkui-components-containerreader-breakpointoptions-i.md) | No | An array of breakpoint values in vp units |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setContainerReaderOptions

```TypeScript
default setContainerReaderOptions(value: ContainerReaderInfo): this
```

Set ContainerReader options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContainerReaderAttribute-default setContainerReaderOptions(value: ContainerReaderInfo): this--><!--Device-ContainerReaderAttribute-default setContainerReaderOptions(value: ContainerReaderInfo): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ContainerReaderInfo](arkts-arkui-arkui-components-containerreader-containerreaderinfo-i.md) | Yes | Used to specify the parameters for container dimension reading and breakpoint analysis. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

