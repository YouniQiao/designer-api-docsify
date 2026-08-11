# SwiperAttribute

Defines the swiper attribute functions.

**Inheritance/Implementation:** SwiperAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface SwiperAttribute extends CommonMethod--><!--Device-unnamed-export declare interface SwiperAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ignoreHiddenItem

```TypeScript
default ignoreHiddenItem(enabled: boolean | undefined): this
```

When the Visibility property of a child node is set to None, whether it will occupy space for display.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default ignoreHiddenItem(enabled: boolean | undefined): this--><!--Device-SwiperAttribute-default ignoreHiddenItem(enabled: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes | whether child node will occupy space for display.&lt;br&gt;The value **true** means it dose not occupy space, and **false** means the opposite.&lt;br&gt;If the input parameter is invalid, the value **false** is used. |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of swiper. |

