# abort

## Modules to Import

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## abort

```TypeScript
function abort(handle: number, options: HuksOptions, callback: AsyncCallback<HuksResult>): void
```

Aborts a key operation. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [abortSession](arkts-universalkeystore-huks-abortsession-f.md)(handle: number, options: HuksOptions, callback: AsyncCallback&lt;void&gt;)

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handle | number | Yes |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[HuksResult](arkts-universalkeystore-huks-huksresult-i.md)&gt; | Yes |


## abort

```TypeScript
function abort(handle: number, options: HuksOptions): Promise<HuksResult>
```

Aborts a key operation. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [abortSession](arkts-universalkeystore-huks-abortsession-f.md)(handle: number, options: HuksOptions)

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handle | number | Yes |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[HuksResult](arkts-universalkeystore-huks-huksresult-i.md)&gt; |
