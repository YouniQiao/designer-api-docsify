# ContactAttributes

联系人属性列表，一般作为入参用来标识希望查询的联系人属性。当传入为null时，默认查询全部属性。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-contact-class ContactAttributes--><!--Device-contact-class ContactAttributes-End-->

**System capability:** SystemCapability.Applications.ContactsData

## Modules to Import

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## attributes

```TypeScript
attributes: Attribute[]
```

联系人的属性列表，如果为空，则查询联系人的所有属性字段（包括姓名、电话、邮箱等）。

**Type:** [Attribute](arkts-contacts-contact-attribute-e.md)[]

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ContactAttributes-attributes: Attribute[]--><!--Device-ContactAttributes-attributes: Attribute[]-End-->

**System capability:** SystemCapability.Applications.ContactsData

