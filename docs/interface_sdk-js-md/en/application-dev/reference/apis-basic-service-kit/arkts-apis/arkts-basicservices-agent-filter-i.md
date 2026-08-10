# Filter

过滤条件。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-agent-interface Filter--><!--Device-agent-interface Filter-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
import { request } from 'kits/@kit.BasicServicesKit';
```

## action

```TypeScript
action?: Action
```

任务操作选项。

- UPLOAD表示上传任务。  
- DOWNLOAD表示下载任务。  
- 如果未填写，则查询所有任务。

**Type:** [Action](arkts-basicservices-agent-action-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Filter-action?: Action--><!--Device-Filter-action?: Action-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## after

```TypeScript
after?: long
```

开始的Unix时间戳（毫秒），默认值为调用时刻减24小时。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Filter-after?: long--><!--Device-Filter-after?: long-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## before

```TypeScript
before?: long
```

结束的Unix时间戳（毫秒），默认为调用时刻。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Filter-before?: long--><!--Device-Filter-before?: long-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## mode

```TypeScript
mode?: Mode
```

任务模式。

- FOREGROUND表示前台任务。  
- BACKGROUND表示后台任务。  
- 如果未填写，则查询所有任务。

**Type:** [Mode](arkts-basicservices-agent-mode-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Filter-mode?: Mode--><!--Device-Filter-mode?: Mode-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## state

```TypeScript
state?: State
```

指定任务的状态。如果未填写，则查询所有任务。

**Type:** [State](arkts-basicservices-agent-state-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Filter-state?: State--><!--Device-Filter-state?: State-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

