# isDLPFeatureProvided

## Modules to Import

```TypeScript
```

## isDLPFeatureProvided

```TypeScript
function isDLPFeatureProvided(): Promise<boolean>
```

Checks whether the current system provides the encryption protection feature. This API is available only for enterprise devices and must be enabled by the [MDM](../../../mdm/mdm-kit-intro.md) kit. After the API is successfully called, the query result is returned, indicating whether the system supports DLP encryption. This API uses a promise to return the result. This API checks whether the current system supports the DLP encryption function, so that compatibility processing or function degradation can be performed on devices that do not support this function. > **NOTE：**> > This API is enabled by the [MDM](../../../mdm/mdm-kit-intro.md) kit and is used for enterprise devices. For > other devices (such as consumer devices), this API is inapplicable. Calling it returns **false**.

**Since:** 12

<!--Device-dlpPermission-function isDLPFeatureProvided(): Promise<boolean>--><!--Device-dlpPermission-function isDLPFeatureProvided(): Promise<boolean>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

**Examples**

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.isDLPFeatureProvided().then((isFeatureProvided) => { // Check whether the current system provides the encryption protection feature.
  console.info('isFeatureProvided', JSON.stringify(isFeatureProvided));
}).catch((err: BusinessError) => {
  console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
});
```
