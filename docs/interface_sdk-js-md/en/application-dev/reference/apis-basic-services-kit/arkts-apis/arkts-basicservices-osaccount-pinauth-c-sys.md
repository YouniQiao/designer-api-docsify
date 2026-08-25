# PINAuth (System API)

Provides APIs for PIN authentication.

**Since:** 8

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## constructor

```TypeScript
constructor()
```

Creates a PIN authentication instance.

**Since:** 8

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## registerInputer

```TypeScript
registerInputer(inputer: IInputer): void
```

Registers a PIN inputer.

**Since:** 8

**Required permissions:** ohos.permission.ACCESS_PIN_AUTH

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| inputer | [IInputer](arkts-basicservices-osaccount-iinputer-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300103](../errorcode-account.md#12300103-credential-inputer-already-exists) |

## unregisterInputer

```TypeScript
unregisterInputer(): void
```

Unregisters this PIN inputer.

**Since:** 8

**Required permissions:** ohos.permission.ACCESS_PIN_AUTH

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
