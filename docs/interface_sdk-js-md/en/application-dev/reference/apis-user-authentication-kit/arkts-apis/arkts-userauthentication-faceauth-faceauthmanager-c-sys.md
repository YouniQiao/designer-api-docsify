# FaceAuthManager (System API)

人脸认证管理器对象。用于提供人脸录入过程中的管理功能，目前支持设置人脸预览界面的Surface ID。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-faceAuth-class FaceAuthManager--><!--Device-faceAuth-class FaceAuthManager-End-->

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

用于创建人脸认证管理器对象。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

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

用于在录入人脸时设置人脸预览界面的Surface ID。该接口需要配合  
[addCredential](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-useridentitymanager-c-sys.md/arkts-basicservices-osaccount-useridentitymanager-c-sys.md#addcredential)使用，通过  
[getXComponentSurfaceId](../../apis-arkui/arkts-apis/arkts-arkui-xcomponent-xcomponentcontroller-c.md/arkts-arkui-xcomponent-xcomponentcontroller-c.md#getxcomponentsurfaceid)组件的Surface来显示人脸预览画面。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_USER_IDM

<!--Device-FaceAuthManager-setSurfaceId(surfaceId: string): void--><!--Device-FaceAuthManager-setSurfaceId(surfaceId: string): void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.FaceAuth

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| surfaceId | string | Yes | [XComponent](../../apis-arkui/arkts-components/arkts-arkui-xcomponent-i)持有Surface的ID。用于在人脸录入过程中显示人脸 预览画面。 &lt;br&gt;**说明：**需在XComponent完成初始化后，通过[getXComponentSurfaceId](../../apis-arkui/arkts-apis/arkts-arkui-xcomponent-xcomponentcontroller-c.md/arkts-arkui-xcomponent-xcomponentcontroller-c.md#getxcomponentsurfaceid)方法 获取有效的surfaceId，若传入无效的surfaceId可能导致预览画面无法正常显示或接口调用失败。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12700001 | The service is unavailable. |
| 201 | Permission denied. |
| 202 | Permission denied. Called by non-system application. |

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

