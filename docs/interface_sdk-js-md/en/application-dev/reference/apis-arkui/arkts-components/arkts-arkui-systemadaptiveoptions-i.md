# SystemAdaptiveOptions

系统自适应调节参数，系统会默认开启根据芯片算力进行自适应效果调节的能力。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

<!--Device-unnamed-declare interface SystemAdaptiveOptions--><!--Device-unnamed-declare interface SystemAdaptiveOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## disableSystemAdaptation

```TypeScript
disableSystemAdaptation?: boolean
```

系统自适应调节参数，推荐不携带该参数。该参数只影响低算力设备，低算力设备的定义由设备厂商决定。在低芯片算力的设备上，会根据算力和负载等条件，自动决策是否使用低算力的近似效果替代原有效果，比如模糊效果会结合接口中携带的模糊相关参数值及其他低算力处理逻辑，进行自适应效果降级处理。如果想关闭该功能，可以将该标志置为true。

默认值：false

**Type:** boolean

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**Widget capability:** This API can be used in ArkTS widgets since API version 19.

<!--Device-SystemAdaptiveOptions-disableSystemAdaptation?: boolean--><!--Device-SystemAdaptiveOptions-disableSystemAdaptation?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

