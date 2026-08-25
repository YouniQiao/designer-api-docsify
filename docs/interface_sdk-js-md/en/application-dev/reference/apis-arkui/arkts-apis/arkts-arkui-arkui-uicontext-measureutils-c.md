# MeasureUtils

Provides APIs for measuring text metrics, such as text height and width.

> **NOTE：**&gt;
> - In the following API examples, you must first use [getMeasureUtils()](arkts-arkui-arkui-uicontext-uicontext-c.md#getmeasureutils) in
> **UIContext** to obtain a **MeasureUtils** instance, and then call the APIs using the obtained instance.&gt;
> - To perform more complex text measurements, use the [Paragraph](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-paragraph-c.md) API.&gt;
> - Avoid using
> [ApplicationContext.setFontSizeScale](../../apis-ability-kit/arkts-apis/arkts-ability-applicationcontext-c.md#setfontsizescale)
> during text measurement API calls. To ensure timing correctness and the accuracy of measurement results, manually
> listen for font scale changes.&gt;
> - For measuring text after truncation, direct use of the string length for truncation may lead to inaccuracies.
> This is because certain Unicode characters (for example, emojis) have code points with a length greater than 1, and
> truncating by string length can split these multi-code-point characters, resulting in incorrect text display or
> measurement errors. As such, you are advised to perform iterative truncation processing based on Unicode code
> points. For details, see [Example 2 in measureTextSize](#measuretextsize).

**Since:** 12

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AtomicServiceBar, ComponentUtils, ContextMenuController, CursorController, DialogPresenter, DragController, Font, KeyboardAvoidMode, MediaQuery, OverlayManager, PromptAction, Router, UIContext, UIInspector, UIObserver, PageInfo, SwiperDynamicSyncScene, SwiperDynamicSyncSceneType, MarqueeDynamicSyncScene, MarqueeDynamicSyncSceneType, MeasureUtils, FrameCallback, OverlayManagerOptions, TargetInfo, TextMenuController, NodeIdentity, NodeRenderState, NodeRenderStateChangeCallback, Magnifier, ResolvedUIContext, TextSelectionClearPolicy, CustomKeyboardContinueFeature, BackgroundLuminanceSamplingConfigs, LuminanceSampler } from 'kits/@kit.ArkUI';
import { GestureListenerType, GestureActionPhase, GestureTriggerInfo, GestureObserverConfigs, GestureListenerCallback } from 'kits/@kit.ArkUI';
import { SwiperContentInfo, SwiperItemInfo } from 'kits/@kit.ArkUI';
import { BackPressActionProposal, BaseGestureHandlingProposal, ClickActionProposal, GestureHandlingResolution, NoneActionProposal, PageSwitchActionProposal, ScrollActionProposal, SelectActionProposal, SmartGestureController, TargetedGestureProposal } from 'kits/@kit.ArkUI';
```

## getParagraphs

```TypeScript
getParagraphs(styledString: StyledString, options?: TextLayoutOptions): Array<Paragraph>
```

Converts a styled string into an array of corresponding [Paragraph](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-paragraph-c.md) objects based on text layout options.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| styledString | [StyledString](arkts-arkui-styledstring-c.md) | Yes |
| options | [TextLayoutOptions](arkts-arkui-textlayoutoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;Paragraph & gt; |

## measureText

```TypeScript
measureText(options: MeasureOptions): number
```

Measures the single-line display width of the specified text. For multi-line text (separated by newline characters **\n**), this API returns the width of the longest line.

> **NOTE：**&gt;
> **measureText** always measures single-line text width. Layout constraints in **options** (**constraintWidth**,
> **maxLines**, and more) do not affect results. For layout-constrained width measurement, use
> [measureTextSize](#measuretextsize).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [MeasureOptions](arkts-arkui-measure-measureoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## measureTextSize

```TypeScript
measureTextSize(options: MeasureOptions): SizeOptions
```

Measures the width and height of the given single-line text.

> **NOTE：**&gt;
> When calling this MPI, do not use ApplicationContext.setFontSizeScale to set the font size scaling ratio. To
> ensure the correctness of the time sequence, you are advised to monitor the font scaling changes by yourself to
> ensure the accuracy of the calculation result.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [MeasureOptions](arkts-arkui-measure-measureoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SizeOptions](arkts-arkui-sizeoptions-i.md) |
