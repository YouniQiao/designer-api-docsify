# isShortcutSupported

## isShortcutSupported

```TypeScript
function isShortcutSupported(): boolean
```

查询当前设备是否支持快捷方式。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-shortcutManager-function isShortcutSupported(): boolean--><!--Device-shortcutManager-function isShortcutSupported(): boolean-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
import { shortcutManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = shortcutManager.isShortcutSupported();
  console.info('isShortcutSupported data is' + JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  console.error(`isShortcutSupported errData is errCode:${err.code}  message:${err.message}`);
}
```
