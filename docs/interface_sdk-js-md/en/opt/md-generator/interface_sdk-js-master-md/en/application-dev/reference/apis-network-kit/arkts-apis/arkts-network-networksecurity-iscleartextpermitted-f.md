# isCleartextPermitted

## Modules to Import

```TypeScript
import { networkSecurity } from 'kits/@kit.NetworkKit';
```

## isCleartextPermitted

```TypeScript
export function isCleartextPermitted(): boolean
```

Checks whether the Cleartext traffic is permitted.To invoke this method, you must have the {@code ohos.permission.INTERNET} permission.

**Since:** 18

**Required permissions:** ohos.permission.INTERNET

<!--Device-networkSecurity-export function isCleartextPermitted(): boolean--><!--Device-networkSecurity-export function isCleartextPermitted(): boolean-End-->

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { networkSecurity } from '@kit.NetworkKit';

try {
  let result: boolean = networkSecurity.isCleartextPermitted();
  console.info(`isCleartextPermitted Result: ${JSON.stringify(result)}`);
} catch (error) {
  console.error(`isCleartextPermitted Error: ${JSON.stringify(error)}`);
}
```
