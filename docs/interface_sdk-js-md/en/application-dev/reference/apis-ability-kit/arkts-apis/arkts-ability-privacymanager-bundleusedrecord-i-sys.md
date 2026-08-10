# BundleUsedRecord (System API)

某个应用或设备的访问记录。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-privacyManager-interface BundleUsedRecord--><!--Device-privacyManager-interface BundleUsedRecord-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { privacyManager } from 'kits/@kit.AbilityKit';
```

## bundleName

```TypeScript
bundleName: string
```

使用权限的应用包名。在本端场景下可用于直接定位目标应用；分布式场景下该字段无效。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-BundleUsedRecord-bundleName: string--><!--Device-BundleUsedRecord-bundleName: string-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## deviceId

```TypeScript
deviceId: string
```

使用权限的应用所在设备ID。主要在分布式场景下用于识别远端设备来源；本端场景下通常可忽略该字段。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-BundleUsedRecord-deviceId: string--><!--Device-BundleUsedRecord-deviceId: string-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## deviceName

```TypeScript
deviceName?: string
```

使用权限的应用所在设备名称，仅用于分布式场景。可用于在界面中展示更易理解的设备标识。默认值：空字符串。

**Type:** string

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-BundleUsedRecord-deviceName?: string--><!--Device-BundleUsedRecord-deviceName?: string-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## isRemote

```TypeScript
isRemote: boolean
```

是否是分布式场景的访问记录。false表示本端应用记录，true表示远端设备上的权限使用记录。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-BundleUsedRecord-isRemote: boolean--><!--Device-BundleUsedRecord-isRemote: boolean-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## permissionRecords

```TypeScript
permissionRecords: Array<PermissionUsedRecord>
```

当前应用或设备下的权限使用记录集合。每个元素对应一个具体权限，可进一步查看访问次数、拒绝次数、最后访问时间及明细记录。

**Type:** Array&lt;PermissionUsedRecord&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-BundleUsedRecord-permissionRecords: Array<PermissionUsedRecord>--><!--Device-BundleUsedRecord-permissionRecords: Array<PermissionUsedRecord>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## tokenId

```TypeScript
tokenId: int
```

使用权限的应用身份标识。分布式场景下该字段无效，需结合deviceId和deviceName识别来源设备。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-BundleUsedRecord-tokenId: int--><!--Device-BundleUsedRecord-tokenId: int-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

