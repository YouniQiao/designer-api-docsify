# Portrait

联系人的头像类。

> **说明：**
> 
> 从API version 22开始，支持通过uri和[PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md/arkts-image-image-pixelmap-i.md)格式设置联系人头像资源(暂不支持通过
> [addContactViaUI](arkts-contacts-contact-addcontactviaui-f.md#addcontactviaui)、
> [saveToExistingContactViaUI](arkts-contacts-contact-savetoexistingcontactviaui-f.md#savetoexistingcontactviaui)接口设置)。
> 
> uri为可访问的联系人头像文件地址，[PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md/arkts-image-image-pixelmap-i.md)为通过联系人头像资源生成的
> [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md/arkts-image-image-pixelmap-i.md)对象。
> 
> 从API version 22开始，支持通过uri格式读取联系人头像资源，该格式仅支持以
> [fs.open](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-open-f.md/arkts-corefile-file-fs-open-f.md#open)方式打开，无法直接在Image组件内显示，需读取后转换为
> [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md/arkts-image-image-pixelmap-i.md)格式显示。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-contact-class Portrait--><!--Device-contact-class Portrait-End-->

**System capability:** SystemCapability.Applications.ContactsData

## Modules to Import

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## photo

```TypeScript
photo?: image.PixelMap
```

PixelMap格式的联系人头像。

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

uri格式联系人头像。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Portrait-uri: string--><!--Device-Portrait-uri: string-End-->

**System capability:** SystemCapability.Applications.ContactsData

