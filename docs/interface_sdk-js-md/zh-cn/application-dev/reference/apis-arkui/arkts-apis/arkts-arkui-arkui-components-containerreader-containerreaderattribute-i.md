# ContainerReaderAttribute

Defines the container reader attribute.

**继承/实现关系：** ContainerReaderAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export declare interface ContainerReaderAttribute extends CommonMethod--><!--Device-unnamed-export declare interface ContainerReaderAttribute extends CommonMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { BreakpointOptions, ContainerReader, ContainerReaderAttribute } from 'kits/@kit.ArkUI';
```

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<ContainerReaderAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Sets the attribute modifier.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ContainerReaderAttribute-default attributeModifier(modifier: AttributeModifier<ContainerReaderAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-ContainerReaderAttribute-default attributeModifier(modifier: AttributeModifier<ContainerReaderAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ContainerReaderAttribute](arkts-arkui-arkui-components-containerreader-containerreaderattribute-i.md)&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## breakpointConfig

```TypeScript
default breakpointConfig(value?: BreakpointOptions): this
```

Sets the breakpoint configuration for container dimension analysis.Defines a set of threshold values that trigger different layout behaviors based on container size.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ContainerReaderAttribute-default breakpointConfig(value?: BreakpointOptions): this--><!--Device-ContainerReaderAttribute-default breakpointConfig(value?: BreakpointOptions): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BreakpointOptions](arkts-arkui-arkui-components-containerreader-breakpointoptions-i.md) | 否 | An array of breakpoint values in vp units |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## setContainerReaderOptions

```TypeScript
default setContainerReaderOptions(value: ContainerReaderInfo): this
```

Set ContainerReader options.

**起始版本：** 26.1.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ContainerReaderAttribute-default setContainerReaderOptions(value: ContainerReaderInfo): this--><!--Device-ContainerReaderAttribute-default setContainerReaderOptions(value: ContainerReaderInfo): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ContainerReaderInfo](arkts-arkui-arkui-components-containerreader-containerreaderinfo-i.md) | 是 | Used to specify the parameters for container dimension reading and breakpoint analysis. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

