# animateToImmediately

## animateToImmediately

```TypeScript
export declare function animateToImmediately(value: AnimateParam, processor: VoidCallback): void
```

Define animation functions for immediate distribution. This interface depends on the UI context and cannot be used when the UI context is unclear. It is recommended to use animateToImmediately to explicitly specify the UI context.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function animateToImmediately(value: AnimateParam, processor: VoidCallback): void--><!--Device-unnamed-export declare function animateToImmediately(value: AnimateParam, processor: VoidCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [AnimateParam](arkts-common-animateparam-i.md) | Yes | Set animation effect parameters. |
| processor | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) | Yes | Specify the closure function that displays dynamic effects, and the system will automatically insert transition animations for state changes caused by the closure function. |

