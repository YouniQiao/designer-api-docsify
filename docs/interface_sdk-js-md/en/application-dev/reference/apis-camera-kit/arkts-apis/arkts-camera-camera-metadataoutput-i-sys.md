# MetadataOutput

MetadataOutput implements metadata streams. It inherits from [CameraOutput](arkts-camera-camera-cameraoutput-i.md).

**Inheritance/Implementation:** MetadataOutput extends [CameraOutput](arkts-camera-camera-cameraoutput-i.md)

**Since:** 23

<!--Device-camera-interface MetadataOutput--><!--Device-camera-interface MetadataOutput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## addMetadataObjectTypes

```TypeScript
addMetadataObjectTypes(types: Array<MetadataObjectType>): void
```

Adds the types of metadata objects to be detected.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MetadataOutput-addMetadataObjectTypes(types: Array<MetadataObjectType>): void--><!--Device-MetadataOutput-addMetadataObjectTypes(types: Array<MetadataObjectType>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| types | Array&lt;[MetadataObjectType](arkts-camera-camera-metadataobjecttype-e.md)&gt; | Yes | Metadata object types, which are obtained through **getSupportedOutputCapability**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.<br>**Applicable version:** 13 - 22 |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect. |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function addMetadataObjectTypes(metadataOutput: camera.MetadataOutput, types: Array<camera.MetadataObjectType>): void {
  try {
    metadataOutput.addMetadataObjectTypes(types);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`addMetadataObjectTypes error. error code: ${err.code}`);
  }
}
```

## removeMetadataObjectTypes

```TypeScript
removeMetadataObjectTypes(types: Array<MetadataObjectType>): void
```

Removes the types of metadata objects to be detected.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MetadataOutput-removeMetadataObjectTypes(types: Array<MetadataObjectType>): void--><!--Device-MetadataOutput-removeMetadataObjectTypes(types: Array<MetadataObjectType>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| types | Array&lt;[MetadataObjectType](arkts-camera-camera-metadataobjecttype-e.md)&gt; | Yes | Metadata object types, which are obtained through **getSupportedOutputCapability**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.<br>**Applicable version:** 13 - 22 |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect. |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function removeMetadataObjectTypes(metadataOutput: camera.MetadataOutput, types: Array<camera.MetadataObjectType>): void {
  try {
    metadataOutput.removeMetadataObjectTypes(types);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`removeMetadataObjectTypes error. error code: ${err.code}`);
  }
}
```

