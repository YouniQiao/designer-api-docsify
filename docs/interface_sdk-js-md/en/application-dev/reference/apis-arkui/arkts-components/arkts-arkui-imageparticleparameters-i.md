# ImageParticleParameters

设置图片选项。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-interface ImageParticleParameters--><!--Device-unnamed-interface ImageParticleParameters-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## objectFit

```TypeScript
objectFit?: ImageFit
```

图片显示模式。

**Type:** [ImageFit](../arkts-apis/arkts-arkui-imagefit-e.md)

**Default:** ImageFit.Cover

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ImageParticleParameters-objectFit?: ImageFit--><!--Device-ImageParticleParameters-objectFit?: ImageFit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## size

```TypeScript
size: ParticleTuple<Dimension, Dimension>
```

图像尺寸。

默认值：[0, 0]

**Type:** [ParticleTuple](../arkts-apis/arkts-arkui-particletuple-t.md)&lt;[Dimension](../arkts-apis/arkts-arkui-dimension-t.md), [Dimension](../arkts-apis/arkts-arkui-dimension-t.md)&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ImageParticleParameters-size: ParticleTuple<Dimension, Dimension>--><!--Device-ImageParticleParameters-size: ParticleTuple<Dimension, Dimension>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## src

```TypeScript
src: ResourceStr
```

图片路径，支持本地图片和网络图片，引用方式请参考[加载图片资源](../../../ui/arkts-graphics-display.md#加载图片资源)。

暂不支持svg图片类型。

src未发生变化时，会优先使用缓存的资源，无法动态切换资源。如需动态切换资源建议切换为不同的src。

**Type:** [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ImageParticleParameters-src: ResourceStr--><!--Device-ImageParticleParameters-src: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

