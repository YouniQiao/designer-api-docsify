# ListFrameNode

定义List类型的FrameNode。

**继承/实现关系：** ListFrameNode extends TypedFrameNode<ListAttribute>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(options?: ListOptions): ListAttribute
```

初始化List类型的FrameNode。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ListOptions](../arkts-components/arkts-arkui-listoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ListAttribute](arkts-arkui-list-listattribute-i.md) |
