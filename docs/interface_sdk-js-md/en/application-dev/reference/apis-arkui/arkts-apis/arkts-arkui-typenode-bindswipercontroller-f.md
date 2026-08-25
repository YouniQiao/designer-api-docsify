# bindSwiperController

## bindSwiperController

```TypeScript
export function bindSwiperController(node: FrameNode, controller: SwiperController): void
```

Bind the controller of FrameNode which type is Swiper.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes |
| controller | [SwiperController](arkts-arkui-swiper-swipercontroller-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100023](../errorcode-node.md#100023-parameter-error) |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |
