# getModelResult (System API)

## Modules to Import

```TypeScript
import { securityGuard } from '@kit.SecurityGuardKit';
```

## getModelResult

```TypeScript
function getModelResult(rule: ModelRule): Promise<ModelResult>
```

Request security model result from security guard.

**Since:** 12

**Deprecated since:** -1

**Required permissions:** ohos.permission.QUERY_SECURITY_MODEL_RESULT

<!--Device-securityGuard-function getModelResult(rule: ModelRule): Promise<ModelResult>--><!--Device-securityGuard-function getModelResult(rule: ModelRule): Promise<ModelResult>-End-->

**System capability:** SystemCapability.Security.SecurityGuard

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rule | [ModelRule](arkts-securityguard-securityguard-modelrule-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ModelResult](arkts-securityguard-securityguard-modelresult-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
