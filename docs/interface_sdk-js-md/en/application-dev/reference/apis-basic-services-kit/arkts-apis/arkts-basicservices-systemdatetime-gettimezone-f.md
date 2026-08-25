# getTimezone

## Modules to Import

```TypeScript
import { systemDateTime } from 'kits/@kit.BasicServicesKit';
```

## getTimezone

```TypeScript
function getTimezone(callback: AsyncCallback<string>): void
```

Obtains the system time zone. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.Time

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |


## getTimezone

```TypeScript
function getTimezone(): Promise<string>
```

Obtains the system time zone. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.Time

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |
