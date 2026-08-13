# FaceAuthManager (System API)

Provides APIs for facial authentication management. It provides management features during face enrollment, including setting the surface ID of the face preview page.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-faceAuth-class FaceAuthManager--><!--Device-faceAuth-class FaceAuthManager-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.FaceAuth

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { faceAuth } from '@kit.UserAuthenticationKit';
```

## constructor

```TypeScript
constructor()
```

Creates a face authentication manager object.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-FaceAuthManager-constructor()--><!--Device-FaceAuthManager-constructor()-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.FaceAuth

**System API:** This is a system API.

## Examples

```TypeScript
import { faceAuth } from '@kit.UserAuthenticationKit';

let faceAuthManager = new faceAuth.FaceAuthManager();
```

## setSurfaceId

```TypeScript
setSurfaceId(surfaceId: string): void
```

Sets the surface ID of the face preview page during face enrollment. This API must be used together with [addCredential](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-useridentitymanager-c-sys.md#addCredential) to display the face preview page through the surface of the getXComponentSurfaceId component.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_USER_IDM

<!--Device-FaceAuthManager-setSurfaceId(surfaceId: string): void--><!--Device-FaceAuthManager-setSurfaceId(surfaceId: string): void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.FaceAuth

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| surfaceId | string | Yes | ID of the surface held by XComponent. This ID is used to display the face preview page during face enrollment. &lt;br&gt;**Note:** A valid **surfaceId** must be obtained through the getXComponentSurfaceId method after **XComponent** initialization. An invalid **surfaceId** may cause the preview page to fail to display or the API call to fail. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12700001](../errorcode-useriam.md#12700001-facial-authentication-service-unavailable) | The service is unavailable. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied. Called by non-system application. |

## Examples

```TypeScript
import { faceAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';

// The surfaceId is obtained from the XComponent control. The surfaceId here is only an example.
let surfaceId = '123456';
let manager = new faceAuth.FaceAuthManager();
try {
  manager.setSurfaceId(surfaceId);
  console.info('set surface id success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`set surface id failed, Code is ${err?.code}, message is ${err?.message}`);
}
```

