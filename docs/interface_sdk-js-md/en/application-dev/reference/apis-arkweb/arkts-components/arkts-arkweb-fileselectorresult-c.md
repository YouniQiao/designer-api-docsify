# FileSelectorResult

定义文件选择器结果，与 {@link onFileSelectorShow} 方法相关联。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-unnamed-declare class FileSelectorResult--><!--Device-unnamed-declare class FileSelectorResult-End-->

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

FileSelectorResult的构造函数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FileSelectorResult-constructor()--><!--Device-FileSelectorResult-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## handleFileList

```TypeScript
handleFileList(fileList: Array<string>): void
```

选择文件列表。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FileSelectorResult-handleFileList(fileList: Array<string>): void--><!--Device-FileSelectorResult-handleFileList(fileList: Array<string>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fileList | Array&lt;string&gt; | Yes | List of files that need to be operated. |

