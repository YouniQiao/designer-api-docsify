# NodeContent

NodeContent is the entity encapsulation of the node content.

**Inheritance/Implementation:** NodeContent extends Content

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class NodeContent--><!--Device-unnamed-export declare class NodeContent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addFrameNode

```TypeScript
addFrameNode(node: FrameNode): void
```

Add FrameNode to NodeContent based on parameters.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeContent-addFrameNode(node: FrameNode): void--><!--Device-NodeContent-addFrameNode(node: FrameNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-framenode-c.md) | Yes | Newly added FrameNode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100025](../../apis-arkui/errorcode-node.md#100025-invalid-parameter-value) | The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'node' is invalid: it cannot be adopted." |

## constructor

```TypeScript
constructor()
```

constructor

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeContent-constructor()--><!--Device-NodeContent-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## removeFrameNode

```TypeScript
removeFrameNode(node: FrameNode): void
```

Delete the target FrameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeContent-removeFrameNode(node: FrameNode): void--><!--Device-NodeContent-removeFrameNode(node: FrameNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-framenode-c.md) | Yes | FrameNode deleted. |

