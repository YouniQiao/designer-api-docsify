# FaceAuthManager (System API)

Provides APIs for facial authentication management. It provides management features during face enrollment, including setting the surface ID of the face preview page.

**Since:** 23

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

Sets the surface ID of the face preview page during face enrollment. This API must be used together with [addCredential](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-useridentitymanager-c-sys.md#addCredential) to display the face preview page through the surface of the [getXComponentSurfaceId](../../apis-arkui/arkts-components/arkts-arkui-xcomponentcontroller-c.md#getXComponentSurfaceId) component.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_USER_IDM

<!--Device-FaceAuthManager-setSurfaceId(surfaceId: string): void--><!--Device-FaceAuthManager-setSurfaceId(surfaceId: string): void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.FaceAuth

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| surfaceId | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12700001](../errorcode-useriam.md#12700001-facial-authentication-service-unavailable) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { faceAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain this surfaceId through the XComponentController.getXComponentSurfaceId() method from the XComponent component. This is only an example.
let surfaceId = '123456';
let manager = new faceAuth.FaceAuthManager();
try {
  manager.setSurfaceId(surfaceId);
  console.info('set surface id successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`set surface id failed, Code is ${err?.code}, message is ${err?.message}`);
}
```
