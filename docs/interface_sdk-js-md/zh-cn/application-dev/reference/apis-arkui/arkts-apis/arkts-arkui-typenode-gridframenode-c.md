# GridFrameNode

定义Grid类型的FrameNode。

**继承/实现关系：** GridFrameNode extends TypedFrameNode<GridAttribute>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(scroller?: Scroller, layoutOptions?: GridLayoutOptions): GridAttribute
```

初始化Grid类型的FrameNode。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scroller | [Scroller](arkts-arkui-scroll-scroller-c.md) | 否 |
| layoutOptions | [GridLayoutOptions](arkts-arkui-grid-gridlayoutoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [GridAttribute](../arkts-components/arkts-arkui-grid-attribute.md) |
