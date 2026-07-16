# FileSelectorParam

Encompassed message information as parameters to {@link onFileSelectorShow} method.

**Since:** 9

<!--Device-unnamed-declare class FileSelectorParam--><!--Device-unnamed-declare class FileSelectorParam-End-->

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

Constructor.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FileSelectorParam-constructor()--><!--Device-FileSelectorParam-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## getAcceptType

```TypeScript
getAcceptType(): Array<string>
```

Gets an array of acceptable MIME type.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FileSelectorParam-getAcceptType(): Array<string>--><!--Device-FileSelectorParam-getAcceptType(): Array<string>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [Array](../../apis-na/arkts-apis/arkts-na-array-i.md)<string> | Return an array of acceptable MIME type. |

## getAcceptableFileTypes

```TypeScript
getAcceptableFileTypes(): Array<Array<AcceptableFileType>>
```

Gets an array of selected types for web page files.

**Since:** 23

<!--Device-FileSelectorParam-getAcceptableFileTypes(): Array<Array<AcceptableFileType>>--><!--Device-FileSelectorParam-getAcceptableFileTypes(): Array<Array<AcceptableFileType>>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [Array](../../apis-na/arkts-apis/arkts-na-array-i.md)<Array<AcceptableFileType>> | Return an array of selected types for web page files. |

## getDefaultPath

```TypeScript
getDefaultPath(): string
```

Get the default path opened when pulling up the selector.

**Since:** 23

<!--Device-FileSelectorParam-getDefaultPath(): string--><!--Device-FileSelectorParam-getDefaultPath(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Return to the default path opened when pulling up the selector. |

## getDescriptions

```TypeScript
getDescriptions(): Array<string>
```

Gets a description array of file types.

**Since:** 23

<!--Device-FileSelectorParam-getDescriptions(): Array<string>--><!--Device-FileSelectorParam-getDescriptions(): Array<string>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [Array](../../apis-na/arkts-apis/arkts-na-array-i.md)<string> | Return an array of description of the file type. |

## getMimeTypes

```TypeScript
getMimeTypes(): Array<string>
```

Gets an array of raw acceptable MIME type.

**Since:** 18

<!--Device-FileSelectorParam-getMimeTypes(): Array<string>--><!--Device-FileSelectorParam-getMimeTypes(): Array<string>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [Array](../../apis-na/arkts-apis/arkts-na-array-i.md)<string> | Return an array of raw acceptable MIME type. |

## getMode

```TypeScript
getMode(): FileSelectorMode
```

Gets the FileSelectorMode of this file selector.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FileSelectorParam-getMode(): FileSelectorMode--><!--Device-FileSelectorParam-getMode(): FileSelectorMode-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [FileSelectorMode](arkts-arkweb-fileselectormode-e.md) | Return the FileSelectorMode of this file selector. |

## getSuggestedName

```TypeScript
getSuggestedName(): string
```

Gets suggested file names.

**Since:** 23

<!--Device-FileSelectorParam-getSuggestedName(): string--><!--Device-FileSelectorParam-getSuggestedName(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Return the suggested file names. |

## getTitle

```TypeScript
getTitle(): string
```

Gets the title of this file selector.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FileSelectorParam-getTitle(): string--><!--Device-FileSelectorParam-getTitle(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Return the title of this file selector. |

## isAcceptAllOptionExcluded

```TypeScript
isAcceptAllOptionExcluded(): boolean
```

Gets whether to filter fully matching file types.

**Since:** 23

<!--Device-FileSelectorParam-isAcceptAllOptionExcluded(): boolean--><!--Device-FileSelectorParam-isAcceptAllOptionExcluded(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Return whether to filter all matching file types. |

## isCapture

```TypeScript
isCapture(): boolean
```

Gets whether this file selector use a live media captured value.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FileSelectorParam-isCapture(): boolean--><!--Device-FileSelectorParam-isCapture(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Return {@code true} if captured media; return {@code false} otherwise. |

