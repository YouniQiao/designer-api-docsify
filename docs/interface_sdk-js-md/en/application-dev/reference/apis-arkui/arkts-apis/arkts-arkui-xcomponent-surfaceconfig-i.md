# SurfaceConfig

用于描述XComponent持有的Surface在渲染时是否需要被视为不透明。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface SurfaceConfig--><!--Device-unnamed-export declare interface SurfaceConfig-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isOpaque

```TypeScript
isOpaque?: boolean
```

XComponent持有的Surface在渲染时是否需要被视为不透明，未设置时默认取值为false，即在渲染时会应用Surface中绘制内容像素的透明度。

true：表示需要被视为不透明；false：表示不需要被视为不透明。

默认值：false

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SurfaceConfig-isOpaque?: boolean--><!--Device-SurfaceConfig-isOpaque?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

