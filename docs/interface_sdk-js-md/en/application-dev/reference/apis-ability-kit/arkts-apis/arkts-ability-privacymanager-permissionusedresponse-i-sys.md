# PermissionUsedResponse (System API)

表示所有应用或设备的访问记录。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-privacyManager-interface PermissionUsedResponse--><!--Device-privacyManager-interface PermissionUsedResponse-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { privacyManager } from 'kits/@kit.AbilityKit';
```

## beginTime

```TypeScript
beginTime: long
```

查询记录的起始时间。单位为：毫秒。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedResponse-beginTime: long--><!--Device-PermissionUsedResponse-beginTime: long-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## bundleRecords

```TypeScript
bundleRecords: Array<BundleUsedRecord>
```

每个元素表示一个应用维度下的权限访问记录，开发者可进一步遍历permissionRecords获取具体权限使用详情。

**Type:** Array&lt;BundleUsedRecord&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedResponse-bundleRecords: Array<BundleUsedRecord>--><!--Device-PermissionUsedResponse-bundleRecords: Array<BundleUsedRecord>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## endTime

```TypeScript
endTime: long
```

查询记录的终止时间。单位为：毫秒。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-PermissionUsedResponse-endTime: long--><!--Device-PermissionUsedResponse-endTime: long-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

