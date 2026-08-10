# CliInfo (System API)

表示CLI（Command Line Interface，命令行界面）信息。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-abilityAccessCtrl-interface CliInfo--><!--Device-abilityAccessCtrl-interface CliInfo-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { Context, Permissions, PermissionRequestResult } from 'kits/@kit.AbilityKit';
```

## cliName

```TypeScript
cliName: string
```

CLI名称。该字段不能为空，且长度不能超过256个字符。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CliInfo-cliName: string--><!--Device-CliInfo-cliName: string-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## subCliName

```TypeScript
subCliName: string
```

CLI子命令名称。该字段可以为空，但长度不能超过256个字符。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CliInfo-subCliName: string--><!--Device-CliInfo-subCliName: string-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

