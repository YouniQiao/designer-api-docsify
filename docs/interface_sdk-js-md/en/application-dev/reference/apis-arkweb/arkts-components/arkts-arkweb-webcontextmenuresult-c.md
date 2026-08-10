# WebContextMenuResult

Defines the context menu result, related to {@link WebContextMenuResult} method.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-unnamed-declare class WebContextMenuResult--><!--Device-unnamed-declare class WebContextMenuResult-End-->

**System capability:** SystemCapability.Web.Webview.Core

## closeContextMenu

```TypeScript
closeContextMenu(): void
```

在WebContextMenuResult中无其他调用且需要关闭上下文菜单时，开发者需调用此函数关闭菜单。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebContextMenuResult-closeContextMenu(): void--><!--Device-WebContextMenuResult-closeContextMenu(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

WebContextMenuResult的构造函数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebContextMenuResult-constructor()--><!--Device-WebContextMenuResult-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## copy

```TypeScript
copy(): void
```

执行与此上下文菜单关联的复制操作。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebContextMenuResult-copy(): void--><!--Device-WebContextMenuResult-copy(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## copyImage

```TypeScript
copyImage(): void
```

若WebContextMenuParam包含图片内容，该函数将复制当前上下文菜单对应的图片。若WebContextMenuParam不包含图片内容，则该函数不执行任何操作。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebContextMenuResult-copyImage(): void--><!--Device-WebContextMenuResult-copyImage(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## cut

```TypeScript
cut(): void
```

执行与此上下文菜单关联的剪切操作。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebContextMenuResult-cut(): void--><!--Device-WebContextMenuResult-cut(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## paste

```TypeScript
paste(): void
```

执行与此上下文菜单关联的粘贴操作。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebContextMenuResult-paste(): void--><!--Device-WebContextMenuResult-paste(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## pasteAndMatchStyle

```TypeScript
pasteAndMatchStyle(): void
```

执行与此上下文菜单关联的粘贴并匹配样式操作。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-WebContextMenuResult-pasteAndMatchStyle(): void--><!--Device-WebContextMenuResult-pasteAndMatchStyle(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## redo

```TypeScript
redo(): void
```

执行与此上下文菜单关联的重做操作。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-WebContextMenuResult-redo(): void--><!--Device-WebContextMenuResult-redo(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## requestPasswordAutoFill

```TypeScript
requestPasswordAutoFill(): void
```

请求将密码保险箱内容填充到输入框中。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-WebContextMenuResult-requestPasswordAutoFill(): void--><!--Device-WebContextMenuResult-requestPasswordAutoFill(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## saveImage

```TypeScript
saveImage(): void
```

执行与此上下文菜单关联的“另存为图像”操作将触发下载过程。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebContextMenuResult-saveImage(): void--><!--Device-WebContextMenuResult-saveImage(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## selectAll

```TypeScript
selectAll(): void
```

执行与此上下文菜单关联的全选操作。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebContextMenuResult-selectAll(): void--><!--Device-WebContextMenuResult-selectAll(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## undo

```TypeScript
undo(): void
```

执行与此上下文菜单关联的撤销操作。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-WebContextMenuResult-undo(): void--><!--Device-WebContextMenuResult-undo(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

