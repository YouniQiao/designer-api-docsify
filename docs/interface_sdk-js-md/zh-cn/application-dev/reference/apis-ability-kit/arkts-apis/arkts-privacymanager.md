# @ohos.privacyManager(Privacy Management)

###### Core Enum Types
 - **[PermissionUsageFlag](arkts-ability-privacymanager-permissionusageflag-e-sys.md):** 权限使用记录查询方式枚举，用于指定查询汇总数据或明细数据。
 - **[PermissionActiveStatus](arkts-ability-privacymanager-permissionactivestatus-e-sys.md):** 权限使用状态变化类型枚举，用于表示未使用、前台使用或后台使用状态。
 - **[PermissionUsedType](arkts-ability-privacymanager-permissionusedtype-e-sys.md):** 敏感权限使用类型枚举，用于表示通过普通授权、Picker或安全控件方式使用敏感权限。
 ###### Core Interface Types
 - **[PermissionUsedRequest](arkts-ability-privacymanager-permissionusedrequest-i-sys.md):** 权限使用记录查询请求对象，用于指定查询应用、权限、时间范围和查询方式。
 - **[PermissionUsedResponse](arkts-ability-privacymanager-permissionusedresponse-i-sys.md):** 权限使用记录查询响应对象，用于返回查询时间范围和应用维度记录集合。
 - **[BundleUsedRecord](arkts-ability-privacymanager-bundleusedrecord-i-sys.md):** 应用或设备维度的权限使用记录对象，用于返回某个应用或远端设备的权限访问记录。
 - **[PermissionUsedRecord](arkts-ability-privacymanager-permissionusedrecord-i-sys.md):** 单个权限的访问记录对象，用于返回访问次数、拒绝次数、最后访问时间和明细记录。
 - **[UsedRecordDetail](arkts-ability-privacymanager-usedrecorddetail-i-sys.md):** 单次访问记录详情对象，用于返回访问状态、时间戳、访问时长和使用类型等信息。
 - **[ActiveChangeResponse](arkts-ability-privacymanager-activechangeresponse-i-sys.md):** 权限使用状态变化事件对象，用于返回权限活跃状态变化详情。
 - **[PermissionUsedTypeInfo](arkts-ability-privacymanager-permissionusedtypeinfo-i-sys.md):** 权限使用类型信息对象，用于返回应用访问敏感权限时的使用类型。
 - **[AddPermissionUsedRecordOptions](arkts-ability-privacymanager-addpermissionusedrecordoptions-i-sys.md):** 添加权限使用记录可选参数对象，用于指定敏感权限使用类型和扩展身份。
 - **[PermissionUsingOptions](arkts-ability-privacymanager-permissionusingoptions-i-sys.md):** 权限使用可选参数对象，用于指定扩展身份。
 ###### Core Function Types
 - **[addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md):** 添加权限使用记录。
 - **[getPermissionUsedRecord](arkts-ability-privacymanager-getpermissionusedrecord-f-sys.md):** 查询权限使用记录。
 - **[setPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md):** 设置权限使用记录开关状态。
 - **[getPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-getpermissionusedrecordtogglestatus-f-sys.md):** 查询权限使用记录开关状态。
 - **[startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md):** 标记开始使用敏感权限。
 - **[stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md):** 标记停止使用敏感权限。
 - **[checkPermissionInUse](arkts-ability-privacymanager-checkpermissioninuse-f-sys.md):** C检查指定权限当前是否正在被使用。
 - **[on](arkts-ability-privacymanager-on-f-sys.md):** 订阅权限使用状态变化事件。
 - **[off](arkts-ability-privacymanager-off-f-sys.md):** 取消订阅权限使用状态变化事件。
 - **[getPermissionUsedTypeInfos](arkts-ability-privacymanager-getpermissionusedtypeinfos-f-sys.md):** 查询敏感权限访问类型信息。
 ###### Core Class
 - **privacyManager:** Provides the core class for privacy management.
 


**起始版本：** 9

**系统能力：** SystemCapability.Security.AccessToken

## 导入模块

```TypeScript
import { privacyManager } from 'kits/@kit.AbilityKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addPermissionUsedRecord(Privacy Management)](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md) |
| [addPermissionUsedRecord(Privacy Management)](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md) |
| [checkPermissionInUse(Privacy Management)](arkts-ability-privacymanager-checkpermissioninuse-f-sys.md) |
| [getPermissionUsedRecord(Privacy Management)](arkts-ability-privacymanager-getpermissionusedrecord-f-sys.md) |
| [getPermissionUsedRecord(Privacy Management)](arkts-ability-privacymanager-getpermissionusedrecord-f-sys.md) |
| [getPermissionUsedRecordToggleStatus(Privacy Management)](arkts-ability-privacymanager-getpermissionusedrecordtogglestatus-f-sys.md) |
| [getPermissionUsedRecordToggleStatus(Privacy Management)](arkts-ability-privacymanager-getpermissionusedrecordtogglestatus-f-sys.md) |
| [getPermissionUsedTypeInfos(Privacy Management)](arkts-ability-privacymanager-getpermissionusedtypeinfos-f-sys.md) |
| off(Privacy Management) |
| on(Privacy Management) |
| [setPermissionUsedRecordToggleStatus(Privacy Management)](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md) |
| [setPermissionUsedRecordToggleStatus(Privacy Management)](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md) |
| [startUsingPermission(Privacy Management)](arkts-ability-privacymanager-startusingpermission-f-sys.md) |
| [startUsingPermission(Privacy Management)](arkts-ability-privacymanager-startusingpermission-f-sys.md) |
| [startUsingPermission(Privacy Management)](arkts-ability-privacymanager-startusingpermission-f-sys.md) |
| [startUsingPermission(Privacy Management)](arkts-ability-privacymanager-startusingpermission-f-sys.md) |
| [stopUsingPermission(Privacy Management)](arkts-ability-privacymanager-stopusingpermission-f-sys.md) |
| [stopUsingPermission(Privacy Management)](arkts-ability-privacymanager-stopusingpermission-f-sys.md) |
| [stopUsingPermission(Privacy Management)](arkts-ability-privacymanager-stopusingpermission-f-sys.md) |
| [stopUsingPermission(Privacy Management)](arkts-ability-privacymanager-stopusingpermission-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [ActiveChangeResponse(Privacy Management)](arkts-ability-privacymanager-activechangeresponse-i-sys.md) |
| [AddPermissionUsedRecordOptions(Privacy Management)](arkts-ability-privacymanager-addpermissionusedrecordoptions-i-sys.md) |
| [BundleUsedRecord(Privacy Management)](arkts-ability-privacymanager-bundleusedrecord-i-sys.md) |
| [PermissionUsedRecord(Privacy Management)](arkts-ability-privacymanager-permissionusedrecord-i-sys.md) |
| [PermissionUsedRequest(Privacy Management)](arkts-ability-privacymanager-permissionusedrequest-i-sys.md) |
| [PermissionUsedResponse(Privacy Management)](arkts-ability-privacymanager-permissionusedresponse-i-sys.md) |
| [PermissionUsedTypeInfo(Privacy Management)](arkts-ability-privacymanager-permissionusedtypeinfo-i-sys.md) |
| [PermissionUsingOptions(Privacy Management)](arkts-ability-privacymanager-permissionusingoptions-i-sys.md) |
| [UsedRecordDetail(Privacy Management)](arkts-ability-privacymanager-usedrecorddetail-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [PermissionActiveStatus(Privacy Management)](arkts-ability-privacymanager-permissionactivestatus-e-sys.md) |
| [PermissionUsageFlag(Privacy Management)](arkts-ability-privacymanager-permissionusageflag-e-sys.md) |
| [PermissionUsedType(Privacy Management)](arkts-ability-privacymanager-permissionusedtype-e-sys.md) | 表示通过何种方式使用敏感权限的枚举。  \| 名称 \| 值 \| 说明 \| \| ----------------------- \| -- \| ---------------- \| \| NORMAL_TYPE \| 0 \| 表示通过弹窗授权或设置授权来使用敏感权限。 \| \| PICKER_TYPE \| 1 \| 表示通过某个PICKER服务来使用敏感权限，但此方式不会授予权限。 \| \| SECURITY_COMPONENT_TYPE \| 2 \| 表示通过安全控件授权的方式来使用敏感权限。安全控件是系统提供的授权控件，用户点击后应用可临时获取对应权限。 \|
<!--DelEnd-->
