# ArrowStyle

Arrow object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ArrowStyle--><!--Device-unnamed-export declare interface ArrowStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## arrowColor

```TypeScript
arrowColor?: ResourceColor
```

设置箭头颜色。默认值： '#182431'，深灰色。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Default:** #182431

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrowStyle-arrowColor?: ResourceColor--><!--Device-ArrowStyle-arrowColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## arrowSize

```TypeScript
arrowSize?: Length
```

设置箭头大小。在导航点两侧显示时：在导航点两侧显示时：默认值：18vp在组件两侧显示时：默认值：24vp。

**Type:** [Length](arkts-arkui-length-t.md)

**Default:** When isSidebarMiddle is false, the default value is 18vp, Otherwise, the default value is 24vp

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrowStyle-arrowSize?: Length--><!--Device-ArrowStyle-arrowSize?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

设置底板颜色。在导航点两侧显示：透明色.在组件两侧显示：默认值：'#19182431'，半透明深灰色。 默认值： '#00000000'。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Default:** When isSidebarMiddle is false, the default value is #00000000, Otherwise, the default value is #19182431

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrowStyle-backgroundColor?: ResourceColor--><!--Device-ArrowStyle-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundSize

```TypeScript
backgroundSize?: Length
```

设置底板大小。不支持设置百分比。&lt;br&gt;在导航点两侧显示：默认值：24vp在组件两侧显示：默认值：32vp。

**Type:** [Length](arkts-arkui-length-t.md)

**Default:** When isSidebarMiddle is false, the default value is 24vp, Otherwise,the default value is 32vp

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrowStyle-backgroundSize?: Length--><!--Device-ArrowStyle-backgroundSize?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isSidebarMiddle

```TypeScript
isSidebarMiddle?: boolean
```

设置箭头显示位置。true：箭头居中显示在Swiper组件两侧；false：箭头显示在导航点指示器两侧。默认值： false。

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrowStyle-isSidebarMiddle?: boolean--><!--Device-ArrowStyle-isSidebarMiddle?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showBackground

```TypeScript
showBackground?: boolean
```

设置箭头底板是否显示。true：箭头底板显示；false：箭头底板不显示。默认值： false。

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrowStyle-showBackground?: boolean--><!--Device-ArrowStyle-showBackground?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

