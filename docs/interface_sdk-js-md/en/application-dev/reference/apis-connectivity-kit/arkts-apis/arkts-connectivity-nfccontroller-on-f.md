# on

## Modules to Import

```TypeScript
import { nfcController } from 'kits/@kit.ConnectivityKit';
```

## on("nfcStateChange")

```TypeScript
function on(type: "nfcStateChange", callback: Callback<NfcState>): void
```

Enables listening for NFC state changes. This API uses an asynchronous callback to return the result.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | "nfcStateChange" | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NfcState](arkts-connectivity-nfccontroller-nfcstate-e.md)&gt; | Yes |
