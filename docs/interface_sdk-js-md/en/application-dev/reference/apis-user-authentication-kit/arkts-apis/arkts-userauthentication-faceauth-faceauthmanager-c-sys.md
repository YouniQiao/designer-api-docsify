# FaceAuthManager (System API)

Provides APIs for facial authentication management. It provides management features during face enrollment, including setting the **SurfaceId** of the face preview page.

**Since:** 9

**System capability:** SystemCapability.UserIAM.UserAuth.FaceAuth

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { faceAuth } from 'kits/@kit.UserAuthenticationKit';
```

## constructor

```TypeScript
constructor()
```

Creates a face authentication manager object.

**Since:** 9

**System capability:** SystemCapability.UserIAM.UserAuth.FaceAuth

**System API:** This is a system API.

## setSurfaceId

```TypeScript
setSurfaceId(surfaceId: string): void
```

Sets the **SurfaceId** of the face preview page during face enrollment. This API must be used together with [addCredential](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-useridentitymanager-c-sys.md#addcredential). Use the [getXComponentSurfaceId](../../apis-arkui/arkts-components/arkts-arkui-xcomponentcontroller-c.md#getxcomponentsurfaceid) method to obtain the **SurfaceId** of the **XComponent** component to display the face preview page.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_USER_IDM

**System capability:** SystemCapability.UserIAM.UserAuth.FaceAuth

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| surfaceId | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12700001](../errorcode-useriam.md#12700001-facial-authentication-service-unavailable) |
