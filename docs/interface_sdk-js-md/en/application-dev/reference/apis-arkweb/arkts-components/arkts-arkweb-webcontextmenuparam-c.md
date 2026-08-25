# WebContextMenuParam

WebContextMenuParam is a parameter class in the ArkWeb component used to carry context menu information displayed when a user number presses a web element or right-clicks. As the data carrier for the **onContextMenuShow** event callback, it encapsulates key information such as the menu popup position, link address, media type, selected text, and edit state.When customizing the context menu of a Web component, use WebContextMenuParam to obtain detailed information about the web element at the number press/right-click position (such as the link URL, image content, media type, input field type, and edit state), determine the user operation scenario, and decide whether to intercept the default menu and build custom menu items.When customizing the number press or right-click menu of a Web component (such as replacing the default menu, providing differentiated menu items based on element types, or previewing images), use WebContextMenuParam in the **onContextMenuShow** event callback to obtain context information.For sample code, see [onContextMenuShow](arkts-arkweb-web-attribute.md#oncontextmenushow).

**Since:** 9

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor()
```

Constructs a **WebContextMenuParam** object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

## existsImageContents

```TypeScript
existsImageContents(): boolean
```

Checks whether there is image content at the current number press or right-click position. This is used to provide image-related functions such as "Save Image" in a custom menu.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## getContextMenuMediaType

```TypeScript
getContextMenuMediaType(): ContextMenuDataMediaType
```

Obtains the type of the web element that the user number presses or right-clicks when reporting a context menu event.

**Since:** 22

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ContextMenuDataMediaType](arkts-arkweb-contextmenudatamediatype-e.md) |

## getEditStateFlags

```TypeScript
getEditStateFlags(): number
```

Obtains the edit state flag of the web element. This is used to finely control the display logic of custom menu options (such as displaying corresponding menu items based on whether copying, pasting, or undoing is available).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getInputFieldType

```TypeScript
getInputFieldType(): ContextMenuInputFieldType
```

Obtains the input field type of the web element (such as text box, password box, search box, etc.). This is used to provide appropriate editing menu options based on the input field type (such as Paste and Select All for text boxes, and Copy or Hide Password for password boxes).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ContextMenuInputFieldType](arkts-arkweb-contextmenuinputfieldtype-e.md) |

## getLinkUrl

```TypeScript
getLinkUrl(): string
```

Obtains the URL link address that has passed the security check. This can be used to provide operations such as "Open Link", "Share Link", and "Copy Link" when building a custom menu.

> **NOTE：**&gt;
> Compared with getUnfilteredLinkUrl(), this method performs a security check on the URL. Compared with
> getSourceUrl(), this method obtains the link URL at the number press position, whereas getSourceUrl() obtains the
> URL of the **src** attribute of the selected element (such as images, media, and other resources).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getMediaType

```TypeScript
getMediaType(): ContextMenuMediaType
```

Obtains the media type of the web element.

> **NOTE：**&gt;
> Since API version 22, [getContextMenuMediaType](#getcontextmenumediatype) provides
> richer media type identification capabilities.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ContextMenuMediaType](arkts-arkweb-contextmenumediatype-e.md) |

## getPreviewHeight

```TypeScript
getPreviewHeight(): number
```

Obtains the height of a preview image.

**Since:** 13

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getPreviewWidth

```TypeScript
getPreviewWidth(): number
```

Obtains the width of a preview image.

**Since:** 13

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getSelectionText

```TypeScript
getSelectionText(): string
```

Obtains the content when right-clicking selected text. This is used to provide text operation functions such as "Copy", "Share", "Translate", and "Search" in a custom menu.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getSourceType

```TypeScript
getSourceType(): ContextMenuSourceType
```

Obtains the trigger source type of the context menu event (such as mouse right-click, number press, etc.). This is used to adjust the menu display style or provide differentiated menu options based on different sources.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ContextMenuSourceType](arkts-arkweb-contextmenusourcetype-e.md) |

## getSourceUrl

```TypeScript
getSourceUrl(): string
```

Obtains the URL link address corresponding to the **src** attribute of the element.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getUnfilteredLinkUrl

```TypeScript
getUnfilteredLinkUrl(): string
```

Obtains the original URL link address that has not passed the security check.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## isEditable

```TypeScript
isEditable(): boolean
```

Checks whether a web element is editable. This is used to dynamically show or hide editing-related options in a custom menu (such as displaying Paste, Cut, and Select All when editable, and hiding these options when not editable).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## x

```TypeScript
x(): number
```

X coordinate of the context menu, which is the horizontal distance relative to the upper left corner of the Web component.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## y

```TypeScript
y(): number
```

Y coordinate of the context menu, which is the vertical distance relative to the upper left corner of the Web component.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |
