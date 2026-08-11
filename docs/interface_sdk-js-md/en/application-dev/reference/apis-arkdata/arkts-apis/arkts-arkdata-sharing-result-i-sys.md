# Result (System API)

Represents the device-cloud sharing result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-sharing-interface Result<T>--><!--Device-sharing-interface Result<T>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudData } from 'kits/@kit.ArkData';
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

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

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

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

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

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

