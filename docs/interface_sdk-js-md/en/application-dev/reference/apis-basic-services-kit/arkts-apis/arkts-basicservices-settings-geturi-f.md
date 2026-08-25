# getURI

## Modules to Import

```TypeScript
import { settings } from 'kits/@kit.BasicServicesKit';
```

## getURI

```TypeScript
function getURI(name: string, callback: AsyncCallback<object>): void
```

Constructs a URI for a specific name-value pair for monitoring data of the ability that uses the Data template.

**Since:** 7

**Deprecated since:** 9

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;object&gt; | Yes |


## getURI

```TypeScript
function getURI(name: string): Promise<object>
```

Constructs a URI for a specific name-value pair for monitoring data of the ability that uses the Data template.

**Since:** 7

**Deprecated since:** 9

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;object & gt; |
