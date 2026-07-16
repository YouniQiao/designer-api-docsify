# WebContextMenuParam

Defines the context menu param, related to {@link WebContextMenuParam} method.

**Since:** 9

<!--Device-unnamed-declare class WebContextMenuParam--><!--Device-unnamed-declare class WebContextMenuParam-End-->

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

Constructor.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebContextMenuParam-constructor()--><!--Device-WebContextMenuParam-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## existsImageContents

```TypeScript
existsImageContents(): boolean
```

Long press menu location has image content.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebContextMenuParam-existsImageContents(): boolean--><!--Device-WebContextMenuParam-existsImageContents(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Return whether this context menu has image content. |

## getContextMenuMediaType

```TypeScript
getContextMenuMediaType(): ContextMenuDataMediaType
```

Returns the type of context node.

**Since:** 22

<!--Device-WebContextMenuParam-getContextMenuMediaType(): ContextMenuDataMediaType--><!--Device-WebContextMenuParam-getContextMenuMediaType(): ContextMenuDataMediaType-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [ContextMenuDataMediaType](arkts-arkweb-contextmenudatamediatype-e.md) | Returns the type of context node. |

## getEditStateFlags

```TypeScript
getEditStateFlags(): number
```

Returns the context editable flags {@link ContextMenuEditStateFlags}.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebContextMenuParam-getEditStateFlags(): number--><!--Device-WebContextMenuParam-getEditStateFlags(): number-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | @syscap SystemCapability.Web.Webview.Core@atomicservice |

## getInputFieldType

```TypeScript
getInputFieldType(): ContextMenuInputFieldType
```

Returns input field type if the context menu was invoked on an input field.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebContextMenuParam-getInputFieldType(): ContextMenuInputFieldType--><!--Device-WebContextMenuParam-getInputFieldType(): ContextMenuInputFieldType-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [ContextMenuInputFieldType](arkts-arkweb-contextmenuinputfieldtype-e.md) | Input field type if the context menu was invoked on an input field. |

## getLinkUrl

```TypeScript
getLinkUrl(): string
```

If the long-press location is the link returns the link's security-checked URL.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebContextMenuParam-getLinkUrl(): string--><!--Device-WebContextMenuParam-getLinkUrl(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | If relate to a link return link url, else return null. |

## getMediaType

```TypeScript
getMediaType(): ContextMenuMediaType
```

Returns the type of context node.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebContextMenuParam-getMediaType(): ContextMenuMediaType--><!--Device-WebContextMenuParam-getMediaType(): ContextMenuMediaType-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [ContextMenuMediaType](arkts-arkweb-contextmenumediatype-e.md) | Returns the type of context node. |

## getPreviewHeight

```TypeScript
getPreviewHeight(): number
```

Returns the selection menu preview height.

**Since:** 13

<!--Device-WebContextMenuParam-getPreviewHeight(): number--><!--Device-WebContextMenuParam-getPreviewHeight(): number-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | The preview menu height. Unit: px. |

## getPreviewWidth

```TypeScript
getPreviewWidth(): number
```

Returns the selection menu preview width.

**Since:** 13

<!--Device-WebContextMenuParam-getPreviewWidth(): number--><!--Device-WebContextMenuParam-getPreviewWidth(): number-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | The preview menu width. Unit: px. |

## getSelectionText

```TypeScript
getSelectionText(): string
```

Returns the text of the selection.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebContextMenuParam-getSelectionText(): string--><!--Device-WebContextMenuParam-getSelectionText(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Returns the text of the selection, or return null if no text is selected. |

## getSourceType

```TypeScript
getSourceType(): ContextMenuSourceType
```

Returns the context menu source type.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebContextMenuParam-getSourceType(): ContextMenuSourceType--><!--Device-WebContextMenuParam-getSourceType(): ContextMenuSourceType-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [ContextMenuSourceType](arkts-arkweb-contextmenusourcetype-e.md) | @syscap SystemCapability.Web.Webview.Core@atomicservice |

## getSourceUrl

```TypeScript
getSourceUrl(): string
```

Returns the SRC URL if the selected element has a SRC attribute.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebContextMenuParam-getSourceUrl(): string--><!--Device-WebContextMenuParam-getSourceUrl(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | If this context menu is "src" attribute, return link url, else return null. |

## getUnfilteredLinkUrl

```TypeScript
getUnfilteredLinkUrl(): string
```

If the long-press location is the link returns the link's original URL.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebContextMenuParam-getUnfilteredLinkUrl(): string--><!--Device-WebContextMenuParam-getUnfilteredLinkUrl(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | If relate to a link return unfiltered link url, else return null. |

## isEditable

```TypeScript
isEditable(): boolean
```

Returns whether the context is editable.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebContextMenuParam-isEditable(): boolean--><!--Device-WebContextMenuParam-isEditable(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | @syscap SystemCapability.Web.Webview.Core@atomicservice |

## x

```TypeScript
x(): number
```

Horizontal offset coordinates of the menu within the Web component.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebContextMenuParam-x(): number--><!--Device-WebContextMenuParam-x(): number-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | The context menu x coordinate.Returns a non-negative integer if normal, otherwise returns -1.Unit: px. |

## y

```TypeScript
y(): number
```

Vertical offset coordinates for the menu within the Web component.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebContextMenuParam-y(): number--><!--Device-WebContextMenuParam-y(): number-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | The context menu y coordinate.Returns a non-negative integer if normal, otherwise returns -1.Unit: px. |

