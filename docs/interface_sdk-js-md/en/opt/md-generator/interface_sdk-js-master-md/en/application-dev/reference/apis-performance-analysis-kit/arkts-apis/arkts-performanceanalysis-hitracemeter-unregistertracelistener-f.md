# unregisterTraceListener

## Modules to Import

```TypeScript
```

## unregisterTraceListener

```TypeScript
function unregisterTraceListener(index: number): number
```

Unregisters the callback function used to notify whether the trace capture is enabled, which is registered using **registerTraceListener()**.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-hiTraceMeter-function unregisterTraceListener(index: int): int--><!--Device-hiTraceMeter-function unregisterTraceListener(index: int): int-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Examples**

```TypeScript
// Deregister the callback used to notify whether the application trace capture is enabled. index is the callback index returned by hiTraceMeter.registerTraceListener.
let ret = hiTraceMeter.unregisterTraceListener(index);
if (ret < 0) {
  // Handle exceptions.
}
```
