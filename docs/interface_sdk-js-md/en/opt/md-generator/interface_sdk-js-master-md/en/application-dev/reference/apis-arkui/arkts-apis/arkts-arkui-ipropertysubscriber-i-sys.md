# IPropertySubscriber (System API)

Provides an interface for attribute subscribers.

**Since:** 7

<!--Device-unnamed-interface IPropertySubscriber--><!--Device-unnamed-interface IPropertySubscriber-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## aboutToBeDeleted

```TypeScript
aboutToBeDeleted(owningView?: IPropertySubscriber): void
```

Called when the object is about to be destroyed.

**Since:** 7

<!--Device-IPropertySubscriber-aboutToBeDeleted(owningView?: IPropertySubscriber): void--><!--Device-IPropertySubscriber-aboutToBeDeleted(owningView?: IPropertySubscriber): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| owningView | [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md) | No |

## id

```TypeScript
id(): number
```

Obtains the ID.

**Since:** 7

<!--Device-IPropertySubscriber-id(): number--><!--Device-IPropertySubscriber-id(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |
