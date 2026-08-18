# isPiPEnabled

## Modules to Import

```TypeScript
```

## isPiPEnabled

```TypeScript
function isPiPEnabled(): boolean
```

Checks whether the current device supports the PiP feature.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPWindow-function isPiPEnabled(): boolean--><!--Device-PiPWindow-function isPiPEnabled(): boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
let enable: boolean = PiPWindow.isPiPEnabled(); // Check whether the PiP window is supported.
console.info('isPiPEnabled:' + enable);
```
