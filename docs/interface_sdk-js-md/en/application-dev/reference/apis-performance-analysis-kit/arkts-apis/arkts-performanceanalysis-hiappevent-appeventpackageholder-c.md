# AppEventPackageHolder

Defines a subscription data holder for processing event information.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-hiAppEvent-class AppEventPackageHolder--><!--Device-hiAppEvent-class AppEventPackageHolder-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## constructor

```TypeScript
constructor(watcherName: string)
```

Constructs an **AppEventPackageHolder** instance. You can call [addWatcher]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ to add an event watcher, and then associate the **AppEventPackageHolder** instance with the watcher added in the application based on the watcher name.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppEventPackageHolder-constructor(watcherName: string)--><!--Device-AppEventPackageHolder-constructor(watcherName: string)-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| watcherName | string | Yes | Name of the event watcher added through [addWatcher]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. If no watcher is added, no data is displayed by default. |

**Example**

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

ArkTS-Dyn:
```TypeScript
setRow(size: number): void
```

ArkTS-Sta:
```TypeScript
setRow(size: int): void
```

Sets the number of data records of the event package obtained each time. When **setRow()** and **setSize()** are called at the same time, only **setRow()** takes effect.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AppEventPackageHolder-setRow(size: int): void--><!--Device-AppEventPackageHolder-setRow(size: int): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Number of events. The value range is (0, 2^31-1]. If the value is out of the range, an exception is thrown. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [11104001](../errorcode-hiappevent.md#11104001-invalid-event-package-size) | Invalid size value. Possibly caused by the size value is less than or equal to zero. |

**Example**

```TypeScript
// Create an AppEventPackageHolder instance. holder3 holds the event data subscribed by Watcher1 added through addWatcher.
let holder3: hiAppEvent.AppEventPackageHolder = new hiAppEvent.AppEventPackageHolder("Watcher1");
// Set the number of data records for obtaining the event package each time to 1000.
holder3.setRow(1000);
```

## setSize

ArkTS-Dyn:
```TypeScript
setSize(size: number): void
```

ArkTS-Sta:
```TypeScript
setSize(size: int): void
```

Sets the threshold for the data size of the event package obtained each time.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppEventPackageHolder-setSize(size: int): void--><!--Device-AppEventPackageHolder-setSize(size: int): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Data size threshold, in bytes. The value range is [0, 2^31-1]. If the value is out of the range, an exception is thrown. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [11104001](../errorcode-hiappevent.md#11104001-invalid-event-package-size) | Invalid size value. Possibly caused by the size value is less than or equal to zero. |

**Example**

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

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppEventPackageHolder-takeNext(): AppEventPackage--><!--Device-AppEventPackageHolder-takeNext(): AppEventPackage-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Event package object. If all subscription event data has been retrieved, **null** is returned. |

**Example**

```TypeScript
// Create an AppEventPackageHolder instance. holder4 holds the event data subscribed by Watcher1 added through addWatcher.
let holder4: hiAppEvent.AppEventPackageHolder = new hiAppEvent.AppEventPackageHolder("Watcher1");
// Obtain the subscribed event.
let eventPkg: hiAppEvent.AppEventPackage | null = holder4.takeNext();
```

## takeNext

```TypeScript
takeNext(): AppEventPackage | null
```

Obtains the subscription event.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_The system obtains the subscription event data based on the data size threshold specified by setSize or the number of data records specified by setRow. By default, one subscription event data record is obtained. When all subscription event data is obtained, null is returned.\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_When setRow and setSize are called at the same time, only setRow takes effect.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AppEventPackageHolder-takeNext(): AppEventPackage | null--><!--Device-AppEventPackageHolder-takeNext(): AppEventPackage | null-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Event package object. If all subscription event data has been retrieved, null is returned. |

