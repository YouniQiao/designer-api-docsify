# updatePolicyFile (System API)

## Modules to Import

```TypeScript
```

## updatePolicyFile

```TypeScript
function updatePolicyFile(policyFile: PolicyFile): Promise<void>
```

Update the policy file.

**Since:** 12

**Required permissions:** ohos.permission.MANAGE_SECURITY_GUARD_CONFIG

<!--Device-securityGuard-function updatePolicyFile(policyFile: PolicyFile): Promise<void>--><!--Device-securityGuard-function updatePolicyFile(policyFile: PolicyFile): Promise<void>-End-->

**System capability:** SystemCapability.Security.SecurityGuard

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| policyFile | [PolicyFile](arkts-securityguard-securityguard-policyfile-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
