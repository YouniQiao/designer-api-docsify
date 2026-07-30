# AlbumPickerController

A controller that enables applications to send data to the **AlbumPickerComponent**.

**Since:** 20

**Decorator:** @Observed

<!--Device-unnamed-export declare class AlbumPickerController--><!--Device-unnamed-export declare class AlbumPickerController-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { EmptyAreaClickCallback, AlbumPickerComponent, AlbumInfo, AlbumPickerOptions, AlbumPickerController } from '@kit.MediaLibraryKit';
```

## setFontSize

```TypeScript
setFontSize(fontSize: number | string): void
```

Sets the font size of the album list.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AlbumPickerController-setFontSize(fontSize: number | string): void--><!--Device-AlbumPickerController-setFontSize(fontSize: number | string): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fontSize | number \| string | Yes | Font size. For details about the value range, see [fontSize](TextAttribute#fontSize). |

