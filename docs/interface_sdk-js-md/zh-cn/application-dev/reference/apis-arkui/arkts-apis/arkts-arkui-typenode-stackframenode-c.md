# StackFrameNode

定义Stack类型的FrameNode。

**继承/实现关系：** StackFrameNode extends TypedFrameNode<StackAttribute>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(options?: StackOptions): StackAttribute
```

初始化Stack类型的FrameNode。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [StackOptions](../arkts-components/arkts-arkui-stackoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [StackAttribute](../arkts-components/arkts-arkui-stack-attribute.md) |
