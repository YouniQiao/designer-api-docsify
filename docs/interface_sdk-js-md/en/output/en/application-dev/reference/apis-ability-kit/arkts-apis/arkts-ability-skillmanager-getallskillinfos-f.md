# getAllSkillInfos

## getAllSkillInfos

```TypeScript
function getAllSkillInfos(flags: int, userId?: int): Promise<Array<SkillInfo>>
```

Obtains all SkillInfo objects installed on the device. To query information for other local accounts, the permission ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS must additionally be granted.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.MANAGE_SKILL_PRIVILEGE or ohos.permission.MANAGE_SKILL

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-skillManager-function getAllSkillInfos(flags: int, userId?: int): Promise<Array<SkillInfo>>--><!--Device-skillManager-function getAllSkillInfos(flags: int, userId?: int): Promise<Array<SkillInfo>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| flags | int | Yes | { |
| userId | int | No | Indicates the user ID. If not provided, the user ID of the caller is used. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;SkillInfo&gt;&gt; | Returns the list of SkillInfo objects. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) | The specified user ID is not found. |

