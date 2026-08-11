# @ohos.contact

The **contact** module provides contact management functions, such as adding, deleting, and updating contacts.

**Since:** 7

<!--Device-unnamed-declare namespace contact--><!--Device-unnamed-declare namespace contact-End-->

**System capability:** SystemCapability.Applications.ContactsData

## Modules to Import

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## Summary

### Functions

| [Name](arkts-contacts-contact-name-c.md) |
| --- |
| [addContact](arkts-contacts-contact-addcontact-f.md#addcontact) |
| [addContact](arkts-contacts-contact-addcontact-f.md#addcontact-1) |
| [addContact](arkts-contacts-contact-addcontact-f.md#addcontact-2) |
| [addContact](arkts-contacts-contact-addcontact-f.md#addcontact-3) |
| [addContactViaUI](arkts-contacts-contact-addcontactviaui-f.md#addcontactviaui) |
| [addContacts](arkts-contacts-contact-addcontacts-f.md#addcontacts) |
| [deleteContact](arkts-contacts-contact-deletecontact-f.md#deletecontact) |
| [deleteContact](arkts-contacts-contact-deletecontact-f.md#deletecontact-1) |
| [deleteContact](arkts-contacts-contact-deletecontact-f.md#deletecontact-2) |
| [deleteContact](arkts-contacts-contact-deletecontact-f.md#deletecontact-3) |
| [hasMatchedCallLog](arkts-contacts-contact-hasmatchedcalllog-f.md#hasmatchedcalllog) |
| [hasMatchedCallLog](arkts-contacts-contact-hasmatchedcalllog-f.md#hasmatchedcalllog-1) |
| [importContactsViaUI](arkts-contacts-contact-importcontactsviaui-f.md#importcontactsviaui) |
| [isLocalContact](arkts-contacts-contact-islocalcontact-f.md#islocalcontact) |
| [isLocalContact](arkts-contacts-contact-islocalcontact-f.md#islocalcontact-1) |
| [isLocalContact](arkts-contacts-contact-islocalcontact-f.md#islocalcontact-2) |
| [isLocalContact](arkts-contacts-contact-islocalcontact-f.md#islocalcontact-3) |
| [isMyCard](arkts-contacts-contact-ismycard-f.md#ismycard) |
| [isMyCard](arkts-contacts-contact-ismycard-f.md#ismycard-1) |
| [isMyCard](arkts-contacts-contact-ismycard-f.md#ismycard-2) |
| [isMyCard](arkts-contacts-contact-ismycard-f.md#ismycard-3) |
| [queryContact](arkts-contacts-contact-querycontact-f.md#querycontact) |
| [queryContact](arkts-contacts-contact-querycontact-f.md#querycontact-1) |
| [queryContact](arkts-contacts-contact-querycontact-f.md#querycontact-2) |
| [queryContact](arkts-contacts-contact-querycontact-f.md#querycontact-3) |
| [queryContact](arkts-contacts-contact-querycontact-f.md#querycontact-4) |
| [queryContact](arkts-contacts-contact-querycontact-f.md#querycontact-5) |
| [queryContact](arkts-contacts-contact-querycontact-f.md#querycontact-6) |
| [queryContact](arkts-contacts-contact-querycontact-f.md#querycontact-7) |
| [queryContact](arkts-contacts-contact-querycontact-f.md#querycontact-8) |
| [queryContact](arkts-contacts-contact-querycontact-f.md#querycontact-9) |
| [queryContactSyncInfo](arkts-contacts-contact-querycontactsyncinfo-f.md#querycontactsyncinfo) |
| [queryContacts](arkts-contacts-contact-querycontacts-f.md#querycontacts) |
| [queryContacts](arkts-contacts-contact-querycontacts-f.md#querycontacts-1) |
| [queryContacts](arkts-contacts-contact-querycontacts-f.md#querycontacts-2) |
| [queryContacts](arkts-contacts-contact-querycontacts-f.md#querycontacts-3) |
| [queryContacts](arkts-contacts-contact-querycontacts-f.md#querycontacts-4) |
| [queryContacts](arkts-contacts-contact-querycontacts-f.md#querycontacts-5) |
| [queryContacts](arkts-contacts-contact-querycontacts-f.md#querycontacts-6) |
| [queryContacts](arkts-contacts-contact-querycontacts-f.md#querycontacts-7) |
| [queryContacts](arkts-contacts-contact-querycontacts-f.md#querycontacts-8) |
| [queryContacts](arkts-contacts-contact-querycontacts-f.md#querycontacts-9) |
| [queryContactsByEmail](arkts-contacts-contact-querycontactsbyemail-f.md#querycontactsbyemail) |
| [queryContactsByEmail](arkts-contacts-contact-querycontactsbyemail-f.md#querycontactsbyemail-1) |
| [queryContactsByEmail](arkts-contacts-contact-querycontactsbyemail-f.md#querycontactsbyemail-2) |
| [queryContactsByEmail](arkts-contacts-contact-querycontactsbyemail-f.md#querycontactsbyemail-3) |
| [queryContactsByEmail](arkts-contacts-contact-querycontactsbyemail-f.md#querycontactsbyemail-4) |
| [queryContactsByEmail](arkts-contacts-contact-querycontactsbyemail-f.md#querycontactsbyemail-5) |
| [queryContactsByEmail](arkts-contacts-contact-querycontactsbyemail-f.md#querycontactsbyemail-6) |
| [queryContactsByEmail](arkts-contacts-contact-querycontactsbyemail-f.md#querycontactsbyemail-7) |
| [queryContactsByEmail](arkts-contacts-contact-querycontactsbyemail-f.md#querycontactsbyemail-8) |
| [queryContactsByEmail](arkts-contacts-contact-querycontactsbyemail-f.md#querycontactsbyemail-9) |
| [queryContactsByPhoneNumber](arkts-contacts-contact-querycontactsbyphonenumber-f.md#querycontactsbyphonenumber) |
| [queryContactsByPhoneNumber](arkts-contacts-contact-querycontactsbyphonenumber-f.md#querycontactsbyphonenumber-1) |
| [queryContactsByPhoneNumber](arkts-contacts-contact-querycontactsbyphonenumber-f.md#querycontactsbyphonenumber-2) |
| [queryContactsByPhoneNumber](arkts-contacts-contact-querycontactsbyphonenumber-f.md#querycontactsbyphonenumber-3) |
| [queryContactsByPhoneNumber](arkts-contacts-contact-querycontactsbyphonenumber-f.md#querycontactsbyphonenumber-4) |
| [queryContactsByPhoneNumber](arkts-contacts-contact-querycontactsbyphonenumber-f.md#querycontactsbyphonenumber-5) |
| [queryContactsByPhoneNumber](arkts-contacts-contact-querycontactsbyphonenumber-f.md#querycontactsbyphonenumber-6) |
| [queryContactsByPhoneNumber](arkts-contacts-contact-querycontactsbyphonenumber-f.md#querycontactsbyphonenumber-7) |
| [queryContactsByPhoneNumber](arkts-contacts-contact-querycontactsbyphonenumber-f.md#querycontactsbyphonenumber-8) |
| [queryContactsByPhoneNumber](arkts-contacts-contact-querycontactsbyphonenumber-f.md#querycontactsbyphonenumber-9) |
| [queryContactsCount](arkts-contacts-contact-querycontactscount-f.md#querycontactscount) |
| [queryGroups](arkts-contacts-contact-querygroups-f.md#querygroups) |
| [queryGroups](arkts-contacts-contact-querygroups-f.md#querygroups-1) |
| [queryGroups](arkts-contacts-contact-querygroups-f.md#querygroups-2) |
| [queryGroups](arkts-contacts-contact-querygroups-f.md#querygroups-3) |
| [queryGroups](arkts-contacts-contact-querygroups-f.md#querygroups-4) |
| [queryGroups](arkts-contacts-contact-querygroups-f.md#querygroups-5) |
| [queryHolders](arkts-contacts-contact-queryholders-f.md#queryholders) |
| [queryHolders](arkts-contacts-contact-queryholders-f.md#queryholders-1) |
| [queryHolders](arkts-contacts-contact-queryholders-f.md#queryholders-2) |
| [queryHolders](arkts-contacts-contact-queryholders-f.md#queryholders-3) |
| [queryKey](arkts-contacts-contact-querykey-f.md#querykey) |
| [queryKey](arkts-contacts-contact-querykey-f.md#querykey-1) |
| [queryKey](arkts-contacts-contact-querykey-f.md#querykey-2) |
| [queryKey](arkts-contacts-contact-querykey-f.md#querykey-3) |
| [queryKey](arkts-contacts-contact-querykey-f.md#querykey-4) |
| [queryKey](arkts-contacts-contact-querykey-f.md#querykey-5) |
| [queryMyCard](arkts-contacts-contact-querymycard-f.md#querymycard) |
| [queryMyCard](arkts-contacts-contact-querymycard-f.md#querymycard-1) |
| [queryMyCard](arkts-contacts-contact-querymycard-f.md#querymycard-2) |
| [queryMyCard](arkts-contacts-contact-querymycard-f.md#querymycard-3) |
| [queryMyCard](arkts-contacts-contact-querymycard-f.md#querymycard-4) |
| [queryMyCard](arkts-contacts-contact-querymycard-f.md#querymycard-5) |
| [saveToExistingContactViaUI](arkts-contacts-contact-savetoexistingcontactviaui-f.md#savetoexistingcontactviaui) |
| [selectContact](arkts-contacts-contact-selectcontact-f.md#selectcontact) |
| [selectContact](arkts-contacts-contact-selectcontact-f.md#selectcontact-1) |
| [selectContacts](arkts-contacts-contact-selectcontacts-f.md#selectcontacts) |
| [selectContacts](arkts-contacts-contact-selectcontacts-f.md#selectcontacts-1) |
| [selectContacts](arkts-contacts-contact-selectcontacts-f.md#selectcontacts-2) |
| [selectContacts](arkts-contacts-contact-selectcontacts-f.md#selectcontacts-3) |
| [syncContacts](arkts-contacts-contact-synccontacts-f.md#synccontacts) |
| [updateContact](arkts-contacts-contact-updatecontact-f.md#updatecontact) |
| [updateContact](arkts-contacts-contact-updatecontact-f.md#updatecontact-1) |
| [updateContact](arkts-contacts-contact-updatecontact-f.md#updatecontact-2) |
| [updateContact](arkts-contacts-contact-updatecontact-f.md#updatecontact-3) |
| [updateContact](arkts-contacts-contact-updatecontact-f.md#updatecontact-4) |
| [updateContact](arkts-contacts-contact-updatecontact-f.md#updatecontact-5) |

### Classes

| [Name](arkts-contacts-contact-name-c.md) |
| --- |
| [Contact](arkts-contacts-contact-contact-c.md) |
| [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) |
| [Email](arkts-contacts-contact-email-c.md) |
| [Event](arkts-contacts-contact-event-c.md) |
| [Group](arkts-contacts-contact-group-c.md) |
| [Holder](arkts-contacts-contact-holder-c.md) |
| [ImAddress](arkts-contacts-contact-imaddress-c.md) |
| [Name](arkts-contacts-contact-name-c.md) |
| [NickName](arkts-contacts-contact-nickname-c.md) |
| [Note](arkts-contacts-contact-note-c.md) |
| [Organization](arkts-contacts-contact-organization-c.md) |
| [PhoneNumber](arkts-contacts-contact-phonenumber-c.md) |
| [Portrait](arkts-contacts-contact-portrait-c.md) |
| [PostalAddress](arkts-contacts-contact-postaladdress-c.md) |
| [Relation](arkts-contacts-contact-relation-c.md) |
| [SipAddress](arkts-contacts-contact-sipaddress-c.md) |
| [Website](arkts-contacts-contact-website-c.md) |

### Interfaces

| [Name](arkts-contacts-contact-name-c.md) |
| --- |
| [ContactSelectionFilter](arkts-contacts-contact-contactselectionfilter-i.md) |
| [ContactSelectionOptions](arkts-contacts-contact-contactselectionoptions-i.md) |
| [ContactSyncInfo](arkts-contacts-contact-contactsyncinfo-i.md) |
| [ContactSyncProgress](arkts-contacts-contact-contactsyncprogress-i.md) |
| [DataFilter](arkts-contacts-contact-datafilter-i.md) |
| [FilterClause](arkts-contacts-contact-filterclause-i.md) |
| [FilterOptions](arkts-contacts-contact-filteroptions-i.md) |

### Enums

| [Name](arkts-contacts-contact-name-c.md) |
| --- |
| [Attribute](arkts-contacts-contact-attribute-e.md) |
| [ContactSyncMode](arkts-contacts-contact-contactsyncmode-e.md) |
| [DataField](arkts-contacts-contact-datafield-e.md) |
| [FilterCondition](arkts-contacts-contact-filtercondition-e.md) |
| [FilterType](arkts-contacts-contact-filtertype-e.md) |
