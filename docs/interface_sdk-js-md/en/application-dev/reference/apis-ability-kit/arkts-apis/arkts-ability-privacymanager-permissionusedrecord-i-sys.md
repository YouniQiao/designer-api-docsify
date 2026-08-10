# PermissionUsedRecord (System API)

某个权限的访问记录。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-privacyManager-interface PermissionUsedRecord--><!--Device-privacyManager-interface PermissionUsedRecord-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { privacyManager } from 'kits/@kit.AbilityKit';
```

## accessCount

```TypeScript
accessCount: int
```

该权限访问总次数，表示在查询时间窗口内成功使用该权限的累计次数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRecord-accessCount: int--><!--Device-PermissionUsedRecord-accessCount: int-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## accessRecords

```TypeScript
accessRecords: Array<UsedRecordDetail>
```

访问记录集合，仅当flag为FLAG_PERMISSION_USAGE_DETAIL时生效。

默认值：查询最近10条成功访问记录。

**Type:** Array&lt;UsedRecordDetail&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRecord-accessRecords: Array<UsedRecordDetail>--><!--Device-PermissionUsedRecord-accessRecords: Array<UsedRecordDetail>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## enhancedIdentity

```TypeScript
enhancedIdentity?: string
```

扩展身份，长度不超过48个字符。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PermissionUsedRecord-enhancedIdentity?: string--><!--Device-PermissionUsedRecord-enhancedIdentity?: string-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## lastAccessDuration

```TypeScript
lastAccessDuration: long
```

最后一次访问时长。单位为：毫秒。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRecord-lastAccessDuration: long--><!--Device-PermissionUsedRecord-lastAccessDuration: long-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## lastAccessTime

```TypeScript
lastAccessTime: long
```

最后一次访问时间。单位为：毫秒。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRecord-lastAccessTime: long--><!--Device-PermissionUsedRecord-lastAccessTime: long-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## lastRejectTime

```TypeScript
lastRejectTime: long
```

最后一次拒绝时间。单位为：毫秒。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRecord-lastRejectTime: long--><!--Device-PermissionUsedRecord-lastRejectTime: long-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## permissionName

```TypeScript
permissionName: Permissions
```

权限名，用于标识当前统计记录对应的敏感权限。

**Type:** [Permissions](arkts-ability-permissions-t.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRecord-permissionName: Permissions--><!--Device-PermissionUsedRecord-permissionName: Permissions-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## rejectCount

```TypeScript
rejectCount: int
```

该权限拒绝总次数，表示在查询时间窗口内权限访问失败或被拒绝的累计次数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRecord-rejectCount: int--><!--Device-PermissionUsedRecord-rejectCount: int-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## rejectRecords

```TypeScript
rejectRecords: Array<UsedRecordDetail>
```

拒绝记录集合，仅当flag为FLAG_PERMISSION_USAGE_DETAIL时生效。

默认值：查询最近10条失败或拒绝记录。

**Type:** Array&lt;UsedRecordDetail&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRecord-rejectRecords: Array<UsedRecordDetail>--><!--Device-PermissionUsedRecord-rejectRecords: Array<UsedRecordDetail>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

