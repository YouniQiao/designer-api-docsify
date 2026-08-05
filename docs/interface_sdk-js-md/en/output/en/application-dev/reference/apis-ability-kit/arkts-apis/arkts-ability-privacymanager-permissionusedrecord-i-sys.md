# PermissionUsedRecord (System API)

Represents the access records of a permission.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-privacyManager-interface PermissionUsedRecord--><!--Device-privacyManager-interface PermissionUsedRecord-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## accessCount

```TypeScript
accessCount: int
```

Total number of accesses for this permission, indicating the cumulative number of successful uses of this permission within the query time window.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRecord-accessCount: int--><!--Device-PermissionUsedRecord-accessCount: int-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## accessRecords

```TypeScript
accessRecords: Array<UsedRecordDetail>
```

Access record collection, effective only when flag is FLAG\_PERMISSION\_USAGE\_DETAIL. Default value: Query the last 10 successful access records.

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

Extension identity, with a maximum length of 48 characters.

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

Last access duration. Unit: milliseconds.

**Type:** long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRecord-lastAccessDuration: long--><!--Device-PermissionUsedRecord-lastAccessDuration: long-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## lastAccessTime

```TypeScript
lastAccessTime: long
```

Last time when the permission was accessed. Unit: milliseconds.

**Type:** long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRecord-lastAccessTime: long--><!--Device-PermissionUsedRecord-lastAccessTime: long-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## lastRejectTime

```TypeScript
lastRejectTime: long
```

Last time when the access to the permission was rejected. Unit: milliseconds.

**Type:** long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRecord-lastRejectTime: long--><!--Device-PermissionUsedRecord-lastRejectTime: long-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## permissionName

```TypeScript
permissionName: Permissions
```

Permission name, used to identify the sensitive permission corresponding to the current statistical record.

**Type:** Permissions

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRecord-permissionName: Permissions--><!--Device-PermissionUsedRecord-permissionName: Permissions-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## rejectCount

```TypeScript
rejectCount: int
```

Total number of rejections for this permission, indicating the cumulative number of failed or denied permission accesses within the query time window.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRecord-rejectCount: int--><!--Device-PermissionUsedRecord-rejectCount: int-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## rejectRecords

```TypeScript
rejectRecords: Array<UsedRecordDetail>
```

Rejection record collection, effective only when flag is FLAG\_PERMISSION\_USAGE\_DETAIL. Default value: Query the last 10 failed or rejected records.

**Type:** Array&lt;UsedRecordDetail&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRecord-rejectRecords: Array<UsedRecordDetail>--><!--Device-PermissionUsedRecord-rejectRecords: Array<UsedRecordDetail>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

