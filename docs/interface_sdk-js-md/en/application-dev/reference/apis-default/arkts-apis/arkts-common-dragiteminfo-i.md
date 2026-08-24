# DragItemInfo

DragItemInfo object description

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface DragItemInfo--><!--Device-unnamed-export declare interface DragItemInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## builder

```TypeScript
builder?: CustomBuilder
```

拖拽过程中显示自定义组件，如果设置了pixelMap，则忽略此值。  
**说明：**不支持全局builder，如果builder中使用了Image组件，应尽量开启同步加载，即 配置Image的 syncLoad为true，该builder只用于生成当次拖拽 中显示的图片，builder的修改不会同步到当前正在拖拽的图片，对builder的修改需要在下一次拖拽时生 效。builder传参时，建议传参格式为builder: ()=&gt;{this.customBuilder()}，用以保证this指向的正确 性。具体请参考 将@Builder装饰的函数当作CustomBuilder类型使用。

**Type:** [CustomBuilder](arkts-custombuilder-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragItemInfo-builder?: CustomBuilder--><!--Device-DragItemInfo-builder?: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## extraInfo

```TypeScript
extraInfo?: string
```

拖拽项的附加信息，用于描述拖拽项。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragItemInfo-extraInfo?: string--><!--Device-DragItemInfo-extraInfo?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pixelMap

```TypeScript
pixelMap?: PixelMap
```

设置拖拽过程中显示的图片。

**Type:** [PixelMap](arkts-pixelmap-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragItemInfo-pixelMap?: PixelMap--><!--Device-DragItemInfo-pixelMap?: PixelMap-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

