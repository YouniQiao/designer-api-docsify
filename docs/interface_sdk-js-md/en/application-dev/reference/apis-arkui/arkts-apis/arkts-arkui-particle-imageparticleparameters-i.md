# ImageParticleParameters

设置图片选项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface ImageParticleParameters--><!--Device-unnamed-export interface ImageParticleParameters-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## objectFit

```TypeScript
objectFit?: ImageFit
```

图片显示模式。

**Type:** [ImageFit](arkts-arkui-imagefit-e.md)

**Default:** ImageFit.Cover

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageParticleParameters-objectFit?: ImageFit--><!--Device-ImageParticleParameters-objectFit?: ImageFit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## size

```TypeScript
size: ParticleTuple<Dimension, Dimension>
```

图像尺寸。

默认值：[0, 0]

**Type:** [ParticleTuple](arkts-arkui-particletuple-t.md)&lt;[Dimension](arkts-arkui-dimension-t.md), [Dimension](arkts-arkui-dimension-t.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageParticleParameters-size: ParticleTuple<Dimension, Dimension>--><!--Device-ImageParticleParameters-size: ParticleTuple<Dimension, Dimension>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## src

```TypeScript
src: ResourceStr
```

图片路径，支持本地图片和网络图片，引用方式请参考[加载图片资源](../../../ui/arkts-graphics-display.md#加载图片资源)。

暂不支持svg图片类型。

src未发生变化时，会优先使用缓存的资源，无法动态切换资源。如需动态切换资源建议切换为不同的src。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageParticleParameters-src: ResourceStr--><!--Device-ImageParticleParameters-src: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

