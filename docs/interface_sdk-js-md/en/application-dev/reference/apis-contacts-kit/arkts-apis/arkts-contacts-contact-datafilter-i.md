# DataFilter

联系人数据过滤项。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

<!--Device-contact-interface DataFilter--><!--Device-contact-interface DataFilter-End-->

**System capability:** SystemCapability.Applications.Contacts

## Modules to Import

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## field

```TypeScript
field: DataField
```

联系人数据字段。

**Type:** [DataField](arkts-contacts-contact-datafield-e.md)

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-DataFilter-field: DataField--><!--Device-DataFilter-field: DataField-End-->

**System capability:** SystemCapability.Applications.Contacts

## options

```TypeScript
options: Array<FilterOptions>
```

联系人过滤参数，数组中多个FilterOptions之间是“或”的关系，数组的最大长度为3。

**Type:** Array&lt;FilterOptions&gt;

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-DataFilter-options: Array<FilterOptions>--><!--Device-DataFilter-options: Array<FilterOptions>-End-->

**System capability:** SystemCapability.Applications.Contacts

