# KeyRequestCallback

```TypeScript
type KeyRequestCallback = (assetId: string, requestData: Uint8Array) => void
```

The callback of key request.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-avSession-type KeyRequestCallback = (assetId: string, requestData: Uint8Array) => void--><!--Device-avSession-type KeyRequestCallback = (assetId: string, requestData: Uint8Array) => void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assetId | string | Yes |
| requestData | Uint8Array | Yes |
