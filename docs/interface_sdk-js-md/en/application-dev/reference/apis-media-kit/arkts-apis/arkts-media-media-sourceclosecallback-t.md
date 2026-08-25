# SourceCloseCallback

```TypeScript
type SourceCloseCallback = (uuid: number) => void
```

This callback function is implemented by applications to release related resources.

> **NOTE：**&gt;
> The client must return the handle immediately after processing the request.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uuid | number | Yes |
