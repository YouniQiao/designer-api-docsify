# setScreenWatermarkImage

## 导入模块

```TypeScript
import { securityManager } from 'kits/@kit.MDMKit';
```

## setScreenWatermarkImage

```TypeScript
function setScreenWatermarkImage(admin: Want, pixelMap: image.PixelMap): void
```

设置屏幕水印策略，对所有用户生效。

> **说明：**&gt;
> 1.屏幕水印策略会将设置的图片平铺覆盖整个屏幕，建议使用带透明度的图片以确保设备屏幕内容可见。&gt;
> 2.当水印图片尺寸小于屏幕时，图片会被拉伸；当水印图片尺寸大于屏幕时，图片会被压缩。该实现方式与应用级别水印的重复平铺方式不同。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| pixelMap | image.PixelMap | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
