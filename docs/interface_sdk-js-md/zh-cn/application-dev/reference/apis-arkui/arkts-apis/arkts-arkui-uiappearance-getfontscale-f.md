# getFontScale

## 导入模块

```TypeScript
import { uiAppearance } from '@kit.ArkUI';
```

## getFontScale

```TypeScript
function getFontScale(): number
```

获取系统当前的字体大小缩放比例。该比例为系统设置中用户配置的字体大小相对于默认字体大小的倍数，取值范围请参考系统字体大小设置。开发者可基于该比例值调整应用内字体大小，以适配用户的字体偏好设置。<!--Del-->

> **说明：**

> 该接口在API version 19及之前版本中为系统接口。开发者使用该接口时需要申请
> [ohos.permission.UPDATE_CONFIGURATION](../../../security/AccessToken/permissions-for-system-apps.md#ohospermissionupdate_configuration)
> 权限。
<!--DelEnd-->

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** 
- API版本12 - 19：ohos.permission.UPDATE_CONFIGURATION

**系统能力：** SystemCapability.ArkUI.UiAppearance

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [500001](../errorcode-uiappearance.md#500001-内部错误) |

**示例**

```TypeScript
import { uiAppearance } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let fontScale = uiAppearance.getFontScale();
  console.info('Get fontScale ' + fontScale);
} catch (error) {
  let err = error as BusinessError;
  console.error(`Get fontScale failed. Code: ${err.code}, message: ${err.message}`);
}
```
