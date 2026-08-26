# ContactAttributes

Provides a list of contact attributes, which are generally used as arguments. If **null** is passed, all attributes are queried by default.

**Since:** 7

**System capability:** SystemCapability.Applications.ContactsData

## Modules to Import

```TypeScript
import contact from '@kit.ContactsKit';
```

## attributes

```TypeScript
attributes: Attribute[]
```

Indicates the contact attributes.

**Type:** [Attribute](arkts-contacts-contact-attribute-e.md)[]

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Applications.ContactsData

**Examples**

Creates data in JSON format.

```TypeScript
let contactAttributes: contact.ContactAttributes = {
    attributes: [
        contact.Attribute.ATTR_EMAIL,
        contact.Attribute.ATTR_NAME,
        contact.Attribute.ATTR_PHONE
    ]
};
```
