# isCleartextPermitted

## Modules to Import

```TypeScript
import { networkSecurity } from 'kits/@kit.NetworkKit';
```

## isCleartextPermitted

```TypeScript
export function isCleartextPermitted(): boolean
```

Checks whether plaintext HTTP access is allowed from the preset **network_config.json** file of the application. By default, plaintext HTTP access is allowed.

**Since:** 18

**Required permissions:** ohos.permission.INTERNET

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
