# ChipV2Accessibility

定义ChipV2无障碍属性

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export declare class ChipV2Accessibility--><!--Device-unnamed-export declare class ChipV2Accessibility-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(config: ChipV2AccessibilityConfig)
```

ChipV2Accessibility的构造函数

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipV2Accessibility-constructor(config: ChipV2AccessibilityConfig)--><!--Device-ChipV2Accessibility-constructor(config: ChipV2AccessibilityConfig)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [ChipV2AccessibilityConfig](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-chipv2-chipv2accessibilityconfig-i.md) | 是 | 无障碍配置 |

## accessibilityDescription

```TypeScript
@Trace
  public accessibilityDescription?: ResourceStr
```

设置无障碍功能描述。

**类型：** ResourceStr

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipV2Accessibility-@Trace  public accessibilityDescription?: ResourceStr--><!--Device-ChipV2Accessibility-@Trace  public accessibilityDescription?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
@Trace
  public accessibilityLevel?: string
```

设置无障碍级别。

**类型：** string

**默认值：** auto

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipV2Accessibility-@Trace  public accessibilityLevel?: string--><!--Device-ChipV2Accessibility-@Trace  public accessibilityLevel?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## accessibilityText

```TypeScript
@Trace
  public accessibilityText?: ResourceStr
```

设置无障碍功能文本。

**类型：** ResourceStr

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ChipV2Accessibility-@Trace  public accessibilityText?: ResourceStr--><!--Device-ChipV2Accessibility-@Trace  public accessibilityText?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

