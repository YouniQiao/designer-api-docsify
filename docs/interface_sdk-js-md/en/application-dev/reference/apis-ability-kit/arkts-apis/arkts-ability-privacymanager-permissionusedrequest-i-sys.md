# PermissionUsedRequest (System API)

表示使用记录的查询请求。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-privacyManager-interface PermissionUsedRequest--><!--Device-privacyManager-interface PermissionUsedRequest-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { privacyManager } from 'kits/@kit.AbilityKit';
```

## beginTime

```TypeScript
beginTime?: long
```

查询的起始时间。单位为：毫秒。默认值：0，表示不限制起始时间。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

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

目标应用的包名。

默认值：查询所有应用。

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

目标应用所在设备的ID。

默认值：本端设备ID。

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

查询的终止时间，不早于beginTime，否则返回错误码12100001。单位为：毫秒。默认值：0，表示不限制终止时间。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

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

指定查询方式。设置为FLAG_PERMISSION_USAGE_SUMMARY时返回汇总信息；设置为FLAG_PERMISSION_USAGE_DETAIL时返回明细记录。

**Type:** [PermissionUsageFlag](arkts-ability-privacymanager-permissionusageflag-e-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRequest-flag: PermissionUsageFlag--><!--Device-PermissionUsedRequest-flag: PermissionUsageFlag-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## isRemote

```TypeScript
isRemote?: boolean
```

指定是否查询远端设备。false表示查询本端设备的权限使用记录，true表示查询远端设备记录。

默认值：false。

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

需要查询的权限集合。默认值：空，表示查询所有权限的使用记录。

**Type:** Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRequest-permissionNames?: Array<Permissions>--><!--Device-PermissionUsedRequest-permissionNames?: Array<Permissions>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## tokenId

```TypeScript
tokenId?: int
```

目标应用的身份标识。目标应用的身份标识。可通过应用BundleInfo中的ApplicationInfo中的  
 [accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid)字段获取。 该参数必须为大于0的整数，传入0时返回错误码12100001。 &lt;br&gt;BundleInfo获取可参考：[bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync)。

默认值：0，查询所有应用。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedRequest-tokenId?: int--><!--Device-PermissionUsedRequest-tokenId?: int-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

