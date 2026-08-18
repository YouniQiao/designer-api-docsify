# @ohos.buffer

/*
 Copyright (c) 2022 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (The type of "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


**Since:** 23

<!--Device-unnamed-declare namespace buffer--><!--Device-unnamed-declare namespace buffer-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { buffer } from '@kit.ArkTS';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [alloc](arkts-arkts-buffer-alloc-f.md#alloc) | Creates and initializes a **Buffer** object of the specified length. |
| [allocUninitialized](arkts-arkts-buffer-allocuninitialized-f.md#allocuninitialized) | Creates a **Buffer** object of the specified size, without initializing it. This API does not allocate memory from the buffer pool. You need to use [fill()](arkts-arkts-buffer-buffer-c.md#fill) to initialize the **Buffer** object created. |
| [allocUninitializedFromPool](arkts-arkts-buffer-allocuninitializedfrompool-f.md#allocuninitializedfrompool) | Creates a **Buffer** object of the specified size from the buffer pool, without initializing it. You need to use [fill()](arkts-arkts-buffer-buffer-c.md#fill) to initialize the **Buffer** object created. |
| [byteLength](arkts-arkts-buffer-bytelength-f.md#bytelength) | Obtains the number of bytes of a string based on the encoding format. |
| [byteLength](arkts-arkts-buffer-bytelength-f.md#bytelength) | Obtains the number of bytes of a string based on the encoding format. |
| [compare](arkts-arkts-buffer-compare-f.md#compare) | Compares two **Buffer** objects. This API is used for sorting **Buffer** objects. |
| [compare](arkts-arkts-buffer-compare-f.md#compare) | Compares buf1 to buf2 |
| [concat](arkts-arkts-buffer-concat-f.md#concat) | Concatenates an array of **Buffer** objects of the specified length into a new object. |
| [from](arkts-arkts-buffer-from-f.md#from) | Creates a **Buffer** object with the specified array. |
| [from](arkts-arkts-buffer-from-f.md#from) | Creates a **Buffer** object of the specified length that shares memory with ArrayBuffer. |
| [from](arkts-arkts-buffer-from-f.md#from) | This creates a view of the ArrayBuffer without copying the underlying memory. |
| [from](arkts-arkts-buffer-from-f.md#from) | Copies the data of a passed **Buffer** object to create a new **Buffer** object and returns the new one. Creates a **Buffer** object based on the memory of a passed **Uint8Array** object and returns the new object, maintaining the memory association of the data. |
| [from](arkts-arkts-buffer-from-f.md#from) | Creates a **Buffer** object based on the specified object. |
| [from](arkts-arkts-buffer-from-f.md#from) | Creates a **Buffer** object based on a string in the given encoding format. |
| [isBuffer](arkts-arkts-buffer-isbuffer-f.md#isbuffer) | Checks whether the specified object is a **Buffer** object. |
| [isEncoding](arkts-arkts-buffer-isencoding-f.md#isencoding) | Checks whether the encoding format is supported. |
| [transcode](arkts-arkts-buffer-transcode-f.md#transcode) | Transcodes a **Buffer** or **Uint8Array** object from one encoding format to another. |

### Classes

| Name | Description |
| --- | --- |
| [Blob](arkts-arkts-buffer-blob-c.md) | Process data as blob type |
| [Buffer](arkts-arkts-buffer-buffer-c.md) | The Buffer object is a method of handling buffers dedicated to binary data. |

### Interfaces

| Name | Description |
| --- | --- |
| [BlobOptions](arkts-arkts-buffer-bloboptions-i.md) | Defines the Blob related options parameters. |
| [TypedArray](arkts-arkts-buffer-typedarray-i.md) | TypedArray inherits the features and methods of Int8Array |

### Types

| Name | Description |
| --- | --- |
| [ArrayUnionType](arkts-arkts-buffer-arrayuniontype-t.md) | ArrayUnionType features and methods |
| [BufferEncoding](arkts-arkts-buffer-bufferencoding-t.md) | Enumerates the supported encoding formats. |
| [TypedArray](arkts-arkts-buffer-typedarray-t.md) | TypedArray features and methods |

