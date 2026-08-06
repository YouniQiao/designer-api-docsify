# Portrait

Defines a contact's portrait.
    **NOTE**  
    
    Since API version 22, contact portraits can be set in URI or [PixelMap]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_  
    format. (Currently, contact avatars cannot be set through the [addContactViaUI]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ or  
    [saveToExistingContactViaUI]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ API.)  
    
    URI indicates the address of the contact portrait file that can be accessed, and  
    [PixelMap]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ indicates the [PixelMap]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_  
    object generated based on the contact portrait resource.  
    
    Since API version 22, the profile picture resource can be read through URI. The resource can be opened only in  
    [fs.open]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_ mode and cannot be directly displayed in the **Image** component using a URI. You need to read  
    the resource and display it in [PixelMap]\_\_\_JSDOC\_LINK\_DESC\_USD\_6\_\_\_ format.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-contact-class Portrait--><!--Device-contact-class Portrait-End-->

**System capability:** SystemCapability.Applications.ContactsData

## photo

```TypeScript
photo?: image.PixelMap
```

Contact portrait in PixelMap format.

**Type:** image.PixelMap

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Portrait-photo?: image.PixelMap--><!--Device-Portrait-photo?: image.PixelMap-End-->

**System capability:** SystemCapability.Applications.ContactsData

## uri

```TypeScript
uri: string
```

Contact portrait in URI format.

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Portrait-uri: string--><!--Device-Portrait-uri: string-End-->

**System capability:** SystemCapability.Applications.ContactsData

