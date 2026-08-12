# grantToolPermissionsByUser (System API)

## grantToolPermissionsByUser

```TypeScript
export function grantToolPermissionsByUser(userAuthResult: UserAuthResult[]): Promise<TicketInfo[]>
```

Grants tool permissions based on user authorization results.This function grants permissions for tools (CLI commands or APIs) according to the user's authorization decisions.After successful authorization, tickets are generated which can be used for permission verification.

**Since:** 26.0.0

**Required permissions:** ohos.permission.MANAGE_TOOL_RUNTIME_PERMISSIONS

<!--Device-abilityToolAccessCtrl-export function grantToolPermissionsByUser(userAuthResult: UserAuthResult[]): Promise<TicketInfo[]>--><!--Device-abilityToolAccessCtrl-export function grantToolPermissionsByUser(userAuthResult: UserAuthResult[]): Promise<TicketInfo[]>-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userAuthResult | [UserAuthResult[]](../../apis-user-authentication-kit/arkts-apis/arkts-userauthentication-userauth-userauthresult-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[TicketInfo](arkts-ability-abilitytoolaccessctrl-ticketinfo-i-sys.md)[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 24010004 |
| 24010005 |
| 24010002 |
| 24010003 |
| 24010000 |
| 24010001 |
