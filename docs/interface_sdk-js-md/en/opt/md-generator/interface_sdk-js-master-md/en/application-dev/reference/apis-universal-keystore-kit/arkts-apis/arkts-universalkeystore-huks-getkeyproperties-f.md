# getKeyProperties

## Modules to Import

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## getKeyProperties

```TypeScript
function getKeyProperties(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksResult>): void
```

Obtains key properties. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [huks.getKeyItemProperties](arkts-universalkeystore-huks-getkeyitemproperties-f.md#getkeyitemproperties)(

<!--Device-huks-function getKeyProperties(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksResult>): void--><!--Device-huks-function getKeyProperties(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksResult>): void-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyAlias | string | Yes |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;HuksResult&gt; | Yes |

## Examples

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';

/* Set options to emptyOptions. */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
huks.getKeyProperties(keyAlias, emptyOptions, (err, data) => {
});
```


## getKeyProperties

```TypeScript
function getKeyProperties(keyAlias: string, options: HuksOptions): Promise<HuksResult>
```

Obtains key properties. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [huks.getKeyItemProperties](arkts-universalkeystore-huks-getkeyitemproperties-f.md#getkeyitemproperties)(keyAlias:

<!--Device-huks-function getKeyProperties(keyAlias: string, options: HuksOptions): Promise<HuksResult>--><!--Device-huks-function getKeyProperties(keyAlias: string, options: HuksOptions): Promise<HuksResult>-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyAlias | string | Yes |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;HuksResult&gt; |

## Examples

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';

/* Set options to emptyOptions. */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
let result = huks.getKeyProperties(keyAlias, emptyOptions);
```
