# startCastDeviceDiscovery (System API)

## startCastDeviceDiscovery

```TypeScript
function startCastDeviceDiscovery(callback: AsyncCallback<void>): void
```

Start device discovery.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-avSession-function startCastDeviceDiscovery(callback: AsyncCallback<void>): void--><!--Device-avSession-function startCastDeviceDiscovery(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | a callback function |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avSession.startCastDeviceDiscovery((err: BusinessError) => {
  if (err) {
    console.error(`startCastDeviceDiscovery BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('startCastDeviceDiscovery successfully');
  }
});
```


## startCastDeviceDiscovery

```TypeScript
function startCastDeviceDiscovery(filter: int, callback: AsyncCallback<void>): void
```

Start device discovery.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-avSession-function startCastDeviceDiscovery(filter: int, callback: AsyncCallback<void>): void--><!--Device-avSession-function startCastDeviceDiscovery(filter: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | device filter when discovering, can be an union of { |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | a callback function |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | parameter check failed. 1.Mandatory parameters are left unspecified.2.Parameter verification failed. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filter = 2;
avSession.startCastDeviceDiscovery(filter, (err: BusinessError) => {
  if (err) {
    console.error(`startCastDeviceDiscovery BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('startCastDeviceDiscovery successfully');
  }
});
```


## startCastDeviceDiscovery

```TypeScript
function startCastDeviceDiscovery(filter?: int, drmSchemes?: Array<string>): Promise<void>
```

Start device discovery.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-avSession-function startCastDeviceDiscovery(filter?: int, drmSchemes?: Array<string>): Promise<void>--><!--Device-avSession-function startCastDeviceDiscovery(filter?: int, drmSchemes?: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | No | device filter when discovering, can be an union of \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 12 |
| drmSchemes | Array&lt;string&gt; | No | filter drm-enabled devices which are represented by uuid.It is effective when protocol type is TYPE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CAST\_\_\_ESCAPED\_UNDERSCORE\_\_\_PLUS\_\_\_ESCAPED\_UNDERSCORE\_\_\_STREAM.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 12 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise for the result |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | parameter check failed. 1.Mandatory parameters are left unspecified.2.Incorrect parameter types. 3.Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filter = 2;
let drmSchemes = ['3d5e6d35-9b9a-41e8-b843-dd3c6e72c42c'];
avSession.startCastDeviceDiscovery(filter, drmSchemes).then(() => {
  console.info('startCastDeviceDiscovery successfully');
}).catch((err: BusinessError) => {
  console.error(`startCastDeviceDiscovery BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

