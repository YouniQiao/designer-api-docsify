# write

## Modules to Import

```TypeScript
```

## write

```TypeScript
function write(eventName: string, eventType: EventType, keyValues: object): Promise<void>
```

Writes event information to the event file of the current day. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [write](arkts-performanceanalysis-hiappevent-write-f.md)

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventName | string | Yes |
| eventType | [EventType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-screenlock-eventtype-t-sys.md) | Yes |
| keyValues | object | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |


## write

```TypeScript
function write(eventName: string, eventType: EventType, keyValues: object, callback: AsyncCallback<void>): void
```

Writes event information to the event file of the current day. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [write](arkts-performanceanalysis-hiappevent-write-f.md)

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventName | string | Yes |
| eventType | [EventType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-screenlock-eventtype-t-sys.md) | Yes |
| keyValues | object | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |
