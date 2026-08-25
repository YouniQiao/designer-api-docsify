# killProcessWithAccount (System API)

## Modules to Import

```TypeScript
```

## killProcessWithAccount

```TypeScript
function killProcessWithAccount(bundleName: string, accountId: number): Promise<void>
```

Kill process with account.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [killProcessWithAccount](arkts-ability-appmanager-killprocesswithaccount-f-sys.md)

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS and ohos.permission.CLEAN_BACKGROUND_PROCESSES

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| accountId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |


## killProcessWithAccount

```TypeScript
function killProcessWithAccount(bundleName: string, accountId: number, callback: AsyncCallback<void>): void
```

Kill process with account.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [killProcessWithAccount](arkts-ability-appmanager-killprocesswithaccount-f-sys.md)

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS and ohos.permission.CLEAN_BACKGROUND_PROCESSES

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| accountId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |
