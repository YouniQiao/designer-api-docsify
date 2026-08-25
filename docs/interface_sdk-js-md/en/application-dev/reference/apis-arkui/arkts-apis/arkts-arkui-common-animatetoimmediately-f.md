# animateToImmediately

## animateToImmediately

```TypeScript
export declare function animateToImmediately(value: AnimateParam, processor: VoidCallback): void
```

Define animation functions for immediate distribution. This interface depends on the UI context and cannot be used when the UI context is unclear. It is recommended to use animateToImmediately to explicitly specify the UI context.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [AnimateParam](arkts-arkui-common-animateparam-i.md) | Yes |
| processor | [VoidCallback](arkts-arkui-voidcallback-t.md) | Yes |
