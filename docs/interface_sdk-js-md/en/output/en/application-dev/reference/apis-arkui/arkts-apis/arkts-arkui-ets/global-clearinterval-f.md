# clearInterval

## clearInterval

```TypeScript
export declare function clearInterval(intervalID?: number): void
```

Cancels the repeated timer set via **setInterval()**. The timer object is stored in the thread where the timer is created and must be deleted in that thread.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-export declare function clearInterval(intervalID?: number): void--><!--Device-unnamed-export declare function clearInterval(intervalID?: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| intervalID | number | No | ID of the repeated timer to be canceled, which must match the return value of the **setInterval** API used to create the repeated timer. If this parameter is omitted or the repeated timer ID does not exist, no timer will be canceled. |

