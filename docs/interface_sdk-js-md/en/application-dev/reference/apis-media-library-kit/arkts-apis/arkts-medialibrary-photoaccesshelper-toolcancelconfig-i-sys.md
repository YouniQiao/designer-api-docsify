# ToolCancelConfig (System API)

Configuration for canceling an analysis tool.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

<!--Device-photoAccessHelper-interface ToolCancelConfig--><!--Device-photoAccessHelper-interface ToolCancelConfig-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## param

```TypeScript
param?: string
```

Parameters for canceling the analysis tool, in JSON string format. The total length must not exceed 16KB.

**Type:** string

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolCancelConfig-param?: string--><!--Device-ToolCancelConfig-param?: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## taskId

```TypeScript
taskId: string
```

Task ID to cancel. It is a valid ID returned by **invokeAnalysisTool**.

**Type:** string

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolCancelConfig-taskId: string--><!--Device-ToolCancelConfig-taskId: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

