# DragItemInfo

定义拖拽过程中拖拽项的相关信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare interface DragItemInfo--><!--Device-unnamed-declare interface DragItemInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## builder

```TypeScript
builder?: CustomBuilder
```

拖拽过程中显示自定义组件，如果设置了pixelMap，则忽略此值。

**说明：**

不支持全局builder。如果builder中使用了[Image](../../apis-image-kit/arkts-apis/arkts-multimedia-image.md/arkts-multimedia-image.md)组件，应尽量开启同步加载，即配置Image的[syncLoad](../arkts-apis/arkts-arkui-image-imageattribute-i.md/arkts-arkui-image-imageattribute-i.md#syncload)为true。该builder只用于生成当次拖拽中显示的图片，builder的修改不会同步到当前正在拖拽的图片，对builder的修改需要在下一次拖拽时生效。

builder传参时，建议传参格式为builder: ()=>{this.customBuilder()}，用以保证this指向的正确性。具体请参考  
[将@Builder装饰的函数当作CustomBuilder类型使用](../../../ui/state-management/arkts-builder.md#将builder装饰的函数当作custombuilder类型使用)。

**Type:** [CustomBuilder](arkts-arkui-custombuilder-t.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DragItemInfo-builder?: CustomBuilder--><!--Device-DragItemInfo-builder?: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## extraInfo

```TypeScript
extraInfo?: string
```

拖拽项的附加信息，用于描述拖拽项。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DragItemInfo-extraInfo?: string--><!--Device-DragItemInfo-extraInfo?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pixelMap

```TypeScript
pixelMap?: PixelMap
```

设置拖拽过程中显示的图片。

**Type:** [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DragItemInfo-pixelMap?: PixelMap--><!--Device-DragItemInfo-pixelMap?: PixelMap-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

