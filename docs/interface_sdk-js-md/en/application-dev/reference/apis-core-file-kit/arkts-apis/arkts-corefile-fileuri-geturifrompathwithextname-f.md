# getUriFromPathWithExtName

## Modules to Import

```TypeScript
import { fileUri } from '@kit.CoreFileKit';
```

## getUriFromPathWithExtName

```TypeScript
function getUriFromPathWithExtName(path: string, extensionName: string): string
```

Generates a URI based on the file path in the application sandbox. Chinese characters and non-digit characters in the path are encoded into percentages.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-fileUri-function getUriFromPathWithExtName(path: string, extensionName: string): string--><!--Device-fileUri-function getUriFromPathWithExtName(path: string, extensionName: string): string-End-->

**System capability:** SystemCapability.FileManagement.AppFileService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | File path in the application sandbox. |
| extensionName | string | Yes | Extension ability name of the application. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Generated URI. |
