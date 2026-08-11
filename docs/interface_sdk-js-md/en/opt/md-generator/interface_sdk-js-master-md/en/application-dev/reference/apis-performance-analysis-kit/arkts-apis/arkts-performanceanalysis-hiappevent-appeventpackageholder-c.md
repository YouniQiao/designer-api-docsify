# AppEventPackageHolder

Defines a subscription data holder for processing event information.

**Since:** 9

<!--Device-hiAppEvent-class AppEventPackageHolder--><!--Device-hiAppEvent-class AppEventPackageHolder-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## constructor

```TypeScript
constructor(watcherName: string)
```

Constructs an **AppEventPackageHolder** instance. You can call [addWatcher](arkts-performanceanalysis-hiappevent-addwatcher-f.md#addwatcher) to add an event watcher, and then associate the **AppEventPackageHolder** instance with the watcher added in the application based on the watcher name.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppEventPackageHolder-constructor(watcherName: string)--><!--Device-AppEventPackageHolder-constructor(watcherName: string)-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| watcherName | string | Yes |

## Examples

```TypeScript
// Add the Watcher1 to subscribe to system events.
hiAppEvent.addWatcher({
  name: "Watcher1",
  appEventFilters: [
    {
      domain: hiAppEvent.domain.OS,
    }
  ],
});

// Create an AppEventPackageHolder instance. holder1 holds the event data subscribed by Watcher1 added through addWatcher.
let holder1: hiAppEvent.AppEventPackageHolder = new hiAppEvent.AppEventPackageHolder("Watcher1");
```

## setRow

```TypeScript
setRow(size: number): void
```

Sets the number of data records of the event package obtained each time. When **setRow()** and **setSize()** are called at the same time, only **setRow()** takes effect.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AppEventPackageHolder-setRow(size: int): void--><!--Device-AppEventPackageHolder-setRow(size: int): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [11104001](../errorcode-hiappevent.md#11104001-invalid-event-package-size) |

## Examples

```TypeScript
// Create an AppEventPackageHolder instance. holder3 holds the event data subscribed by Watcher1 added through addWatcher.
let holder3: hiAppEvent.AppEventPackageHolder = new hiAppEvent.AppEventPackageHolder("Watcher1");
// Set the number of data records for obtaining the event package each time to 1000.
holder3.setRow(1000);
```

## setSize

```TypeScript
setSize(size: number): void
```

Sets the threshold for the data size of the event package obtained each time.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppEventPackageHolder-setSize(size: int): void--><!--Device-AppEventPackageHolder-setSize(size: int): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [11104001](../errorcode-hiappevent.md#11104001-invalid-event-package-size) |

## Examples

```TypeScript
// Create an AppEventPackageHolder instance. holder2 holds the event data subscribed by Watcher1 added through addWatcher.
let holder2: hiAppEvent.AppEventPackageHolder = new hiAppEvent.AppEventPackageHolder("Watcher1");
// Set the data size threshold for obtaining the event package each time to 1000 bytes.
holder2.setSize(1000);
```

## takeNext

```TypeScript
takeNext(): AppEventPackage
```

Obtains the subscription event.

The system obtains the subscription event data based on the data size threshold specified by **setSize** or the number of data records specified by **setRow**. By default, one subscription event data record is obtained. When all subscription event data is obtained, **null** is returned.

When **setRow** and **setSize** are called at the same time, only **setRow** takes effect.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppEventPackageHolder-takeNext(): AppEventPackage--><!--Device-AppEventPackageHolder-takeNext(): AppEventPackage-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AppEventPackage](arkts-performanceanalysis-hiappevent-appeventpackage-i.md) |

## Examples

```TypeScript
// Create an AppEventPackageHolder instance. holder4 holds the event data subscribed by Watcher1 added through addWatcher.
let holder4: hiAppEvent.AppEventPackageHolder = new hiAppEvent.AppEventPackageHolder("Watcher1");
// Obtain the subscribed event.
let eventPkg: hiAppEvent.AppEventPackage | null = holder4.takeNext();
```
