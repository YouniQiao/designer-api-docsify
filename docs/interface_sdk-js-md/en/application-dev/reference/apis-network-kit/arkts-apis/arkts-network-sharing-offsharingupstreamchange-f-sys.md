# off_sharingUpstreamChange (System API)

## Modules to Import

```TypeScript
import { sharing } from 'sharing';
```

## off_sharingUpstreamChange

```TypeScript
function off(type: 'sharingUpstreamChange', callback?: Callback<NetHandle>): void
```

Unregister a callback for the sharing upstream network change.

**Since:** 9

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-sharing-function off(type: 'sharingUpstreamChange', callback?: Callback<NetHandle>): void--><!--Device-sharing-function off(type: 'sharingUpstreamChange', callback?: Callback<NetHandle>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.NetSharing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sharingUpstreamChange' | Yes | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NetHandle&gt; | No | the callback function that returns the network handle. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

**Examples**

```TypeScript
import { sharing } from '@kit.NetworkKit';

sharing.off('sharingUpstreamChange', (data: object) => {
  console.info(JSON.stringify(data));
});
```

