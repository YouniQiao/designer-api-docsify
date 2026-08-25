# PatternLock属性/事件

除支持[通用属性](arkts-arkui-commonmethod-c.md)外，还支持以下属性。除支持[通用事件](arkts-arkui-commonmethod-c.md)外，还支持以下事件。

**继承/实现关系：** PatternLockAttribute extends CommonMethod<PatternLockAttribute>

**起始版本：** 9

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## activateCircleStyle

```TypeScript
activateCircleStyle(options: Optional<CircleStyleOptions>)
```

设置宫格圆点在“激活”状态下的背景圆环样式。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;[CircleStyleOptions](arkts-arkui-circlestyleoptions-i.md)&gt; | 是 |

## activeColor

```TypeScript
activeColor(value: ResourceColor)
```

设置宫格圆点在“激活”状态的填充颜色，“激活”状态为手指经过圆点但还未选中的状态。未通过该接口设置时，默认填充颜色为'#ff182431'（深灰色）。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## autoReset

```TypeScript
autoReset(value: boolean)
```

设置在完成密码输入后再次在组件区域按下时是否重置组件状态。未通过该接口设置时，默认重置组件状态。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## backgroundColor

```TypeScript
backgroundColor(value: ResourceColor)
```

设置背景颜色。未通过该接口设置时，默认为透明，无背景色。

> **说明：**&gt;
> 从API version 20开始，该接口支持在attributeModifier中调用。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## circleRadius

```TypeScript
circleRadius(value: Length)
```

设置宫格中圆点的半径。未通过该接口设置时，默认半径为6vp。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |

## onDotConnect

```TypeScript
onDotConnect(callback: import('../api/@ohos.base').Callback<number>)
```

密码输入选中宫格圆点时触发该回调。

> **说明：**&gt;
> 从API version 20开始，该接口支持在attributeModifier中调用。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | import('../api/@ohos.base').Callback & lt;number & gt; | 是 |

## onPatternComplete

```TypeScript
onPatternComplete(callback: (input: Array<number>) => void)
```

密码输入结束时触发该回调。

> **说明：**&gt;
> 该回调在密码输入结束时触发，返回完整密码数组。与[onDotConnect](#ondotconnect)的关系：onDotConnect在选中每个圆点时实时触发，
> onPatternComplete在输入结束时触发，两者可以配合使用以实现实时反馈和最终验证。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (input: Array & lt;number & gt;) = & gt; void | 是 |

## pathColor

```TypeScript
pathColor(value: ResourceColor)
```

设置连线的颜色。未通过该接口设置时，默认连线颜色为'#33182431'（深灰色，20%不透明度）。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## pathStrokeWidth

```TypeScript
pathStrokeWidth(value: number | string)
```

设置连线的宽度。未通过该接口设置时，默认连线宽度为12vp。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number \| string | 是 |

## regularColor

```TypeScript
regularColor(value: ResourceColor)
```

设置宫格圆点在“未选中”状态的填充颜色。未通过该接口设置时，默认填充颜色为'#ff182431'（深灰色）。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## selectedColor

```TypeScript
selectedColor(value: ResourceColor)
```

设置宫格圆点在“选中”状态的填充颜色。未通过该接口设置时，默认填充颜色为'#ff182431'（深灰色）。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## sideLength

```TypeScript
sideLength(value: Length)
```

设置组件的宽度和高度（宽高相同）。当设置为0或负数时，组件不显示。未通过该接口设置时，默认宽高为288vp。

> **说明：**&gt;
> PatternLock组件设置了通用属性宽高比[aspectRatio](arkts-arkui-commonmethod-c.md#aspectratio)，且不等于1时（组件尺寸被设定为长方形），九宫格依然绘制为正方形（超出组件范围）。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |

## skipUnselectedPoint

```TypeScript
skipUnselectedPoint(skipped: boolean)
```

设置未选中的宫格圆点在密码路径经过时是否跳过选中。未通过该接口设置时，未选中的宫格圆点在密码路径经过时默认自动选中。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| skipped | boolean | 是 |
