# ProgressCode

表示端云同步过程的状态码。请使用枚举名称而非枚举值。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-relationalStore-enum ProgressCode--><!--Device-relationalStore-enum ProgressCode-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## SUCCESS

```TypeScript
SUCCESS = 0
```

表示端云同步过程成功。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ProgressCode-SUCCESS = 0--><!--Device-ProgressCode-SUCCESS = 0-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## UNKNOWN_ERROR

```TypeScript
UNKNOWN_ERROR = 1
```

表示端云同步过程遇到未知错误。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ProgressCode-UNKNOWN_ERROR = 1--><!--Device-ProgressCode-UNKNOWN_ERROR = 1-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## NETWORK_ERROR

```TypeScript
NETWORK_ERROR = 2
```

表示端云同步过程遇到网络错误。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ProgressCode-NETWORK_ERROR = 2--><!--Device-ProgressCode-NETWORK_ERROR = 2-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## CLOUD_DISABLED

```TypeScript
CLOUD_DISABLED = 3
```

表示云端不可用。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ProgressCode-CLOUD_DISABLED = 3--><!--Device-ProgressCode-CLOUD_DISABLED = 3-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## LOCKED_BY_OTHERS

```TypeScript
LOCKED_BY_OTHERS = 4
```

表示有其他设备正在端云同步，本设备无法进行端云同步。

请确保无其他设备占用云端资源后，再使用本设备进行端云同步任务。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ProgressCode-LOCKED_BY_OTHERS = 4--><!--Device-ProgressCode-LOCKED_BY_OTHERS = 4-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## RECORD_LIMIT_EXCEEDED

```TypeScript
RECORD_LIMIT_EXCEEDED = 5
```

表示本次端云同步需要同步的条目或大小超出最大值。由云端配置最大值。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ProgressCode-RECORD_LIMIT_EXCEEDED = 5--><!--Device-ProgressCode-RECORD_LIMIT_EXCEEDED = 5-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## NO_SPACE_FOR_ASSET

```TypeScript
NO_SPACE_FOR_ASSET = 6
```

表示云空间剩余空间小于待同步的资产大小。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ProgressCode-NO_SPACE_FOR_ASSET = 6--><!--Device-ProgressCode-NO_SPACE_FOR_ASSET = 6-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## BLOCKED_BY_NETWORK_STRATEGY

```TypeScript
BLOCKED_BY_NETWORK_STRATEGY = 7
```

表示端云同步被网络策略限制。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ProgressCode-BLOCKED_BY_NETWORK_STRATEGY = 7--><!--Device-ProgressCode-BLOCKED_BY_NETWORK_STRATEGY = 7-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## STOP_CLOUD_SYNC

```TypeScript
STOP_CLOUD_SYNC = 8
```

表示端云同步被停止。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProgressCode-STOP_CLOUD_SYNC = 8--><!--Device-ProgressCode-STOP_CLOUD_SYNC = 8-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

