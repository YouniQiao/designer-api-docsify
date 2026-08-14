# on_sharingStateChange (System API)

## Modules to Import

```TypeScript
import { sharing } from 'sharing';
```

## on_sharingStateChange

```TypeScript
function on(type: 'sharingStateChange', callback: Callback<boolean>): void
```

Register a callback for the global network sharing state change.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-sharing-function on(type: 'sharingStateChange', callback: Callback<boolean>): void--><!--Device-sharing-function on(type: 'sharingStateChange', callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.NetSharing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sharingStateChange' | Yes | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes | the callback function that returns the status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

## Examples

```TypeScript
import { sharing } from '@kit.NetworkKit';

sharing.on('sharingStateChange', (data: boolean) => {
  console.info('on sharingStateChange: ' + JSON.stringify(data));
});
```

