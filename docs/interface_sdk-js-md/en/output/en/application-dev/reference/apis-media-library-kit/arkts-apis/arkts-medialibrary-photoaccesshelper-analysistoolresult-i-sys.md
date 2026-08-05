# AnalysisToolResult (System API)

Result of an analysis tool execution.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

<!--Device-photoAccessHelper-interface AnalysisToolResult--><!--Device-photoAccessHelper-interface AnalysisToolResult-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## errCode

```TypeScript
errCode: int
```

Error code of the tool execution. The value 0 indicates success. Possible error codes: \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_23800203 - Temperature is too high. \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_23800204 - Battery level is too low. \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_23800205 - Storage space is insufficient. \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_23800206 - Power saving mode is enabled. \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_23800207 - Intelligent analysis service is already running. \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_23800208 - Intelligent analysis switch is disabled. \_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_23800209 - Analysis service error. Check the logs for details. \_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_23800301 - Internal system error.

**Type:** int

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnalysisToolResult-errCode: int--><!--Device-AnalysisToolResult-errCode: int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## result

```TypeScript
result?: string
```

Result of the tool execution, in JSON string format.

**Type:** string

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnalysisToolResult-result?: string--><!--Device-AnalysisToolResult-result?: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

