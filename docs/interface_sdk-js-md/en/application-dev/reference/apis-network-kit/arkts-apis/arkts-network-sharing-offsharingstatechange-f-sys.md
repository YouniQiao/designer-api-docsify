# off_sharingStateChange (System API)

## Modules to Import

```TypeScript
import { sharing } from '@kit.NetworkKit';
```

## off_sharingStateChange('sharingStateChange')

```TypeScript
function off(type: 'sharingStateChange', callback?: Callback<boolean>): void
```

Unregisters the network sharing status change event. This method uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-sharing-function off(type: 'sharingStateChange', callback?: Callback<boolean>): void--><!--Device-sharing-function off(type: 'sharingStateChange', callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.NetSharing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sharingStateChange' | Yes | Event type. The value **sharingStateChange** indicates a network sharing status change event. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | No | Callback invoked when the network sharing state changes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

**Examples**

```TypeScript
import { sharing } from '@kit.NetworkKit';

sharing.off('sharingStateChange', (data: boolean) => {
  console.info(JSON.stringify(data));
});
```

