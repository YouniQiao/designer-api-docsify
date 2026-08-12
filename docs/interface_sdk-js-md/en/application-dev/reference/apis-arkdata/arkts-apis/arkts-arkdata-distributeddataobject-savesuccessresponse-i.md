# SaveSuccessResponse

Represents the information returned by the callback of save..

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-distributedDataObject-interface SaveSuccessResponse--><!--Device-distributedDataObject-interface SaveSuccessResponse-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

## Modules to Import

```TypeScript
import { distributedDataObject } from '@kit.ArkData';
```

## deviceId

```TypeScript
deviceId: string
```

ID of the device where the distributed data object is stored. The value local indicates a local device.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-SaveSuccessResponse-deviceId: string--><!--Device-SaveSuccessResponse-deviceId: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

## sessionId

```TypeScript
sessionId: string
```

Unique ID for multi-device collaboration.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-SaveSuccessResponse-sessionId: string--><!--Device-SaveSuccessResponse-sessionId: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

## version

```TypeScript
version: int
```

Version of the saved object, which is a non-negative integer.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-SaveSuccessResponse-version: int--><!--Device-SaveSuccessResponse-version: int-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

