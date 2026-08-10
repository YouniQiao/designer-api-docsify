# FilterClause

联系人过滤条件。多个筛选条件之间是“或者”的关系，如果参数是数组类型，数组最多只能包含3个元素。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

<!--Device-contact-interface FilterClause--><!--Device-contact-interface FilterClause-End-->

**System capability:** SystemCapability.Applications.Contacts

## Modules to Import

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## dataItem

```TypeScript
dataItem?: DataFilter
```

联系人数据过滤项。

**Type:** [DataFilter](arkts-contacts-contact-datafilter-i.md)

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FilterClause-dataItem?: DataFilter--><!--Device-FilterClause-dataItem?: DataFilter-End-->

**System capability:** SystemCapability.Applications.Contacts

## focusModeList

```TypeScript
focusModeList?: Array<FilterOptions>
```

专注模式。

**Type:** Array&lt;FilterOptions&gt;

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FilterClause-focusModeList?: Array<FilterOptions>--><!--Device-FilterClause-focusModeList?: Array<FilterOptions>-End-->

**System capability:** SystemCapability.Applications.Contacts

## id

```TypeScript
id?: Array<FilterOptions>
```

联系人id。

**Type:** Array&lt;FilterOptions&gt;

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FilterClause-id?: Array<FilterOptions>--><!--Device-FilterClause-id?: Array<FilterOptions>-End-->

**System capability:** SystemCapability.Applications.Contacts

## name

```TypeScript
name?: Array<FilterOptions>
```

联系人姓名。

**Type:** Array&lt;FilterOptions&gt;

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FilterClause-name?: Array<FilterOptions>--><!--Device-FilterClause-name?: Array<FilterOptions>-End-->

**System capability:** SystemCapability.Applications.Contacts

