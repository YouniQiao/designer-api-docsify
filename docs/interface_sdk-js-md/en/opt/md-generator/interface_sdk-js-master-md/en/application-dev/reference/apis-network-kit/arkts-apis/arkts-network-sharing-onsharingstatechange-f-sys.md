# on_sharingStateChange (System API)

## Modules to Import

```TypeScript
import { sharing } from '@kit.NetworkKit';
```

## on_sharingStateChange

```TypeScript
function on(type: 'sharingStateChange', callback: Callback<boolean>): void
```

Register a callback for the global network sharing state change.

**Since:** 9

**Deprecated since:** -1

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-sharing-function on(type: 'sharingStateChange', callback: Callback<boolean>): void--><!--Device-sharing-function on(type: 'sharingStateChange', callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.NetSharing

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'sharingStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { sharing } from '@kit.NetworkKit';

sharing.on('sharingStateChange', (data: boolean) => {
  console.info('on sharingStateChange: ' + JSON.stringify(data));
});
```
