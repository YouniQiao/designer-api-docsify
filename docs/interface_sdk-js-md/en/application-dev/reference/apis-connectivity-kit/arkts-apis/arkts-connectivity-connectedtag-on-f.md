# on

## Modules to Import

```TypeScript
import { connectedTag } from 'kits/@kit.ConnectivityKit';
```

## on("notify")

```TypeScript
function on(type: "notify", callback: Callback<number>): void
```

Registers the NFC field strength state events.

**Since:** 8

**Required permissions:** ohos.permission.NFC_TAG

**System capability:** SystemCapability.Communication.ConnectedTag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | "notify" | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |
