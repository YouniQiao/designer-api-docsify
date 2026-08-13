# OnMessageCallback

```TypeScript
type OnMessageCallback = (msgId: string, msgParam?: ArrayBuffer) => void
```

Callback function on receiving a custom message.

**Since:** 23

**Deprecated since:** -1

<!--Device-inputMethod-type OnMessageCallback = (msgId: string, msgParam?: ArrayBuffer) => void--><!--Device-inputMethod-type OnMessageCallback = (msgId: string, msgParam?: ArrayBuffer) => void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [msgId](../../apis-network-kit/arkts-apis/arkts-network-eap-eapdata-i.md) | string | Yes |
| msgParam | ArrayBuffer | No |
