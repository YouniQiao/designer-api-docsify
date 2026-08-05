# off

## off('notify')

```TypeScript
function off(type: 'notify', callback?: Callback<number>): void
```

Unsubscribes NFC RF status change events. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_All callback functions will be unregistered If there is no specific callback parameter.\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-connectedTag-function off(type: 'notify', callback?: Callback<number>): void--><!--Device-connectedTag-function off(type: 'notify', callback?: Callback<number>): void-End-->

**System capability:** SystemCapability.Communication.ConnectedTag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'notify' | Yes | The callback type. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;number&gt; | No | The callback function to be unregistered. |

