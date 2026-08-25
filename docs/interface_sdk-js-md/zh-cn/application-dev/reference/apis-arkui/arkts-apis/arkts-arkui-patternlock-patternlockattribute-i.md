# PatternLockAttribute

除支持通用属性外，还支持以下属性。除支持通用事件外，还支持以下事件。

**继承/实现关系：** PatternLockAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## activateCircleStyle

```TypeScript
default activateCircleStyle(options: CircleStyleOptions | undefined): this
```

设置宫格圆点在“激活”状态下的背景圆环样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [CircleStyleOptions](arkts-arkui-patternlock-circlestyleoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [PatternLockAttribute](arkts-arkui-patternlock-patternlockattribute-i.md) |

## activeColor

```TypeScript
default activeColor(value: ResourceColor | undefined): this
```

设置宫格圆点在“激活”状态的填充颜色，“激活”状态为手指经过圆点但还未选中的状态。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [PatternLockAttribute](arkts-arkui-patternlock-patternlockattribute-i.md) |

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<PatternLockAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置组件的动态属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[PatternLockAttribute](arkts-arkui-patternlock-patternlockattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [PatternLockAttribute](arkts-arkui-patternlock-patternlockattribute-i.md) |

## autoReset

```TypeScript
default autoReset(value: boolean | undefined): this
```

设置在完成密码输入后再次在组件区域按下时是否重置组件状态。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [PatternLockAttribute](arkts-arkui-patternlock-patternlockattribute-i.md) |

## backgroundColor

```TypeScript
default backgroundColor(value: ResourceColor | undefined): this
```

设置背景颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [PatternLockAttribute](arkts-arkui-patternlock-patternlockattribute-i.md) |

## circleRadius

```TypeScript
default circleRadius(value: Length | undefined): this
```

设置宫格中圆点的半径。设置为0或负数时，取默认值。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [PatternLockAttribute](arkts-arkui-patternlock-patternlockattribute-i.md) |

## onDotConnect

```TypeScript
default onDotConnect(callback: Callback<int> | undefined): this
```

密码输入选中宫格圆点时触发该回调。回调参数为选中宫格圆点顺序的数字，数字为选中宫格圆点的索引值（第一行圆点从左往右依次为0、1、2，第二行圆点从左往右依次为3、4、5，第三行圆点从左往右依次为6、7、8）。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;int&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [PatternLockAttribute](arkts-arkui-patternlock-patternlockattribute-i.md) |

## onPatternComplete

```TypeScript
default onPatternComplete(callback: Callback<Array<int>> | undefined): this
```

密码输入结束时触发该回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;Array&lt;int&gt;&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [PatternLockAttribute](arkts-arkui-patternlock-patternlockattribute-i.md) |

## pathColor

```TypeScript
default pathColor(value: ResourceColor | undefined): this
```

设置连线的颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [PatternLockAttribute](arkts-arkui-patternlock-patternlockattribute-i.md) |

## pathStrokeWidth

```TypeScript
default pathStrokeWidth(value: double | string | undefined): this
```

设置连线的宽度。设置为0或负数时连线不显示。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [PatternLockAttribute](arkts-arkui-patternlock-patternlockattribute-i.md) |

## regularColor

```TypeScript
default regularColor(value: ResourceColor | undefined): this
```

设置宫格圆点在“未选中”状态的填充颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [PatternLockAttribute](arkts-arkui-patternlock-patternlockattribute-i.md) |

## selectedColor

```TypeScript
default selectedColor(value: ResourceColor | undefined): this
```

设置宫格圆点在“选中”状态的填充颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [PatternLockAttribute](arkts-arkui-patternlock-patternlockattribute-i.md) |

## setPatternLockOptions

```TypeScript
default setPatternLockOptions(controller?: PatternLockController): this
```

设置PatternLock组件选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| controller | [PatternLockController](arkts-arkui-patternlock-patternlockcontroller-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [PatternLockAttribute](arkts-arkui-patternlock-patternlockattribute-i.md) |

## sideLength

```TypeScript
default sideLength(value: Length | undefined): this
```

设置组件的宽度和高度（宽高相同）。当设置为0或负数时，组件不显示。

> **说明：**&gt;
> PatternLock组件设置了通用属性宽高比aspectRatio，且不等于1时（组件尺寸被设定为长方形），九宫格依然绘制为正方形（超出组件范围）。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [PatternLockAttribute](arkts-arkui-patternlock-patternlockattribute-i.md) |

## skipUnselectedPoint

```TypeScript
default skipUnselectedPoint(skipped: boolean | undefined): this
```

设置未选中的宫格圆点在密码路径经过时是否自动选中。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| skipped | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [PatternLockAttribute](arkts-arkui-patternlock-patternlockattribute-i.md) |
