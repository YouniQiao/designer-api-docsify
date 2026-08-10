# Contact

联系人对象类。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-contact-class Contact--><!--Device-contact-class Contact-End-->

**System capability:** SystemCapability.Applications.ContactsData

## Modules to Import

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## INVALID_CONTACT_ID

```TypeScript
static readonly INVALID_CONTACT_ID: -1
```

默认联系人的id，值为-1。

**Type:** -1

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Contact-static readonly INVALID_CONTACT_ID: -1--><!--Device-Contact-static readonly INVALID_CONTACT_ID: -1-End-->

**System capability:** SystemCapability.Applications.ContactsData

## contactAttributes

```TypeScript
contactAttributes?: ContactAttributes
```

联系人的属性列表，如果为空，则查询联系人的所有属性字段（包括姓名、电话、邮箱等）。

**Type:** [ContactAttributes](arkts-contacts-contact-contactattributes-c.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Contact-contactAttributes?: ContactAttributes--><!--Device-Contact-contactAttributes?: ContactAttributes-End-->

**System capability:** SystemCapability.Applications.ContactsData

## emails

```TypeScript
emails?: Email[]
```

联系人的邮箱地址列表。

**Type:** [Email](arkts-contacts-contact-email-c.md)[]

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Contact-emails?: Email[]--><!--Device-Contact-emails?: Email[]-End-->

**System capability:** SystemCapability.Applications.ContactsData

## events

```TypeScript
events?: Event[]
```

联系人的生日、周年纪念等重要日期列表。

**Type:** [Event](arkts-contacts-contact-event-c.md)[]

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Contact-events?: Event[]--><!--Device-Contact-events?: Event[]-End-->

**System capability:** SystemCapability.Applications.ContactsData

## groups

```TypeScript
groups?: Group[]
```

联系人的群组列表。

**Type:** [Group](arkts-contacts-contact-group-c.md)[]

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Contact-groups?: Group[]--><!--Device-Contact-groups?: Group[]-End-->

**System capability:** SystemCapability.Applications.ContactsData

## id

```TypeScript
readonly id?: number
```

联系人的id，由系统自动生成。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Contact-readonly id?: number--><!--Device-Contact-readonly id?: number-End-->

**System capability:** SystemCapability.Applications.ContactsData

## imAddresses

```TypeScript
imAddresses?: ImAddress[]
```

联系人的即时消息地址列表。

**Type:** [ImAddress](arkts-contacts-contact-imaddress-c.md)[]

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Contact-imAddresses?: ImAddress[]--><!--Device-Contact-imAddresses?: ImAddress[]-End-->

**System capability:** SystemCapability.Applications.ContactsData

## key

```TypeScript
readonly key?: string
```

联系人的唯一查询键key，由系统自动生成。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Contact-readonly key?: string--><!--Device-Contact-readonly key?: string-End-->

**System capability:** SystemCapability.Applications.ContactsData

## name

```TypeScript
name?: Name
```

联系人的姓名。

**Type:** [Name](arkts-contacts-contact-name-c.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Contact-name?: Name--><!--Device-Contact-name?: Name-End-->

**System capability:** SystemCapability.Applications.ContactsData

## nickName

```TypeScript
nickName?: NickName
```

联系人的昵称。

**Type:** [NickName](arkts-contacts-contact-nickname-c.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Contact-nickName?: NickName--><!--Device-Contact-nickName?: NickName-End-->

**System capability:** SystemCapability.Applications.ContactsData

## note

```TypeScript
note?: Note
```

联系人的备注。

**Type:** [Note](arkts-contacts-contact-note-c.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Contact-note?: Note--><!--Device-Contact-note?: Note-End-->

**System capability:** SystemCapability.Applications.ContactsData

## organization

```TypeScript
organization?: Organization
```

联系人的组织信息。

**Type:** [Organization](arkts-contacts-contact-organization-c.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Contact-organization?: Organization--><!--Device-Contact-organization?: Organization-End-->

**System capability:** SystemCapability.Applications.ContactsData

## phoneNumbers

```TypeScript
phoneNumbers?: PhoneNumber[]
```

联系人的电话号码列表。

**Type:** [PhoneNumber](arkts-contacts-contact-phonenumber-c.md)[]

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Contact-phoneNumbers?: PhoneNumber[]--><!--Device-Contact-phoneNumbers?: PhoneNumber[]-End-->

**System capability:** SystemCapability.Applications.ContactsData

## portrait

```TypeScript
portrait?: Portrait
```

联系人的头像。

**Type:** [Portrait](arkts-contacts-contact-portrait-c.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Contact-portrait?: Portrait--><!--Device-Contact-portrait?: Portrait-End-->

**System capability:** SystemCapability.Applications.ContactsData

## postalAddresses

```TypeScript
postalAddresses?: PostalAddress[]
```

联系人的邮政地址列表。

**Type:** [PostalAddress](arkts-contacts-contact-postaladdress-c.md)[]

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Contact-postalAddresses?: PostalAddress[]--><!--Device-Contact-postalAddresses?: PostalAddress[]-End-->

**System capability:** SystemCapability.Applications.ContactsData

## relations

```TypeScript
relations?: Relation[]
```

联系人的关系列表。

**Type:** [Relation](arkts-contacts-contact-relation-c.md)[]

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Contact-relations?: Relation[]--><!--Device-Contact-relations?: Relation[]-End-->

**System capability:** SystemCapability.Applications.ContactsData

## sipAddresses

```TypeScript
sipAddresses?: SipAddress[]
```

联系人的会话发起协议(SIP)地址列表。

**Type:** [SipAddress](arkts-contacts-contact-sipaddress-c.md)[]

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Contact-sipAddresses?: SipAddress[]--><!--Device-Contact-sipAddresses?: SipAddress[]-End-->

**System capability:** SystemCapability.Applications.ContactsData

## websites

```TypeScript
websites?: Website[]
```

联系人的网站列表。

**Type:** [Website](arkts-contacts-contact-website-c.md)[]

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Contact-websites?: Website[]--><!--Device-Contact-websites?: Website[]-End-->

**System capability:** SystemCapability.Applications.ContactsData

