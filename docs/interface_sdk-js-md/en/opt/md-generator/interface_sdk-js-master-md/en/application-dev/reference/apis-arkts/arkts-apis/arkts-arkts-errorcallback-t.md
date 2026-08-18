# ErrorCallback

```TypeScript
type ErrorCallback = (err: ErrorEvent) => void
```

The event handler to be called when an exception occurs during worker execution.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-type ErrorCallback = (err: ErrorEvent) => void--><!--Device-unnamed-type ErrorCallback = (err: ErrorEvent) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| err | [ErrorEvent](arkts-arkts-worker-errorevent-i.md) | Yes |
