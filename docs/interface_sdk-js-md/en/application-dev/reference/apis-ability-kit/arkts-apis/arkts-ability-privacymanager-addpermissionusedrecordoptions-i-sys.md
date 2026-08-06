# AddPermissionUsedRecordOptions (System API)

Represents the options for adding a permission usage record.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-privacyManager-interface AddPermissionUsedRecordOptions--><!--Device-privacyManager-interface AddPermissionUsedRecordOptions-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## enhancedIdentity

```TypeScript
enhancedIdentity?: string
```

Extension identity, used to identify additional identity information of the caller. This field is passed in when it is necessary to distinguish permission usage records from different call sources under the same application.The length does not exceed 48 characters. Passing an excessively long value when calling  
[addPermissionUsedRecord]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ will return error code 12100001.The maximum length is 48. Default value: empty string.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AddPermissionUsedRecordOptions-enhancedIdentity?: string--><!--Device-AddPermissionUsedRecordOptions-enhancedIdentity?: string-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

## usedType

```TypeScript
usedType?: PermissionUsedType
```

Sensitive permission usage type.

Default value: NORMAL\_TYPE.

**Type:** PermissionUsedType

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AddPermissionUsedRecordOptions-usedType?: PermissionUsedType--><!--Device-AddPermissionUsedRecordOptions-usedType?: PermissionUsedType-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

