# ProgressDetails

描述数据库整体执行端云同步任务上传和下载的统计信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-relationalStore-interface ProgressDetails--><!--Device-relationalStore-interface ProgressDetails-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## code

```TypeScript
code: ProgressCode
```

表示端云同步过程的状态。

**Type:** [ProgressCode](arkts-arkdata-relationalstore-progresscode-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ProgressDetails-code: ProgressCode--><!--Device-ProgressDetails-code: ProgressCode-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## details

```TypeScript
details: Record<string, TableDetails>
```

表示端云同步各表的统计信息。

键表示表名，值表示该表的端云同步过程统计信息。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, TableDetails&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ProgressDetails-details: Record<string, TableDetails>--><!--Device-ProgressDetails-details: Record<string, TableDetails>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## message

```TypeScript
message?: string
```

同步状态的详细消息。通过message信息查看详细的失败原因。默认值为空。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProgressDetails-message?: string--><!--Device-ProgressDetails-message?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## schedule

```TypeScript
schedule: Progress
```

表示端云同步过程。

**Type:** [Progress](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-progress-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ProgressDetails-schedule: Progress--><!--Device-ProgressDetails-schedule: Progress-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

