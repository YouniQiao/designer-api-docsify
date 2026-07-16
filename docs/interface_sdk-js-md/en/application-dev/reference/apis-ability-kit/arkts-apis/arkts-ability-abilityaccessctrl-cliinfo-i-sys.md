# CliInfo (System API)

Represents CLI (Command Line Interface) information.

**Since:** 26.0.0

<!--Device-abilityAccessCtrl-interface CliInfo--><!--Device-abilityAccessCtrl-interface CliInfo-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { Context, Permissions, PermissionRequestResult } from '@kit.AbilityKit';
```

## cliName

```TypeScript
cliName: string
```

CLI name. This field cannot be empty and its length cannot exceed 256 characters.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-CliInfo-cliName: string--><!--Device-CliInfo-cliName: string-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## subCliName

```TypeScript
subCliName: string
```

CLI sub-command name. This field can be empty, but its length cannot exceed 256 characters.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-CliInfo-subCliName: string--><!--Device-CliInfo-subCliName: string-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

