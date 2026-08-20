# BaseSpan

定义BaseSpan基础类，包含Span的通用属性。

**继承/实现关系：** BaseSpan extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface BaseSpan--><!--Device-unnamed-export declare interface BaseSpan-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## baselineOffset

```TypeScript
baselineOffset(value: LengthMetrics | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-BaseSpan-baselineOffset(value: LengthMetrics | undefined): this--><!--Device-BaseSpan-baselineOffset(value: LengthMetrics | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LengthMetrics](../../apis-default/arkts-apis/arkts-graphics-lengthmetrics-c.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## textBackgroundStyle

```TypeScript
textBackgroundStyle(style: TextBackgroundStyle | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-BaseSpan-textBackgroundStyle(style: TextBackgroundStyle | undefined): this--><!--Device-BaseSpan-textBackgroundStyle(style: TextBackgroundStyle | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [TextBackgroundStyle](arkts-arkui-span-textbackgroundstyle-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

设置Span基线的偏移量。此属性与父组件的baselineOffset是共存的。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BaseSpan-default--><!--Device-BaseSpan-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

