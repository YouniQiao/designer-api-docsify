# TextClock

## TextClock

```TypeScript
export declare function TextClock(
    options?: TextClockOptions
): TextClockAttribute
```

创建文本时钟组件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function TextClock(    options?: TextClockOptions): TextClockAttribute--><!--Device-unnamed-export declare function TextClock(    options?: TextClockOptions): TextClockAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TextClockOptions](arkts-arkui-textclock-textclockoptions-i.md) | 否 | 通过文本显示当前系统时间的组件参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |  |


## TextClock

```TypeScript
export declare function TextClock(
    style: CustomBuilderT<TextClockAttribute>,
): TextClockAttribute
```

定义TextClock组件。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function TextClock(    style: CustomBuilderT<TextClockAttribute>,): TextClockAttribute--><!--Device-unnamed-export declare function TextClock(    style: CustomBuilderT<TextClockAttribute>,): TextClockAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md)&gt; | 是 | TextClock属性的实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |  |

