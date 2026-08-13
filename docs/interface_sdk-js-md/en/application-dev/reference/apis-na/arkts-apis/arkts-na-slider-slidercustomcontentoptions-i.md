# SliderCustomContentOptions

Defines the options for customizing the accessibility of content within a slider. These options can be used to enhance the user experience for assistive technologies.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface SliderCustomContentOptions--><!--Device-unnamed-export declare interface SliderCustomContentOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityDescription

```TypeScript
accessibilityDescription?: ResourceStr
```

A more detailed description for accessibility. This can provide additional context about the slider content for users relying on assistive technologies. The default value is the device's default accessibility prompt.

**Type:** [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderCustomContentOptions-accessibilityDescription?: ResourceStr--><!--Device-SliderCustomContentOptions-accessibilityDescription?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityGroup

```TypeScript
accessibilityGroup?: boolean
```

Indicates whether the slider content should be treated as an accessibility group.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderCustomContentOptions-accessibilityGroup?: boolean--><!--Device-SliderCustomContentOptions-accessibilityGroup?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
accessibilityLevel?: string
```

The accessibility level of the slider content. This could be used to indicate the importance or priority of the content for assistive technologies.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderCustomContentOptions-accessibilityLevel?: string--><!--Device-SliderCustomContentOptions-accessibilityLevel?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityText

```TypeScript
accessibilityText?: ResourceStr
```

The text used for accessibility purposes. This text will be read by screen readers to provide a more descriptive label for the slider content. The default value is an empty string.

**Type:** [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderCustomContentOptions-accessibilityText?: ResourceStr--><!--Device-SliderCustomContentOptions-accessibilityText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

