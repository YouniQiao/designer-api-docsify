# ChipGroupV2Item

每个ChipV2的非通用属性

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-unnamed-export declare class ChipGroupV2Item--><!--Device-unnamed-export declare class ChipGroupV2Item-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(config: ChipGroupV2ItemConfig)
```

ChipGroupV2Item的构造函数

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroupV2Item-constructor(config: ChipGroupV2ItemConfig)--><!--Device-ChipGroupV2Item-constructor(config: ChipGroupV2ItemConfig)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [ChipGroupV2ItemConfig](arkts-arkui-advanced-chipgroupv2-chipgroupv2itemconfig-i.md) | 是 | ChipGroupV2每一项配置 |

## accessibilityDescription

```TypeScript
@Trace
  public accessibilityDescription?: ResourceStr
```

设置ChipGroupV2项的无障碍功能描述。

**类型：** ResourceStr

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroupV2Item-@Trace  public accessibilityDescription?: ResourceStr--><!--Device-ChipGroupV2Item-@Trace  public accessibilityDescription?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
@Trace
  public accessibilityLevel?: string
```

设置ChipGroupV2项的无障碍重要性。

**类型：** string

**默认值：** auto

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroupV2Item-@Trace  public accessibilityLevel?: string--><!--Device-ChipGroupV2Item-@Trace  public accessibilityLevel?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## allowClose

```TypeScript
@Trace
  public allowClose?: boolean
```

是否展示关闭图标

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroupV2Item-@Trace  public allowClose?: boolean--><!--Device-ChipGroupV2Item-@Trace  public allowClose?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## closeIcon

```TypeScript
@Trace
  public closeIcon?: ChipV2CloseConfig
```

当'allowClose'为true时，为默认关闭图标设置config。

**类型：** [ChipV2CloseConfig](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-chipv2-chipv2closeconfig-i.md)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroupV2Item-@Trace  public closeIcon?: ChipV2CloseConfig--><!--Device-ChipGroupV2Item-@Trace  public closeIcon?: ChipV2CloseConfig-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## label

```TypeScript
@Trace
  public label: ChipV2Label
```

标签。

**类型：** [ChipV2Label](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-chipv2-chipv2label-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroupV2Item-@Trace  public label: ChipV2Label--><!--Device-ChipGroupV2Item-@Trace  public label: ChipV2Label-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## prefixIcon

```TypeScript
@Trace
  public prefixIcon?: ChipV2PrefixImageIcon
```

前缀图标。

**类型：** [ChipV2PrefixImageIcon](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-chipv2-chipv2prefiximageicon-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroupV2Item-@Trace  public prefixIcon?: ChipV2PrefixImageIcon--><!--Device-ChipGroupV2Item-@Trace  public prefixIcon?: ChipV2PrefixImageIcon-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## prefixSymbolIcon

```TypeScript
@Trace
  public prefixSymbolIcon?: ChipV2PrefixSymbolIcon
```

前缀符号图标。

**类型：** [ChipV2PrefixSymbolIcon](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-chipv2-chipv2prefixsymbolicon-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroupV2Item-@Trace  public prefixSymbolIcon?: ChipV2PrefixSymbolIcon--><!--Device-ChipGroupV2Item-@Trace  public prefixSymbolIcon?: ChipV2PrefixSymbolIcon-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## suffixIcon

```TypeScript
@Trace
  public suffixIcon?: ChipV2SuffixImageIcon
```

后缀图标。

**类型：** [ChipV2SuffixImageIcon](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-chipv2-chipv2suffiximageicon-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroupV2Item-@Trace  public suffixIcon?: ChipV2SuffixImageIcon--><!--Device-ChipGroupV2Item-@Trace  public suffixIcon?: ChipV2SuffixImageIcon-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## suffixSymbolIcon

```TypeScript
@Trace
  public suffixSymbolIcon?: ChipV2SuffixSymbolIcon
```

后缀符号图标。

**类型：** [ChipV2SuffixSymbolIcon](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-chipv2-chipv2suffixsymbolicon-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipGroupV2Item-@Trace  public suffixSymbolIcon?: ChipV2SuffixSymbolIcon--><!--Device-ChipGroupV2Item-@Trace  public suffixSymbolIcon?: ChipV2SuffixSymbolIcon-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

