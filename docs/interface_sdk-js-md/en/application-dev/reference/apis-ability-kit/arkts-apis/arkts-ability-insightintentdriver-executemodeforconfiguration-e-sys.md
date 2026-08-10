# ExecuteModeForConfiguration (System API)

[使用配置文件开发的意图](../../../application-models/insight-intent-config-development.md)支持的意图执行模式。例如，将  
[insight_intent.json配置文件](../../../application-models/insight-intent-config-development.md#insight_intentjson配置文件说明)中的executeMode设置为"foreground"，表示支持与UIAbility组件绑定的意图在前台运行。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-insightIntentDriver-enum ExecuteModeForConfiguration--><!--Device-insightIntentDriver-enum ExecuteModeForConfiguration-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## FOREGROUND

```TypeScript
FOREGROUND = 0
```

表示支持与UIAbility组件绑定的意图在前台运行。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExecuteModeForConfiguration-FOREGROUND = 0--><!--Device-ExecuteModeForConfiguration-FOREGROUND = 0-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## BACKGROUND

```TypeScript
BACKGROUND = 1
```

表示支持与UIAbility组件绑定的意图在后台运行。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExecuteModeForConfiguration-BACKGROUND = 1--><!--Device-ExecuteModeForConfiguration-BACKGROUND = 1-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

