# MarqueeFrameNode

定义Marquee类型的FrameNode。

**继承/实现关系：** MarqueeFrameNode extends TypedFrameNode<MarqueeAttribute>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(value: MarqueeOptions): MarqueeAttribute
```

初始化Marquee类型的FrameNode。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [MarqueeOptions](arkts-arkui-marquee-marqueeoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |
