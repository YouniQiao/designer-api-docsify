# applyQuickFix (System API)

## Modules to Import

```TypeScript
import { quickFixManager } from 'kits/@kit.AbilityKit';
```

## applyQuickFix

```TypeScript
function applyQuickFix(hapModuleQuickFixFiles: Array<string>, callback: AsyncCallback<void>): void
```

Applies a quick fix patch. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.INSTALL_BUNDLE

**System capability:** SystemCapability.Ability.AbilityRuntime.QuickFix

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hapModuleQuickFixFiles | Array & lt;string & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [18500002](../errorcode-ability.md#18500002-invalid-patch-package) |
| [18500008](../errorcode-ability.md#18500008-internal-error) |


## applyQuickFix

```TypeScript
function applyQuickFix(hapModuleQuickFixFiles: Array<string>): Promise<void>
```

Applies a quick fix patch. This API uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.INSTALL_BUNDLE

**System capability:** SystemCapability.Ability.AbilityRuntime.QuickFix

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hapModuleQuickFixFiles | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [18500002](../errorcode-ability.md#18500002-invalid-patch-package) |
| [18500008](../errorcode-ability.md#18500008-internal-error) |
