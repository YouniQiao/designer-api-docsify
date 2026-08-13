# @ohos.privacyManager

本模块主要提供权限使用记录等隐私管理接口，支持系统应用记录、查询、监听和控制敏感权限的使用情况。 权限使用记录用于描述某项敏感权限何时被使用、以何种方式被使用、当前是否处于使用中，以及这些使用记录是否允许被记录或查询。 该模块主要用于以下场景： - 添加/查询指定应用的敏感权限访问记录。 - 订阅权限使用状态变化事件，感知权限从未使用到前台使用、后台使用的变化，与业务逻辑进行联动。 - 控制当前用户的权限访问记录开关。 - 查询某个权限当前是否正在被使用。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace privacyManager--><!--Device-unnamed-declare namespace privacyManager-End-->

**系统能力：** SystemCapability.Security.AccessToken

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md#addPermissionUsedRecord（系统接口）) |
| [addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md#addPermissionUsedRecord（系统接口）) |
| [checkPermissionInUse](arkts-ability-privacymanager-checkpermissioninuse-f-sys.md#checkPermissionInUse（系统接口）) |
| [getPermissionUsedRecord](arkts-ability-privacymanager-getpermissionusedrecord-f-sys.md#getPermissionUsedRecord（系统接口）) |
| [getPermissionUsedRecord](arkts-ability-privacymanager-getpermissionusedrecord-f-sys.md#getPermissionUsedRecord（系统接口）) |
| [getPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-getpermissionusedrecordtogglestatus-f-sys.md#getPermissionUsedRecordToggleStatus（系统接口）) |
| [getPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-getpermissionusedrecordtogglestatus-f-sys.md#getPermissionUsedRecordToggleStatus（系统接口）) |
| [getPermissionUsedTypeInfos](arkts-ability-privacymanager-getpermissionusedtypeinfos-f-sys.md#getPermissionUsedTypeInfos（系统接口）) |
| [offActiveStateChange](arkts-ability-privacymanager-offactivestatechange-f-sys.md#offActiveStateChange（系统接口）) |
| off_activeStateChange |
| [onActiveStateChange](arkts-ability-privacymanager-onactivestatechange-f-sys.md#onActiveStateChange（系统接口）) |
| on_activeStateChange |
| [setPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md#setPermissionUsedRecordToggleStatus（系统接口）) |
| [setPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md#setPermissionUsedRecordToggleStatus（系统接口）) |
| [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startUsingPermission（系统接口）) |
| [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startUsingPermission（系统接口）) |
| [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startUsingPermission（系统接口）) |
| [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startUsingPermission（系统接口）) |
| [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopUsingPermission（系统接口）) |
| [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopUsingPermission（系统接口）) |
| [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopUsingPermission（系统接口）) |
| [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopUsingPermission（系统接口）) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [ActiveChangeResponse](arkts-ability-privacymanager-activechangeresponse-i-sys.md) |
| [AddPermissionUsedRecordOptions](arkts-ability-privacymanager-addpermissionusedrecordoptions-i-sys.md) |
| [BundleUsedRecord](arkts-ability-privacymanager-bundleusedrecord-i-sys.md) |
| [PermissionUsedRecord](arkts-ability-privacymanager-permissionusedrecord-i-sys.md) |
| [PermissionUsedRequest](arkts-ability-privacymanager-permissionusedrequest-i-sys.md) |
| [PermissionUsedResponse](arkts-ability-privacymanager-permissionusedresponse-i-sys.md) |
| [PermissionUsedTypeInfo](arkts-ability-privacymanager-permissionusedtypeinfo-i-sys.md) |
| [PermissionUsingOptions](arkts-ability-privacymanager-permissionusingoptions-i-sys.md) |
| [UsedRecordDetail](arkts-ability-privacymanager-usedrecorddetail-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [PermissionActiveStatus](arkts-ability-privacymanager-permissionactivestatus-e-sys.md) |
| [PermissionUsageFlag](arkts-ability-privacymanager-permissionusageflag-e-sys.md) |
| [PermissionUsedType](arkts-ability-privacymanager-permissionusedtype-e-sys.md) | 表示通过何种方式使用敏感权限的枚举。 \| 名称 \| 值 \| 说明 \| \| ----------------------- \| -- \| ---------------- \| \| NORMAL_TYPE \| 0 \| 表示通过弹窗授权或设置授权来使用敏感权限。 \| \| PICKER_TYPE \| 1 \| 表示通过某个PICKER服务来使用敏感权限，但此方式不会授予权限。 \| \| SECURITY_COMPONENT_TYPE \| 2 \| 表示通过安全控件授权的方式来使用敏感权限。安全控件是系统提供的授权控件，用户点击后应用可临时获取对应权限。 \|
<!--DelEnd-->
