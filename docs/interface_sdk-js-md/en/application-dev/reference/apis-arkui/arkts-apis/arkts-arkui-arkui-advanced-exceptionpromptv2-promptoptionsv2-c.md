# PromptOptionsV2

Configuration parameter of ExceptionPromptV2.Use @ObservedV2 and @Trace to support deep observation and dynamic refresh of properties.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @ObservedV2

<!--Device-unnamed-export declare class PromptOptionsV2--><!--Device-unnamed-export declare class PromptOptionsV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(config?: PromptOptionsV2Config)
```

Constructor of PromptOptionsV2.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptOptionsV2-constructor(config?: PromptOptionsV2Config)--><!--Device-PromptOptionsV2-constructor(config?: PromptOptionsV2Config)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Configuration information of ExceptionPromptV2 |

## actionText

```TypeScript
public actionText?: ResourceStr
```

Text of the icon on the right of the ExceptionPromptV2.If this parameter is not set or is set to undefined, the text is not displayed.

**Type:** ResourceStr

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptOptionsV2-public actionText?: ResourceStr--><!--Device-PromptOptionsV2-public actionText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
public icon?: ResourceStr
```

Icon style of the ExceptionPromptV2.If this parameter is not set or is set to undefined, the icon is not displayed.

**Type:** ResourceStr

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptOptionsV2-public icon?: ResourceStr--><!--Device-PromptOptionsV2-public icon?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isShown

```TypeScript
public isShown?: boolean
```

Whether the ExceptionPromptV2 is displayed.true: The exception prompt is displayed.false: The exception prompt is hidden.Default value: false.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptOptionsV2-public isShown?: boolean--><!--Device-PromptOptionsV2-public isShown?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## marginTop

```TypeScript
public marginTop: Dimension
```

Top margin of the ExceptionPromptV2.Distance from the top to the content area of ExceptionPromptV2.

**Type:** Dimension

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptOptionsV2-public marginTop: Dimension--><!--Device-PromptOptionsV2-public marginTop: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## marginType

```TypeScript
public marginType: MarginTypeV2
```

Margin Type of ExceptionPromptV2.Margin from the content area to the edge of the container.

**Type:** MarginTypeV2

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptOptionsV2-public marginType: MarginTypeV2--><!--Device-PromptOptionsV2-public marginType: MarginTypeV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## symbolStyle

```TypeScript
public symbolStyle?: SymbolGlyphModifier
```

Symbol icon style of the ExceptionPromptV2, which has higher priority than icon.If this parameter is not set or is set to undefined, the symbol icon is not displayed.

**Type:** SymbolGlyphModifier

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptOptionsV2-public symbolStyle?: SymbolGlyphModifier--><!--Device-PromptOptionsV2-public symbolStyle?: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## tip

```TypeScript
public tip?: ResourceStr
```

Text content of the ExceptionPromptV2.By default, the following text resources are provided:1. ohos\_network\_not\_connected: displayed when no Internet connection.2. ohos\_network\_connected\_unstable: displayed when the Internet connection is unstable.3. ohos\_unstable\_connect\_server: displayed when the server fails to be connected.4. ohos\_custom\_network\_tips\_left: displayed when an Internet connection is available but the location fails to be obtained.If this parameter is not set or is set to undefined, the text content is not displayed.

**Type:** ResourceStr

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromptOptionsV2-public tip?: ResourceStr--><!--Device-PromptOptionsV2-public tip?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

