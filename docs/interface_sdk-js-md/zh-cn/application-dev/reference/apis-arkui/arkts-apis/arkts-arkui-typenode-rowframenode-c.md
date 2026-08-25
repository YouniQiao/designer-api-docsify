# RowFrameNode

定义Row类型的FrameNode。

**继承/实现关系：** RowFrameNode extends TypedFrameNode<RowAttribute>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(options?: RowOptions | RowOptionsV2): RowAttribute
```

初始化Row类型的FrameNode。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | RowOptions \| [RowOptionsV2](../arkts-components/arkts-arkui-rowoptionsv2-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [RowAttribute](../arkts-components/arkts-arkui-row-attribute.md) |
