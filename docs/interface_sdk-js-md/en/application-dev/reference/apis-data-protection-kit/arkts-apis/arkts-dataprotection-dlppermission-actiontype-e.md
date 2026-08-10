# ActionType

表示在文件设定的权限时间到期后所执行的动作枚举，默认为NOT_OPEN。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-dlpPermission-export enum ActionType--><!--Device-dlpPermission-export enum ActionType-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## NOT_OPEN

```TypeScript
NOT_OPEN = 0
```

表示超过权限管控时间后，用户无权限打开DLP文件。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-ActionType-NOT_OPEN = 0--><!--Device-ActionType-NOT_OPEN = 0-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## OPEN

```TypeScript
OPEN = 1
```

表示超过权限管控时间后，登录账号仍可打开DLP文件，且拥有编辑权限。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-ActionType-OPEN = 1--><!--Device-ActionType-OPEN = 1-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

