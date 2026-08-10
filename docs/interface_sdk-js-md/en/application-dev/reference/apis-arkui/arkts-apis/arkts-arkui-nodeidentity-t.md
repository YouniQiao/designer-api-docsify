# NodeIdentity

```TypeScript
export declare type NodeIdentity = string | int
```

定义可用于标识节点的类型，string类型时为inspector id，number类型时为系统分配的唯一id。set through .id attribute, and for the int type, it's the unique ID got from the FrameNode by getUniqueID method.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare type NodeIdentity = string | int--><!--Device-unnamed-export declare type NodeIdentity = string | int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| --- | --- |
| string |  |
| int |  |

