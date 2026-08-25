# isDomainAccountSupported

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## isDomainAccountSupported

```TypeScript
function isDomainAccountSupported(): Promise<boolean>
```

Checks whether this domain account is supported. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
