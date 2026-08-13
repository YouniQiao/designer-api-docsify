# startCastDeviceDiscovery (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## startCastDeviceDiscovery

```TypeScript
function startCastDeviceDiscovery(callback: AsyncCallback<void>): void
```

Start device discovery.

**Since:** 23

**Deprecated since:** -1

<!--Device-avSession-function startCastDeviceDiscovery(callback: AsyncCallback<void>): void--><!--Device-avSession-function startCastDeviceDiscovery(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
avSession.startCastDeviceDiscovery(() => {
    console.info('Succeeded in starting cast device discovery.');
});
```


## startCastDeviceDiscovery

```TypeScript
function startCastDeviceDiscovery(filter: number, callback: AsyncCallback<void>): void
```

Start device discovery.

**Since:** 23

**Deprecated since:** -1

<!--Device-avSession-function startCastDeviceDiscovery(filter: int, callback: AsyncCallback<void>): void--><!--Device-avSession-function startCastDeviceDiscovery(filter: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
let filter = 2;
avSession.startCastDeviceDiscovery(filter, () => {
    console.info('Succeeded in starting cast device discovery.');
});
```


## startCastDeviceDiscovery

```TypeScript
function startCastDeviceDiscovery(filter?: number, drmSchemes?: Array<string>): Promise<void>
```

Start device discovery.

**Since:** 23

**Deprecated since:** -1

<!--Device-avSession-function startCastDeviceDiscovery(filter?: int, drmSchemes?: Array<string>): Promise<void>--><!--Device-avSession-function startCastDeviceDiscovery(filter?: int, drmSchemes?: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | number | No |
| [drmSchemes](arkts-avsession-avsession-avmetadata-i.md) | Array & lt;string & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
let filter = 2;
let drmSchemes = ['3d5e6d35-9b9a-41e8-b843-dd3c6e72c42c'];
avSession.startCastDeviceDiscovery(filter, drmSchemes).then(() => {
  console.info('Succeeded in starting cast device discovery.');
});
```
