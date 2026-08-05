# BundleUsedRecord (System API)

Represents the access records of an application or device.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-privacyManager-interface BundleUsedRecord--><!--Device-privacyManager-interface BundleUsedRecord-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName: string
```

Bundle name of the application using the permission. In local scenarios, it can be used to directly locate the target application; this field is invalid in distributed scenarios.

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

ID of the device where the application using the permission is located. Mainly used to identify the source of a remote device in distributed scenarios; this field can usually be ignored in local scenarios.

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

Name of the device where the application using the permission is located, used only in distributed scenarios. It can be used to display a more understandable device identifier in the UI. Default value: Empty string.

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

Whether it is an access record in a distributed scenario. false indicates a local application record, and true indicates a permission usage record on a remote device.

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

Collection of permission usage records under the current application or device. Each element corresponds to a specific permission, allowing further viewing of access count, rejection count, last access time, and detailed records.

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

Application identity identifier for using the permission. This field is invalid in distributed scenarios; the source device must be identified using deviceId and deviceName.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-BundleUsedRecord-tokenId: int--><!--Device-BundleUsedRecord-tokenId: int-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

