# FaceAuthManager（系统接口）

人脸认证管理器对象。用于提供人脸录入过程中的管理功能，目前支持设置人脸预览界面的SurfaceId。

**起始版本：** 9

**系统能力：** SystemCapability.UserIAM.UserAuth.FaceAuth

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { faceAuth } from 'kits/@kit.UserAuthenticationKit';
```

## constructor

```TypeScript
constructor()
```

用于创建人脸认证管理器对象。

**起始版本：** 9

**系统能力：** SystemCapability.UserIAM.UserAuth.FaceAuth

**系统接口：** 此接口为系统接口。

## setSurfaceId

```TypeScript
setSurfaceId(surfaceId: string): void
```

用于在录入人脸时设置人脸预览界面的SurfaceId。该接口需要配合 [addCredential](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-useridentitymanager-c-sys.md#addcredential)使用，通过 [getXComponentSurfaceId](../../apis-arkui/arkts-components/arkts-arkui-xcomponentcontroller-c.md#getxcomponentsurfaceid)方法获取XComponent组件的SurfaceId来显示人脸预览画面。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_USER_IDM

**系统能力：** SystemCapability.UserIAM.UserAuth.FaceAuth

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| surfaceId | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12700001](../errorcode-useriam.md#12700001-人脸服务不可用) |
