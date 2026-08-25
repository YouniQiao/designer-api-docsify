# FontCollection

Represents a font collection, which manages the font resources required for text typesetting. FontCollection provides font matching and glyph lookup capabilities for [ParagraphBuilder](arkts-arkgraphics2d-text-paragraphbuilder-c.md), and serves as a fundamental component of the text typesetting pipeline. It provides a global instance ([getGlobalInstance](#getglobalinstance)) and local instances ([getLocalInstance](#getlocalinstance)). Fonts loaded by the global instance are shared within the app, making it suitable for common app scenarios. Local instances are independent of each other, and fonts loaded by a local instance take effect only for that instance without affecting others, making them recommended for widget scenarios. Custom fonts can be loaded through [loadFontSync](#loadfontsync) or [loadFont](#loadfont).

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## clearCaches

```TypeScript
clearCaches(): void
```

Clears the font typesetting cache. The font typesetting cache has a memory limit and an automatic clearing mechanism. It occupies limited memory. You are not advised to clear it unless there are special memory requirements.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

## getGlobalInstance

```TypeScript
static getGlobalInstance(): FontCollection
```

Obtains a global **FontCollection** instance.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FontCollection](arkts-arkgraphics2d-text-fontcollection-c.md) |

## getLocalInstance

```TypeScript
static getLocalInstance(): FontCollection
```

Obtains the local **FontCollection** instance. This API is recommended for widgets.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FontCollection](arkts-arkgraphics2d-text-fontcollection-c.md) |

## loadFont

```TypeScript
loadFont(name: string, path: string | Resource): Promise<void>
```

Loads the custom font. This API uses a promise to return the result. In this API, **name** specifies the alias of the font, and the custom font effect can be displayed only when the value of **name** is set in **fontFamilies** in **[TextStyle](arkts-arkgraphics2d-text-textstyle-i.md)**. The supported font file formats are TTF and OTF.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 22.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| path | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## loadFontSync

```TypeScript
loadFontSync(name: string, path: string | Resource): void
```

Loads a custom font. This API returns the result synchronously. In this API, **name** specifies the alias of the font, and the custom font effect can be displayed only when the value of **name** is set in **fontFamilies** in **[TextStyle](arkts-arkgraphics2d-text-textstyle-i.md)**. The supported font file formats are TTF and OTF.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| path | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

## loadFontSyncWithCheck

```TypeScript
loadFontSyncWithCheck(name: string, path: string | Resource, index?: number): void
```

Loads a custom font. This API returns the result synchronously. In this API, **name** specifies the alias of the font, and the custom font effect can be displayed only when the value of **name** is set in **fontFamilies** in **[TextStyle](arkts-arkgraphics2d-text-textstyle-i.md)**. The supported font file formats are TTF, OTF, and TTC.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| path | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |
| index | number | No |

**Error codes:**

| Error Code ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) |
| [25900002](../errorcode-drawing.md#25900002-file-not-found) |
| [25900003](../errorcode-drawing.md#25900003-failed-to-open-the-file) |
| [25900004](../errorcode-drawing.md#25900004-failed-to-locate-the-file) |
| [25900005](../errorcode-drawing.md#25900005-failed-to-obtain-the-file-size) |
| [25900006](../errorcode-drawing.md#25900006-failed-to-read-the-file) |
| [25900007](../errorcode-drawing.md#25900007-empty-file) |
| [25900008](../errorcode-drawing.md#25900008-file-damaged) |

## loadFontWithCheck

```TypeScript
loadFontWithCheck(name: string, path: string | Resource, index?: number): Promise<void>
```

Loads a custom font. This API uses a promise to return the result. In this API, **name** specifies the alias of the font, and the custom font effect can be displayed only when the value of **name** is set in **fontFamilies** in **[TextStyle](arkts-arkgraphics2d-text-textstyle-i.md)**. The supported font file formats are TTF, OTF, and TTC.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| path | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |
| index | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) |
| [25900002](../errorcode-drawing.md#25900002-file-not-found) |
| [25900003](../errorcode-drawing.md#25900003-failed-to-open-the-file) |
| [25900004](../errorcode-drawing.md#25900004-failed-to-locate-the-file) |
| [25900005](../errorcode-drawing.md#25900005-failed-to-obtain-the-file-size) |
| [25900006](../errorcode-drawing.md#25900006-failed-to-read-the-file) |
| [25900007](../errorcode-drawing.md#25900007-empty-file) |
| [25900008](../errorcode-drawing.md#25900008-file-damaged) |

## setParagraphCachesEnabled

```TypeScript
setParagraphCachesEnabled(enable: boolean): void
```

Sets whether to enable the typesetting paragraph caching. Typesetting paragraph caching can accelerate the typesetting of repeated text, but it will occupy extra memory. Before this API is called, the system enables typesetting paragraph caching by default.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

## unloadFont

```TypeScript
unloadFont(name: string): Promise<void>
```

Uninstalls a specified custom font. This API uses a promise to return the result.After this API is called to unload a custom font corresponding to a font alias, the custom font is no longer available.All layout objects that use the font alias must be destroyed and recreated.  
- Unloading a non-existent font alias does not produce any effect and does not throw an error.  
- This operation only affects future font usage.  
- Unloading a font that is currently in use may lead to text rendering exceptions (such as garbled characters or  
missing glyphs).

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 22.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## unloadFontSync

```TypeScript
unloadFontSync(name: string): void
```

Uninstalls a specified custom font. This API is synchronous.After this API is called to unload a custom font corresponding to a font alias, the custom font is no longer available.All layout objects that use the font alias must be destroyed and recreated.  
- Unloading a non-existent font alias does not produce any effect and does not throw an error.  
- This operation only affects future font usage.  
- Unloading a font that is currently in use may lead to text rendering exceptions (such as garbled characters or  
missing glyphs).

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 22.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
