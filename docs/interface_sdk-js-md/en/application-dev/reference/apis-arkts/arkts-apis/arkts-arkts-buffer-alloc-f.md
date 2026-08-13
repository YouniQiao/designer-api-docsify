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

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function alloc(size: int, fill?: string | Buffer | int | double | long, encoding?: BufferEncoding): Buffer--><!--Device-buffer-function alloc(size: int, fill?: string | Buffer | int | double | long, encoding?: BufferEncoding): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | int | Yes | Size of the **Buffer** object to create, in bytes. |
| fill | string \| [Buffer](arkts-arkts-buffer-buffer-c.md) \| int \| double \| long | No | Value to be filled in the buffer. The default value is **0**.<br>**Since:** 9 - 10 |
| encoding | BufferEncoding | No | Encoding format (valid only when **fill** is a string). The default value is **'utf8'**. |

**Return value:**

| Type | Description |
| --- | --- |
| [Buffer](arkts-arkts-buffer-buffer-c.md) | Buffer** object created. |

