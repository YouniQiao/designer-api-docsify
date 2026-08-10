# Font

class Font

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class Font--><!--Device-unnamed-export declare class Font-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from 'kits/@kit.ArkUI';
```

## getFontByName

```TypeScript
getFontByName(fontName: string): font.FontInfo
```

根据名称获取系统字体的详细信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Font-getFontByName(fontName: string): font.FontInfo--><!--Device-Font-getFontByName(fontName: string): font.FontInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fontName | string | Yes | font name |

**Return value:**

| Type | Description |
| --- | --- |
| font.FontInfo | Returns the font info |

## getSystemFontList

```TypeScript
getSystemFontList(): Array<string>
```

Gets a list of fonts supported by system.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Font-getSystemFontList(): Array<string>--><!--Device-Font-getSystemFontList(): Array<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | A list of font names |

## registerFont

```TypeScript
registerFont(options: font.FontOptions): void
```

在字体管理器中注册自定义字体。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Font-registerFont(options: font.FontOptions): void--><!--Device-Font-registerFont(options: font.FontOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | font.FontOptions | Yes | FontOptions |

