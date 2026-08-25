# BaseSpan

定义BaseSpan基础类，包含Span的通用属性。

**继承/实现关系：** BaseSpan extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## baselineOffset

```TypeScript
default baselineOffset(value: LengthMetrics | undefined): this
```

设置Span基线的偏移量。此属性与父组件的baselineOffset是共存的。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## textBackgroundStyle

```TypeScript
default textBackgroundStyle(style: TextBackgroundStyle | undefined): this
```

设置文本背景样式。作为ContainerSpan的子组件时可以继承 它的此属性值，优先使用其自身的此属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [TextBackgroundStyle](arkts-arkui-span-textbackgroundstyle-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| T |
