# DecorationStyle

Describes the text decorative line style.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare class DecorationStyle--><!--Device-unnamed-declare class DecorationStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value: DecorationStyleInterface)
```

A constructor used to create a text decorative line style.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DecorationStyle-constructor(value: DecorationStyleInterface)--><!--Device-DecorationStyle-constructor(value: DecorationStyleInterface)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [DecorationStyleInterface](arkts-arkui-decorationstyleinterface-i.md) | Yes | Text decorative line options.&lt;br&gt;Default value:&lt;br&gt;{&lt;br&gt; type: TextDecorationType.None,&lt;br&gt; color: Color.Black,&lt;br&gt; style: TextDecorationStyle.SOLID &lt;br&gt;} |

## constructor

```TypeScript
constructor(value: DecorationStyleInterface, options?: DecorationOptions)
```

Constructor of a text decoration line style, including additional configuration options.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DecorationStyle-constructor(value: DecorationStyleInterface, options?: DecorationOptions)--><!--Device-DecorationStyle-constructor(value: DecorationStyleInterface, options?: DecorationOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [DecorationStyleInterface](arkts-arkui-decorationstyleinterface-i.md) | Yes | Text decorative line options.&lt;br&gt;Default value:&lt;br&gt;{&lt;br&gt; type: TextDecorationType.None,&lt;br&gt; color: Color.Black,&lt;br&gt; style: TextDecorationStyle.SOLID, &lt;br&gt; thicknessScale: 1.0 &lt;br&gt;} |
| options | [DecorationOptions](arkts-arkui-styledstring-decorationoptions-i.md) | No | Additional configuration options for the text decoration line.&lt;br&gt;Default value:&lt;br&gt;{&lt;br&gt; enableMultiType: undefined&lt;br&gt;} |

## color

```TypeScript
readonly color?: ResourceColor
```

Color of the text decorative line.

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DecorationStyle-readonly color?: ResourceColor--><!--Device-DecorationStyle-readonly color?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## options

```TypeScript
readonly options?: DecorationOptions
```

Additional configuration options for the text decoration line style.

**Type:** [DecorationOptions](arkts-arkui-styledstring-decorationoptions-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DecorationStyle-readonly options?: DecorationOptions--><!--Device-DecorationStyle-readonly options?: DecorationOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
readonly style?: TextDecorationStyle
```

Style of the text decorative line.

**Type:** [TextDecorationStyle](arkts-arkui-enums-textdecorationstyle-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DecorationStyle-readonly style?: TextDecorationStyle--><!--Device-DecorationStyle-readonly style?: TextDecorationStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## thicknessScale

```TypeScript
readonly thicknessScale?: number
```

Scale factor for the thickness of the text decoration line.

**Type:** number

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DecorationStyle-readonly thicknessScale?: number--><!--Device-DecorationStyle-readonly thicknessScale?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
readonly type: TextDecorationType
```

Type of the text decorative line.

**Type:** [TextDecorationType](arkts-arkui-textdecorationtype-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DecorationStyle-readonly type: TextDecorationType--><!--Device-DecorationStyle-readonly type: TextDecorationType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

