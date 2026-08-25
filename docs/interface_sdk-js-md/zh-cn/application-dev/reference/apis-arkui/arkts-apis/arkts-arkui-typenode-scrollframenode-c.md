# ScrollFrameNode

定义Scroll类型的FrameNode。

**继承/实现关系：** ScrollFrameNode extends TypedFrameNode<ScrollAttribute>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(scroller?: Scroller): ScrollAttribute
```

初始化Scroll类型的FrameNode。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scroller | [Scroller](arkts-arkui-scroll-scroller-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ScrollAttribute](arkts-arkui-scroll-scrollattribute-i.md) |
