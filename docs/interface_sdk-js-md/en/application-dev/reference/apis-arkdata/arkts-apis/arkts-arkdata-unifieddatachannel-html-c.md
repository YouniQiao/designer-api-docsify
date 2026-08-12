# HTML

Represents the HTML data. It is a child class of [Text](arkts-arkdata-unifieddatachannel-text-c.md#Text).

**Inheritance/Implementation:** HTML extends [Text](arkts-arkdata-unifieddatachannel-text-c.md#Text)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unifiedDataChannel-class HTML extends Text--><!--Device-unifiedDataChannel-class HTML extends Text-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from '@kit.ArkData';
```

## htmlContent

```TypeScript
set htmlContent(value: string)
```

Indicates the content of html, with html tags

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HTML-set htmlContent(value: string)--><!--Device-HTML-set htmlContent(value: string)-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## plainContent

```TypeScript
plainContent?: string
```

Plaintext without HTML tags. This parameter is optional. The default value is an empty string.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HTML-plainContent?: string--><!--Device-HTML-plainContent?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## uriAuthorizationPolicies

```TypeScript
set uriAuthorizationPolicies(value: Array<UriPermission> | undefined)
```

Defines URI authorization policies for drag intention.

**Type:** Array&lt;[UriPermission](arkts-arkdata-unifieddatachannel-uripermission-e.md)&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-HTML-set uriAuthorizationPolicies(value: Array<UriPermission> | undefined)--><!--Device-HTML-set uriAuthorizationPolicies(value: Array<UriPermission> | undefined)-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

