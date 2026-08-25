# WebContextMenuResult

Defines the context menu result, related to [WebContextMenuResult](#webcontextmenuresult) method.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## closeContextMenu

```TypeScript
closeContextMenu(): void
```

When close context menu without other call in WebContextMenuResult, User should call this function to close menu

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

Constructor.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## copy

```TypeScript
copy(): void
```

Executes the copy operation related to this context menu.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## copyImage

```TypeScript
copyImage(): void
```

If WebContextMenuParam has image content, this function will copy image related to this context menu. If WebContextMenuParam has no image content, this function will do nothing.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## cut

```TypeScript
cut(): void
```

Executes the cut operation related to this context menu.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## paste

```TypeScript
paste(): void
```

Executes the paste operation related to this context menu.<p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> Permissions need to be configured: ohos.permission.READ_PASTEBOARD. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## pasteAndMatchStyle

```TypeScript
pasteAndMatchStyle(): void
```

Executes the paste and match style operation related to this context menu.<p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> Permissions need to be configured: ohos.permission.READ_PASTEBOARD. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## redo

```TypeScript
redo(): void
```

Executes the redo operation related to this context menu.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## requestPasswordAutoFill

```TypeScript
requestPasswordAutoFill(): void
```

Request to fill the password vault contents into the input field.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## saveImage

```TypeScript
saveImage(): void
```

Performing the "Save As Image" operation associated with this context menu will trigger the download process.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

## selectAll

```TypeScript
selectAll(): void
```

Executes the selectAll operation related to this context menu.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## undo

```TypeScript
undo(): void
```

Executes the undo operation related to this context menu.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core
