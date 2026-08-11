# init

## Modules to Import

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## init

```TypeScript
function init(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksHandle>): void
```

Initializes a session for a key operation. This API uses an asynchronous callback to return the result.

The **huks.init**, **huks.update**, and **huks.finish** must be used together.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [huks.initSession](arkts-universalkeystore-huks-initsession-f.md#initsession)(keyAlias:

<!--Device-huks-function init(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksHandle>): void--><!--Device-huks-function init(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksHandle>): void-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyAlias | string | Yes |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;HuksHandle&gt; | Yes |


## init

```TypeScript
function init(keyAlias: string, options: HuksOptions): Promise<HuksHandle>
```

Initializes a session for a key operation. This API uses a promise to return the result.

The **huks.init**, **huks.update**, and **huks.finish** must be used together.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [huks.initSession](arkts-universalkeystore-huks-initsession-f.md#initsession)(keyAlias:

<!--Device-huks-function init(keyAlias: string, options: HuksOptions): Promise<HuksHandle>--><!--Device-huks-function init(keyAlias: string, options: HuksOptions): Promise<HuksHandle>-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyAlias | string | Yes |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;HuksHandle&gt; |
