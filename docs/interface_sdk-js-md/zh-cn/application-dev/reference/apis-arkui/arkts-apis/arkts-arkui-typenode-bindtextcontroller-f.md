# bindTextController

## bindTextController

```TypeScript
export function bindTextController(node: FrameNode, controller: TextController): void
```

绑定Text节点的控制器。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | 是 |
| controller | [TextController](arkts-arkui-text-textcontroller-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100023](../errorcode-node.md#100023-参数错误) |
| [100021](../errorcode-node.md#100021-framenode节点不可修改) |
