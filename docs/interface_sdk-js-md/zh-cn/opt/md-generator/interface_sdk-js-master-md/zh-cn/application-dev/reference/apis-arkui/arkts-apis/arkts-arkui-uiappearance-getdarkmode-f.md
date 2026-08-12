# getDarkMode

## getDarkMode

```TypeScript
function getDarkMode(): DarkMode
```

获取系统当前的深浅色模式配置。适用于需要根据系统外观模式动态适配应用UI主题的场景，例如应用内实现深色/浅色主题风格自动切换。

&lt;!--Del--&gt;

> **说明：**

> 该接口在API version 19及之前版本中为系统接口。开发者使用该接口时需要申请
> [ohos.permission.UPDATE_CONFIGURATION](../../../security/AccessToken/permissions-for-system-apps.md#ohospermissionupdate_configuration)
> 权限。

&lt;!--DelEnd--&gt;

**起始版本：** 20

**需要权限：** 
- API版本10 - 19：ohos.permission.UPDATE_CONFIGURATION

<!--Device-uiAppearance-function getDarkMode(): DarkMode--><!--Device-uiAppearance-function getDarkMode(): DarkMode-End-->

**系统能力：** SystemCapability.ArkUI.UiAppearance

**返回值：**

| 类型 |
| --- |
| [DarkMode](arkts-arkui-uiappearance-darkmode-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [500001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-uiappearance.md#500001-内部错误) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { uiAppearance } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let darkMode = uiAppearance.getDarkMode();
  console.info('Get dark-mode ' + darkMode);
} catch (error) {
  let err = error as BusinessError;
  console.error(`Get dark-mode failed. Code: ${err.code}, message: ${err.message}`);
}
```
