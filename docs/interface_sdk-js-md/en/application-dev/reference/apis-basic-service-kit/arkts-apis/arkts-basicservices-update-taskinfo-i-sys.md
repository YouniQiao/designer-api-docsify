# TaskInfo (System API)

任务信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-update-export interface TaskInfo--><!--Device-update-export interface TaskInfo-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { update } from 'kits/@kit.BasicServicesKit';
```

## existTask

```TypeScript
existTask: boolean
```

是否存在升级任务，用于判断当前是否有进行中的升级任务。

使用场景：在执行升级操作前查询任务状态，避免重复操作；在升级流程中监控任务状态变化。true表示存在进行中的升级任务(如下载或安装任务)，需要等待任务完成或取消后再执行新任务。false表示当前无任务，可以开始新的升级流程。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-TaskInfo-existTask: boolean--><!--Device-TaskInfo-existTask: boolean-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## taskBody

```TypeScript
taskBody: TaskBody
```

任务数据。

**Type:** [TaskBody](arkts-basicservices-update-taskbody-i-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-TaskInfo-taskBody: TaskBody--><!--Device-TaskInfo-taskBody: TaskBody-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

