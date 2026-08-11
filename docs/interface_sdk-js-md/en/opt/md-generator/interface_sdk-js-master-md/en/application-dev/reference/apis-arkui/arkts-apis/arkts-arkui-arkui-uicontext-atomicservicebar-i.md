# AtomicServiceBar

interface AtomicServiceBar

**Since:** 11

<!--Device-unnamed-export interface AtomicServiceBar--><!--Device-unnamed-export interface AtomicServiceBar-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from 'kits/@kit.ArkUI';
```

## getBarRect

```TypeScript
getBarRect(): Frame
```

Get size and position of the bar.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-AtomicServiceBar-getBarRect(): Frame--><!--Device-AtomicServiceBar-getBarRect(): Frame-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Frame](arkts-arkui-graphics-frame-i.md) |

## onBarRectChange

```TypeScript
onBarRectChange(callback: Callback<Frame>): void
```

When size and position of the bar changed, callback will be called.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AtomicServiceBar-onBarRectChange(callback: Callback<Frame>): void--><!--Device-AtomicServiceBar-onBarRectChange(callback: Callback<Frame>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Frame&gt; | Yes |

## setBackgroundColor

```TypeScript
setBackgroundColor(color: Nullable< Color | number | string>): void
```

Set the background color of the bar.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceBar-setBackgroundColor(color: Nullable< Color | number | string>): void--><!--Device-AtomicServiceBar-setBackgroundColor(color: Nullable< Color | number | string>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | [Nullable](arkts-arkui-nullable-t.md)&lt;Color \| number \| string&gt; | Yes |

## setIconColor

```TypeScript
setIconColor(color: Nullable< Color | number | string>): void
```

Set the color of the icon on the bar.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceBar-setIconColor(color: Nullable< Color | number | string>): void--><!--Device-AtomicServiceBar-setIconColor(color: Nullable< Color | number | string>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | [Nullable](arkts-arkui-nullable-t.md)&lt;Color \| number \| string&gt; | Yes |

## setTitleContent

```TypeScript
setTitleContent(content: string): void
```

Set the title of the bar.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceBar-setTitleContent(content: string): void--><!--Device-AtomicServiceBar-setTitleContent(content: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| content | string | Yes |

## setTitleFontStyle

```TypeScript
setTitleFontStyle(font: FontStyle): void
```

Set the font style of the bar's title.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceBar-setTitleFontStyle(font: FontStyle): void--><!--Device-AtomicServiceBar-setTitleFontStyle(font: FontStyle): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| font | [FontStyle](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-fontstyle-e.md) | Yes |

## setVisible

```TypeScript
setVisible(visible: boolean): void
```

Set the visibility of the bar, except the icon.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AtomicServiceBar-setVisible(visible: boolean): void--><!--Device-AtomicServiceBar-setVisible(visible: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| visible | boolean | Yes |
