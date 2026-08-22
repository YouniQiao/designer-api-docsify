# ShadowOptions

Define the options of shadow

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface ShadowOptions--><!--Device-unnamed-export declare interface ShadowOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color?: Color | string | Resource | ColoringStrategy
```

Color of the shadow. Default value: **Black**

**Type:** [Color](../../apis-arkui/arkts-apis/arkts-arkui-color-e.md) \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| [ColoringStrategy](../../apis-arkui/arkts-apis/arkts-arkui-coloringstrategy-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShadowOptions-color?: Color | string | Resource | ColoringStrategy--><!--Device-ShadowOptions-color?: Color | string | Resource | ColoringStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fill

```TypeScript
fill?: boolean
```

Whether to fill the inside of the component with shadow. **true**: Fill the inside of the component with shadow. <br>**false**: Do not fill the inside of the component with shadow. <br>The default value is **false**. <br>**NOTE：**<br>This attribute does not take effect in textShadow.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShadowOptions-fill?: boolean--><!--Device-ShadowOptions-fill?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offsetX

```TypeScript
offsetX?: double | Resource
```

Offset of the shadow along the x-axis. Unit is px. Default value is 0.

**Type:** double \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShadowOptions-offsetX?: double | Resource--><!--Device-ShadowOptions-offsetX?: double | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offsetY

```TypeScript
offsetY?: double | Resource
```

Offset of the shadow along the y-axis. Unit is px. Default value is 0.

**Type:** double \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShadowOptions-offsetY?: double | Resource--><!--Device-ShadowOptions-offsetY?: double | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## radius

```TypeScript
radius: double | Resource | undefined
```

Blur radius of the shadow. Default value: 0px.

undefined means setting to default value.

**Type:** double \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShadowOptions-radius: double | Resource | undefined--><!--Device-ShadowOptions-radius: double | Resource | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type?: ShadowType
```

Shadow type. <br>Default value: **COLOR**.

**Type:** [ShadowType](arkts-common-shadowtype-e.md)

**Default:** ShadowType.COLOR

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShadowOptions-type?: ShadowType--><!--Device-ShadowOptions-type?: ShadowType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

