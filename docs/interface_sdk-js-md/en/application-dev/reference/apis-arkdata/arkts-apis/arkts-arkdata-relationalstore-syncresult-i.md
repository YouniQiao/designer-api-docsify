# SyncResult

表示设备同步结果。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-relationalStore-interface SyncResult--><!--Device-relationalStore-interface SyncResult-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## code

```TypeScript
readonly code:SyncResultCode
```

表示同步结果的状态码。

**Type:** [SyncResultCode](arkts-arkdata-relationalstore-syncresultcode-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SyncResult-readonly code:SyncResultCode--><!--Device-SyncResult-readonly code:SyncResultCode-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## device

```TypeScript
readonly device:string
```

表示同步的设备ID，可通过  
[getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)等接口获取所有可信设备ID列表。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SyncResult-readonly device:string--><!--Device-SyncResult-readonly device:string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## message

```TypeScript
readonly message:string
```

表示同步结果的信息。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SyncResult-readonly message:string--><!--Device-SyncResult-readonly message:string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

