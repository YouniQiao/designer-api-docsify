# Rect

## Rect

```TypeScript
export declare function Rect(
    options?: RectOptions | RoundedRectOptions
): RectAttribute
```

用于绘制矩形的构造函数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [RectOptions](arkts-arkui-rect-rectoptions-i.md) \| [RoundedRectOptions](arkts-arkui-rect-roundedrectoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [RectAttribute](arkts-arkui-rect-rectattribute-i.md) |


## Rect

```TypeScript
export declare function Rect(
    style: CustomBuilderT<RectAttribute>,
): RectAttribute
```

Defines Rect Component.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[RectAttribute](arkts-arkui-rect-rectattribute-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [RectAttribute](arkts-arkui-rect-rectattribute-i.md) |
