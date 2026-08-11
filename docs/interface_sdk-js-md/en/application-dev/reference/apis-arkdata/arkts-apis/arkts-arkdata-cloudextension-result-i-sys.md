# Result (System API)

Represents the data sharing result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cloudExtension-export interface Result<T>--><!--Device-cloudExtension-export interface Result<T>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudExtension } from 'kits/@kit.ArkData';
```

## code

```TypeScript
code: int
```

Error code.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Result-code: int--><!--Device-Result-code: int-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## description

```TypeScript
description?: string
```

Detailed description of the error code. The default value is undefined.

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Result-description?: string--><!--Device-Result-description?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## value

```TypeScript
value?: T
```

Value returned. The specific type is specified by the T parameter. The default value is undefined.

**Type:** T

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Result-value?: T--><!--Device-Result-value?: T-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

