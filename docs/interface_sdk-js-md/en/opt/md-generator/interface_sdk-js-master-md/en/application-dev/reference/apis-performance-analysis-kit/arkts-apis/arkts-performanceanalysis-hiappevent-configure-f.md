# configure

## Modules to Import

```TypeScript
import { hiAppEvent } from '@kit.PerformanceAnalysisKit';
```

## configure

```TypeScript
function configure(config: ConfigOption): void
```

Configures the application event logging function, such as setting the logging switch and directory storage quota.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-hiAppEvent-function configure(config: ConfigOption): void--><!--Device-hiAppEvent-function configure(config: ConfigOption): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [ConfigOption](arkts-performanceanalysis-hiappevent-configoption-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [11103001](../errorcode-hiappevent.md#11103001-invalid-maximum-storage-quota) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

```TypeScript
// Disable the event logging function.
let config1: hiAppEvent.ConfigOption = {
  disable: true,
};
hiAppEvent.configure(config1);

// Set the maximum size of the file storage directory to 100 MB.
let config2: hiAppEvent.ConfigOption = {
  maxStorage: '100M',
};
hiAppEvent.configure(config2);
```
