# BorderImageOption

Border image option

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare interface BorderImageOption--><!--Device-unnamed-declare interface BorderImageOption-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fill

```TypeScript
fill?: boolean
```

设置边框图片是否中心填充。true表示中心填充，false表示非中心填充。

默认值：false

**Type:** boolean

**Default:** false

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-BorderImageOption-fill?: boolean--><!--Device-BorderImageOption-fill?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## outset

```TypeScript
outset?: Length | EdgeWidths | LocalizedEdgeWidths
```

设置边框图片向外延伸距离。

默认值：0

**说明：**

设置负数时取默认值。

参数类型为[Length](../arkts-apis/arkts-arkui-length-t.md/arkts-arkui-length-t.md)时，统一设置四条边框的向外延伸距离。

参数类型为[EdgeWidths](../arkts-apis/arkts-arkui-units-edgewidths-i.md/arkts-arkui-units-edgewidths-i.md)时：

- Top：设置边框图片上边框向外延伸的距离。

- Bottom：设置边框图片下边框向外延伸的距离。

- Left：设置边框图片左边框向外延伸的距离。

- Right：设置边框图片右边框向外延伸的距离。

参数类型为[LocalizedEdgeWidths](../arkts-apis/arkts-arkui-units-localizededgewidths-i.md/arkts-arkui-units-localizededgewidths-i.md)&lt;sup&gt;12+&lt;/sup&gt;时：

- Top：设置边框图片上边框向外延伸的距离。

- Bottom：设置边框图片下边框向外延伸的距离。

- Start：设置边框图片左边框向外延伸的距离。

从右至左显示语言模式下为设置边框图片右边框向外延伸的距离。

- End：设置边框图片右边框向外延伸的距离。

从右至左显示语言模式下为设置边框图片左边框向外延伸的距离。

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md) \| EdgeWidths \| LocalizedEdgeWidths

**Default:** 0

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-BorderImageOption-outset?: Length | EdgeWidths | LocalizedEdgeWidths--><!--Device-BorderImageOption-outset?: Length | EdgeWidths | LocalizedEdgeWidths-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## repeat

```TypeScript
repeat?: RepeatMode
```

设置被切割的图片在边框上的重复方式。

默认值：RepeatMode.Stretch

**Type:** [RepeatMode](../arkts-apis/arkts-arkui-common-repeatmode-e.md)

**Default:** RepeatMode.Stretch

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-BorderImageOption-repeat?: RepeatMode--><!--Device-BorderImageOption-repeat?: RepeatMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## slice

```TypeScript
slice?: Length | EdgeWidths | LocalizedEdgeWidths
```

设置边框图片左上角、右上角、左下角以及右下角的切割宽高。

默认值：0

**说明：**

设置负数时取默认值。

参数类型为[Length](../arkts-apis/arkts-arkui-length-t.md/arkts-arkui-length-t.md)时，统一设置四个角的宽高。

参数类型为[EdgeWidths](../arkts-apis/arkts-arkui-units-edgewidths-i.md/arkts-arkui-units-edgewidths-i.md)时：

- Top：设置图片上侧被切割的高。

- Bottom：设置图片下侧被切割的高。

- Left：设置图片左侧被切割的宽。

- Right：设置图片右侧被切割的宽。

参数类型为[LocalizedEdgeWidths](../arkts-apis/arkts-arkui-units-localizededgewidths-i.md/arkts-arkui-units-localizededgewidths-i.md)&lt;sup&gt;12+&lt;/sup&gt;时：

- Top：设置图片上侧被切割的高。

- Bottom：设置图片下侧被切割的高。

- Start：设置图片左侧被切割的宽。

从右至左显示语言模式下为设置图片右侧被切割的宽。

- End：设置图片右侧被切割的宽。

从右至左显示语言模式下为设置图片左侧被切割的宽。

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md) \| EdgeWidths \| LocalizedEdgeWidths

**Default:** 0

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-BorderImageOption-slice?: Length | EdgeWidths | LocalizedEdgeWidths--><!--Device-BorderImageOption-slice?: Length | EdgeWidths | LocalizedEdgeWidths-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## source

```TypeScript
source?: string | Resource | LinearGradient
```

边框图源或者渐变色设置。参数类型为string类型时，用于设置边框图源，引用方式请参考[加载图片资源](../../../ui/arkts-graphics-display.md#加载图片资源)。

默认值：undefined（不设置边框图源）

**说明：**

边框图源仅适用于容器组件，如[Row](../arkts-apis/arkts-arkui-row-row-f.md/arkts-arkui-row-row-f.md#row)、[Column](../arkts-apis/arkts-arkui-column-column-f.md/arkts-arkui-column-column-f.md#column)、[Flex](../arkts-apis/arkts-arkui-flex-flex-f.md/arkts-arkui-flex-flex-f.md#flex)，在非容器组件上使用会失效。

**Type:** string \| Resource \| LinearGradient

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-BorderImageOption-source?: string | Resource | LinearGradient--><!--Device-BorderImageOption-source?: string | Resource | LinearGradient-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width?: Length | EdgeWidths | LocalizedEdgeWidths
```

设置图片边框宽度。

默认值：0

**说明：**

设置负数时取默认值。

参数类型为[Length](../arkts-apis/arkts-arkui-length-t.md/arkts-arkui-length-t.md)时，统一设置四条边框的宽度。

参数类型为[EdgeWidths](../arkts-apis/arkts-arkui-units-edgewidths-i.md/arkts-arkui-units-edgewidths-i.md)时：

- Top：设置图片边框上边框的宽。

- Bottom：设置图片边框下边框的宽。

- Left：设置图片边框左边框的宽。

- Right：设置图片边框右边框的宽。

参数类型为[LocalizedEdgeWidths](../arkts-apis/arkts-arkui-units-localizededgewidths-i.md/arkts-arkui-units-localizededgewidths-i.md)&lt;sup&gt;12+&lt;/sup&gt;时：

- Top：设置图片边框上边框的宽。

- Bottom：设置图片边框下边框的宽。

- Start：设置图片边框左边框的宽。

从右至左显示语言模式下为设置图片边框右边框宽。

- End：设置图片边框右边框宽。

从右至左显示语言模式下为设置图片边框左边框的宽。

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md) \| EdgeWidths \| LocalizedEdgeWidths

**Default:** 0

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-BorderImageOption-width?: Length | EdgeWidths | LocalizedEdgeWidths--><!--Device-BorderImageOption-width?: Length | EdgeWidths | LocalizedEdgeWidths-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

