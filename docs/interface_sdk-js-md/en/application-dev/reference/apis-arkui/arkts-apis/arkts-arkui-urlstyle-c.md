# UrlStyle

超链接对象说明。

默认颜色、字号、字重分别是'#ff0a59f7'、'16fp'、'FontWeight.Regular'，若属性字符串设置TextStyle，则TextStyle优先级更高。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

<!--Device-unnamed-declare class UrlStyle--><!--Device-unnamed-declare class UrlStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(url: string)
```

超链接对象的构造函数。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-UrlStyle-constructor(url: string)--><!--Device-UrlStyle-constructor(url: string)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | 超链接URL设置项。需为有效的URL地址。 |

## url

```TypeScript
readonly url: string
```

获取属性字符串的超链接内容。

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-UrlStyle-readonly url: string--><!--Device-UrlStyle-readonly url: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

