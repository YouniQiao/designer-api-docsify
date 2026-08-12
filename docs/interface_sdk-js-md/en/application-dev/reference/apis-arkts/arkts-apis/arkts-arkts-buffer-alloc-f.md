# alloc

## Modules to Import

```TypeScript
import { buffer } from '@kit.ArkTS';
```

## alloc

```TypeScript
function alloc(size: int, fill?: string | Buffer | int | double | long, encoding?: BufferEncoding): Buffer
```

Creates and initializes a **Buffer** object of the specified length.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function alloc(size: int, fill?: string | Buffer | int | double | long, encoding?: BufferEncoding): Buffer--><!--Device-buffer-function alloc(size: int, fill?: string | Buffer | int | double | long, encoding?: BufferEncoding): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Size of the **Buffer** object to create, in bytes. |
| fill | ArkTS-Dyn: string \| [Buffer](arkts-arkts-buffer-buffer-c.md) \| number \| number \| number  <br>ArkTS-Sta：string \| [Buffer](arkts-arkts-buffer-buffer-c.md) \| int \| double \| long | No | Value to be filled in the buffer. The default value is **0**.<br>**Since:** 9 - 10 |
| encoding | BufferEncoding | No | Encoding format (valid only when **fill** is a string). The default value is **'utf8'**. |

**Return value:**

| Type | Description |
| --- | --- |
| [Buffer](arkts-arkts-buffer-buffer-c.md) | Buffer** object created. |

