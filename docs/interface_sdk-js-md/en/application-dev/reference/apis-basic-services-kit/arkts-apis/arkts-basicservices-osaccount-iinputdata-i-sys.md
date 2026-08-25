# IInputData (System API)

Provides the password data callback.

**Since:** 8

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## onSetData

```TypeScript
onSetData(authSubType: AuthSubType, data: Uint8Array): void
```

Called to notify the caller the data is set.

**Since:** 8

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| authSubType | [AuthSubType](arkts-basicservices-osaccount-authsubtype-e-sys.md) | Yes |
| data | Uint8Array | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
