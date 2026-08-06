# clearTimeout

## clearTimeout

```TypeScript
export declare function clearTimeout(timeoutID?: number): void
```

Cancels a timer set via **setTimeout()**.The timer object is stored in the thread where the timer is created and must be deleted in that thread.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-export declare function clearTimeout(timeoutID?: number): void--><!--Device-unnamed-export declare function clearTimeout(timeoutID?: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeoutID | number | No | The ID of the timer to be canceled, which must be the same as the return value of **setTimeout()**. If this parameter is omitted or the specified timer ID does not exist, no timer will be canceled. |

