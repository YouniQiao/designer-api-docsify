# getSwiperAttribute

## getSwiperAttribute

```TypeScript
export function getSwiperAttribute(node: FrameNode): SwiperAttribute | undefined
```

获取Swiper的FrameNode的属性实例来设置属性。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function getSwiperAttribute(node: FrameNode): SwiperAttribute | undefined--><!--Device-typeNode-export function getSwiperAttribute(node: FrameNode): SwiperAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 目标Swiper节点 |

**Return value:**

| Type | Description |
| --- | --- |
| [SwiperAttribute](../arkts-components/arkts-arkui-swiper-attribute.md) | Return the attribute instance of FrameNode, and return undefined if it does not exist. |

