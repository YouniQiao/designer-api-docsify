# PermissionUsedRequest (System API)

Represents the request for querying permission usage records.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-privacyManager-interface PermissionUsedRequest--><!--Device-privacyManager-interface PermissionUsedRequest-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## beginTime

```TypeScript
beginTime?: long
```

Start time of the query.Unit: milliseconds. Default value: **0**, indicating no limit on the start time.

**Type:** long

**Default:** 0

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRequest-beginTime?: long--><!--Device-PermissionUsedRequest-beginTime?: long-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName?: string
```

Bundle name of the target application.

Default value: queries all applications.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRequest-bundleName?: string--><!--Device-PermissionUsedRequest-bundleName?: string-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## deviceId

```TypeScript
deviceId?: string
```

ID of the device where the target application is located.

Default value: local device ID.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRequest-deviceId?: string--><!--Device-PermissionUsedRequest-deviceId?: string-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## endTime

```TypeScript
endTime?: long
```

End time of the query. It must not be earlier than beginTime; otherwise, error code 12100001 is returned.Unit: milliseconds. Default value: **0**, indicating no limit on the end time.

**Type:** long

**Default:** 0

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRequest-endTime?: long--><!--Device-PermissionUsedRequest-endTime?: long-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## flag

```TypeScript
flag: PermissionUsageFlag
```

Used to specify the query mode. When set to **FLAG\_PERMISSION\_USAGE\_SUMMARY**, summary information is returned;when set to **FLAG\_PERMISSION\_USAGE\_DETAIL**, detailed records are returned.

**Type:** PermissionUsageFlag

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRequest-flag: PermissionUsageFlag--><!--Device-PermissionUsedRequest-flag: PermissionUsageFlag-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## isRemote

```TypeScript
isRemote?: boolean
```

Used to specify whether to query remote devices. The value **false** means to query the permission usage records of the local device, and **true** means to query the records of remote devices.

Default value: **false**.

**Type:** boolean

**Default:** false

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRequest-isRemote?: boolean--><!--Device-PermissionUsedRequest-isRemote?: boolean-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## permissionNames

```TypeScript
permissionNames?: Array<Permissions>
```

Set of permissions to query.Default value: Empty string. Means querying usage records of all permissions.

**Type:** Array&lt;Permissions&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRequest-permissionNames?: Array<Permissions>--><!--Device-PermissionUsedRequest-permissionNames?: Array<Permissions>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## tokenId

```TypeScript
tokenId?: int
```

Identity identifier of the target application. It can be obtained through the  
[accessTokenId]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ field of ApplicationInfo.

Default value: **0**, queries all applications.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRequest-tokenId?: int--><!--Device-PermissionUsedRequest-tokenId?: int-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

