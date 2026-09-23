# BackgroundColorStyle

```TypeScript
declare class BackgroundColorStyle
```

Describes the text background color style.

**Since:** 14

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(textBackgroundStyle: TextBackgroundStyle)
```

A constructor used to create the text background color. If this API is not used to set the value, the default background color is **Color.Transparent** and the corner radius is **0**.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| textBackgroundStyle | [TextBackgroundStyle](../arkts-components/arkts-arkui-span-comp-textbackgroundstyle-i.md) | Yes | Text background color setting item. |

## textBackgroundStyle

```TypeScript
readonly textBackgroundStyle: TextBackgroundStyle
```

Text background color of the styled string.

Default value:

**{

color: Color.Transparent,

radius: 0

}**

**Type:** [TextBackgroundStyle](../arkts-components/arkts-arkui-span-comp-textbackgroundstyle-i.md)

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
