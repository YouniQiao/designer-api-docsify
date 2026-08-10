# isStorageTypeSupported

## Modules to Import

```TypeScript
import { preferences } from 'kits/@kit.ArkData';
```

## isStorageTypeSupported

```TypeScript
function isStorageTypeSupported(type: StorageType): boolean
```

判断当前平台是否支持传入的存储模式，此为同步接口。如果当前平台支持传入的存储模式时，该接口返回true；反之，返回false。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-preferences-function isStorageTypeSupported(type: StorageType): boolean--><!--Device-preferences-function isStorageTypeSupported(type: StorageType): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [StorageType](arkts-arkdata-preferences-storagetype-e.md) | Yes | 需要判断是否支持的存储模式。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true表示当前平台支持当前校验的存储模式，false表示当前平台不支持当前校验的存储模式。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: Incorrect parameter types |

## Examples

```TypeScript
let xmlType = preferences.StorageType.XML;
let gskvType = preferences.StorageType.GSKV;
let isXmlSupported = preferences.isStorageTypeSupported(xmlType);
let isGskvSupported = preferences.isStorageTypeSupported(gskvType);
console.info("Is xml supported in current platform: " + isXmlSupported);
console.info("Is gskv supported in current platform: " + isGskvSupported);
```

