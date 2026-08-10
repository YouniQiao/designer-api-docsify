# ImageCompleteEvent

图片数据加载成功和解码成功时触发回调的返回对象。

当组件的参数类型为[AnimatedDrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)时该事件不触发。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface ImageCompleteEvent--><!--Device-unnamed-export interface ImageCompleteEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## componentHeight

```TypeScript
componentHeight: int
```

组件的高。

单位：像素

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageCompleteEvent-componentHeight: int--><!--Device-ImageCompleteEvent-componentHeight: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## componentWidth

```TypeScript
componentWidth: int
```

组件的宽。

单位：像素

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageCompleteEvent-componentWidth: int--><!--Device-ImageCompleteEvent-componentWidth: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentHeight

```TypeScript
contentHeight: int
```

图片实际绘制的高度。

单位：像素

**说明：**

仅在loadingStatus返回1时有效。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageCompleteEvent-contentHeight: int--><!--Device-ImageCompleteEvent-contentHeight: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentOffsetX

```TypeScript
contentOffsetX: int
```

实际绘制内容相对于组件自身的x轴偏移。

单位：像素

**说明：**

仅在loadingStatus返回1时有效。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageCompleteEvent-contentOffsetX: int--><!--Device-ImageCompleteEvent-contentOffsetX: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentOffsetY

```TypeScript
contentOffsetY: int
```

实际绘制内容相对于组件自身的y轴偏移。

单位：像素

**说明：**

仅在loadingStatus返回1时有效。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageCompleteEvent-contentOffsetY: int--><!--Device-ImageCompleteEvent-contentOffsetY: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentWidth

```TypeScript
contentWidth: int
```

图片实际绘制的宽度。

单位：像素

**说明：**

仅在loadingStatus返回1时有效。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageCompleteEvent-contentWidth: int--><!--Device-ImageCompleteEvent-contentWidth: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
height: int
```

图片的高。

单位：像素

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageCompleteEvent-height: int--><!--Device-ImageCompleteEvent-height: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## loadingStatus

```TypeScript
loadingStatus: int
```

图片加载成功的状态值。

**说明：**

返回的状态值为0时，表示图片数据加载成功。返回的状态值为1时，表示图片解码成功。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageCompleteEvent-loadingStatus: int--><!--Device-ImageCompleteEvent-loadingStatus: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width: int
```

图片的宽。

单位：像素

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageCompleteEvent-width: int--><!--Device-ImageCompleteEvent-width: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

