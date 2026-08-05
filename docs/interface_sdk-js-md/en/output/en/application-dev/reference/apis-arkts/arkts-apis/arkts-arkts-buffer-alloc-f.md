# alloc

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
| size | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Size of the **Buffer** object to create, in bytes. |
| fill | ArkTS-Dyn: string \| Buffer \| number \| number \| number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：string \| Buffer \| int \| double \| long | No | Value to be filled in the buffer. The default value is **0**.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 9 - 10 |
| encoding | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Encoding format (valid only when **fill** is a string). The default value is **'utf8'**. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | **Buffer** object created. |

