# bindSwiperController

## bindSwiperController

```TypeScript
export function bindSwiperController(node: FrameNode, controller: SwiperController): void
```

Bind the controller of FrameNode which type is Swiper.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function bindSwiperController(node: FrameNode, controller: SwiperController): void--><!--Device-typeNode-export function bindSwiperController(node: FrameNode, controller: SwiperController): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | the target FrameNode. |
| controller | [SwiperController](../arkts-components/arkts-arkui-swipercontroller-c.md) | Yes | the controller which is bind to the target FrameNode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) | The FrameNode is not modifiable. |
| [100023](../errorcode-node.md#100023-parameter-error) | Parameter error. Possible causes: 1. The component type of the node is incorrect. 2. The node is null or undefined. 3. The controller is null or undefined. |

