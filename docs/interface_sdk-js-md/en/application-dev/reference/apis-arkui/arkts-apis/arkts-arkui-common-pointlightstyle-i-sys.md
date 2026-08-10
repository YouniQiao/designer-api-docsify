# PointLightStyle (System API)

通过设置光源和被照亮的类型实现点光源照亮周围组件的UI效果。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface PointLightStyle--><!--Device-unnamed-export declare interface PointLightStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## bloom

```TypeScript
bloom?: double
```

设置组件的发光强度，取值范围为[0, 1]，超出取值范围时会转换为默认值。

默认值：0

**Type:** double

**Default:** 0

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PointLightStyle-bloom?: double--><!--Device-PointLightStyle-bloom?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## illuminated

```TypeScript
illuminated?: IlluminatedType
```

设置当前组件是否可以被光源照亮，以及被照亮的类型。

默认值：IlluminatedType.NONE

**Type:** [IlluminatedType](arkts-arkui-illuminatedtype-e-sys.md)

**Default:** IlluminatedType.NONE

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PointLightStyle-illuminated?: IlluminatedType--><!--Device-PointLightStyle-illuminated?: IlluminatedType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## lightSource

```TypeScript
lightSource?: LightSource
```

设置光源属性，光源会影响到周围标记为可以被照亮的组件，并在组件上产生光效。

默认值：无光源

**Type:** [LightSource](arkts-arkui-common-lightsource-i-sys.md)

**Default:** undefined

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PointLightStyle-lightSource?: LightSource--><!--Device-PointLightStyle-lightSource?: LightSource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

