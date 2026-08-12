# CloudEnhancementTaskState (System API)

Represents the cloud enhancement task information, which includes the cloud enhancement task state and other information related to certain states.

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-photoAccessHelper-interface CloudEnhancementTaskState--><!--Device-photoAccessHelper-interface CloudEnhancementTaskState-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## expectedDuration

```TypeScript
readonly expectedDuration?: int
```

Queuing time. This parameter is mandatory when **taskStage** is   
**CloudEnhancementTaskStage.TASK_STAGE_EXECUTING**.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-CloudEnhancementTaskState-readonly expectedDuration?: int--><!--Device-CloudEnhancementTaskState-readonly expectedDuration?: int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## statusCode

```TypeScript
readonly statusCode?: int
```

Status code. This parameter is mandatory when **taskStage** is **CloudEnhancementTaskStage.TASK_STAGE_FAILED**.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-CloudEnhancementTaskState-readonly statusCode?: int--><!--Device-CloudEnhancementTaskState-readonly statusCode?: int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## taskStage

```TypeScript
readonly taskStage: CloudEnhancementTaskStage
```

Cloud enhancement task state.

**Type:** [CloudEnhancementTaskStage](arkts-medialibrary-photoaccesshelper-cloudenhancementtaskstage-e-sys.md)

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-CloudEnhancementTaskState-readonly taskStage: CloudEnhancementTaskStage--><!--Device-CloudEnhancementTaskState-readonly taskStage: CloudEnhancementTaskStage-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## totalFileSize

```TypeScript
readonly totalFileSize?: int
```

Total file size. This parameter is mandatory when **taskStage** is   
**CloudEnhancementTaskStage.TASK_STAGE_UPLOADING** or **CloudEnhancementTaskStage.TASK_STAGE_DOWNLOADING**.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-CloudEnhancementTaskState-readonly totalFileSize?: int--><!--Device-CloudEnhancementTaskState-readonly totalFileSize?: int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## transferredFileSize

```TypeScript
readonly transferredFileSize?: int
```

Size of the file transferred. This parameter is mandatory when **taskStage** is   
**CloudEnhancementTaskStage.TASK_STAGE_UPLOADING** or **CloudEnhancementTaskStage.TASK_STAGE_DOWNLOADING**.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-CloudEnhancementTaskState-readonly transferredFileSize?: int--><!--Device-CloudEnhancementTaskState-readonly transferredFileSize?: int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

