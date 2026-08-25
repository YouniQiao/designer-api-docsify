# Group

Defines a contact group.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**System capability:** SystemCapability.Applications.ContactsData

## Modules to Import

```TypeScript
import { contact } from '@kit.ContactsKit';
```

## groupId

```TypeScript
groupId?: number
```

ID of a contact group.

**Type:** number

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Applications.ContactsData

## title

```TypeScript
title: string
```

Name of a contact group.

**Type:** string

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Applications.ContactsData

**Examples**

Create contact data in JSON format:

```TypeScript
let group: contact.Group = {
    groupId: 1,
    title: "title"
};
```
