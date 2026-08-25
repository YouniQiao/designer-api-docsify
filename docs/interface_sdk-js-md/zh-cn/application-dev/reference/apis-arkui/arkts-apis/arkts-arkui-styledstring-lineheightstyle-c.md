# LineHeightStyle

文本行高对象说明。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(lineHeight: LengthMetrics)
```

文本行高的构造函数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [lineHeight](#lineheight) | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) | 是 |

## constructor

```TypeScript
constructor(lineHeight: LengthMetrics, lineHeightMultiple: double)
```

文本行高及倍数的构造函数。

> **说明：**&gt;
> - lineHeightMultiple与lineHeight或
> [LineSpacingStyle](arkts-arkui-styledstring-linespacingstyle-c.md)同时设置
> 时，仅lineHeightMultiple生效，行高为该行最高字体高度与倍数的乘积。&gt;
> - lineHeightMultiple小于0或undefined时不生效，使用lineHeight和
> [LineSpacingStyle](arkts-arkui-styledstring-linespacingstyle-c.md)设置行高和
> 行间距。&gt;
> - lineHeightMultiple等于0时等效于设置为1。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [lineHeight](#lineheight) | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) | 是 |
| [lineHeightMultiple](#lineheightmultiple) | double | 是 |

## lineHeight

```TypeScript
readonly lineHeight: double
```

获取属性字符串的文本行高。单位：[vp

**类型：** double

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## lineHeightMultiple

```TypeScript
readonly lineHeightMultiple?: double
```

文本行高的倍数值。实际生效的行高为该行最高的字体高度与倍数的乘积。

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
