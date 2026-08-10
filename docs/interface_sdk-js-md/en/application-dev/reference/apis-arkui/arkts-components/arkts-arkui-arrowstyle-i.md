# ArrowStyle

左右箭头属性。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface ArrowStyle--><!--Device-unnamed-declare interface ArrowStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## arrowColor

```TypeScript
arrowColor?: ResourceColor
```

设置箭头颜色。

默认值：'#182431'

**Type:** [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)

**Default:** #182431

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ArrowStyle-arrowColor?: ResourceColor--><!--Device-ArrowStyle-arrowColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## arrowSize

```TypeScript
arrowSize?: Length
```

设置箭头大小。

在导航点两侧显示时：

默认值：18vp

在组件两侧显示时：

默认值：24vp

**说明：**

showBackground为true时，arrowSize为backgroundSize的3/4。

不支持设置百分比。

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md)

**Default:** When isSidebarMiddle is false, the default value is 18vp, Otherwise, the default value is 24vp

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ArrowStyle-arrowSize?: Length--><!--Device-ArrowStyle-arrowSize?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

设置底板颜色。

在导航点两侧显示：

默认值：'#00000000'

在组件两侧显示：

默认值：'#19182431'

**Type:** [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)

**Default:** When isSidebarMiddle is false, the default value is #00000000, Otherwise,the default value is #1918243 1 [since 10 - 10] @default When isSidebarMiddle is false, the default value is #00000000, Otherwise, the default value is #1918243 1 [since 11]

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ArrowStyle-backgroundColor?: ResourceColor--><!--Device-ArrowStyle-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundSize

```TypeScript
backgroundSize?: Length
```

设置底板大小。

在导航点两侧显示：

默认值：24vp

在组件两侧显示：

默认值：32vp

不支持设置百分比。

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md)

**Default:** When isSidebarMiddle is false, the default value is 24vp, Otherwise,the default value is 32vp

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ArrowStyle-backgroundSize?: Length--><!--Device-ArrowStyle-backgroundSize?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isSidebarMiddle

```TypeScript
isSidebarMiddle?: boolean
```

设置箭头显示位置。为true时箭头居中显示在Swiper组件两侧，为false时显示在导航点指示器两侧。

默认值：false

默认显示在导航点指示器两侧。

**Type:** boolean

**Default:** false

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ArrowStyle-isSidebarMiddle?: boolean--><!--Device-ArrowStyle-isSidebarMiddle?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showBackground

```TypeScript
showBackground?: boolean
```

设置箭头底板是否显示。为true时箭头底板显示，为false时箭头底板不显示。

默认值：false

**Type:** boolean

**Default:** false

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ArrowStyle-showBackground?: boolean--><!--Device-ArrowStyle-showBackground?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

